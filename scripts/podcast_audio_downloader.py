#!/usr/bin/env python3
"""
播客音频下载器
从YouTube/Apple Podcasts/Spotify下载播客音频
"""

import os
import json
import re
from pathlib import Path
from datetime import datetime
from urllib.parse import urlparse
import subprocess

BASE_DIR = Path("/Users/zhiyangyu/.box/Workspace/anima-base-scheduled")
MEDIA_DIR = BASE_DIR / "media" / "audio" / "podcast"

# 播客源配置
PODCAST_SOURCES = {
    "lennys-podcast": {
        "youtube_url": "https://www.youtube.com/@LennysPodcast",
        "person": "lenny-rachitsky",
        "max_episodes": 10,
        "priority": "high"
    },
    "how-i-built-this": {
        "youtube_url": "https://www.youtube.com/@HowIBuiltThis",
        "person": "multiple",
        "max_episodes": 10,
        "priority": "medium"
    },
    "masters-of-scale": {
        "youtube_url": "https://www.youtube.com/@MastersOfScale",
        "person": "brian-chesky",  # Brian Chesky有嘉宾
        "max_episodes": 5,
        "priority": "high"
    },
    "a16z-podcast": {
        "youtube_url": "https://www.youtube.com/@a16z",
        "person": "ben-horowitz",
        "max_episodes": 10,
        "priority": "medium"
    }
}

class PodcastAudioDownloader:
    """播客音频下载器"""
    
    def __init__(self, log_file=None):
        self.media_dir = MEDIA_DIR
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
    
    def download_playlist(self, playlist_url, person_name, max_episodes=10):
        """下载播客播放列表"""
        # 创建人物目录
        person_dir = self.media_dir / person_name
        person_dir.mkdir(parents=True, exist_ok=True)
        
        # 下载命令
        cmd = [
            "yt-dlp",
            playlist_url,
            "-f", "bestaudio[ext=m4a]/bestaudio/best",
            "--extract-audio",
            "--audio-format", "mp3",
            "--audio-quality", "0",
            "--write-info-json",
            "--write-description",
            "--write-thumbnail",
            "--download-archive", str(person_dir / "downloaded.txt"),
            "--max-downloads", str(max_episodes),
            "--output", str(person_dir / "%(upload_date)s-%(title)s.%(ext)s")
        ]
        
        try:
            print(f"\n📥 开始下载播客音频...")
            print(f"   播放列表: {playlist_url}")
            print(f"   最大集数: {max_episodes}")
            print(f"   输出目录: {person_dir}")
            
            result = subprocess.run(
                cmd,
                capture_output=True,
                text=True,
                timeout=1800  # 30分钟超时
            )
            
            # 统计下载的文件
            audio_files = list(person_dir.glob("*.mp3"))
            success_count = len(audio_files)
            
            if success_count > 0:
                print(f"✅ 成功下载 {success_count} 集音频")
                
                # 记录下载的文件
                for audio_file in audio_files:
                    self.downloaded.append(str(audio_file))
                
                return success_count
            else:
                print(f"⚠️  未下载到新文件")
                print(f"   输出: {result.stdout[:500]}")
                return 0
                
        except subprocess.TimeoutExpired:
            print(f"❌ 下载超时")
            self.errors.append(f"下载超时: {playlist_url}")
            return 0
        except Exception as e:
            print(f"❌ 下载异常: {e}")
            self.errors.append(f"下载异常: {playlist_url} - {e}")
            return 0
    
    def transcribe_audio(self, audio_file):
        """转录音频（集成Whisper，可选）"""
        print(f"\n🎤 转录音频: {audio_file.name}")
        
        # 检查是否已转录
        transcript_file = audio_file.with_suffix('.txt')
        if transcript_file.exists():
            print(f"  ⏭️  转录文件已存在")
            return transcript_file
        
        # 这里可以使用OpenAI Whisper API或本地Whisper
        # 暂时跳过，作为后续扩展
        print(f"  ⏸️  转录功能待配置Whisper API")
        return None
    
    def process_podcast(self, podcast_name, podcast_config):
        """处理单个播客"""
        print(f"\n{'='*60}")
        print(f"🎙️  播客: {podcast_name}")
        print(f"{'='*60}")
        
        youtube_url = podcast_config.get("youtube_url")
        person = podcast_config.get("person")
        max_episodes = podcast_config.get("max_episodes", 10)
        
        if not youtube_url:
            print(f"⚠️  未配置YouTube URL")
            return 0
        
        # 下载音频
        success = self.download_playlist(youtube_url, person, max_episodes)
        
        # 转录音频（可选）
        if success > 0:
            person_dir = self.media_dir / person
            audio_files = list(person_dir.glob("*.mp3"))[-success:]  # 最新的文件
            
            for audio_file in audio_files:
                self.transcribe_audio(audio_file)
        
        return success
    
    def run(self, podcasts=None):
        """运行下载任务"""
        print(f"{'='*60}")
        print("播客音频下载器")
        print(f"{'='*60}")
        print(f"时间: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        print(f"输出目录: {self.media_dir}")
        
        # 检查yt-dlp
        if not self.check_yt_dlp():
            print("\n❌ 请先安装 yt-dlp:")
            print("   pip install yt-dlp")
            return False
        
        # 确定要处理的播客
        if podcasts:
            targets = {k: PODCAST_SOURCES[k] for k in podcasts if k in PODCAST_SOURCES}
        else:
            # 按优先级排序
            targets = dict(sorted(
                PODCAST_SOURCES.items(),
                key=lambda x: x[1].get('priority', 'low')
            ))
        
        # 处理每个播客
        total_success = 0
        for podcast_name, podcast_config in targets.items():
            success = self.process_podcast(podcast_name, podcast_config)
            total_success += success
        
        # 输出总结
        print(f"\n{'='*60}")
        print("📊 下载总结")
        print(f"{'='*60}")
        print(f"处理播客: {len(targets)}")
        print(f"总下载: {total_success} 集音频")
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
            "type": "podcast_audio",
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
    
    downloader = PodcastAudioDownloader()
    
    # 支持命令行参数指定播客
    if len(sys.argv) > 1:
        podcasts = sys.argv[1].split(',')
    else:
        podcasts = None  # 处理所有
    
    success = downloader.run(podcasts)
    sys.exit(0 if success else 1)
