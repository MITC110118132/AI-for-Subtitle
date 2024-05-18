from PyQt6 import QtWidgets, QtCore
from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
from PyQt6.QtGui import *
from PyQt6.QtMultimedia import *
from PyQt6.QtMultimediaWidgets import *
import sys

class Tips(QWidget):
    closed = QtCore.pyqtSignal() #判定關閉視窗
    def __init__(self):
        
        super().__init__()
        self.setWindowTitle("How to Embed")
        self.setFixedSize(960,540)
        layout_Scribe = QVBoxLayout(self)
        Scribe = QLabel(self)
        Scribe.setText('''
                       Font(字體):選擇嵌入時字幕的字形，可自行將檔案(.ttf/.ttc)匯入至Font資料夾(※需選擇與SRT檔案語言相容字體檔案)\n
                       Font Size(字體大小):選擇嵌入時字幕的字體大小\n
                       FontColor(字體顏色):選擇嵌入時字幕的字體顏色\n
                       Background(背景):選擇字幕的背景顏色\n
                       Subtitle Location(字幕位置):選擇字幕想擺放在畫面的位置\n
                       Choose MP4/MP3:選擇欲嵌入字幕之影片/音檔\n
                       Output path:嵌入字幕後影片之儲存位置\n
                       Output Video Name:嵌入字幕後之影片名稱\n
                       SRT(字幕檔案):選擇在Whisper頁面轉譯完成的檔案\n
                       快捷鍵 : Play -> Ctrl+Q  Pause -> Ctrl+W  Stop -> Ctrl+E  Save -> Ctrl+S''')
        Scribe.setStyleSheet('''
                    QLabel{
                            font-size: 16px;
                            color: aqua;
                    }
                    ''')
        layout_Scribe.addWidget(Scribe)
        layout_Scribe.addSpacing(100)

        cancel = QtWidgets.QPushButton("Close",self)
        cancel.setText('OK！')  
        cancel.setGeometry(400,490,150,30)
        cancel.clicked.connect(self.srt_close)
        cancel.setStyleSheet('''
                QPushButton:hover{
                            border:3px solid #000;
                            background:yellow;
                            border-radius: 15px;
                            font-weight: bold;
                            font-size: 17px;
                }
                QPushButton {
                border:1px solid black;
                background: gray;
                font: 20px;
                color: aqua;
                font-family: arial;
                }
        ''')
        self.BackGround()

    
    def srt_close(self):
        print("返回主頁面")
        self.close()

    #設置本頁背景
    def BackGround(self):
        label = QLabel(self)
        label.setGeometry(0,0,960,540)
        pixmap = QPixmap('./images/BG03.png')
        label.setPixmap(pixmap)
        label.lower()

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = Tips()
    window.show()
    sys.exit(app.exec())