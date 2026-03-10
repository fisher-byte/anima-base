#!/usr/bin/env python3
"""
Anima Base 持续内容采集系统
自动从多个来源持续采集内容
"""

import feedparser
import json
import os
import re
import yaml
import hashlib
from datetime import datetime
from pathlib import Path
from urllib.parse import urlparse

# 配置
BASE_DIR = Path("/root/.openclaw/workspace/anima-base")
COLLECTION_LOG = BASE_DIR / "COLLECTION_LOG.md"
SOURCES_FILE = BASE_DIR / "sources" / "SOURCES.md"

# RSS 源配置 - 详细版
RSS_SOURCES = {
    "product": [
        {
            "name": "Lenny's Newsletter",
            "url": "https://www.lennysnewsletter.com/feed",
            "person": "lenny-rachitsky",
            "category": "product",
            "content_type": "newsletter",
            "language": "en",
            "priority": "high"
        },
        {
            "name": "First Round Review",
            "url": "https://review.firstround.com/feed",
            "person": "first-round",
            "category": "product",
            "content_type": "article",
            "language": "en",
            "priority": "high"
        },
        {
            "name": "SVPG Blog",
            "url": "https://www.svpg.com/feed/",
            "person": "marty-cagan",
            "category": "product",
            "content_type": "article",
            "language": "en",
            "priority": "high"
        },
    ],
    "marketing": [
        {
            "name": "Seth Godin Blog",
            "url": "https://seths.blog/feed/",
            "person": "seth-godin",
            "category": "marketing",
            "content_type": "blog",
            "language": "en",
            "priority": "high"
        },
    ],
    "growth": [
        {
            "name": "GrowthHackers",
            "url": "https://growthhackers.com/feed",
            "person": "growthhackers",
            "category": "growth",
            "content_type": "article",
            "language": "en",
            "priority": "medium"
        },
    ]
}

