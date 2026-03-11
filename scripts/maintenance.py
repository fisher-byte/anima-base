#!/usr/bin/env python3
"""
维护脚本
清理旧日志、生成报告、检查健康状态
"""

import os
import json
import shutil
from pathlib import Path
from datetime import datetime, timedelta
from collections import defaultdict

BASE_DIR = Path("/Users/zhiyangyu/.box/Workspace/anima-base-scheduled")
LOG_DIR = BASE_DIR / "scripts" / "logs"
MEDIA_DIR = BASE_DIR / "media"
FILES_DIR = BASE_DIR / "files"
PEOPLE_DIR = BASE_DIR / "people"
TRANSLATIONS_DIR = BASE_DIR / "translations"
REPORT_DIR = BASE_DIR / "output" / "reports"

class MaintenanceManager:
    """维护管理器"""
    
    def __init__(self):
        self.base_dir = BASE_DIR
        self.log_dir = LOG_DIR
        self.media_dir = MEDIA_DIR
        self.files_dir = FILES_DIR
        self.people_dir = PEOPLE_DIR
        self.translations_dir = TRANSLATIONS_DIR
        self.report_dir = REPORT_DIR
        self.report_dir.mkdir(parents=True, exist_ok=True)
        
    def cleanup_old_logs(self, days=30):
        """清理旧日志"""
        print(f"\n🧹 清理 {days} 天前的旧日志...")
        
        cutoff_date = datetime.now() - timedelta(days=days)
        deleted_count = 0
        
        for log_file in self.log_dir.glob("*.log"):
            if log_file.is_file():
                file_time = datetime.fromtimestamp(log_file.stat().st_mtime)
                if file_time < cutoff_date:
                    try:
                        log_file.unlink()
                        deleted_count += 1
                        print(f"  删除: {log_file.name}")
                    except Exception as e:
                        print(f"  ⚠️  删除失败: {log_file.name} - {e}")
        
        print(f"✅ 清理完成: {deleted_count} 个文件")
        return deleted_count
    
    def count_files(self):
        """统计各类文件数量"""
        print(f"\n📊 文件统计...")
        
        stats = {
            "media_audio_youtube": len(list((self.media_dir / "audio" / "youtube").rglob("*"))) if (self.media_dir / "audio" / "youtube").exists() else 0,
            "media_audio_podcast": len(list((self.media_dir / "audio" / "podcast").rglob("*"))) if (self.media_dir / "audio" / "podcast").exists() else 0,
            "files_html": len(list(self.files_dir.rglob("*.html"))),
            "files_pdf": len(list(self.files_dir.rglob("*.pdf"))),
            "people_profiles": len(list(self.people_dir.rglob("profile.md"))),
            "people_quotes": len(list(self.people_dir.rglob("quotes.md"))),
            "people_articles": len(list(self.people_dir.rglob("articles/*.md"))),
            "people_podcasts": len(list(self.people_dir.rglob("podcasts/*.md"))),
            "translations_zh_cn": len(list(self.translations_dir.rglob("*.md"))) if self.translations_dir.exists() else 0,
        }
        
        for category, count in stats.items():
            print(f"  {category}: {count}")
        
        return stats
    
    def check_health(self):
        """检查系统健康状态"""
        print(f"\n🏥 系统健康检查...")
        
        issues = []
        
        # 检查目录
        required_dirs = [self.media_dir, self.files_dir, self.people_dir]
        for dir_path in required_dirs:
            if not dir_path.exists():
                issues.append(f"目录不存在: {dir_path}")
        
        # 检查日志文件
        if not self.log_dir.exists():
            issues.append(f"日志目录不存在: {self.log_dir}")
        
        # 检查核心人物
        core_people = [
            "lenny-rachitsky",
            "brian-chesky",
            "shreyas-doshi",
            "marty-cagan",
            "gokul-rajaram"
        ]
        
        for person in core_people:
            person_dir = self.people_dir / "product" / person
            if not person_dir.exists():
                person_dir = self.people_dir / "growth" / person
                if not person_dir.exists():
                    issues.append(f"人物目录缺失: {person}")
            else:
                # 检查profile.md
                profile = person_dir / "profile.md"
                if not profile.exists():
                    issues.append(f"Profile缺失: {person}")
        
        # 检查翻译
        if self.translations_dir.exists():
            translation_count = len(list(self.translations_dir.rglob("*.md")))
            if translation_count == 0:
                issues.append("翻译目录为空")
        
        # 输出结果
        if not issues:
            print("✅ 系统健康，无问题")
            return True
        else:
            print(f"⚠️  发现 {len(issues)} 个问题:")
            for issue in issues[:20]:
                print(f"  - {issue}")
            return False
    
    def generate_report(self):
        """生成执行报告"""
        print(f"\n📝 生成执行报告...")
        
        report = {
            "timestamp": datetime.now().isoformat(),
            "stats": self.count_files(),
            "health": self.check_health(),
            "recent_activity": self.get_recent_activity()
        }
        
        # 保存报告
        report_file = self.report_dir / f"report_{datetime.now().strftime('%Y%m%d')}.json"
        with open(report_file, 'w') as f:
            json.dump(report, f, indent=2)
        
        print(f"✅ 报告已生成: {report_file}")
        return report
    
    def get_recent_activity(self):
        """获取最近活动"""
        print(f"\n📅 最近活动...")
        
        activity = []
        
        # 分析collection.log
        log_file = self.base_dir / "scripts" / "collection.log"
        if log_file.exists():
            try:
                with open(log_file, 'r') as f:
                    for line in f:
                        try:
                            entry = json.loads(line)
                            activity.append(entry)
                        except json.JSONDecodeError:
                            continue
            except Exception as e:
                print(f"  ⚠️  读取日志失败: {e}")
        
        # 按类型统计
        activity_by_type = defaultdict(int)
        for entry in activity[-50:]:  # 最近50条
            activity_type = entry.get("type", "unknown")
            activity_by_type[activity_type] += 1
        
        print("  最近活动统计（最近50条）:")
        for activity_type, count in activity_by_type.items():
            print(f"    {activity_type}: {count}")
        
        return dict(activity_by_type)
    
    def run(self, args=None):
        """运行维护任务"""
        print(f"{'='*60}")
        print("维护脚本")
        print(f"{'='*60}")
        print(f"时间: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        
        if not args or "--cleanup" in args:
            self.cleanup_old_logs()
        
        if not args or "--stats" in args:
            self.count_files()
        
        if not args or "--health" in args:
            self.check_health()
        
        if not args or "--report" in args:
            self.generate_report()
        
        print(f"\n{'='*60}")
        print("✅ 维护任务完成")
        print(f"{'='*60}")


if __name__ == "__main__":
    import sys
    
    manager = MaintenanceManager()
    
    args = sys.argv[1:] if len(sys.argv) > 1 else None
    manager.run(args)
