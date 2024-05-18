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
        self.setWindowTitle("How to Transcribe")
        self.setFixedSize(960,540)
        self.BackGround()
        self.setWindowFlag(Qt.WindowType.WindowStaysOnTopHint)
        #app.setStyle("Fusion")

        Main = QtWidgets.QLabel(self)
        Main.setGeometry(350,20,300,60)
        Main.setText('How to use?')
        Main.setStyleSheet('border: 1px solid #ff0; color: red; font-size: 36pt')
        #MS1 = QtWidgets.QLabel(whisper_ok)
        #MS1.setGeometry(75,100,250,15)
        #MS1.setText('字幕檔案轉錄成功囉')

        layout_Scribe = QHBoxLayout(self)
        Scribe = QLabel(self)
        Scribe.setText('''
                       一.選擇欲轉錄影片的原始語言(Choose Language)\n
                       二.選擇轉錄之語言模組(請根據設備硬體規格選擇最適當的項目)(Choose Models)\n
                       三.選擇影片(Choose Video or Audio)\n
                       四.選擇想要輸出的文字格式(Choose formatted text)\n
                       五.輸入音檔出現詞彙增加轉譯精準度(Prompt)\n
                       六.選擇輸出完畢後的存放位置(Choose Saved Path you want)\n
                       以上完畢之後 即可以點選生成按鈕 開始轉錄影片(Start to Speech to txt)''')
        Scribe.setStyleSheet('''
                    QLabel{
                            font-size: 20px;
                            color: aqua;
                    }


        ''')
        layout_Scribe.addWidget(Scribe,alignment=Qt.AlignmentFlag.AlignCenter)
        #layout_Scribe.addSpacing(100)

        cancel = QtWidgets.QPushButton("Close",self)
        #cancel.layout
        cancel.setText('OK！')  
        cancel.setGeometry(400,490,150,30)
        cancel.clicked.connect(self.srt_close) 
        cancel.setStyleSheet('''
                QPushButton:hover{
                            border:3px solid #000;
                            background:green;
                            border-radius: 15px;
                            font-weight: bold;
                            font-size: 17px;
                }
                QPushButton {
                border:transparent;
                font: 20px;
                color: white;
                font-family: arial;
                }
        ''')

    
    def srt_close(self):
        print("返回主頁面")
        self.close()
    
    #設置本頁背景
    def BackGround(self):
        label = QLabel(self)
        label.setGeometry(0,-200,1200,945)
        pixmap = QPixmap('./images/BG03.png')
        label.setPixmap(pixmap)
        label.lower()


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = Tips()
    window.show()
    sys.exit(app.exec())