class ContentCollector:
    def __init__(self):
        self.base_dir = BASE_DIR
        self.collected_count = 0
        self.errors = []
        self.log_entries = []
        
    def slugify(self, text):
        """转换为文件名友好格式"""
        text = str(text).lower()
        text = re.sub(r'[^\w\s-]', '', text)
        text = re.sub(r'[-\s]+', '-', text)
        return text[:80]
    
    def generate_id(self, url, title):
        """生成内容唯一ID"""
        content = f"{url}:{title}"
        return hashlib.md5(content.encode()).hexdigest()[:12]
    
    def extract_full_content(self, entry):
        """提取完整内容"""
        content_parts = []
        
        # 尝试各种内容字段
        if hasattr(entry, 'content'):
            for content in entry.content:
                content_parts.append(content.value)
        elif hasattr(entry, 'summary_detail'):
            content_parts.append(entry.summary_detail.value)
        elif hasattr(entry, 'summary'):
            content_parts.append(entry.summary)
        elif hasattr(entry, 'description'):
            content_parts.append(entry.description)
        
        return '\n\n'.join(content_parts) if content_parts else "[Content extraction failed]"
    
    def extract_publish_date(self, entry):
        """提取发布日期"""
        if hasattr(entry, 'published'):
            return entry.published
        elif hasattr(entry, 'updated'):
            return entry.updated
        elif hasattr(entry, 'created'):
            return entry.created
        return datetime.now().isoformat()
    
    def save_content(self, source_config, entry):
        """保存内容到文件"""
        try:
            title = entry.get('title', 'Untitled')
            link = entry.get('link', '')
            content_id = self.generate_id(link, title)
            
            # 提取完整内容
            full_content = self.extract_full_content(entry)
            publish_date = self.extract_publish_date(entry)
            
            # 确定保存路径
            person_name = source_config.get('person', 'uncategorized')
            content_type = source_config.get('content_type', 'article')
            category = source_config.get('category', 'uncategorized')
            
            person_dir = self.base_dir / category / person_name / content_type + 's'
            person_dir.mkdir(parents=True, exist_ok=True)
            
            # 生成文件名
            date_prefix = datetime.now().strftime('%Y%m%d')
            filename = f"{date_prefix}-{self.slugify(title)}-{content_id}.md"
            filepath = person_dir / filename
            
            # 检查是否已存在
            if filepath.exists():
                return None, "Already exists"
            
            # 构建详细的 frontmatter
            frontmatter = {
                "type": content_type,
                "content_id": content_id,
                "title": title,
                "person": person_name,
                "category": category,
                "date_collected": datetime.now().isoformat(),
                "source": {
                    "name": source_config['name'],
                    "url": link,
                    "rss_url": source_config['url'],
                    "type": "rss",
                    "published": publish_date,
                    "language": source_config.get('language', 'en')
                },
                "collection_method": "rss_auto",
                "tags": source_config.get('tags', []),
                "priority": source_config.get('priority', 'medium'),
                "status": "raw",
                "verified": False
            }
            
            # 写入文件
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write("---\n")
                f.write(yaml.dump(frontmatter, allow_unicode=True, default_flow_style=False))
                f.write("---\n\n")
                
                # 目录
                f.write("## 目录\n\n")
                f.write("- [来源信息](#来源信息)\n")
                f.write("- [原始内容](#原始内容)\n")
                f.write("- [相关链接](#相关链接)\n\n")
                f.write("---\n\n")
                
                # 来源信息
                f.write("## 来源信息\n\n")
                f.write(f"- **来源名称**: {source_config['name']}\n")
                f.write(f"- **原始链接**: [{link}]({link})\n")
                f.write(f"- **RSS源**: {source_config['url']}\n")
                f.write(f"- **发布时间**: {publish_date}\n")
                f.write(f"- **采集时间**: {datetime.now().isoformat()}\n")
                f.write(f"- **内容类型**: {content_type}\n")
                f.write(f"- **语言**: {source_config.get('language', 'en')}\n\n")
                
                # 原始内容
                f.write("## 原始内容\n\n")
                f.write(full_content)
                f.write("\n\n")
                
                # 相关链接
                f.write("---\n\n")
                f.write("## 相关链接\n\n")
                f.write(f"- [原始文章]({link})\n")
                f.write(f"- [人物档案](../profile.md)\n")
                
                f.write(f"\n\n---\n\n")
                f.write(f"*Auto-collected by Anima Base Collector*\n")
                f.write(f"*Collection ID: {content_id}*\n")
            
            self.collected_count += 1
            return filepath, "Success"
            
        except Exception as e:
            error_msg = f"Error saving {title}: {str(e)}"
            self.errors.append(error_msg)
            return None, error_msg
    
    def collect_feed(self, source_config):
        """采集单个RSS源"""
        try:
            print(f"\n📡 [{source_config['category']}] {source_config['name']}")
            print(f"   URL: {source_config['url']}")
            
            feed = feedparser.parse(source_config['url'])
            
            if feed.bozo:
                print(f"   ⚠️ Warning: {feed.bozo_exception}")
            
            entries = feed.entries[:10]  # 取最新10条
            print(f"   Found {len(entries)} entries")
            
            saved_count = 0
            skipped_count = 0
            
            for entry in entries:
                filepath, status = self.save_content(source_config, entry)
                if filepath:
                    print(f"   ✅ Saved: {filepath.name}")
                    saved_count += 1
                elif status == "Already exists":
                    skipped_count += 1
                else:
                    print(f"   ❌ Error: {status}")
            
            # 记录日志
            self.log_entries.append({
                "time": datetime.now().isoformat(),
                "source": source_config['name'],
                "action": "rss_collect",
                "result": f"saved:{saved_count}, skipped:{skipped_count}",
                "status": "success" if saved_count > 0 else "no_new"
            })
            
        except Exception as e:
            error_msg = f"Feed collection failed: {str(e)}"
            print(f"   ❌ {error_msg}")
            self.errors.append(error_msg)
            self.log_entries.append({
                "time": datetime.now().isoformat(),
                "source": source_config['name'],
                "action": "rss_collect",
                "result": error_msg,
                "status": "error"
            })
    
    def update_collection_log(self):
        """更新采集日志"""
        log_content = f"# 内容采集日志\n\n"
        log_content += f"**Last Updated**: {datetime.now().isoformat()}\n\n"
        log_content += f"**Total Collections This Run**: {self.collected_count}\n\n"
        log_content += f"**Errors**: {len(self.errors)}\n\n"
        
        log_content += "## 本次采集记录\n\n"
        log_content += "| 时间 | 来源 | 操作 | 结果 | 状态 |\n"
        log_content += "|------|------|------|------|------|\n"
        
        for entry in self.log_entries:
            log_content += f"| {entry['time'][:19]} | {entry['source']} | {entry['action']} | {entry['result']} | {entry['status']} |\n"
        
        log_content += "\n## 错误记录\n\n"
        if self.errors:
            for error in self.errors:
                log_content += f"- ❌ {error}\n"
        else:
            log_content += "- ✅ No errors\n"
        
        # 追加到主日志文件
        with open(COLLECTION_LOG, 'a', encoding='utf-8') as f:
            f.write(f"\n\n## {datetime.now().isoformat()}\n\n")
            f.write(f"Collected: {self.collected_count} items\n")
            f.write(f"Errors: {len(self.errors)}\n")
    
    def run(self):
        """运行采集任务"""
        print("=" * 70)
        print("🚀 Anima Base - Continuous Content Collection System")
        print(f"⏰ Started: {datetime.now().isoformat()}")
        print("=" * 70)
        
        # 采集所有RSS源
        for category, sources in RSS_SOURCES.items():
            print(f"\n📁 CATEGORY: {category.upper()}")
            print("-" * 70)
            for source in sources:
                self.collect_feed(source)
        
        # 更新日志
        self.update_collection_log()
        
        # 输出总结
        print("\n" + "=" * 70)
        print("📊 COLLECTION SUMMARY")
        print("=" * 70)
        print(f"Total new items collected: {self.collected_count}")
        print(f"Total errors: {len(self.errors)}")
        
        if self.errors:
            print("\n❌ ERRORS:")
            for error in self.errors[:5]:  # 只显示前5个错误
                print(f"  - {error}")
        
        print("\n✅ Collection complete!")
        print("=" * 70)
        
        return self.collected_count, self.errors


if __name__ == "__main__":
    collector = ContentCollector()
    collector.run()
