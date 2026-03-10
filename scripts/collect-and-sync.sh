#!/bin/bash
# 简化版持续采集脚本
# 每15分钟执行一次内容检查和Git同步

set -e

BASE_DIR="/root/.openclaw/workspace/anima-base"
LOG_FILE="$BASE_DIR/collection.log"

echo "========================================" >> "$LOG_FILE"
echo "🚀 Collection Run: $(date '+%Y-%m-%d %H:%M:%S')" >> "$LOG_FILE"
echo "========================================" >> "$LOG_FILE"

# 检查GitHub连接
echo "📡 Checking GitHub connection..." >> "$LOG_FILE"
if curl -s --max-time 10 https://github.com > /dev/null 2>&1; then
    echo "✅ GitHub is reachable" >> "$LOG_FILE"
    
    # 尝试推送
    cd "$BASE_DIR"
    if [ -n "$(git status --porcelain)" ]; then
        echo "📝 Changes detected, committing..." >> "$LOG_FILE"
        git add -A
        git commit -m "Auto-update: $(date '+%Y-%m-%d %H:%M')" >> "$LOG_FILE" 2>&1 || true
        
        echo "🚀 Pushing to GitHub..." >> "$LOG_FILE"
        git push origin main >> "$LOG_FILE" 2>&1 &
        echo "✅ Push initiated (background)" >> "$LOG_FILE"
    else
        echo "✅ No changes to commit" >> "$LOG_FILE"
    fi
else
    echo "❌ GitHub not reachable, will retry next run" >> "$LOG_FILE"
fi

# 记录当前状态
echo "" >> "$LOG_FILE"
echo "📊 Current Status:" >> "$LOG_FILE"
echo "- Total profiles: $(find $BASE_DIR -name 'profile.md' | wc -l)" >> "$LOG_FILE"
echo "- Total index files: $(find $BASE_DIR/index -name '*.md' 2>/dev/null | wc -l)" >> "$LOG_FILE"
echo "- Total content files: $(find $BASE_DIR -name '*.md' | wc -l)" >> "$LOG_FILE"
echo "- Repository size: $(du -sh $BASE_DIR | cut -f1)" >> "$LOG_FILE"

echo "" >> "$LOG_FILE"
echo "✅ Run complete at $(date '+%H:%M:%S')" >> "$LOG_FILE"
echo "" >> "$LOG_FILE"

# 保留最近1000行日志
tail -n 1000 "$LOG_FILE" > "$LOG_FILE.tmp" && mv "$LOG_FILE.tmp" "$LOG_FILE"
