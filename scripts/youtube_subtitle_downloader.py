#!/usr/bin/env python3
"""
YouTube字幕下载器
下载指定人物的所有YouTube视频字幕，保存为原文
"""

import os
import json
import re
from pathlib import Path
from datetime import datetime
from urllib.parse import urlparse
import subprocess

BASE_DIR = Path("/Users/zhiyangyu/.box/Workspace/anima-base-scheduled")
MEDIA_DIR = BASE_DIR / "media" / "audio" / "youtube"
PEOPLE_DIR = BASE_DIR / "people"

# 核心5位专家的YouTube频道/关键词配置
YOUTUBE_TARGETS = {
    "lenny-rachitsky": {
        "channels": ["Lenny Rachitsky"],
        "keywords": ["Lenny's Podcast", "Lenny Rachitsky"],
        "priority": "high"
    },
    "brian-chesky": {
        "channels": ["Airbnb", "Brian Chesky"],
        "keywords": ["Brian Chesky", "Airbnb CEO"],
        "priority": "high"
    },
    "shreyas-doshi": {
        "channels": ["Shreyas Doshi"],
        "keywords": ["Shreyas Doshi", "Product Leadership"],
        "priority": "high"
    },
    "marty-cagan": {
        "channels": ["SVPG", "Marty Cagan"],
        "keywords": ["Marty Cagan", "SVPG", "Product Management"],
        "priority": "high"
    },
    "gokul-rajaram": {
        "channels": ["Gokul Rajaram"],
        "keywords": ["Gokul Rajaram", "SPADE", "Product Leadership"],
        "priority": "high"
    }
}

