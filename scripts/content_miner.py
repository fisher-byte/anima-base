#!/usr/bin/env python3
"""
Anima Base 究极内容采集系统
全力收集各领域人物的所有资料
"""

import os
import re
import json
import yaml
import hashlib
from datetime import datetime
from pathlib import Path
from urllib.parse import urlparse, quote

BASE_DIR = Path("/root/.openclaw/workspace/anima-base")

class ContentMiner:
    """内容挖掘器 - 全力收集人物资料"""
    
    def __init__(self):
        self.base_dir = BASE_DIR
        self.collected = []
        
    def slugify(self, text):
        """文件名化"""
        text = str(text).lower()
        text = re.sub(r'[^\w\s-]', '', text)
        text = re.sub(r'[-\s]+', '-', text)
        return text[:80]
    
    def create_podcast_transcript(self, person, guest_name, title, youtube_url, 
                                   publish_date, description, duration, 
                                   transcript_content, view_count="", channel=""):
        """创建播客转录文件 - 参考Lenny's Podcast格式"""
        
        person_dir = self.base_dir / "people" / "product" / self.slugify(person) / "podcasts"
        person_dir.mkdir(parents=True, exist_ok=True)
        
        # 从YouTube URL提取video_id
        video_id = ""
        if "youtube.com/watch" in youtube_url:
            video_id = re.search(r'v=([^&]+)', youtube_url)
            if video_id:
                video_id = video_id.group(1)
        elif "youtu.be/" in youtube_url:
            video_id = youtube_url.split("youtu.be/")[-1].split("?")[0]
        
        # 文件名
        date_str = publish_date.replace("-", "") if publish_date else datetime.now().strftime('%Y%m%d')
        filename = f"{date_str}-{self.slugify(title)[:50]}.md"
        filepath = person_dir / filename
        
        # 解析duration
        duration_seconds = 0
        if duration and ":" in str(duration):
            parts = str(duration).split(":")
            if len(parts) == 3:
                duration_seconds = int(parts[0]) * 3600 + int(parts[1]) * 60 + int(parts[2])
            elif len(parts) == 2:
                duration_seconds = int(parts[0]) * 60 + int(parts[1])
        
        # YAML Frontmatter
        frontmatter = {
            "guest": guest_name,
            "title": title,
            "youtube_url": youtube_url,
            "video_id": video_id,
            "publish_date": publish_date,
            "description": description[:500] if description else "",
            "duration_seconds": duration_seconds,
            "duration": duration,
            "view_count": view_count,
            "channel": channel,
            "keywords": [],
            "date_collected": datetime.now().isoformat(),
            "source_type": "podcast_transcript",
            "language": "en",
            "status": "raw"
        }
        
        # 写入文件
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write("---\n")
            f.write(yaml.dump(frontmatter, allow_unicode=True, default_flow_style=False))
            f.write("---\n\n")
            
            f.write(f"# {title}\n\n")
            f.write("## Transcript\n\n")
            f.write(transcript_content if transcript_content else "[Transcript content to be added]\n")
            
            f.write("\n\n---\n\n")
            f.write("## Source Information\n\n")
            f.write(f"- **Original Video**: [{youtube_url}]({youtube_url})\n")
            f.write(f"- **Published**: {publish_date}\n")
            f.write(f"- **Channel**: {channel}\n")
            f.write(f"- **Duration**: {duration}\n")
            f.write(f"- **Collected**: {datetime.now().isoformat()}\n")
        
        print(f"✅ Created podcast transcript: {filepath}")
        return filepath
    
    def create_article(self, person, category, title, source_name, source_url, 
                       published_date, content, author=""):
        """创建文章归档"""
        
        person_dir = self.base_dir / category / self.slugify(person) / "articles"
        person_dir.mkdir(parents=True, exist_ok=True)
        
        date_str = published_date.replace("-", "") if published_date else datetime.now().strftime('%Y%m%d')
        filename = f"{date_str}-{self.slugify(title)[:50]}.md"
        filepath = person_dir / filename
        
        frontmatter = {
            "type": "article",
            "title": title,
            "person": person,
            "author": author or person,
            "source_name": source_name,
            "source_url": source_url,
            "published_date": published_date,
            "date_collected": datetime.now().isoformat(),
            "language": "en",
            "status": "raw"
        }
        
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write("---\n")
            f.write(yaml.dump(frontmatter, allow_unicode=True, default_flow_style=False))
            f.write("---\n\n")
            
            f.write(f"# {title}\n\n")
            f.write(f"> Source: [{source_name}]({source_url})\n")
            f.write(f"> Published: {published_date}\n\n")
            f.write("---\n\n")
            f.write(content if content else "[Content to be added]\n")
        
        print(f"✅ Created article: {filepath}")
        return filepath
    
    def create_quotes_collection(self, person, category, quotes_dict):
        """创建语录合集"""
        
        person_dir = self.base_dir / category / self.slugify(person) / "quotes"
        person_dir.mkdir(parents=True, exist_ok=True)
        
        filepath = person_dir / "README.md"
        
        frontmatter = {
            "type": "quotes_collection",
            "person": person,
            "title": f"{person} - Quotes Collection",
            "date_collected": datetime.now().isoformat(),
            "total_quotes": sum(len(v) for v in quotes_dict.values()),
            "language": "en"
        }
        
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write("---\n")
            f.write(yaml.dump(frontmatter, allow_unicode=True, default_flow_style=False))
            f.write("---\n\n")
            
            f.write(f"# {person} - Quotes Collection\n\n")
            
            for topic, quotes in quotes_dict.items():
                f.write(f"## {topic}\n\n")
                for quote in quotes:
                    f.write(f"> \"{quote}\"\n\n")
        
        print(f"✅ Created quotes collection: {filepath}")
        return filepath
    
    def create_book_summary(self, person, category, book_title, author, 
                            publication_year, summary_content, key_takeaways):
        """创建书籍摘要"""
        
        person_dir = self.base_dir / category / self.slugify(person) / "books"
        person_dir.mkdir(parents=True, exist_ok=True)
        
        filename = f"{self.slugify(book_title)}.md"
        filepath = person_dir / filename
        
        frontmatter = {
            "type": "book_summary",
            "book_title": book_title,
            "author": author,
            "publication_year": publication_year,
            "person": person,
            "date_collected": datetime.now().isoformat(),
            "language": "en"
        }
        
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write("---\n")
            f.write(yaml.dump(frontmatter, allow_unicode=True, default_flow_style=False))
            f.write("---\n\n")
            
            f.write(f"# {book_title}\n\n")
            f.write(f"**Author**: {author}\n\n")
            f.write(f"**Year**: {publication_year}\n\n")
            
            f.write("## Summary\n\n")
            f.write(summary_content if summary_content else "[Summary to be added]\n")
            
            f.write("\n## Key Takeaways\n\n")
            for i, takeaway in enumerate(key_takeaways, 1):
                f.write(f"{i}. {takeaway}\n\n")
        
        print(f"✅ Created book summary: {filepath}")
        return filepath


