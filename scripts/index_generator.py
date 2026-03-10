#!/usr/bin/env python3
"""
内容索引生成器
自动扫描所有内容并生成主题索引
"""

import os
import yaml
from pathlib import Path
from collections import defaultdict

class IndexGenerator:
    def __init__(self, base_dir="/root/.openclaw/workspace/anima-base"):
        self.base_dir = Path(base_dir)
        self.index_dir = self.base_dir / "index"
        self.index_dir.mkdir(exist_ok=True)
        
        # 主题关键词映射
        self.topic_keywords = {
            "product-management": ["product", "pm", "product manager", "product management", "product strategy"],
            "product-discovery": ["discovery", "customer interview", "user research", "problem discovery"],
            "growth-strategy": ["growth", "growth hacking", "growth strategy", "growth loop", "viral"],
            "growth-tactics": ["tactics", "experiment", "a/b test", "conversion", "activation"],
            "marketing-positioning": ["positioning", "messaging", "brand", "marketing strategy"],
            "content-marketing": ["content", "content strategy", "storytelling", "copywriting"],
            "leadership": ["leadership", "management", "team building", "culture"],
            "career-development": ["career", "promotion", "ic", "manager", "career growth"],
            "strategy": ["strategy", "strategic", "vision", "roadmap", "planning"],
            "execution": ["execution", "delivery", "shipping", "launch"],
        }
    
    def parse_frontmatter(self, filepath):
        """解析 Markdown 文件的 frontmatter"""
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()
            
            if content.startswith('---'):
                parts = content.split('---', 2)
                if len(parts) >= 3:
                    frontmatter = yaml.safe_load(parts[1])
                    body = parts[2]
                    return frontmatter, body
            return {}, content
        except Exception as e:
            print(f"Error parsing {filepath}: {e}")
            return {}, ""
    
    def categorize_content(self, frontmatter, body):
        """根据内容自动分类主题"""
        topics = []
        text = f"{frontmatter.get('title', '')} {body}".lower()
        
        for topic, keywords in self.topic_keywords.items():
            if any(kw in text for kw in keywords):
                topics.append(topic)
        
        return topics if topics else ["uncategorized"]
    
    def scan_content(self):
        """扫描所有内容文件"""
        content_items = []
        
        # 扫描各个领域目录
        for category in ["product", "marketing", "growth", "leadership"]:
            category_dir = self.base_dir / category
            if not category_dir.exists():
                continue
                
            for person_dir in category_dir.iterdir():
                if not person_dir.is_dir() or person_dir.name.startswith('_'):
                    continue
                    
                person_name = person_dir.name
                
                # 扫描所有子目录中的 .md 文件
                for md_file in person_dir.rglob("*.md"):
                    frontmatter, body = self.parse_frontmatter(md_file)
                    topics = self.categorize_content(frontmatter, body)
                    
                    content_items.append({
                        "title": frontmatter.get("title", "Untitled"),
                        "person": person_name,
                        "category": category,
                        "type": frontmatter.get("type", "unknown"),
                        "source": frontmatter.get("source", ""),
                        "filepath": str(md_file.relative_to(self.base_dir)),
                        "topics": topics,
                        "tags": frontmatter.get("tags", []),
                        "date": frontmatter.get("date", "")
                    })
        
        return content_items
    
    def generate_topic_index(self, topic, items):
        """生成单个主题的索引文件"""
        filepath = self.index_dir / f"{topic}.md"
        
        content = f"""# {topic.replace('-', ' ').title()} Index

> Auto-generated index of content related to **{topic.replace('-', ' ').title()}**
> Last updated: {__import__('datetime').datetime.now().strftime('%Y-%m-%d %H:%M')}

## Contents

"""
        
        # 按类型分组
        by_type = defaultdict(list)
        for item in items:
            by_type[item['type']].append(item)
        
        # 输出各类内容
        type_order = ['profile', 'quotes', 'podcast', 'book', 'article']
        
        for content_type in type_order:
            if content_type not in by_type:
                continue
                
            content += f"### {content_type.replace('-', ' ').title()}s\n\n"
            
            for item in sorted(by_type[content_type], key=lambda x: x['person']):
                content += f"- **[{item['person']}](../{item['filepath']})** - {item['title']}\n"
                if item['source']:
                    content += f"  - Source: [{item['source']}]({item['source']})\n"
            
            content += "\n"
        
        # 统计信息
        content += f"""---

## Statistics

- Total items: **{len(items)}**
"""
        for t, items_list in by_type.items():
            content += f"- {t}s: {len(items_list)}\n"
        
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        
        print(f"✅ Generated: {filepath}")
    
    def generate_master_index(self, all_items):
        """生成主索引文件"""
        filepath = self.index_dir / "README.md"
        
        # 按主题分组
        by_topic = defaultdict(list)
        for item in all_items:
            for topic in item['topics']:
                by_topic[topic].append(item)
        
        content = f"""# Anima Base Content Index

> Complete index of all collected content
> Last updated: {__import__('datetime').datetime.now().strftime('%Y-%m-%d %H:%M')}

## Quick Navigation

"""
        
        # 主题索引
        for topic in sorted(by_topic.keys()):
            count = len(by_topic[topic])
            content += f"- [{topic.replace('-', ' ').title()}](./{topic}.md) - {count} items\n"
        
        content += """
## Browse by Category

"""
        
        # 按分类统计
        by_category = defaultdict(list)
        for item in all_items:
            by_category[item['category']].append(item)
        
        for category in ['product', 'marketing', 'growth', 'leadership']:
            if category in by_category:
                items = by_category[category]
                people = set(item['person'] for item in items)
                content += f"### {category.title()} ({len(people)} people, {len(items)} items)\n\n"
                
                for person in sorted(people):
                    person_items = [i for i in items if i['person'] == person]
                    content += f"- [{person}](../{category}/{person}/) - {len(person_items)} items\n"
                
                content += "\n"
        
        # 总体统计
        content += f"""---

## Overall Statistics

- **Total Items**: {len(all_items)}
- **Total People**: {len(set(item['person'] for item in all_items))}
- **Categories**: {len(by_category)}
- **Topics**: {len(by_topic)}

### By Type

"""
        by_type = defaultdict(list)
        for item in all_items:
            by_type[item['type']].append(item)
        
        for t, items in sorted(by_type.items(), key=lambda x: -len(x[1])):
            content += f"- {t}: {len(items)}\n"
        
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        
        print(f"✅ Generated: {filepath}")
    
    def run(self):
        """运行索引生成"""
        print("=" * 60)
        print("📚 Index Generator Starting...")
        print("=" * 60)
        
        # 扫描内容
        print("\n🔍 Scanning content...")
        all_items = self.scan_content()
        print(f"   Found {len(all_items)} content items")
        
        # 按主题分组
        by_topic = defaultdict(list)
        for item in all_items:
            for topic in item['topics']:
                by_topic[topic].append(item)
        
        # 生成各主题索引
        print("\n📝 Generating topic indexes...")
        for topic, items in by_topic.items():
            self.generate_topic_index(topic, items)
        
        # 生成主索引
        print("\n📖 Generating master index...")
        self.generate_master_index(all_items)
        
        print("\n" + "=" * 60)
        print("✅ Index generation complete!")
        print("=" * 60)


if __name__ == "__main__":
    generator = IndexGenerator()
    generator.run()
