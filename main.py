from PyQt6 import QtWidgets, QtCore, QtGui
from moviepy.editor import VideoFileClip, TextClip, CompositeVideoClip
from PyQt6.QtMultimedia import QAudioOutput, QMediaPlayer
from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
from whisper.utils import get_writer
import sys, os, webbrowser, whisper, subprocess, torch, tqdm, chardet
import Qt_ui.SRT_export, Qt_ui.Sub_embed_form, matplotlib.font_manager
from GUI.tips import Tips
from GUI.tips2 import Tips as Tips2
from GUI.SRTok_UI import *
from GUI.User_guide import Guide
sys.setrecursionlimit(3000)

current_dir = os.path.dirname(os.path.abspath(__file__))
bin_dir = os.path.join(current_dir, "Python311", "Library", "bin")
bin_dir = os.path.abspath(bin_dir)
os.environ["PATH"] += os.pathsep + bin_dir

current_dir = os.path.dirname(os.path.abspath(__file__))
imagemagick_dir = os.path.join(current_dir, 'Python311', 'Lib', 'site-packages', 'moviepy', 'ImageMagick-7.1.1-Q16-HDRI')
os.environ['PATH'] = imagemagick_dir + os.pathsep + os.environ['PATH']
subprocess.run(['magick', '--version'])

def torch_check_is_gpu_available():
    if torch.cuda.is_available():
        print(f"GPU 正常運行中: 您目前所運行的是 {torch.cuda.get_device_name(0)}")
    else:
        print("GPU 無效")

#啟動網頁之前綴
def callback(url):
    webbrowser.open_new(url)
#版本更新專用
def gt():
        QDesktopServices.openUrl(QUrl("https://github.com/MITC110118132/AI-for-Subtitle"))
        version.destroy()
        window.destroy()
def bye():
        version.destroy()
        print("選擇不更新")
def check_version(version):      
    # 版本偵測
    Older_Version = "V2.6.6"
    GetVersion = "V2.6.7"
    #等開放Github在使用這塊 否則會無法執行
    #url = 'https://raw.githubusercontent.com/MITC110118132/AI-for-Subtitle/main/version.txt?token=GHSAT0AAAAAACPU6YOXJTHYMHVT3LFXUM2GZPYDSEA'
    #response = urllib.request.urlopen(url)
    #GetVersion = response.read().decode('utf-8')
    #print(GetVersion)
    if Older_Version != GetVersion:
        # 若版本不是最新 提示
        app = QtWidgets.QApplication(sys.argv)
        version.setWindowTitle( '版本更新(最新為' + GetVersion + '; 目前為' + Older_Version + ')' )
        version.resize(400,200)

        Main = QtWidgets.QLabel(version)
        Main.setGeometry(100,30,250,45)
        Main.setText('版本更新')
        Main.setStyleSheet('border: transparent; color: red; font-size: 36pt')
        MS1 = QtWidgets.QLabel(version)
        MS1.setGeometry(75,100,250,15)
        MS1.setText('目前所使用的版本不是最新版，請前往更新！！！')    
        #按鈕設定
        upgrade = QtWidgets.QPushButton(version)  
        upgrade.setGeometry(250,150,75,35)
        upgrade.setText('更新')
        upgrade.clicked.connect(gt)

        cancel = QtWidgets.QPushButton("Close",version)
        cancel.setGeometry(75,150,75,35)
        cancel.setText('再說')  
        cancel.clicked.connect(bye)      

        version.show()
        sys.exit(app.exec())