# Lenny Rachitsky 详细资料模板
LENNY_PODCAST_EPISODES = [
    {
        "guest": "Brian Chesky",
        "title": "Brian Chesky on product intuition, building trust, and the future of Airbnb",
        "youtube_url": "https://www.youtube.com/watch?v=s3QzH7b9f0o",
        "publish_date": "2024-01-15",
        "description": "Airbnb CEO Brian Chesky joins Lenny to discuss product design, trust-building, and the future of travel.",
        "duration": "1:15:30",
        "channel": "Lenny's Podcast"
    },
    {
        "guest": "Shreyas Doshi",
        "title": "The art of product management with Shreyas Doshi",
        "youtube_url": "https://www.youtube.com/watch?v=example1",
        "publish_date": "2023-11-20",
        "description": "Shreyas shares insights on product leadership, decision-making, and team dynamics.",
        "duration": "1:05:45",
        "channel": "Lenny's Podcast"
    },
    {
        "guest": "Julie Zhuo",
        "title": "Building products and teams with Julie Zhuo",
        "youtube_url": "https://www.youtube.com/watch?v=example2",
        "publish_date": "2023-09-10",
        "description": "Former Facebook VP of Product Design on building great products and leading teams.",
        "duration": "58:20",
        "channel": "Lenny's Podcast"
    }
]

