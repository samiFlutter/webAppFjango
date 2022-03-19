git add .
pause
@echo off
set /p commant="Enter commant: "
pause
git commit -a -m " %commant%"
pause
git push 
pause
