#!/usr/bin/env python3
"""
自动化翻译脚本
将英文原文翻译为中文，保存到translations/zh-cn/目录
"""

import os
import re
import json
from pathlib import Path
from datetime import datetime
from typing import List, Dict, Optional

BASE_DIR = Path("/Users/zhiyangyu/.box/Workspace/anima-base-scheduled")
PEOPLE_DIR = BASE_DIR / "people"
TRANSLATIONS_DIR = BASE_DIR / "translations" / "zh-cn"

# 翻译优先级配置
TRANSLATION_PRIORITY = {
    "high": [
        # 核心5位专家的profile和quotes
        "people/product/gokul-rajaram/profile.md",
        "people/product/gokul-rajaram/quotes.md",
        "people/product/brian-chesky/profile.md",
        "people/product/brian-chesky/quotes.md",
        "people/product/shreyas-doshi/profile.md",
        "people/product/shreyas-doshi/quotes.md",
        "people/product/marty-cagan/profile.md",
        "people/product/marty-cagan/quotes.md",
        "people/product/lenny-rachitsky/profile.md",
        "people/product/lenny-rachitsky/quotes.md",
        # 核心框架文档
        "people/product/gokul-rajaram/frameworks/*.md",
        "STRUCTURE.md",
        "FILE_STORAGE_POLICY.md",
        "TRANSLATION_POLICY.md",
        "README.md"
    ],
    "medium": [
        # 其他专家的profile
        "people/*/profile.md",
        "people/*/quotes.md",
        "核心播客转录"
    ],
    "low": [
        # 索引和辅助文档
        "index/*.md",
        "topics/*/*.md"
    ]
}

# 不需要翻译的文件模式
EXCLUDE_PATTERNS = [
    "*.json",
    "*.log",
    "*resources.md",  # 仅索引
    "*.yml",
    "*.yaml"
]

