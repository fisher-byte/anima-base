#!/usr/bin/env python3
"""
RSS 内容收集器
自动抓取订阅源的新文章并保存为 Markdown
"""

import feedparser
import requests
from datetime import datetime
import os
import re
import yaml
from pathlib import Path

# RSS 订阅源配置
RSS_FEEDS = {
    "product": [
        {"name": "Lenny's Newsletter", "url": "https://www.lennysnewsletter.com/feed"},
        {"name": "First Round Review", "url": "https://review.firstround.com/feed"},
        {"name": "SVPG Blog", "url": "https://www.svpg.com/feed/"},
        {"name": "Growth.design", "url": "https://growth.design/feed.xml"},
    ],
    "marketing": [
        {"name": "Seth Godin", "url": "https://seths.blog/feed/"},
        {"name": "Ann Handley", "url": "https://annhandley.com/feed/"},
        {"name": "Content Marketing Institute", "url": "https://contentmarketinginstitute.com/feed/"},
    ],
    "growth": [
        {"name": "Reforge Blog", "url": "https://www.reforge.com/blog/rss.xml"},
        {"name": "GrowthHackers", "url": "https://growthhackers.com/feed"},
    ],
    "leadership": [
        {"name": "First Round Review", "url": "https://review.firstround.com/feed"},
    ]
}

class RSSCollector:
    def __init__(self, base_dir="/root/.openclaw/workspace/anima-base"):
        self.base_dir = Path(base_dir)
        self.collected = []
        
    def slugify(self, text):
        """将标题转换为文件名友好的格式"""
        text = text.lower()
        text = re.sub(r'[^\w\s-]', '', text)
        text = re.sub(r'[-\s]+', '-', text)
        return text[:50]  # 限制长度
    
    def extract_content(self, entry):
        """从 entry 中提取文章内容"""
        # 优先使用 content，其次 summary，最后 description
        if hasattr(entry, 'content'):
            return entry.content[0].value if entry.content else ""
        elif hasattr(entry, 'summary'):
            return entry.summary
        elif hasattr(entry, 'description'):
            return entry.description
        return ""
    
    def save_article(self, category, feed_name, entry):
        """保存文章为 Markdown 文件"""
        title = entry.get('title', 'Untitled')
        published = entry.get('published', datetime.now().isoformat())
        link = entry.get('link', '')
        content = self.extract_content(entry)
        
        # 创建文件名
        date_str = datetime.now().strftime('%Y-%m-%d')
        filename = f"{date_str}-{self.slugify(title)}.md"
        
        # 确定保存路径（先放在 articles 目录，后续人工分类）
        save_dir = self.base_dir / category / "_incoming" / feed_name.lower().replace(' ', '-')
        save_dir.mkdir(parents=True, exist_ok=True)
        
        filepath = save_dir / filename
        
        # 构建 frontmatter
        frontmatter = {
            "type": "article",
            "title": title,
            "source": link,
            "feed": feed_name,
            "published": published,
            "date_collected": datetime.now().isoformat(),
            "category": category,
            "tags": [],
            "language": "en"
        }
        
        # 写入文件
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write("---\n")
            f.write(yaml.dump(frontmatter, allow_unicode=True))
            f.write("---\n\n")
            f.write(f"# {title}\n\n")
            f.write(f"**Source:** [{link}]({link})\n\n")
            f.write(f"**Feed:** {feed_name}\n\n")
            f.write(f"**Published:** {published}\n\n")
            f.write("---\n\n")
            f.write(content)
        
        self.collected.append({
            "category": category,
            "feed": feed_name,
            "title": title,
            "filepath": str(filepath)
        })
        
        print(f"✅ Saved: {filepath}")
        return filepath
    
    def collect_feed(self, category, feed_info):
        """采集单个 RSS 源"""
        try:
            print(f"\n📡 Collecting: {feed_info['name']} ({feed_info['url']})")
            feed = feedparser.parse(feed_info['url'])
            
            if feed.bozo:
                print(f"⚠️ Warning: {feed.bozo_exception}")
            
            entries = feed.entries[:5]  # 只取最新的5条
            print(f"   Found {len(entries)} entries")
            
            for entry in entries:
                self.save_article(category, feed_info['name'], entry)
                
        except Exception as e:
            print(f"❌ Error collecting {feed_info['name']}: {e}")
    
    def run(self):
        """运行采集任务"""
        print("=" * 60)
        print("🚀 RSS Content Collector Starting...")
        print(f"⏰ {datetime.now().isoformat()}")
        print("=" * 60)
        
        for category, feeds in RSS_FEEDS.items():
            print(f"\n📁 Category: {category.upper()}")
            print("-" * 40)
            for feed in feeds:
                self.collect_feed(category, feed)
        
        # 输出统计
        print("\n" + "=" * 60)
        print("📊 Collection Summary")
        print("=" * 60)
        print(f"Total articles collected: {len(self.collected)}")
        
        # 按分类统计
        by_category = {}
        for item in self.collected:
            cat = item['category']
            by_category[cat] = by_category.get(cat, 0) + 1
        
        for cat, count in by_category.items():
            print(f"  {cat}: {count} articles")
        
        return self.collected


if __name__ == "__main__":
    collector = RSSCollector()
    collector.run()