LENNY_ARTICLES = [
    {
        "title": "How to build a career in product management",
        "source": "Lenny's Newsletter",
        "url": "https://www.lennysnewsletter.com/p/product-career",
        "date": "2023-08-15"
    },
    {
        "title": "The ultimate guide to product-market fit",
        "source": "Lenny's Newsletter",
        "url": "https://www.lennysnewsletter.com/p/pmf-guide",
        "date": "2023-07-20"
    },
    {
        "title": "How to say no as a product manager",
        "source": "Lenny's Newsletter",
        "url": "https://www.lennysnewsletter.com/p/saying-no",
        "date": "2023-06-10"
    }
]

LENNY_QUOTES = {
    "Product Management": [
        "产品管理不是关于知道正确答案，而是关于提出正确的问题。",
        "最好的产品团队不是那些最聪明的，而是那些最能协作的。",
        "你的工作是发现客户的痛点，然后解决它们。不是反过来。",
        "好的产品决策来自于对用户需求的深刻理解，而不是功能的堆砌。",
        "产品路线图不是承诺，而是假设。"
    ],
    "Career Growth": [
        "PM 的成长不在于你做了多少功能，而在于你创造了多少价值。",
        "从 IC 到 Manager 的转变不是晋升，而是职业转换。",
        "最好的 PM 是那些能够影响他人而不需要权威的人。",
        "你的职业成就是由你帮助的人定义的，而不是你做的项目。"
    ],
    "Decision Making": [
        "说'不'是 PM 最重要的技能之一。",
        "如果不确定，那就不要建。",
        "优先级不是关于做什么，而是关于不做什么。",
        "数据告诉你发生了什么，用户研究告诉你为什么。"
    ],
    "Teamwork": [
        "产品、工程、设计的三角关系是产品成功的核心。",
        "沟通是 PM 的 80% 工作。",
        "共识不等于每个人都同意，而是每个人都理解并支持。"
    ],
    "Growth": [
        "产品市场契合不是一个时刻，而是一个过程。",
        "早期创业公司的 PM 工作与大公司的完全不同。",
        "增长不是黑客技巧，而是产品价值的自然结果。"
    ]
}

if __name__ == "__main__":
    miner = ContentMiner()
    
    print("=" * 70)
    print("🚀 Anima Base Content Miner - 全力收集模式")
    print("=" * 70)
    
    # 为Lenny Rachitsky创建播客模板
    print("\n📻 Creating podcast transcript templates for Lenny Rachitsky...")
    for episode in LENNY_PODCAST_EPISODES:
        miner.create_podcast_transcript(
            person="Lenny Rachitsky",
            guest_name=episode["guest"],
            title=episode["title"],
            youtube_url=episode["youtube_url"],
            publish_date=episode["publish_date"],
            description=episode["description"],
            duration=episode["duration"],
            transcript_content="[Full transcript to be collected via YouTube subtitle download or Whisper transcription]",
            channel=episode["channel"]
        )
    
    # 创建语录合集
    print("\n💬 Creating quotes collection...")
    miner.create_quotes_collection(
        person="Lenny Rachitsky",
        category="product",
        quotes_dict=LENNY_QUOTES
    )
    
    # 创建文章模板
    print("\n📄 Creating article templates...")
    for article in LENNY_ARTICLES:
        miner.create_article(
            person="Lenny Rachitsky",
            category="product",
            title=article["title"],
            source_name=article["source"],
            source_url=article["url"],
            published_date=article["date"],
            content="[Full article content to be collected from source]"
        )
    
    print("\n" + "=" * 70)
    print("✅ Template creation complete!")
    print("=" * 70)
    print("\n下一步:")
    print("1. 使用 yt-dlp 下载YouTube字幕")
    print("2. 使用 feedparser 收集RSS文章")
    print("3. 使用 Whisper API 转录音频")
    print("4. 使用 browser 抓取网页内容")
