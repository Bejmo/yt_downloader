if exist "main.exe" (
    del main.exe
)
call .\.venv\Scripts\activate

pip install -U pytubefix

pyinstaller main.spec

cd .\dist
move main.exe .\..
cd .\..

rmdir /s /q dist
rmdir /s /q build
rmdir /s /q __pycache__
