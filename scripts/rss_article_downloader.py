#!/usr/bin/env python3
"""
RSS原文下载器
从RSS源下载文章，保存为HTML/PDF原文
"""

import os
import re
import json
import hashlib
from pathlib import Path
from datetime import datetime
from urllib.parse import urlparse
import feedparser
import requests
from bs4 import BeautifulSoup

BASE_DIR = Path("/Users/zhiyangyu/.box/Workspace/anima-base-scheduled")
FILES_DIR = BASE_DIR / "files"
PEOPLE_DIR = BASE_DIR / "people"

# RSS源配置 - 与人物对应
RSS_SOURCES = {
    "product": {
        "Lenny's Newsletter": {
            "url": "https://www.lennysnewsletter.com/feed",
            "person": "lenny-rachitsky",
            "priority": "high"
        },
        "First Round Review": {
            "url": "https://review.firstround.com/feed",
            "person": "multiple",  # 多个专家
            "priority": "high"
        },
        "SVPG Blog": {
            "url": "https://www.svpg.com/feed/",
            "person": "marty-cagan",
            "priority": "high"
        }
    },
    "growth": {
        "GrowthHackers": {
            "url": "https://growthhackers.com/feed",
            "person": "multiple",
            "priority": "medium"
        },
        "Reforge Blog": {
            "url": "https://www.reforge.com/blog/rss.xml",
            "person": "multiple",
            "priority": "medium"
        }
    },
    "marketing": {
        "Seth Godin Blog": {
            "url": "https://seths.blog/feed/",
            "person": "seth-godin",
            "priority": "medium"
        },
        "Moz Blog": {
            "url": "https://moz.com/rss",
            "person": "rand-fishkin",
            "priority": "medium"
        }
    }
}