class AISRT(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.w = None
        self.setWindowTitle("AI for Generating SRT")
        self.setFixedSize(850, 650)
        self.title()
        QssStyle = ''' QPushButton{ background-color: white; border: 2px solid black; border-radius: 11px; color: black; font-size: 20pt } QPushButton:hover{ background-color: yellow; border: 4px solid black;  border-radius: 15px; color: black; font-size: 20pt }  '''
        
        self.btn = QtWidgets.QPushButton(self)
        self.btn.setGeometry(360,230,170,40)
        self.btn.setText('Whisper')
        self.btn.clicked.connect(self.GoWhisper)

        self.btn2 = QtWidgets.QPushButton(self)
        self.btn2.setGeometry(360,430,170,40)
        self.btn2.setText('Quit')
        self.btn2.clicked.connect(Functions.Quit)

        self.btn1 = QtWidgets.QPushButton(self)
        self.btn1.setGeometry(360,330,170,40)
        self.btn1.setText('Embed')
        self.btn1.clicked.connect(self.GoSubtitle)

        self.btn3 = QtWidgets.QPushButton(self)
        self.btn3.setGeometry(810,610,30,30)
        self.btn3.setText('?')
        self.btn3.clicked.connect(self.Guide)

        self.background()
        btns = [self.btn, self.btn1, self.btn2, self.btn3, ]
        for btn in btns:
            btn.setStyleSheet(QssStyle)
    def title(self):
        self.labeltl = QtWidgets.QLabel(self)
        self.labeltl.setText("AI Subtitle")
        self.labeltl.setGeometry(300, 70, 400, 400)
        self.labeltl.setContentsMargins(0,0,0,0)     # 設定邊界
        self.labeltl.setAlignment(QtCore.Qt.AlignmentFlag.AlignTop)
        self.labeltl.setStyleSheet('color: Aqua')
        font = QtGui.QFont()
        font.setFamily('Arial')  # 設定字體
        font.setPointSize(50)   # 文字大小
        self.labeltl.setFont(font) # 設定文字樣式     
    def background(self):
        self.setStyleSheet('background: gray')
        self.setAutoFillBackground(True)
        self.lower()        
    def GoWhisper(self):
        if  self.w is None:
            self.w = SRT_export()
            self.w.show()
            self.hide()
        else:
            self.w.hide()  # 隱藏視窗(保留快取)
            self.w = None  # Discard reference.'''
    def GoSubtitle(self):
        if  self.w is None:
            self.w = Sub_embed_form()
            self.w.show()
            self.hide()
        else:
            self.w.hide()  # 隱藏視窗(保留快取)
            self.w = None  # Discard reference.'''
    def Guide(self):
           self.Guide = Guide()
           self.Guide.show()
class SRT_export(QtWidgets.QMainWindow, Qt_ui.SRT_export.Ui_AI_Transcribe_SRT):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.w = None
        self.css()
        self.setFixedSize(825,650)

        #group
        group = QPixmap('./images/BG02.png')
        self.background02.setPixmap(group)
        #self.background02.lower()

        style_btn = (''' QPushButton{border:1px solid #000;background:#fff;} QPushButton:hover{ border:3px solid #000;  background:#ff0; } ''')
        style_btn2 = (''' QPushButton{ border:1px solid #000; background:#fff; border-radius: 10px;} QPushButton:hover{ border:3px solid #000; background:#ff0; border-radius: 10px;} ''')
        
        #設置本頁背景
        label = QLabel(self)
        label.setGeometry(0,0,825,650)
        pixmap = QPixmap('./images/BG01.png')
        label.setPixmap(pixmap)
        label.lower()

        #語言模組
        model_list = ['tiny','base', 'small', 'medium', 'large-v1', 'large-v2', 'large-v3']

        format = ['all','srt', 'vtt', 'txt', 'tsv', 'json']

        #語言列
        languages = ['afrikaans', 'albanian', 'amharic', 'arabic', 'armenian', 'assamese', 'azerbaijani', 'bashkir', 'basque', 'belarusian', 'bengali', 'bosnian', 'breton', 'bulgarian', 'cantonese', 'catalan', 'chinese', 'croatian', 'czech', 'danish', 'dutch', 'english', 'estonian', 'faroese', 'finnish', 'french', 'galician', 'georgian', 'german', 'greek', 'gujarati', 'haitian creole', 'hausa', 'hawaiian', 'hebrew', 'hindi', 'hungarian', 'icelandic', 'indonesian', 'italian', 'japanese', 'javanese', 'kannada', 'kazakh', 'khmer', 'korean', 'lao', 'latin', 'latvian', 'lingala', 'lithuanian', 'luxembourgish', 'macedonian', 'malagasy', 'malay', 'malayalam', 'maltese', 'maori', 'marathi', 'mongolian', 'myanmar', 'nepali', 'norwegian', 'nynorsk', 'occitan', 'pashto', 'persian', 'polish', 'portuguese', 'punjabi', 'romanian', 'russian', 'sanskrit', 'serbian', 'shona', 'sindhi', 'sinhala', 'slovak', 'slovenian', 'somali', 'spanish', 'sundanese', 'swahili', 'swedish', 'tagalog', 'tajik', 'tamil', 'tatar', 'telugu', 'thai', 'tibetan', 'turkish', 'turkmen', 'ukrainian', 'urdu', 'uzbek', 'vietnamese', 'welsh', 'yiddish', 'yoruba']

        self.Translate_combo.setDisabled(False)
        self.Translate_combo.addItems(languages)
        self.Translate_combo_2.addItems(model_list)
        self.Format_combo.addItems(format)

        self.w = None
        #上一頁
        self.Skip_btn.clicked.connect(self.NextPage)
        self.Skip_btn.setStyleSheet(style_btn)

        #轉錄
        self.Transcribe_btn.clicked.connect(self.Transcribe)
        self.Transcribe_btn.setStyleSheet(style_btn)

        #下一頁
        self.Cancel_btn.clicked.connect(self.UpPage)
        self.Cancel_btn.setStyleSheet(style_btn)

        #選擇影片
        self.ChooseFile_btn.clicked.connect(self.SelectVideo)
        self.ChooseFile_btn.setStyleSheet(style_btn2)

        #儲存路徑
        self.PathFind_btn.clicked.connect(self.SaveFile)
        self.PathFind_btn.setStyleSheet(style_btn2)

        #預設路徑
        self.PathDefault_btn.clicked.connect(self.PathDefault)
        self.PathDefault_btn.setStyleSheet(style_btn2)
        self.PathDefault_btn.setToolTip("Reset Saved Path to ./SRT")
        
        self.Promt_tip.setText("?")
        self.Promt_tip.setToolTip('''《Tip for Prompt》\n一.預設可留空\n二.添加更具體的轉錄描述''')
        self.Promt_tip.setStyleSheet('''
                                     QLabel{
                                     font-size: 15pt;
                                     }
                                     QLabel:hover{
                                     border:3px solid #000;
                                     font: bold;
                                     border-radius:30px;
                                     }
                                     ''')

        #tips
        tippix = QPixmap('./images/Lx.png')
        icon = QIcon(tippix)
        self.tip_btn.setIcon(icon)
        self.tip_btn.setIconSize(pixmap.size())
        self.tip_btn.setToolTip("click it to see How to use")
        self.tip_btn.setStyleSheet('''QPushButton{border:transparent; background:#fff; } QPushButton:hover{ border:3px solid #000; background:pink; } ''')                           
        self.tip_btn.clicked.connect(self.tips)
    #設置Css
    def css(self):
        css =('''color:LimeGreen; font-weight: bold;''')
        self.Language_Translate.setStyleSheet('''color:Chartreuse; font-weight: bold;''')
        self.Language_Translate_2.setStyleSheet('''color:Chartreuse; font-weight: bold;''')
        self.Language_Transcribe.setStyleSheet(css)
        self.SRT_Format.setStyleSheet(css)
        self.SRT_Prompt.setStyleSheet(css)
        self.Output_Path.setStyleSheet(css)
        # Table
        self.image_label = QtWidgets.QLabel(self)
        self.image_label.setGeometry(QtCore.QRect(480,175,315,174))
        pixmap = QtGui.QPixmap("./images/table.png")
        self.image_label.setPixmap(pixmap)
        self.image_label.setScaledContents(True)
        #End

    def tips(self):
            self.tip = Tips()
            self.tip.show()
            self.setDisabled(False)

    def NextPage(self):
        if self.w is None:
            self.w = Sub_embed_form()
            self.w.show()
            self.hide()
        else:
            self.w.hide()  # hide window.
            self.w = None  # Discard reference.
            
    def UpPage(self):
        if self.w is None:
            self.w = AISRT()
            self.w.show()
            self.hide()
        else:
            self.w.hide()  # hide window.
            self.w = None  # Discard reference.

    def SaveFile(self):
        SavePath = QFileDialog.getExistingDirectory(self, "請選擇欲儲存的資料夾位置")
        #成功選取影片
        if SavePath:
            fileName = os.path.basename(SavePath)
            print(fileName)
            self.PathtextEdit.setText(SavePath)
        #反之取消or錯誤
        else:
            print("取消選擇 或者 選取的檔案有誤")
            #QMessageBox.warning(self, "Notice！！！", "取消選擇 或者 選取的檔案有誤")

    def SelectVideo(self):
        self.filePath , self.fileextention = QtWidgets.QFileDialog.getOpenFileName(self, "選擇影片", "", "Audio Files (*.mkv *.mp3 *.m4a *.wav) ;; Video Files (*.mov *.mp4 *.avi *.mpeg *.mpga)")

        #成功選取影片
        if self.filePath:
            self.fileName = os.path.basename(self.filePath)
            print(self.fileName)
            self.Choosed_File.setText(self.filePath)
        #反之取消or錯誤
        else:
            print("取消選擇 或者 選取的檔案有誤")
            #QMessageBox.warning(None, "Notice！！！", "取消選擇 或者 選取的檔案有誤")
        return self.filePath

    #點選預設路徑
    def PathDefault(self):
        self.PathtextEdit.setText("")
        print("改回預設路徑")

    #語音轉錄
    def Transcribe(self):
        dir_name = 'SRT File'
        if not os.path.exists(dir_name):
            os.makedirs(dir_name)

        format_whisper = self.Format_combo.currentText()
        print(self.PathtextEdit.toPlainText())
        
        audio_path = self.Choosed_File.toPlainText()
        model = self.Translate_combo_2.currentText()
        audio_language = self.Translate_combo.currentText()

        if self.PathtextEdit.toPlainText() == "":
            print("偵測到沒有選擇存放位置 自動偵測為預設位置")
            save_path = "./SRT File"
        else:
            save_path = self.PathtextEdit.toPlainText()

        prompt = self.Prompt_text.toPlainText()

        try:
            #判斷轉錄的後續處理
            if audio_path:
                model = whisper.load_model(model)
                output_directory = save_path

                result = model.transcribe(audio_path,
                            language=audio_language,
                            initial_prompt=prompt,
                            verbose=None)
                if format_whisper == 'all':
                    all_writer = get_writer(format_whisper, output_directory)
                    all_writer(result, audio_path)
                    print("小孩子才做選擇，我全都要")
                else:
                    writer = get_writer(format_whisper, output_directory)
                    writer(result, audio_path)
                    print("印出的格式為 ." + format_whisper)
                    
                #跳出成功畫面
                print(self.fileextention)
                if self.fileextention == "Video Files (*.mov *.mp4 *.avi *.mpeg *.mpga)":
                    msgbox = QMessageBox()
                    msgbox.setIcon(QMessageBox.Icon.Information)
                    msgbox.setWindowTitle("轉錄成功")
                    msgbox.setText("是否前往嵌入畫面?")
                    msgbox.setStandardButtons(QMessageBox.StandardButton.Ok | QMessageBox.StandardButton.Cancel)
                    result = msgbox.exec()
                    if result == QMessageBox.StandardButton.Ok:
                        try:
                            self.NextPage()
                            self.w.chooseSrt()
                            self.w.choosemp4()
                        except Exception as e:
                            print("換頁異常")
                    else:
                        pass
                else:
                    self.whisper_ok = srt()
                    self.whisper_ok.show()
                print("轉錄成功")
                self.Prompt_text.setText(None)
                print("存放位置：" + save_path)
            else:
                print("轉錄失敗")
                #QMessageBox.warning(self, "Notice！！！", "轉錄失敗")
                self.whisper_no = srt_fail()
                self.whisper_no.show()
        except torch.cuda.OutOfMemoryError:
            QMessageBox.warning(self, "Notice！！！", "VRAM out of Memory！")
        except FileNotFoundError:
            QMessageBox.warning(self, "Notice！！！", "File is Not Found！！")
        except:
            print("轉錄失敗")
            self.whisper_no = srt_fail()
            self.whisper_no.show()
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
        #預覽
        self.image_label = QtWidgets.QLabel(self)
        self.image_label.setGeometry(QtCore.QRect(50, 190, 420, 230))
        pixmap = QtGui.QPixmap("./images/BG02.png")
        self.image_label.setPixmap(pixmap)
        self.image_label.setScaledContents(True)
        self.text_label = QtWidgets.QLabel("Sample Text", self.image_label)
        self.text_label.adjustSize()
        self.text_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.text_label.setStyleSheet('''background: transparent''')
        #背景
        self.setStyleSheet("background-image: url(./images/BG01.png);")
        self.setAutoFillBackground(True)
        self.lower()
        #volume icon
        self.image_label2 = QtWidgets.QLabel(self)
        self.image_label2.setGeometry(QtCore.QRect(50, 145, 35, 35))
        pixmap2 = QtGui.QPixmap("./images/volume.png")
        self.image_label2.setPixmap(pixmap2)
        self.image_label2.setScaledContents(True)
        #css
        label_style = ('''color: gray; font-weight: bold; background: transparent;''')
        labels = [self.Font, self.FontColor, self.FontSize, self.Background_check, self.px, self.Sub_location, self.SRT,
                   self.Output_path, self.Output_Video_Name, self.label, ]
        for label in labels:
            label.setStyleSheet(label_style)
        obj_style = ('''
                QPushButton, QComboBox, QTextEdit, QPlainTextEdit{
                border:1px solid #000;
                background:#fff;
                }
                QPushButton:hover, QComboBox:hover, QTextEdit:hover{
                border:3px solid #000;
                background:#ff0;
                }
                ''')
        objs = [
            #Button
            self.Stop_btn, self.Play_sounds_btn, self.Pause_btn, self.Embed_btn, self.Finish_btn, self.Return_btn
            , self.SaveAs_btn, self.Folder_btn, self.PathFind_btn, self.Choosemp3_btn, self.Choosemp4_btn, self.info,
            #Combobox
            self.Color_combo, self.BG_combo, self.Font_combo, self.FontSize_combo, self.Location_combo,
            #EditText
            self.Path_text, self.OutName_text, self.SrtName_text, self.SRT_content_plain,]
        for obj in objs:
            obj.setStyleSheet(obj_style)
        #Slider
        self.volume_slider.setStyleSheet('''background: transparent;''')
        self.volume_slider.setRange(0, 100)
        self.volume_slider.setValue(50)
        self.horizontalSlider.setStyleSheet('''background: transparent;''')
        self.horizontalSlider.setRange(0, 100)
        self.horizontalSlider.setValue(0)
        self.audioplayer = QMediaPlayer()
        slider_style = ('''QSlider {
                border-radius: 10px;
            }
            QSlider::groove:horizontal {
                height: 5px;
                background: #000;
            }
            QSlider::handle:horizontal{
                background: blue;
                width: 16px;
                height: 16px;
                margin:-6px 0;
                border-radius:4px;
            }
            QSlider::sub-page:horizontal{
                background:#FF8888;
            }''')
        self.volume_slider.setStyleSheet(slider_style+'''
            QSlider::handle:horizontal{
                background:#FF8888;
                width: 12px;
                margin:-2px 0;
            }''')
        self.horizontalSlider.setStyleSheet(slider_style)
        #手動設定結束
        self.w = None
        self.textPosition()
        self.populateFonts()
        self.Finish_btn.clicked.connect(Functions.Quit)
        self.Return_btn.clicked.connect(self.upPage)
        self.Folder_btn.clicked.connect(self.chooseSrt)
        self.PathFind_btn.clicked.connect(self.choosePath)
        self.SaveAs_btn.clicked.connect(self.saveSrt)
        self.Embed_btn.clicked.connect(self.embed)
        self.Play_sounds_btn.clicked.connect(self.play)
        self.Pause_btn.clicked.connect(self.pause)
        self.Stop_btn.clicked.connect(self.stop)
        self.Choosemp3_btn.clicked.connect(self.choosemp3)
        self.Choosemp4_btn.clicked.connect(self.choosemp4)
        self.Location_combo.currentIndexChanged.connect(self.textPosition)
        self.BG_combo.currentIndexChanged.connect(self.updateStyleSheet)
        self.Font_combo.currentIndexChanged.connect(self.updateStyleSheet)
        self.FontSize_combo.currentIndexChanged.connect(self.updateStyleSheet)
        self.Color_combo.currentIndexChanged.connect(self.updateStyleSheet)
        self.Background_check.stateChanged.connect(self.updateStyleSheet)
        self.volume_slider.valueChanged.connect(self.volumeChange)
        self.info.clicked.connect(self.showInfo)
        self.mp4Path = ""
        self.srtPath = ""
        self.audioOutput = None
        self.selectedFileType = None
        
    def showInfo(self):
        self.infoimg = Tips2()
        self.infoimg.show()
        self.setDisabled(False)
        
    def volumeChange(self,volume):
        if self.audioOutput != None:
            volumeValue = float(volume / 100)
            self.audioOutput.setVolume(volumeValue)
            if  volumeValue ==0.0 :
                pixmap2 = QtGui.QPixmap("./images/novolume.png")
                self.image_label2.setPixmap(pixmap2)
            else :
                pixmap2 = QtGui.QPixmap("./images/volume.png")
                self.image_label2.setPixmap(pixmap2)
        
    def upPage(self):
        if self.w is None:
            self.w = SRT_export()
            self.w.show()
            self.hide()
        else:
            self.w.hide()  # hide window.
            self.w = None  # Discard reference.

    def chooseSrt(self):
        self.srtPath, _ = QtWidgets.QFileDialog.getOpenFileName(filter="Subtitle Files (*.srt)")
        if  self.srtPath:  # 偵測是否有選擇到檔案
            self.SrtName_text.setText(self.srtPath)
            with open(self.srtPath, 'rb') as file:  # 以二進位模式打開檔案
                rawdata = file.read()  # 讀取原始檔案內容
                self.SRT_content_plain.setPlainText(rawdata.decode('utf-8'))  # 使用 UTF-8 解碼並設定變數為檔案內容
                
    def choosePath(self):
        self.folderPath = QtWidgets.QFileDialog.getExistingDirectory()
        if self.folderPath:  # 偵測是否有選擇到資料夾
            self.Path_text.setText(self.folderPath)  # 將該檔案之名稱or路徑存入Text儲存
            srt = self.SrtName_text.toPlainText()  # 以SrtName作為檔案名稱
            if srt:  # 該檔案名稱不是無文件
                fileName = os.path.basename(self.SrtName_text.toPlainText()).split(".")[0]
                self.OutName_text.setText(fileName)

    def populateFonts(self):
        font_folder = "./Font/"  # 相对路径到字体文件夹
        font_files = os.listdir(font_folder)
        self.font_name_to_file = {}
        for font_file in font_files:
            font_path = os.path.join(font_folder, font_file)
            font_properties = matplotlib.font_manager.FontProperties(fname=font_path)
            font_name = font_properties.get_name()
            self.font_name_to_file[font_name] = font_path
        font_names = sorted(list(self.font_name_to_file.keys()))
        self.Font_combo.addItems(font_names)
        self.selected_font = font_names[0]  # 默认选择第一个字体

    def saveSrt(self):
        if self.SrtName_text.toPlainText() == "":  # 檢查是否選擇了儲存位置
            self.chooseSrt()
        else:
            with open(self.srtPath, 'wb') as f:  # 以二進位模式打開檔案
                f.write(self.SRT_content_plain.toPlainText().encode('utf-8'))  # 將原始內容以 UTF-8 編碼寫入檔案
    
    def embed(self):
        if self.SrtName_text.toPlainText():
            if self.selectedFileType == 'mp4' and self.mp4Path:
                if self.Path_text.toPlainText():
                    if self.OutName_text.toPlainText():
                        self.audioplayer.stop()
                        self.showPopup()
                    else:
                        QMessageBox.warning(None, "注意", "請輸入生成影片之名稱")
                else:
                    QMessageBox.warning(None, "注意", "請選擇要儲存的位址")
            else:
                QMessageBox.warning(None, "注意", "請選擇要嵌入的影片檔案")
        else:
            QMessageBox.warning(None, "注意", "請選擇要嵌入的文件")
        
    def textPosition(self):
        position = self.Location_combo.currentText()
        if position == "center":
            self.text_label.move(self.image_label.width() // 2 - self.text_label.width() // 2,
                                 self.image_label.height() // 2 - self.text_label.height() // 2)
        elif position == "bottom":
            self.text_label.move(self.image_label.width() // 2 - self.text_label.width() // 2,
                                 self.image_label.height() - self.text_label.height())
        elif position == "right":
            self.text_label.move(self.image_label.width() - self.text_label.width(),
                                 self.image_label.height() // 2 - self.text_label.height() // 2)
        elif position == "left":
            self.text_label.move(0,
                                 self.image_label.height() // 2 - self.text_label.height() // 2)
        elif position == "top":
            self.text_label.move(self.image_label.width() // 2 - self.text_label.width() // 2,
                                 0)
            
    def updateStyleSheet(self):
        font = self.Font_combo.currentText()
        color = self.Color_combo.currentText()
        BG = self.BG_combo.currentText()
        size = self.FontSize_combo.currentText()
        if self.mp4Path:
            resize = self.fontSizeTrans(int(size))
        else:
            resize = size
        if self.Background_check.isChecked():
            BG = self.BG_combo.currentText()
        else:
            BG = "transparent"
        stylesheet = f'font-family: {font}; color: {color}; background: {BG}; font-size: {resize}px;'
        self.text_label.setStyleSheet(stylesheet)
        self.text_label.adjustSize()
        self.textPosition()
    
    def fontSizeTrans(self,size):
        video_clip = VideoFileClip(self.mp4Path)
        video_width = video_clip.size[0]
        resize = int(430 / video_width * int(size))
        video_clip.close()
        return resize
    
    def choosemp3(self) :
        self.audioplayer.stop()
        self.mp3Path, _ = QtWidgets.QFileDialog.getOpenFileName(filter="Audio Files (*.mp3 *.wav *m4a)")
        if  self.mp3Path:
            self.selectedFileType = 'mp3'
            self.mp4Cancel()
            self.soundSetup()
            print(self.mp3Path)
            
    def choosemp4(self) :
        self.audioplayer.stop()
        self.mp4Path, _ = QtWidgets.QFileDialog.getOpenFileName(filter="Video Files (*.mp4 *.avi *.mkv *.mov)")
        if  self.mp4Path:
            self.mp3Path = None
            self.selectedFileType = 'mp4'
            self.extractVideoCover()
            self.soundSetup()
            self.updateStyleSheet()
            print(self.mp4Path)
        else:
            self.mp4Cancel()
            
    def mp4Cancel(self) :
        self.mp4Path = None
        pixmap = QPixmap("./images/BG02.png")  # 图片文件路径
        self.image_label.setPixmap(pixmap)
        self.image_label.setScaledContents(True)  # 让图像适应 QLabel 大小
        
    def extractVideoCover(self):
        # 使用FFmpeg提取封面图像
        subprocess.run(['ffmpeg','-y', '-i', self.mp4Path, '-vframes', '1', 'ffmpegthumbnail.jpg'])
        pixmap = QPixmap("./ffmpegthumbnail.jpg")  # 图片文件路径
        self.image_label.setPixmap(pixmap)
        self.image_label.setScaledContents(True)  # 让图像适应 QLabel 大小

    def soundSetup(self):
        self.audioplayer.stop()
        self.horizontalSlider.sliderMoved.connect(self.onSliderMoved)
        self.horizontalSlider.setValue(0)
        self.Pause_btn.setDisabled(True)
        self.Stop_btn.setDisabled(True)
        self.Play_sounds_btn.setDisabled(False)
        self.audioOutput = QAudioOutput(self)
        self.audioplayer.setAudioOutput(self.audioOutput)
        self.volumeChange(self.volume_slider.value())
        if self.selectedFileType == 'mp4':
            self.audioplayer.setSource(QUrl.fromLocalFile(self.mp4Path))
        elif self.selectedFileType == 'mp3':
            self.audioplayer.setSource(QUrl.fromLocalFile(self.mp3Path))
        self.audioplayer.durationChanged.connect(lambda: self.horizontalSlider.setMaximum(self.audioplayer.duration()))
        self.horizontalSlider.setMaximum(self.audioplayer.duration())
        self.horizontalSlider.update()

    def onSliderMoved(self):
        self.audioplayer.setPosition(self.horizontalSlider.value())

    def playmusic(self):
        progress = self.audioplayer.position()
        self.horizontalSlider.setValue(progress)
        self.label.setText(f'{str(round(progress/1000, 1))}/{str(round(self.audioplayer.duration()/1000, 1))}')

    def play(self):
        self.audioplayer.play()
        self.run()
        self.Pause_btn.setDisabled(False)
        self.Stop_btn.setDisabled(False)
        
    def pause(self):
        self.audioplayer.pause()

    def stop(self):
        self.audioplayer.stop()
        self.Pause_btn.setDisabled(True)
        self.Stop_btn.setDisabled(True)

    def run(self):
        self.timer = QTimer()               # 加入定時器
        self.timer.timeout.connect(self.playmusic)   # 設定定時要執行的 function
        self.timer.start(10)              # 啟用定時器，設定間隔時間為 x 毫秒

    def processVideo(self):
        if self.Background_check.isChecked():
            BG = self.BG_combo.currentText()
        else:
            BG = 'transparent'
        # 读取视频
        video_clip = VideoFileClip(self.mp4Path)
        fps = video_clip.fps
        width, height = video_clip.size
        # 读取SRT文件
        subtitles = self.loadSubtitles(self.srtPath)
        # 处理字幕
        processed_clips = []
        self.chooseFont()
        for subtitle in subtitles:
            subtitle_text = subtitle[0]
            start_time = subtitle[1]
            end_time = subtitle[2]
            # 创建字幕剪辑
            subtitle_clip = TextClip(subtitle_text, fontsize=int(self.FontSize_combo.currentText()), font=self.fontpath,color=self.Color_combo.currentText()
                                     ,bg_color=BG).set_position(self.Location_combo.currentText()).set_duration(end_time - start_time).set_start(start_time)
            processed_clips.append(subtitle_clip)
        # 合成视频
        final_clip = CompositeVideoClip([video_clip] + processed_clips, size=(width, height))
        # 输出视频
        OutputName = self.OutName_text.toPlainText() + ".mp4"
        OutputVideo = self.folderPath + "/" + OutputName
        ffmpeg_params = ['-c:v', 'h264_nvenc', '-preset', 'fast', '-b:v', '5M']
        final_clip.write_videofile(OutputVideo, codec='libx264', fps=fps, ffmpeg_params=ffmpeg_params)
        # 释放资源
        video_clip.close()
        functions_instance = Functions(self)
        functions_instance.delete_file("ffmpegthumbnail.jpg")
        
    def play_video(self):
        try:
            subprocess.Popen([self.mp4Path], shell=True)
        except Exception as e:
            print("播放錯誤:", e)

    def loadSubtitles(self, srtPath):
        subtitles = []
        with open(srtPath, 'r', encoding='utf-8') as f:
            lines = f.readlines()
            for i in range(0, len(lines), 4):
                start_time, end_time = map(self.convertTime, lines[i + 1].strip().split(' --> '))
                text = lines[i + 2].strip()
                subtitles.append((text, start_time, end_time))
        return subtitles

    def convertTime(self, time_str):
        hours, minutes, seconds = map(float, time_str.replace(',', '.').split(':'))
        return hours * 3600 + minutes * 60 + seconds
    
    def chooseFont(self):
        self.selected_font = self.Font_combo.currentText()
        self.fontpath = self.font_name_to_file[self.selected_font]
        print(self.fontpath)

    def showPopup(self):
        msgBox = QMessageBox()
        msgBox.setIcon(QMessageBox.Icon.Information)
        msgBox.setWindowTitle("Check your imformation")
        text = ("Video File: " + str(self.mp4Path) + 
               "\n\nSrt File: " + str(self.srtPath) + 
               "\n\nFont&Size: " + str(self.selected_font) + " / " + str(self.FontSize_combo.currentText()) + "px" + 
               "\n\nSubtitles Location: " + str(self.Location_combo.currentText()) + 
               "\n\nOutput Path: " + str(self.folderPath) + 
               "\n\nOutput Name: " + str(self.OutName_text.toPlainText()))
        if self.Background_check.isChecked():
            text += ("\n\nBackground color: " + str(self.BG_combo.currentText()))
        msgBox.setText(text)
        msgBox.setStandardButtons(QMessageBox.StandardButton.Ok | QMessageBox.StandardButton.Cancel)
        msgBox.setDefaultButton(QMessageBox.StandardButton.Ok)
        result = msgBox.exec()
        if result == QMessageBox.StandardButton.Ok:
            QMessageBox.warning(None, "注意", "影片開始生成")
            self.processVideo()
            QMessageBox.warning(None, "notice", "mission complete!")
            self.mp4Path = self.Path_text.toPlainText() + "/" + self.OutName_text.toPlainText() + ".mp4"
            print(self.mp4Path)
            self.play_video()
        else:
            QMessageBox.warning(None, "notice", "You Cancelled embed")

class Functions:
    def __init__(self, main):
        self.main = main

    def Quit(self):
        Left = QMessageBox()
        functions_instance = Functions(self)
        functions_instance.delete_file("ffmpegthumbnail.jpg")
        Left.information(None, '系統管理者', '程式已安全關閉 請放心退出.')
        app.quit()
            
    def delete_file(self, file_path):
        if os.path.exists(file_path):
            os.remove(file_path)
            
############################################
if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    version = QtWidgets.QWidget() #版本確認用視窗
    window = AISRT()
    window.show()
    torch_check_is_gpu_available()
    sys.exit(app.exec())

