cls 
@ECHO OFF 
title Folder Locker
if EXIST "Locker" goto UNLOCK 
if NOT EXIST userdata goto MDLOCKER 
:CONFIRM 
echo Locked this catalog?(Y/N) 
set/p "cho=>" 
if %cho%==Y goto LOCK 
if %cho%==y goto LOCK 
if %cho%==n goto END 
if %cho%==N goto END 
echo Wrong pick. 
goto CONFIRM 
:LOCK 
ren userdata "Locker" 
attrib +h +s "Locker" 
echo Catalog locked
goto End 
:UNLOCK 
echo Input Key for unlocked
set/p "pass=>" 
if NOT %pass%== Q13 goto FAIL 
attrib -h -s "Locker" 
ren "Locker" userdata 
echo Catalog unlocked
goto End 
:FAIL 
echo Wrong password! 
goto end 
:MDLOCKER 
md userdata 
echo Secret folder created 
goto End 
:End