class RSSArticleDownloader:
    """RSS原文下载器"""
    
    def __init__(self, max_articles_per_feed=50, log_file=None):
        self.base_dir = BASE_DIR
        self.files_dir = FILES_DIR
        self.max_articles = max_articles_per_feed
        self.log_file = log_file or BASE_DIR / "scripts" / "collection.log"
        self.downloaded = []
        self.errors = []
        self.session = requests.Session()
        self.session.headers.update({
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36'
        })
        
    def get_url_hash(self, url):
        """生成URL的哈希值"""
        return hashlib.md5(url.encode()).hexdigest()[:12]
    
    def download_article_html(self, url, title, person_name, category):
        """下载文章HTML"""
        # 创建目录
        articles_dir = self.files_dir / "html" / category / person_name
        articles_dir.mkdir(parents=True, exist_ok=True)
        
        # 生成文件名
        safe_title = re.sub(r'[^\w\s-]', '', title).strip()
        safe_title = safe_title[:80]
        url_hash = self.get_url_hash(url)
        filename = f"{datetime.now().strftime('%Y%m%d')}-{url_hash}-{safe_title}.html"
        filepath = articles_dir / filename
        
        # 检查是否已存在
        if filepath.exists():
            print(f"  ⏭️  已存在: {safe_title[:50]}")
            return filepath
        
        # 下载HTML
        try:
            response = self.session.get(url, timeout=30)
            response.raise_for_status()
            
            # 保存原始HTML
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(response.text)
            
            print(f"  ✅ 下载成功: {safe_title[:50]}")
            self.downloaded.append(str(filepath))
            return filepath
            
        except Exception as e:
            self.errors.append(f"下载失败: {url} - {e}")
            return None
    
    def extract_article_text(self, html_content):
        """从HTML中提取主要内容"""
        try:
            soup = BeautifulSoup(html_content, 'html.parser')
            
            # 移除脚本和样式
            for script in soup(['script', 'style', 'nav', 'footer', 'header']):
                script.decompose()
            
            # 尝试找到主要内容
            main_content = (
                soup.find('article') or
                soup.find('main') or
                soup.find('div', class_=re.compile(r'content|post|article', re.I))
            )
            
            if main_content:
                text = main_content.get_text(separator='\n', strip=True)
            else:
                text = soup.get_text(separator='\n', strip=True)
            
            # 清理
            text = re.sub(r'\n+', '\n', text)
            text = text.strip()
            
            return text[:5000]  # 限制长度
            
        except Exception as e:
            return None
    
    def process_feed(self, category, source_name, source_config):
        """处理单个RSS源"""
        print(f"\n{'='*60}")
        print(f"📰 RSS源: {source_name} ({category})")
        print(f"{'='*60}")
        
        url = source_config["url"]
        person = source_config["person"]
        
        try:
            # 解析RSS
            feed = feedparser.parse(url)
            
            if feed.bozo:
                print(f"⚠️  RSS解析警告: {feed.bozo}")
            
            print(f"📊 总条目数: {len(feed.entries)}")
            
            # 处理每个条目
            success_count = 0
            for entry in feed.entries[:self.max_articles]:
                article_url = entry.get('link')
                article_title = entry.get('title', 'Unknown')
                published = entry.get('published', 'Unknown')
                
                print(f"\n  📄 {article_title[:60]}")
                print(f"     📅 {published}")
                
                # 下载HTML
                if person != "multiple":
                    person_name = person
                else:
                    # 多个专家的文章，使用"articles"作为通用目录
                    person_name = "articles"
                
                filepath = self.download_article_html(
                    article_url,
                    article_title,
                    person_name,
                    category
                )
                
                if filepath:
                    success_count += 1
            
            print(f"\n✅ {source_name}: {success_count}/{len(feed.entries[:self.max_articles])} 文章下载成功")
            return success_count
            
        except Exception as e:
            self.errors.append(f"RSS处理异常: {url} - {e}")
            return 0
    
    def run(self, categories=None, sources=None):
        """运行下载任务"""
        print(f"{'='*60}")
        print("RSS原文下载器")
        print(f"{'='*60}")
        print(f"时间: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        print(f"输出目录: {self.files_dir}")
        
        total_success = 0
        
        # 确定要处理的源
        targets = RSS_SOURCES
        if categories:
            targets = {
                cat: sources_dict
                for cat, sources_dict in RSS_SOURCES.items()
                if cat in categories
            }
        
        # 处理每个源
        for category, sources_dict in targets.items():
            for source_name, source_config in sources_dict.items():
                if sources and source_name not in sources:
                    continue
                
                success = self.process_feed(category, source_name, source_config)
                total_success += success
        
        # 输出总结
        print(f"\n{'='*60}")
        print("📊 下载总结")
        print(f"{'='*60}")
        print(f"总下载: {total_success} 篇文章")
        print(f"失败数量: {len(self.errors)}")
        
        if self.errors:
            print(f"\n❌ 错误列表:")
            for error in self.errors[:10]:
                print(f"  - {error}")
        
        # 记录日志
        self.log_results()
        
        return total_success > 0
    
    def log_results(self):
        """记录结果到日志文件"""
        log_entry = {
            "timestamp": datetime.now().isoformat(),
            "type": "rss_article",
            "downloaded_count": len(self.downloaded),
            "error_count": len(self.errors),
            "downloaded_files": self.downloaded[:10],
            "errors": self.errors[:5]
        }
        
        try:
            with open(self.log_file, 'a') as f:
                f.write(f"{json.dumps(log_entry, ensure_ascii=False)}\n")
            print(f"\n📝 日志已记录: {self.log_file}")
        except Exception as e:
            print(f"⚠️  日志记录失败: {e}")


if __name__ == "__main__":
    import sys
    
    downloader = RSSArticleDownloader(max_articles_per_feed=30)
    
    # 支持命令行参数
    # python rss_article_downloader.py product Lenny's Newsletter
    if len(sys.argv) > 1:
        categories = [sys.argv[1]]
        sources = sys.argv[2].split(',') if len(sys.argv) > 2 else None
    else:
        categories = None
        sources = None
    
    success = downloader.run(categories, sources)
    sys.exit(0 if success else 1)
