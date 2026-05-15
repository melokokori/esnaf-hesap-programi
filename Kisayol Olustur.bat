@echo off
chcp 65001 >nul
set KLASOR=%~dp0
set EXE=%KLASOR%EsnafHesapProgrami.exe
set HEDEF=%USERPROFILE%\Desktop\Esnaf Hesap Programi.lnk

powershell -NoProfile -Command ^
  "$WS = New-Object -ComObject WScript.Shell;" ^
  "$s = $WS.CreateShortcut('%HEDEF%');" ^
  "$s.TargetPath = '%EXE%';" ^
  "$s.WorkingDirectory = '%KLASOR%';" ^
  "$s.IconLocation = '%EXE%,0';" ^
  "$s.Description = 'Esnaf Hesap Programi';" ^
  "$s.Save()"

echo.
echo Kisayol olusturuldu: %HEDEF%
echo Program masaustunden acilabilir.
echo.
pause
