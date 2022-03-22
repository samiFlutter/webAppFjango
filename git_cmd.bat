@echo off
echo  +++++++ adding all new files +++++++
git add .
echo   +++++++ write you comment +++++++
set /p commant="Enter commant ::: "
echo   +++++++Commiting changes +++++++
git commit -a -m " %commant%"
echo +++++++Push to github +++++++
git push 
pause
