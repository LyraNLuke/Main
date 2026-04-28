@echo off
cd /d "%~dp0"
git pull origin master
git add .
git commit -m "Auto sync %date% %time%"
git push origin master
