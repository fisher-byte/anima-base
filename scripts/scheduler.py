#!/usr/bin/env python3
"""
定时任务调度器
管理所有自动化任务的定时执行
"""

import os
import json
from pathlib import Path
from datetime import datetime
from subprocess import run, PIPE

BASE_DIR = Path("/Users/zhiyangyu/.box/Workspace/anima-base-scheduled")
LOG_DIR = BASE_DIR / "scripts" / "logs"

# 定时任务配置
SCHEDULED_TASKS = {
    # 每日任务 - 早上8点
    "daily_rss_collect": {
        "name": "RSS文章采集",
        "script": "rss_article_downloader.py",
        "args": "",
        "schedule": "0 8 * * *",  # cron格式: 分 时 日 月 周
        "enabled": True,
        "priority": "high",
        "description": "从RSS源下载新文章"
    },
    
    # 每日任务 - 早上9点
    "daily_youtube_collect": {
        "name": "YouTube字幕采集",
        "script": "youtube_subtitle_downloader.py",
        "args": "lenny-rachitsky,brian-chesky,shreyas-doshi,marty-cagan,gokul-rajaram",
        "schedule": "0 9 * * *",
        "enabled": False,  # 需要安装yt-dlp
        "priority": "high",
        "description": "下载YouTube视频字幕"
    },
    
    # 每周任务 - 周日下午2点
    "weekly_podcast_collect": {
        "name": "播客音频采集",
        "script": "podcast_audio_downloader.py",
        "args": "lennys-podcast",
        "schedule": "0 14 * * 0",
        "enabled": False,  # 需要安装yt-dlp
        "priority": "medium",
        "description": "下载新播客音频"
    },
    
    # 每周任务 - 周日晚上8点
    "weekly_translation": {
        "name": "文档翻译",
        "script": "auto_translator.py",
        "args": "high",
        "schedule": "0 20 * * 0",
        "enabled": False,  # 需要配置翻译API
        "priority": "medium",
        "description": "翻译核心文档"
    },
    
    # 每15分钟
    "github_sync": {
        "name": "GitHub同步",
        "script": "../scripts/sync-github.sh",
        "args": "",
        "schedule": "*/15 * * * *",
        "enabled": True,
        "priority": "low",
        "description": "每15分钟同步到GitHub"
    },
    
    # 每月1号
    "monthly_cleanup": {
        "name": "月度清理",
        "script": "maintenance.py",
        "args": "--cleanup",
        "schedule": "0 0 1 * *",
        "enabled": True,
        "priority": "low",
        "description": "清理旧日志，生成报告"
    }
}

