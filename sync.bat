@echo off
cd /d "C:\Users\Brian Geisler\gitSynced\main"
git pull origin master
git add .
git commit -m "Auto sync %date% %time%"
git push origin master
