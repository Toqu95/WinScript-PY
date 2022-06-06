taskkill /F /IM notepad.exe
set testlist=1 2 3 4 
(for %%a in (%testlist%) do (
echo %%a
))
Pause