class YouTubeSubtitleDownloader:
    """YouTube字幕下载器"""
    
    def __init__(self, log_file=None):
        self.media_dir = MEDIA_DIR
        self.people_dir = PEOPLE_DIR
        self.log_file = log_file or BASE_DIR / "scripts" / "collection.log"
        self.downloaded = []
        self.errors = []
        
    def check_yt_dlp(self):
        """检查yt-dlp是否安装"""
        try:
            result = subprocess.run(
                ["yt-dlp", "--version"],
                capture_output=True,
                text=True,
                timeout=10
            )
            if result.returncode == 0:
                print(f"✅ yt-dlp已安装: {result.stdout.strip()}")
                return True
        except Exception as e:
            print(f"❌ yt-dlp未安装: {e}")
        return False
    
    def download_video_info(self, query, max_results=10):
        """获取视频信息列表"""
        cmd = [
            "yt-dlp",
            f"ytsearch{max_results}:{query}",
            "--dump-json",
            "--no-download"
        ]
        
        try:
            result = subprocess.run(
                cmd,
                capture_output=True,
                text=True,
                timeout=60
            )
            
            if result.returncode != 0:
                self.errors.append(f"搜索失败: {query} - {result.stderr}")
                return []
            
            videos = []
            for line in result.stdout.strip().split('\n'):
                if line.strip():
                    try:
                        video_info = json.loads(line)
                        videos.append(video_info)
                    except json.JSONDecodeError:
                        continue
            
            return videos
            
        except Exception as e:
            self.errors.append(f"获取视频信息异常: {query} - {e}")
            return []
    
    def download_subtitle(self, video_id, video_title, person_name):
        """下载字幕文件"""
        # 创建人物目录
        person_dir = self.media_dir / person_name
        person_dir.mkdir(parents=True, exist_ok=True)
        
        # 文件名
        safe_title = re.sub(r'[^\w\s-]', '', video_title).strip()
        filename = f"{video_id}-{safe_title[:50]}.en.vtt"
        subtitle_path = person_dir / filename
        
        # 检查是否已存在
        if subtitle_path.exists():
            print(f"  ⏭️  字幕已存在: {safe_title[:50]}")
            return subtitle_path
        
        # 下载字幕
        cmd = [
            "yt-dlp",
            f"https://www.youtube.com/watch?v={video_id}",
            "--write-subs",
            "--write-auto-sub",
            "--sub-lang", "en",
            "--skip-download",
            "--sub-format", "vtt",
            "--output", str(subtitle_path.with_suffix(''))
        ]
        
        try:
            result = subprocess.run(
                cmd,
                capture_output=True,
                text=True,
                timeout=120
            )
            
            if result.returncode == 0 and subtitle_path.exists():
                print(f"  ✅ 下载成功: {safe_title[:50]}")
                self.downloaded.append(str(subtitle_path))
                return subtitle_path
            else:
                self.errors.append(f"下载失败: {video_id} - {result.stderr}")
                return None
                
        except Exception as e:
            self.errors.append(f"下载异常: {video_id} - {e}")
            return None
    
    def process_person(self, person_key, person_config):
        """处理单个人物的所有字幕下载"""
        print(f"\n{'='*60}")
        print(f"📺 处理: {person_key}")
        print(f"{'='*60}")
        
        # 合并所有搜索关键词
        searches = person_config.get("channels", []) + person_config.get("keywords", [])
        
        all_videos = []
        for search in searches[:3]:  # 限制搜索次数
            print(f"\n🔍 搜索: {search}")
            videos = self.download_video_info(search, max_results=5)
            all_videos.extend(videos)
            print(f"  找到 {len(videos)} 个视频")
        
        # 去重
        seen_ids = set()
        unique_videos = []
        for video in all_videos:
            vid = video.get('id')
            if vid and vid not in seen_ids:
                seen_ids.add(vid)
                unique_videos.append(video)
        
        print(f"\n📊 去重后共 {len(unique_videos)} 个视频")
        
        # 下载字幕
        success_count = 0
        for video in unique_videos:
            video_id = video.get('id')
            video_title = video.get('title', 'Unknown')
            
            print(f"\n  📥 {video_title[:60]}")
            subtitle_path = self.download_subtitle(video_id, video_title, person_key)
            
            if subtitle_path:
                success_count += 1
        
        print(f"\n✅ {person_key}: {success_count}/{len(unique_videos)} 字幕下载成功")
        return success_count, len(unique_videos)
    
    def run(self, person_keys=None):
        """运行下载任务"""
        print(f"{'='*60}")
        print("YouTube字幕下载器")
        print(f"{'='*60}")
        print(f"时间: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        print(f"输出目录: {self.media_dir}")
        
        # 检查yt-dlp
        if not self.check_yt_dlp():
            print("\n❌ 请先安装 yt-dlp:")
            print("   pip install yt-dlp")
            return False
        
        # 确定要处理的人物
        if person_keys:
            targets = {k: YOUTUBE_TARGETS[k] for k in person_keys if k in YOUTUBE_TARGETS}
        else:
            targets = YOUTUBE_TARGETS
        
        # 按优先级排序
        sorted_targets = sorted(
            targets.items(),
            key=lambda x: x[1].get('priority', 'low')
        )
        
        # 处理每个人物
        total_success = 0
        total_videos = 0
        
        for person_key, person_config in sorted_targets:
            success, videos = self.process_person(person_key, person_config)
            total_success += success
            total_videos += videos
        
        # 输出总结
        print(f"\n{'='*60}")
        print("📊 下载总结")
        print(f"{'='*60}")
        print(f"处理人物: {len(sorted_targets)}")
        print(f"总视频数: {total_videos}")
        print(f"成功下载: {total_success}")
        print(f"失败数量: {len(self.errors)}")
        
        if self.errors:
            print(f"\n❌ 错误列表:")
            for error in self.errors[:10]:  # 只显示前10个
                print(f"  - {error}")
        
        # 记录日志
        self.log_results()
        
        return total_success > 0
    
    def log_results(self):
        """记录结果到日志文件"""
        log_entry = {
            "timestamp": datetime.now().isoformat(),
            "type": "youtube_subtitle",
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
    # 可以指定人物，默认处理所有核心5位专家
    import sys
    
    downloader = YouTubeSubtitleDownloader()
    
    # 支持命令行参数指定人物
    if len(sys.argv) > 1:
        person_keys = sys.argv[1].split(',')
    else:
        person_keys = None  # 处理所有
    
    success = downloader.run(person_keys)
    sys.exit(0 if success else 1)
