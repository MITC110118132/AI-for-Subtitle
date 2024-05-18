from PyQt6 import QtWidgets, QtCore, QtGui#, QtWebEngineWidgets
from PyQt6.QtWidgets import *
import sys

class Guide(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('User guide')
        self.resize(920, 650)
        self.User_guide()
        self.background()

        self.ok = QPushButton(self)
        self.ok.setText("Understand！")
        self.ok.setStyleSheet('''
                QPushButton{
                border: transparent;
                border-radius: 12px;
                border-color: gray;
                font-size: 12pt;
                font-weight: bold;
                color: #fff;
                }
                QPushButton:hover{
                border:3px solid #000;
                background:#ff0;
                color: black;
                }
                ''')
        self.ok.setGeometry(300,600,250,30)
        self.ok.clicked.connect(self.close)

    def User_guide(self):
        self.label1 = QtWidgets.QLabel(self)
        self.label1.setText('''Speech to SRT:\n
1.Audio Language(影片/音檔語言):下拉選單選擇影片或音檔的原始語言，以下連結查看語言代號(https://en.wikipedia.org/wiki/List_of_ISO_639_language_codes)或瀏覽器搜尋(List of ISO 639 language codes)\n
2.Model(模型大小):本程式會使用獨立顯卡進行轉譯，在右方有標示顯卡VRAM需求，且模型大小會影響轉譯時間\n
3.Audio Transcribe(音訊轉錄):選擇你想要轉譯的影音檔\n
4.Text Format(文字格式):選擇轉譯完成後輸出的文字檔格式\n
5.Prompt(提示字詞):可以輸入些提示字詞讓模型的轉譯結果更加精確\n
6.Saved Path(儲存路徑):選擇轉譯後影音檔的儲存位置\n
7.下一步:將畫面跳轉至字幕嵌入頁面\n\n
字幕嵌入:\n\n
 1.Font(字體):選擇嵌入時字幕的字形，可自行將檔案(.ttf/.ttc)匯入至Font資料夾(※需選擇與SRT檔案語言相容字體檔案)\n
 2.Font Size(字體大小):選擇嵌入時字幕的字體大小　          3.FontColor(字體顏色):選擇嵌入時字幕的字體顏色\n
 4.Background(背景):選擇字幕的背景顏色　　　　　         5.Subtitle Location(字幕位置):選擇字幕想擺放在畫面的位置\n
 6.Choose MP4/MP3:選擇欲嵌入字幕之影片/音檔　　         7.Output path:嵌入字幕後影片之儲存位置\n
 8.Output Video Name:嵌入字幕後之影片名稱　　　　       9.SRT(字幕檔案):選擇在Whisper頁面轉譯完成的檔案\n
 10.Finish:退出程式　　　　　　　　　　　　　　　       11.Embed:完成嵌入''')
        self.label1.setGeometry(10,10,900,630) 
        self.label1.setContentsMargins(0,0,0,0)     # 設定邊界
        self.label1.setWordWrap(True)               # 可以換行
        self.label1.setStyleSheet('''background-color: #007979; color: #97CBFF; border: 4px solid black; border-radius: 11px''')
        self.label1.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeft | QtCore.Qt.AlignmentFlag.AlignTop)  # 對齊方式

        font = QtGui.QFont()                       # 建立文字樣式元件
        font.setFamily('Arial')                     # 設定字體
        font.setPointSize(12)                      # 文字大小
        font.setBold(True)                           # 粗體                     
        self.label1.setFont(font)                   # 設定文字樣式

    def background(self):
        self.setStyleSheet('background: gray')
        self.setAutoFillBackground(True)
        self.lower()
        
if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    Form = Guide()
    Form.show()
    sys.exit(app.exec())