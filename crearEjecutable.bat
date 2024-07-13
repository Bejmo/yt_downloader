del main.exe
pyinstaller main.spec

cd .\dist
move main.exe .\..
cd .\..

rmdir /s /q dist
rmdir /s /q build
