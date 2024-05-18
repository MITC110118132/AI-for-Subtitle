@echo off
setlocal
set IMAGEMAGICK_DIR=%~dp0Python311\Lib\site-packages\moviepy\ImageMagick-7.1.1-Q16-HDRI
set PATH=%IMAGEMAGICK_DIR%;%PATH%

Python311\python.exe main.py

endlocal