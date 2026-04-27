@echo off
cd /d "C:\path\to\your\repo"
git pull origin master
git add .
git commit -m "Auto sync %date% %time%"
git push origin master
