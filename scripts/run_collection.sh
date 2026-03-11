#!/bin/bash
# 一键运行所有采集任务
# 用于手动触发或测试

set -e

BASE_DIR="/Users/zhiyangyu/.box/Workspace/anima-base-scheduled"
SCRIPTS_DIR="$BASE_DIR/scripts"
LOG_DIR="$SCRIPTS_DIR/logs"

# 创建日志目录
mkdir -p "$LOG_DIR"

echo "=========================================="
echo "Anima Base 内容采集任务"
echo "=========================================="
echo "开始时间: $(date '+%Y-%m-%d %H:%M:%S')"
echo ""

# 任务列表
tasks=(
    "youtube_subtitle_downloader.py:YouTube字幕采集"
    "rss_article_downloader.py:RSS文章采集"
    "podcast_audio_downloader.py:播客音频采集"
    "auto_translator.py:文档翻译"
)

success_count=0
total_count=${#tasks[@]}

# 执行每个任务
for task in "${tasks[@]}"; do
    IFS=':' read -r script_name task_name <<< "$task"

    echo ""
    echo "=========================================="
    echo "执行任务: $task_name"
    echo "脚本: $script_name"
    echo "=========================================="

    log_file="$LOG_DIR/$(date '+%Y%m%d_%H%M%S')_${script_name%.py}.log"

    if [ -f "$SCRIPTS_DIR/$script_name" ]; then
        if python3 "$SCRIPTS_DIR/$script_name" >> "$log_file" 2>&1; then
            echo "✅ $task_name 执行成功"
            success_count=$((success_count + 1))
        else
            echo "❌ $task_name 执行失败"
            echo "   日志: $log_file"
            tail -20 "$log_file"
        fi
    else
        echo "⚠️  脚本不存在: $script_name"
    fi
done

echo ""
echo "=========================================="
echo "采集任务总结"
echo "=========================================="
echo "总任务数: $total_count"
echo "成功: $success_count"
echo "失败: $((total_count - success_count))"
echo "结束时间: $(date '+%Y-%m-%d %H:%M:%S')"

# 同步到GitHub
echo ""
echo "=========================================="
echo "同步到GitHub"
echo "=========================================="
bash "$SCRIPTS_DIR/sync-github.sh"

echo ""
echo "✅ 所有任务完成！"