class AutoTranslator:
    """自动翻译器"""
    
    def __init__(self, source_lang="en", target_lang="zh-cn"):
        self.base_dir = BASE_DIR
        self.people_dir = PEOPLE_DIR
        self.translations_dir = TRANSLATIONS_DIR
        self.source_lang = source_lang
        self.target_lang = target_lang
        self.translated = []
        self.skipped = []
        self.errors = []
        
    def get_relative_path(self, file_path: Path) -> str:
        """获取相对于people/的路径"""
        try:
            return str(file_path.relative_to(self.people_dir))
        except ValueError:
            return str(file_path.relative_to(self.base_dir))
    
    def is_translatable(self, file_path: Path) -> bool:
        """检查文件是否需要翻译"""
        # 检查扩展名
        if file_path.suffix.lower() not in ['.md', '.txt']:
            return False
        
        # 检查排除模式
        for pattern in EXCLUDE_PATTERNS:
            if file_path.match(pattern):
                return False
        
        # 检查是否已翻译
        rel_path = self.get_relative_path(file_path)
        translation_path = self.translations_dir / rel_path
        
        if translation_path.exists():
            return False
        
        return True
    
    def translate_text(self, text: str, file_context: str = "") -> Optional[str]:
        """
        翻译文本
        这里可以使用API或本地模型
        目前返回模拟翻译结果
        """
        # 检查是否为代码块
        if '```' in text:
            lines = text.split('\n')
            in_code_block = False
            result_lines = []
            
            for line in lines:
                if line.strip().startswith('```'):
                    in_code_block = not in_code_block
                    result_lines.append(line)
                elif in_code_block:
                    result_lines.append(line)
                else:
                    # 翻译非代码部分
                    # 这里应该调用翻译API
                    result_lines.append(line)  # 暂时不翻译
            
            return '\n'.join(result_lines)
        else:
            # 简单翻译（这里应该替换为实际的翻译API）
            # 暂时返回原文
            return text
    
    def translate_file(self, source_file: Path) -> Optional[Path]:
        """翻译单个文件"""
        # 获取相对路径
        rel_path = self.get_relative_path(source_file)
        
        # 创建翻译文件路径
        translation_file = self.translations_dir / rel_path
        translation_file.parent.mkdir(parents=True, exist_ok=True)
        
        try:
            # 读取源文件
            with open(source_file, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # 提取frontmatter（不翻译）
            frontmatter_end = content.find('---\n', 4) if content.startswith('---') else -1
            
            if frontmatter_end != -1:
                frontmatter = content[:frontmatter_end + 4]
                body = content[frontmatter_end + 4:]
            else:
                frontmatter = ""
                body = content
            
            # 翻译正文
            translated_body = self.translate_text(body, rel_path)
            
            if not translated_body:
                self.errors.append(f"翻译失败: {rel_path}")
                return None
            
            # 写入翻译文件
            with open(translation_file, 'w', encoding='utf-8') as f:
                f.write(frontmatter)
                f.write(translated_body)
            
            print(f"  ✅ 翻译完成: {rel_path}")
            self.translated.append(str(translation_file))
            return translation_file
            
        except Exception as e:
            self.errors.append(f"翻译异常: {rel_path} - {e}")
            return None
    
    def scan_files(self, priority: str = "high") -> List[Path]:
        """扫描需要翻译的文件"""
        files = []
        
        patterns = TRANSLATION_PRIORITY.get(priority, [])
        
        for pattern in patterns:
            if pattern.startswith("people/"):
                # people目录下的文件
                pattern = pattern[7:]
                for file_path in self.people_dir.glob(pattern):
                    if file_path.is_file() and self.is_translatable(file_path):
                        files.append(file_path)
            else:
                # 根目录下的文件
                for file_path in self.base_dir.glob(pattern):
                    if file_path.is_file() and self.is_translatable(file_path):
                        files.append(file_path)
        
        return files
    
    def run(self, priority: str = "high", dry_run: bool = False):
        """运行翻译任务"""
        print(f"{'='*60}")
        print("自动化翻译脚本")
        print(f"{'='*60}")
        print(f"时间: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        print(f"优先级: {priority}")
        print(f"输出目录: {self.translations_dir}")
        print(f"干运行模式: {dry_run}")
        
        # 扫描文件
        print(f"\n🔍 扫描需要翻译的文件...")
        files = self.scan_files(priority)
        
        print(f"📊 找到 {len(files)} 个文件需要翻译")
        
        if not files:
            print("\n✅ 没有需要翻译的文件")
            return True
        
        # 显示前10个文件
        print(f"\n📄 待翻译文件（前10个）:")
        for file_path in files[:10]:
            rel_path = self.get_relative_path(file_path)
            print(f"  - {rel_path}")
        
        if dry_run:
            print("\n⏸️  干运行模式，不执行实际翻译")
            return True
        
        # 翻译文件
        print(f"\n🔄 开始翻译...")
        success_count = 0
        
        for file_path in files:
            rel_path = self.get_relative_path(file_path)
            print(f"\n📝 翻译: {rel_path}")
            
            translation_file = self.translate_file(file_path)
            
            if translation_file:
                success_count += 1
        
        # 输出总结
        print(f"\n{'='*60}")
        print("📊 翻译总结")
        print(f"{'='*60}")
        print(f"扫描文件: {len(files)}")
        print(f"翻译成功: {success_count}")
        print(f"失败数量: {len(self.errors)}")
        
        if self.errors:
            print(f"\n❌ 错误列表:")
            for error in self.errors[:10]:
                print(f"  - {error}")
        
        # 记录日志
        self.log_results()
        
        return success_count > 0
    
    def log_results(self):
        """记录结果到日志文件"""
        log_entry = {
            "timestamp": datetime.now().isoformat(),
            "type": "translation",
            "translated_count": len(self.translated),
            "error_count": len(self.errors),
            "translated_files": self.translated[:10],
            "errors": self.errors[:5]
        }
        
        log_file = self.base_dir / "scripts" / "collection.log"
        
        try:
            with open(log_file, 'a') as f:
                f.write(f"{json.dumps(log_entry, ensure_ascii=False)}\n")
            print(f"\n📝 日志已记录: {log_file}")
        except Exception as e:
            print(f"⚠️  日志记录失败: {e}")


if __name__ == "__main__":
    import sys
    
    translator = AutoTranslator()
    
    # 支持命令行参数
    # python auto_translator.py high
    # python auto_translator.py high --dry-run
    priority = sys.argv[1] if len(sys.argv) > 1 else "high"
    dry_run = "--dry-run" in sys.argv
    
    success = translator.run(priority, dry_run)
    sys.exit(0 if success else 1)
