from PyQt6 import QtWidgets, QtCore, QtGui
from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
from PyQt6.QtGui import *
from PyQt6.QtMultimedia import *

import sys, os
import Qt_ui.SRT_export, Qt_ui.Sub_embed_form, Qt_ui.AISRT
try:
    import chardet
except ModuleNotFoundError:
    import subprocess
    import sys
    subprocess.check_call([sys.executable, "-m", "pip", "install", "chardet"])
    import chardet  # 再次嘗試導入套件

class AISRT(QtWidgets.QMainWindow, Qt_ui.AISRT.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.w = None

        #初始物件
        self.Go = QLabel(self)
        self.Ready = QPushButton(self)
        

        self.setWindowTitle("AI for Generating SRT")
        self.GO()
        self.BackGround()
        self
        
        
        #切換
        self.Ready.clicked.connect(self.Start)

    #設置本頁背景
    def BackGround(self):
        label = QLabel(self)
        label.setGeometry(-70,-750,2000,2000)
        pixmap = QPixmap('./images/FireFly01.jpg')
        label.setPixmap(pixmap)
        label.lower()
        self.Go.stackUnder(self.Ready)
        self.Theme.setStyleSheet('color: red;')
        self.Go.stackUnder(self.Ready) #讓書本顯示在文字下方

    def GO(self):
        self.Go = QLabel(self)
        self.Ready.setGeometry(600,435,226,170)
        self.Go.setGeometry(600,435,226,170)
        self.Go.setScaledContents(True)
        pixmap =  QPixmap('./images/Start.png')
        self.Go.setPixmap(pixmap)
        self.Ready.setText("開始\n設定")
        self.Ready.setStyleSheet('border: transparent; color: aqua; font-size: 36pt')


    def Start(self):
        if  self.w is None:
            self.w = SRT_export()
            self.w.show()
            self.hide()

        else:
            self.w.hide()  # 隱藏視窗(保留快取)
            self.w = None  # Discard reference.
        
class SRT_export(QtWidgets.QMainWindow, Qt_ui.SRT_export.Ui_AI_Transcribe_SRT):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.w = None
        self.css()

        #設置本頁背景
        label = QLabel(self)
        label.setGeometry(0,-250,846,1200)
        pixmap = QPixmap('./images/FireFly06.jpg')
        label.setPixmap(pixmap)
        label.lower()
        
        self.Translate_combo.setDisabled(True)
        self.Language_Translate.clicked.connect(self.Translate)

        self.w = None
        #上一頁
        self.Skip_btn.clicked.connect(self.NextPage)
        self.Transcribe_btn.clicked.connect(self.NextPage)

        #下一頁
        self.Cancel_btn.clicked.connect(self.UpPage)

        #選擇影片
        self.ChooseFile_btn.clicked.connect(self.SelectVideo)

        #儲存路徑
        self.PathFind_btn.clicked.connect(self.SaveFile)

    #設置Css
    def css(self):
        self.Language_Type.setStyleSheet('''color: Aqua; font-weight: bold; text-decoration: underline;''')
        self.Language_Translate.setStyleSheet('''color: Aqua; font-weight: bold; text-decoration: underline;''')
        self.Language_Transcribe.setStyleSheet('''color: Aqua; font-weight: bold; text-decoration: underline;''')
        self.SRT_Format.setStyleSheet('''color: Aqua; font-weight: bold; text-decoration: underline;''')
        self.SRT_Name.setStyleSheet('''color: Aqua; font-weight: bold; text-decoration: underline;''')
        self.Output_Path.setStyleSheet('''color: Aqua; font-weight: bold; text-decoration: underline;''')

    def Translate(self):
        if self.Language_Translate.isEnabled:
            self.Translate_combo.setEnabled(True)
        else:
            self.Translate_combo.setEnabled(False)

    def NextPage(self):
        if self.w is None:
            self.w = Sub_embed_form()
            self.w.show()
            self.hide()

        else:
            self.w.hide()  # Close window.
            self.w = None  # Discard reference.
            
    def UpPage(self):
        if self.w is None:
            self.w = AISRT()
            self.w.show()
            self.hide()
        else:
            self.w.hide()  # Close window.
            self.w = None  # Discard reference.

    def SaveFile(self):
        SavePath = QFileDialog.getExistingDirectory(self, "請選擇欲儲存的資料夾位置")

        #成功選取影片
        if SavePath:
            fileName = os.path.basename(SavePath)
            self.PathtextEdit.setText(fileName)
        #反之取消or錯誤
        else:
            print("取消選擇 或者 選取的檔案有誤")
            QMessageBox.warning(self, "Notice！！！", "取消選擇 或者 選取的檔案有誤")

    def SelectVideo(self):
        filePath , _ = QtWidgets.QFileDialog.getOpenFileName(self, "選擇影片", "", "Video Files (*.mp4 *.avi *.mkv *.mov)")

        #成功選取影片
        if filePath:
            fileName = os.path.basename(filePath)
            self.Choosed_File.setText(fileName)
        #反之取消or錯誤
        else:
            print("取消選擇 或者 選取的檔案有誤")
            QMessageBox.warning(None, "Notice！！！", "取消選擇 或者 選取的檔案有誤")


        #*video_path, _ = QtWidgets.QFileDialog.getOpenFileName(self, "選擇影片", "", "Video Files (*.mp4 *.avi *.mkv)")
        #if video_path:
            # 在這裡可以處理選擇的影片路徑，例如顯示在文本框中或進行其他操作
            #self.Choosed_File.setText(video_path)

        #儲存格式
        #def SaveFile(self):
        #SavePath, _ = QFileDialog.getSaveFileUrl(self, # 父元件
        #"選擇欲儲存的資料夾",             # 對話框視窗標題
        #"./",                       # 初始選擇路徑 
        #"字幕檔 (*.srt);;文字檔 (*.txt);;All Files(*)"    # 可被選擇的檔案類型
        #)

class Sub_embed_form(QtWidgets.QMainWindow, Qt_ui.Sub_embed_form.Ui_SRT_edit_form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.css()
        self.BackGround()

        self.w = None

        self.Finish_btn.clicked.connect(Functions.Quit)
        self.Return_btn.clicked.connect(self.UpPage)
        self.Folder_btn.clicked.connect(self.OpenFolder)
        self.PathFind_btn.clicked.connect(self.ChoosePath)

        self.populate_fonts() # 在初始化时填充字体列表

        validator = QtGui.QIntValidator()
        self.FontSize_line.setValidator(validator)
        self.SaveAs_btn.clicked.connect(self.SaveChanges)
        self.Embed_btn.clicked.connect(self.Embed)

        self.ui()

        self.Play_sounds_btn.clicked.connect(self.Play)
        self.Pause_btn.clicked.connect(self.Pause)
        self.Stop_btn.clicked.connect(self.Stop)
        #self.horizontalSlider.mouseGrabber()

    #設置Css
    def css(self):
        self.SRT.setStyleSheet('''color:red;''')
        self.Font_Size.setStyleSheet('''color:red;''')
        self.Font_Spacing.setStyleSheet('''color:red;''')
        self.Embed_check.setStyleSheet('''color:red;''')
        self.Effect_check.setStyleSheet('''color:red;''')
        self.label_8.setStyleSheet('''color:red;''')
        self.label.setStyleSheet('''color:red; font-size: 12pt''')
        self.Output_path.setStyleSheet('''color:red;''')
        self.Output_Video_Name.setStyleSheet('''color:red;''')

    #設置本頁背景
    def BackGround(self):
        label = QLabel(self)
        label.setGeometry(-70,-300,1200,945)
        pixmap = QPixmap('./images/BackGround03.jpg')
        label.setPixmap(pixmap)
        label.lower()


    def UpPage(self):
        if self.w is None:
            self.w = SRT_export()
            self.w.show()
            self.hide()
        else:
            self.w.hide()  # Close window.
            self.w = None  # Discard reference.
    
    def detect_encoding(self, filePath):
        with open(filePath, 'rb') as f:
            rawdata = f.read()
        return chardet.detect(rawdata)['encoding']
    
    def OpenFolder(self):
        filePath, _ = QtWidgets.QFileDialog.getOpenFileName(filter="Subtitle Files (*.srt)")
        if  filePath:  # 偵測是否有選擇到檔案
            fileName = os.path.basename(filePath)
            self.SrtName_text.setText(fileName)
            encoding = self.detect_encoding(filePath)
            with open(filePath, 'r', encoding=encoding) as file:  #打開檔案
                text = file.read()  # 讀取檔案內容
                self.SRT_content_plain.setPlainText(text)  # 設定變數為檔案內容
                

    def ChoosePath(self):
        folderPath = QtWidgets.QFileDialog.getExistingDirectory()
        if folderPath:  # 偵測是否有選擇到資料夾
            fileName = self.SrtName_text.toPlainText().strip()  # 以SrtName作為檔案名稱
            if fileName:  # 該檔案名稱不是無文件
                self.Path_text.setText(folderPath)  # 將該檔案之名稱or路徑存入Text儲存
                self.SrtName_text.setText(fileName)
            else:
                QMessageBox.warning(None, "注意", "請選擇要轉換的文件")

    def populate_fonts(self):
        font_families = QtGui.QFontDatabase.families()  # 抓取字體資料庫
        self.Font_combo.addItems(font_families) # 把字體列入Font_Combo存放

    def SaveChanges(self):
        text = self.SRT_content_plain.toPlainText()
        fileName, _ = QFileDialog.getSaveFileName(self, "Save File", "", "Subtitle Files (*.srt)")
        if fileName:
            with open(fileName, "w") as file:
                file.write(text)
                self.close
    
    def Embed(self):
        if self.SrtName_text.toPlainText():  # 偵測是否有選擇到檔案
            if self.Path_text.toPlainText():   # 該檔案名稱不是無文件
                if self.OutName_text.toPlainText():
                    QMessageBox.warning(None, "注意", "影片開始生成")
                else:
                    QMessageBox.warning(None, "注意", "請輸入生成影片之名稱")
            else:
                QMessageBox.warning(None, "注意", "請選擇要儲存的位址")
                
        else:
            QMessageBox.warning(None, "注意", "請選擇要轉換的文件")
    
    def ui(self):
        self.horizontalSlider.setRange(0, 100)
        self.horizontalSlider.setValue(0)
        self.Pause_btn.setDisabled(True)
        self.Stop_btn.setDisabled(True)
        self.horizontalSlider.sliderMoved.connect(lambda: self.player.setPosition(self.horizontalSlider.value()))
    
    def playmusic(self):
        progress = self.player.position()
        self.horizontalSlider.setValue(progress)
        self.label.setText(f'{str(round(progress/1000, 1))}/{str(round(self.player.duration()/1000, 1))}')

    def Play(self):
        if self.horizontalSlider.value() == 0 :
            self.player = QMediaPlayer()             # 設定播放器
            self.path = os.getcwd()                  # 取得音樂檔案路徑
            self.qurl = QUrl.fromLocalFile("./Resources/If I Can Stop One Heart From Breaking Piano Arrangement.wav") # 轉換成 QUrl
            self.audio_output = QAudioOutput()
            self.player.setAudioOutput(self.audio_output)         # 播放器與音樂輸出器綁定
            self.player.setSource(self.qurl)
            self.player.durationChanged.connect(lambda: self.horizontalSlider.setMaximum(self.player.duration()))
            self.run()
            self.player.play()
            self.Pause_btn.setDisabled(False)
            self.Stop_btn.setDisabled(False)
        else:
            self.player.play()
            self.Pause_btn.setDisabled(False)
            self.Stop_btn.setDisabled(False)

    def Pause(self):
        if self.horizontalSlider.value() != 0:
            self.player.pause()

    def Stop(self):
        if self.horizontalSlider.value() != 0:
            self.player.stop()
            self.Pause_btn.setDisabled(True)
            self.Stop_btn.setDisabled(True)

    def run(self):
        self.timer = QTimer()               # 加入定時器
        self.timer.timeout.connect(self.playmusic)   # 設定定時要執行的 function
        self.timer.start(10)              # 啟用定時器，設定間隔時間為 x 毫秒

class Functions:
    def __init__(self, main):
        self.main = main

    def Quit(self):
        Left = QMessageBox()
        Left.information(None, '系統管理者', '程式已安全關閉 請放心退出.')
        app.quit()
'''
字幕位置
form for subtitles setting(srt edit)
'''
############################################
if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = AISRT()
    window.show()
    sys.exit(app.exec())
