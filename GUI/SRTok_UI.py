from PyQt6 import QtWidgets
from PyQt6.QtWidgets import *
from PyQt6.QtGui import *
import sys

class srt(QWidget):
    def __init__(self):
        #轉錄成功會出現的畫面
        super().__init__()
        self.setWindowTitle("項目確認")
        self.setFixedSize(400,200)
        self.BackGround()
        #self.setWindowFlag(Qt.WindowType.WindowStaysOnTopHint)

        Main = QtWidgets.QLabel(self)
        Main.setGeometry(100,30,250,45)
        Main.setText('轉錄成功')
        Main.setStyleSheet('border: transparent; color: red; font-size: 36pt')
        #MS1 = QtWidgets.QLabel(whisper_ok)
        #MS1.setGeometry(75,100,250,15)
        #MS1.setText('字幕檔案轉錄成功囉')
                  
        cancel = QtWidgets.QPushButton("Close",self)
        #cancel.layout
        cancel.setText('好的')  
        cancel.clicked.connect(self.srt_close)  
        layout = QHBoxLayout()
        self.setLayout(layout)
        layout.addWidget(cancel)
    
    def srt_close(self):
        print("嵌入結束")
        self.hide()
    
    #設置本頁背景
    def BackGround(self):
        label = QLabel(self)
        label.setGeometry(-70,-300,1200,945)
        pixmap = QPixmap('./images/BackGround03.jpg')
        label.setPixmap(pixmap)
        label.lower()

class srt_fail(QWidget):
    def __init__(self):
        #轉錄失敗會出現的畫面
        super().__init__()
        self.setWindowTitle("轉錄失敗")
        self.setFixedSize(400,200)
        self.BackGround()
        #self.setWindowFlag(Qt.WindowType.WindowStaysOnTopHint)
        
        Main = QtWidgets.QLabel(self)
        Main.setGeometry(100,30,250,45)
        Main.setText('轉錄失敗')
        Main.setStyleSheet('border: transparent; color: red; font-size: 36pt')
        #MS1 = QtWidgets.QLabel(whisper_ok)
        #MS1.setGeometry(75,100,250,15)
        #MS1.setText('字幕檔案轉錄成功囉')
        due = QLabel(self)
        due.setGeometry(25,125,500,100)
        due.setText('檔案沒有選取正確 或者 前置步驟沒有如實完成')
        due.setStyleSheet('border: transparent; color: red; font-size: 13pt')
        
        cancel = QtWidgets.QPushButton("Close",self)
        #cancel.layout
        cancel.setText('好的')  
        cancel.clicked.connect(self.srt_close)  
        layout = QHBoxLayout()
        self.setLayout(layout)

        layout.addWidget(cancel)
    
    def srt_close(self):
        print("嵌入結束")
        self.hide()            
    
    #設置本頁背景
    def BackGround(self):
        label = QLabel(self)
        label.setGeometry(-70,-300,1200,945)
        pixmap = QPixmap('./images/BackGround03.jpg')
        label.setPixmap(pixmap)
        label.lower()

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    sys.exit(app.exec())