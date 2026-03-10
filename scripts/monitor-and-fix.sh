#!/bin/bash
# Anima Base 监控与纠错系统
# 定时检查问题并自动修复

set -e

BASE_DIR="/root/.openclaw/workspace/anima-base"
LOG_FILE="$BASE_DIR/monitor.log"
ERROR_COUNT=0
FIXED_COUNT=0

echo "========================================" >> "$LOG_FILE"
echo "🔍 Monitor Run: $(date '+%Y-%m-%d %H:%M:%S')" >> "$LOG_FILE"
echo "========================================" >> "$LOG_FILE"

cd "$BASE_DIR"

# 1. 检查Git状态
echo "📋 Checking Git status..." >> "$LOG_FILE"
if ! git diff-index --quiet HEAD -- 2>/dev/null; then
    echo "⚠️  Uncommitted changes found" >> "$LOG_FILE"
    git add -A >> "$LOG_FILE" 2>&1
    git commit -m "Auto-fix: Uncommitted changes at $(date '+%H:%M')" >> "$LOG_FILE" 2>&1
    FIXED_COUNT=$((FIXED_COUNT + 1))
else
    echo "✅ Git status clean" >> "$LOG_FILE"
fi

# 2. 检查GitHub连接并同步
echo "📡 Checking GitHub connection..." >> "$LOG_FILE"
if timeout 5 bash -c 'curl -s --max-time 3 https://github.com > /dev/null 2>&1'; then
    echo "✅ GitHub reachable" >> "$LOG_FILE"
    
    # 检查是否有本地提交需要推送
    LOCAL_COMMITS=$(git rev-list --count origin/main..main 2>/dev/null || echo "0")
    if [ "$LOCAL_COMMITS" -gt 0 ]; then
        echo "🚀 Pushing $LOCAL_COMMITS commits to GitHub..." >> "$LOG_FILE"
        git push origin main >> "$LOG_FILE" 2>&1 && echo "✅ Push successful" >> "$LOG_FILE" || echo "⚠️  Push will retry next run" >> "$LOG_FILE"
    else
        echo "✅ No commits to push" >> "$LOG_FILE"
    fi
else
    echo "⚠️  GitHub not reachable" >> "$LOG_FILE"
    ERROR_COUNT=$((ERROR_COUNT + 1))
fi

# 3. 检查文件权限
echo "🔐 Checking file permissions..." >> "$LOG_FILE"
SCRIPTS_DIR="$BASE_DIR/scripts"
if [ -d "$SCRIPTS_DIR" ]; then
    for script in "$SCRIPTS_DIR"/*.sh; do
        if [ -f "$script" ] && [ ! -x "$script" ]; then
            chmod +x "$script"
            echo "✅ Fixed permission: $script" >> "$LOG_FILE"
            FIXED_COUNT=$((FIXED_COUNT + 1))
        fi
    done
fi

# 4. 检查空目录（添加.gitkeep）
echo "📁 Checking empty directories..." >> "$LOG_FILE"
EMPTY_DIRS=$(find "$BASE_DIR" -type d -empty 2>/dev/null | grep -v ".git" | wc -l)
if [ "$EMPTY_DIRS" -gt 0 ]; then
    echo "⚠️  Found $EMPTY_DIRS empty directories" >> "$LOG_FILE"
    find "$BASE_DIR" -type d -empty -exec touch {}/.gitkeep \; 2>/dev/null || true
    echo "✅ Added .gitkeep to empty directories" >> "$LOG_FILE"
    FIXED_COUNT=$((FIXED_COUNT + 1))
fi

# 5. 内容统计
echo "📊 Content Statistics:" >> "$LOG_FILE"
echo "- Profiles: $(find $BASE_DIR -name 'profile.md' | wc -l)" >> "$LOG_FILE"
echo "- Podcasts: $(find $BASE_DIR -path '*/podcasts/*.md' | wc -l)" >> "$LOG_FILE"
echo "- Total MD: $(find $BASE_DIR -name '*.md' | wc -l)" >> "$LOG_FILE"
echo "- Size: $(du -sh $BASE_DIR | cut -f1)" >> "$LOG_FILE"

# 6. 检查关键文件
echo "📄 Checking essential files..." >> "$LOG_FILE"
if [ ! -f "$BASE_DIR/README.md" ]; then
    echo "❌ README.md missing!" >> "$LOG_FILE"
    ERROR_COUNT=$((ERROR_COUNT + 1))
else
    echo "✅ README.md exists" >> "$LOG_FILE"
fi

# 7. 检查索引
echo "📇 Checking index..." >> "$LOG_FILE"
if [ ! -d "$BASE_DIR/index" ]; then
    echo "⚠️  Index missing, regenerating..." >> "$LOG_FILE"
    python3 "$BASE_DIR/scripts/index_generator.py" >> "$LOG_FILE" 2>&1 || true
    FIXED_COUNT=$((FIXED_COUNT + 1))
else
    echo "✅ Index exists" >> "$LOG_FILE"
fi

# 8. 检查Git远程
echo "🔗 Checking Git remote..." >> "$LOG_FILE"
REMOTE_URL=$(git remote get-url origin 2>/dev/null || echo "")
if [ -z "$REMOTE_URL" ]; then
    echo "❌ No Git remote!" >> "$LOG_FILE"
    ERROR_COUNT=$((ERROR_COUNT + 1))
else
    echo "✅ Remote configured" >> "$LOG_FILE"
fi

# 汇总
echo "" >> "$LOG_FILE"
echo "📊 Summary: $ERROR_COUNT errors, $FIXED_COUNT fixed" >> "$LOG_FILE"
echo "Status: $(if [ $ERROR_COUNT -eq 0 ]; then echo '✅ Healthy'; else echo '⚠️  Attention needed'; fi)" >> "$LOG_FILE"

# 保留最近500行日志
tail -n 500 "$LOG_FILE" > "$LOG_FILE.tmp" 2>/dev/null && mv "$LOG_FILE.tmp" "$LOG_FILE" || true

# 如果有修复，推送
echo "" >> "$LOG_FILE"
echo "✅ Monitor complete at $(date '+%H:%M:%S')" >> "$LOG_FILE"
echo "" >> "$LOG_FILE"