class TaskScheduler:
    """任务调度器"""
    
    def __init__(self):
        self.base_dir = BASE_DIR
        self.scripts_dir = self.base_dir / "scripts"
        self.log_dir = LOG_DIR
        self.log_dir.mkdir(exist_ok=True)
        
    def execute_task(self, task_key, task_config):
        """执行单个任务"""
        task_name = task_config["name"]
        script_name = task_config["script"]
        args = task_config.get("args", "")
        
        print(f"\n{'='*60}")
        print(f"📅 执行任务: {task_name} ({task_key})")
        print(f"{'='*60}")
        print(f"时间: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        print(f"脚本: {script_name}")
        print(f"参数: {args}")
        
        # 构建脚本路径
        if script_name.startswith("./") or script_name.startswith("../"):
            script_path = self.base_dir / script_name
        else:
            script_path = self.scripts_dir / script_name
        
        if not script_path.exists():
            print(f"❌ 脚本不存在: {script_path}")
            return False
        
        # 执行脚本
        try:
            if script_path.suffix == '.py':
                cmd = ["python3", str(script_path)]
            else:
                cmd = ["bash", str(script_path)]
            
            if args:
                cmd.extend(args.split())
            
            print(f"\n🚀 执行命令:")
            print(f"   {' '.join(cmd)}")
            
            # 创建日志文件
            log_file = self.log_dir / f"{task_key}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.log"
            
            # 执行并记录输出
            result = run(
                cmd,
                cwd=self.scripts_dir,
                stdout=PIPE,
                stderr=PIPE,
                text=True
            )
            
            # 保存日志
            with open(log_file, 'w') as f:
                f.write(f"Task: {task_name}\n")
                f.write(f"Command: {' '.join(cmd)}\n")
                f.write(f"Time: {datetime.now().isoformat()}\n")
                f.write(f"\n{'='*60}\n")
                f.write("STDOUT:\n")
                f.write(result.stdout)
                f.write(f"\n{'='*60}\n")
                f.write("STDERR:\n")
                f.write(result.stderr)
                f.write(f"\n{'='*60}\n")
                f.write(f"Return Code: {result.returncode}\n")
            
            if result.returncode == 0:
                print(f"\n✅ 任务执行成功")
                print(f"📝 日志: {log_file}")
                return True
            else:
                print(f"\n❌ 任务执行失败")
                print(f"📝 日志: {log_file}")
                return False
                
        except Exception as e:
            print(f"\n❌ 任务执行异常: {e}")
            return False
    
    def run_task(self, task_key):
        """运行指定任务"""
        if task_key not in SCHEDULED_TASKS:
            print(f"❌ 任务不存在: {task_key}")
            return False
        
        task_config = SCHEDULED_TASKS[task_key]
        
        if not task_config.get("enabled", False):
            print(f"⏸️  任务已禁用: {task_key}")
            return False
        
        return self.execute_task(task_key, task_config)
    
    def run_all(self):
        """运行所有启用的任务"""
        print(f"\n{'='*60}")
        print("🚀 运行所有启用的任务")
        print(f"{'='*60}")
        
        success_count = 0
        total_count = 0
        
        for task_key, task_config in SCHEDULED_TASKS.items():
            if task_config.get("enabled", False):
                total_count += 1
                if self.run_task(task_key):
                    success_count += 1
        
        print(f"\n{'='*60}")
        print("📊 任务执行总结")
        print(f"{'='*60}")
        print(f"总任务数: {total_count}")
        print(f"成功: {success_count}")
        print(f"失败: {total_count - success_count}")
        
        return success_count == total_count
    
    def list_tasks(self):
        """列出所有任务"""
        print(f"\n{'='*60}")
        print("📋 定时任务列表")
        print(f"{'='*60}")
        
        for task_key, task_config in SCHEDULED_TASKS.items():
            status = "✅ 启用" if task_config.get("enabled") else "⏸️  禁用"
            priority = task_config.get("priority", "low")
            schedule = task_config.get("schedule", "-")
            
            print(f"\n{task_key}:")
            print(f"  名称: {task_config['name']}")
            print(f"  状态: {status}")
            print(f"  优先级: {priority}")
            print(f"  定时: {schedule}")
            print(f"  描述: {task_config.get('description', '')}")
    
    def generate_cron(self):
        """生成cron配置"""
        print(f"\n{'='*60}")
        print("📅 Cron配置生成")
        print(f"{'='*60}")
        
        for task_key, task_config in SCHEDULED_TASKS.items():
            if task_config.get("enabled"):
                schedule = task_config.get("schedule")
                script_name = task_config.get("script")
                args = task_config.get("args", "")
                
                if script_name.startswith("./") or script_name.startswith("../"):
                    script_path = f"{self.base_dir}/{script_name}"
                else:
                    script_path = f"{self.scripts_dir}/{script_name}"
                
                if args:
                    cron_line = f"{schedule} cd {self.scripts_dir} && python3 {script_name} {args} >> {self.log_dir}/{task_key}.log 2>&1"
                else:
                    cron_line = f"{schedule} cd {self.scripts_dir} && python3 {script_name} >> {self.log_dir}/{task_key}.log 2>&1"
                
                print(f"\n# {task_config['name']}")
                print(cron_line)
        
        print(f"\n{'='*60}")
        print("💡 提示:")
        print("   1. 使用 'crontab -e' 编辑crontab")
        print("   2. 将上述配置添加到crontab")
        print("   3. 确保脚本有执行权限: chmod +x scripts/*.py")


if __name__ == "__main__":
    import sys
    
    scheduler = TaskScheduler()
    
    if len(sys.argv) == 1:
        # 无参数，列出任务
        scheduler.list_tasks()
    elif sys.argv[1] == "list":
        scheduler.list_tasks()
    elif sys.argv[1] == "run-all":
        scheduler.run_all()
    elif sys.argv[1] == "run":
        if len(sys.argv) > 2:
            scheduler.run_task(sys.argv[2])
        else:
            print("用法: python scheduler.py run <task_key>")
    elif sys.argv[1] == "cron":
        scheduler.generate_cron()
    else:
        # 运行指定任务
        scheduler.run_task(sys.argv[1])
