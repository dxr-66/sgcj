@echo off
echo 正在同步文章数据到 GitHub...
git add articles.js
git commit -m "更新文章数据"
git push origin main
echo 同步完成！
echo GitHub Pages 将在几分钟后更新
pause