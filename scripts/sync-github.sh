#!/bin/bash
# GitHub 自动同步脚本
# 自动提交并推送内容到 GitHub

set -e

BASE_DIR="/root/.openclaw/workspace/anima-base"
cd "$BASE_DIR"

# 配置 Git
git config user.name "Anima Bot"
git config user.email "bot@anima-base.local"

# 添加所有变更
echo "📦 Adding changes..."
git add -A

# 检查是否有变更需要提交
if git diff --cached --quiet; then
    echo "✅ No changes to commit"
    exit 0
fi

# 创建提交
echo "📝 Committing changes..."
COMMIT_MSG="Content update: $(date '+%Y-%m-%d %H:%M')"
git commit -m "$COMMIT_MSG"

# 推送到 GitHub
echo "🚀 Pushing to GitHub..."
git push origin main

echo "✅ Sync complete!"
