# Form implementation generated from reading ui file 'Sub_embed_form.ui'
#
# Created by: PyQt6 UI code generator 6.6.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_SRT_edit_form(object):
    def setupUi(self, SRT_edit_form):
        SRT_edit_form.setObjectName("SRT_edit_form")
        SRT_edit_form.setEnabled(True)
        SRT_edit_form.resize(900, 600)
        self.centralwidget = QtWidgets.QWidget(parent=SRT_edit_form)
        self.centralwidget.setObjectName("centralwidget")
        self.OutName_text = QtWidgets.QTextEdit(parent=self.centralwidget)
        self.OutName_text.setGeometry(QtCore.QRect(255, 540, 191, 31))
        font = QtGui.QFont()
        font.setFamily("MV Boli")
        self.OutName_text.setFont(font)
        self.OutName_text.setObjectName("OutName_text")
        self.Output_Video_Name = QtWidgets.QLabel(parent=self.centralwidget)
        self.Output_Video_Name.setGeometry(QtCore.QRect(55, 540, 191, 31))
        font = QtGui.QFont()
        font.setFamily("MV Boli")
        font.setPointSize(14)
        self.Output_Video_Name.setFont(font)
        self.Output_Video_Name.setTextFormat(QtCore.Qt.TextFormat.PlainText)
        self.Output_Video_Name.setObjectName("Output_Video_Name")
        self.Return_btn = QtWidgets.QPushButton(parent=self.centralwidget)
        self.Return_btn.setGeometry(QtCore.QRect(670, 550, 75, 23))
        font = QtGui.QFont()
        font.setFamily("MV Boli")
        font.setPointSize(12)
        self.Return_btn.setFont(font)
        self.Return_btn.setObjectName("Return_btn")
        self.Finish_btn = QtWidgets.QPushButton(parent=self.centralwidget)
        self.Finish_btn.setGeometry(QtCore.QRect(540, 550, 75, 23))
        font = QtGui.QFont()
        font.setFamily("MV Boli")
        font.setPointSize(12)
        self.Finish_btn.setFont(font)
        self.Finish_btn.setObjectName("Finish_btn")
        self.Output_path = QtWidgets.QLabel(parent=self.centralwidget)
        self.Output_path.setGeometry(QtCore.QRect(55, 494, 121, 31))
        font = QtGui.QFont()
        font.setFamily("MV Boli")
        font.setPointSize(14)
        self.Output_path.setFont(font)
        self.Output_path.setTextFormat(QtCore.Qt.TextFormat.PlainText)
        self.Output_path.setObjectName("Output_path")
        self.SrtName_text = QtWidgets.QTextEdit(parent=self.centralwidget)
        self.SrtName_text.setEnabled(False)
        self.SrtName_text.setGeometry(QtCore.QRect(630, 35, 161, 31))
        font = QtGui.QFont()
        font.setFamily("MV Boli")
        self.SrtName_text.setFont(font)
        self.SrtName_text.setObjectName("SrtName_text")
        self.Embed_btn = QtWidgets.QPushButton(parent=self.centralwidget)
        self.Embed_btn.setGeometry(QtCore.QRect(800, 550, 75, 23))
        font = QtGui.QFont()
        font.setFamily("MV Boli")
        font.setPointSize(12)
        self.Embed_btn.setFont(font)
        self.Embed_btn.setObjectName("Embed_btn")
        self.SRT = QtWidgets.QLabel(parent=self.centralwidget)
        self.SRT.setGeometry(QtCore.QRect(580, 35, 41, 31))
        font = QtGui.QFont()
        font.setFamily("MV Boli")
        font.setPointSize(14)
        self.SRT.setFont(font)
        self.SRT.setTextFormat(QtCore.Qt.TextFormat.PlainText)
        self.SRT.setObjectName("SRT")
        self.Path_text = QtWidgets.QTextEdit(parent=self.centralwidget)
        self.Path_text.setEnabled(False)
        self.Path_text.setGeometry(QtCore.QRect(195, 495, 191, 31))
        font = QtGui.QFont()
        font.setFamily("MV Boli")
        self.Path_text.setFont(font)
        self.Path_text.setObjectName("Path_text")
        self.Folder_btn = QtWidgets.QPushButton(parent=self.centralwidget)
        self.Folder_btn.setGeometry(QtCore.QRect(800, 40, 75, 24))
        font = QtGui.QFont()
        font.setFamily("MV Boli")
        self.Folder_btn.setFont(font)
        self.Folder_btn.setObjectName("Folder_btn")
        self.PathFind_btn = QtWidgets.QPushButton(parent=self.centralwidget)
        self.PathFind_btn.setGeometry(QtCore.QRect(400, 500, 75, 24))
        font = QtGui.QFont()
        font.setFamily("MV Boli")
        self.PathFind_btn.setFont(font)
        self.PathFind_btn.setObjectName("PathFind_btn")
        self.SRT_content_plain = QtWidgets.QPlainTextEdit(parent=self.centralwidget)
        self.SRT_content_plain.setGeometry(QtCore.QRect(539, 90, 341, 361))
        font = QtGui.QFont()
        font.setFamily("MV Boli")
        self.SRT_content_plain.setFont(font)
        self.SRT_content_plain.setObjectName("SRT_content_plain")
        self.SaveAs_btn = QtWidgets.QPushButton(parent=self.centralwidget)
        self.SaveAs_btn.setGeometry(QtCore.QRect(540, 465, 75, 24))
        font = QtGui.QFont()
        font.setFamily("MV Boli")
        self.SaveAs_btn.setFont(font)
        self.SaveAs_btn.setObjectName("SaveAs_btn")
        self.Play_sounds_btn = QtWidgets.QPushButton(parent=self.centralwidget)
        self.Play_sounds_btn.setEnabled(False)
        self.Play_sounds_btn.setGeometry(QtCore.QRect(100, 460, 61, 24))
        font = QtGui.QFont()
        font.setFamily("MV Boli")
        self.Play_sounds_btn.setFont(font)
        self.Play_sounds_btn.setObjectName("Play_sounds_btn")
        self.Sub_location = QtWidgets.QLabel(parent=self.centralwidget)
        self.Sub_location.setGeometry(QtCore.QRect(40, 105, 161, 31))
        font = QtGui.QFont()
        font.setFamily("MV Boli")
        font.setPointSize(14)
        self.Sub_location.setFont(font)
        self.Sub_location.setTextFormat(QtCore.Qt.TextFormat.PlainText)
        self.Sub_location.setObjectName("Sub_location")
        self.Font = QtWidgets.QLabel(parent=self.centralwidget)
        self.Font.setGeometry(QtCore.QRect(40, 35, 41, 31))
        font = QtGui.QFont()
        font.setFamily("MV Boli")
        font.setPointSize(14)
        self.Font.setFont(font)
        self.Font.setTextFormat(QtCore.Qt.TextFormat.PlainText)
        self.Font.setObjectName("Font")
        self.Font_combo = QtWidgets.QComboBox(parent=self.centralwidget)
        self.Font_combo.setGeometry(QtCore.QRect(100, 40, 181, 22))
        font = QtGui.QFont()
        font.setFamily("MV Boli")
        self.Font_combo.setFont(font)
        self.Font_combo.setObjectName("Font_combo")
        self.Location_combo = QtWidgets.QComboBox(parent=self.centralwidget)
        self.Location_combo.setGeometry(QtCore.QRect(210, 110, 111, 22))
        font = QtGui.QFont()
        font.setFamily("MV Boli")
        self.Location_combo.setFont(font)
        self.Location_combo.setObjectName("Location_combo")
        self.Location_combo.addItem("")
        self.Location_combo.addItem("")
        self.Location_combo.addItem("")
        self.Location_combo.addItem("")
        self.Location_combo.addItem("")
        self.label = QtWidgets.QLabel(parent=self.centralwidget)
        self.label.setGeometry(QtCore.QRect(380, 430, 121, 20))
        font = QtGui.QFont()
        font.setFamily("MV Boli")
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight|QtCore.Qt.AlignmentFlag.AlignTrailing|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.label.setObjectName("label")
        self.Pause_btn = QtWidgets.QPushButton(parent=self.centralwidget)
        self.Pause_btn.setEnabled(False)
        self.Pause_btn.setGeometry(QtCore.QRect(210, 460, 61, 24))
        font = QtGui.QFont()
        font.setFamily("MV Boli")
        self.Pause_btn.setFont(font)
        self.Pause_btn.setObjectName("Pause_btn")
        self.Stop_btn = QtWidgets.QPushButton(parent=self.centralwidget)
        self.Stop_btn.setEnabled(False)
        self.Stop_btn.setGeometry(QtCore.QRect(320, 460, 61, 24))
        font = QtGui.QFont()
        font.setFamily("MV Boli")
        self.Stop_btn.setFont(font)
        self.Stop_btn.setObjectName("Stop_btn")
        self.horizontalSlider = QtWidgets.QSlider(parent=self.centralwidget)
        self.horizontalSlider.setGeometry(QtCore.QRect(70, 430, 311, 20))
        font = QtGui.QFont()
        font.setFamily("MV Boli")
        self.horizontalSlider.setFont(font)
        self.horizontalSlider.setOrientation(QtCore.Qt.Orientation.Horizontal)
        self.horizontalSlider.setObjectName("horizontalSlider")
        self.Choosemp4_btn = QtWidgets.QPushButton(parent=self.centralwidget)
        self.Choosemp4_btn.setGeometry(QtCore.QRect(310, 150, 91, 24))
        self.Choosemp4_btn.setObjectName("Choosemp4_btn")
        self.Choosemp3_btn = QtWidgets.QPushButton(parent=self.centralwidget)
        self.Choosemp3_btn.setGeometry(QtCore.QRect(410, 150, 91, 24))
        self.Choosemp3_btn.setObjectName("Choosemp3_btn")
        self.px = QtWidgets.QLabel(parent=self.centralwidget)
        self.px.setGeometry(QtCore.QRect(480, 35, 31, 31))
        font = QtGui.QFont()
        font.setFamily("MV Boli")
        font.setPointSize(14)
        self.px.setFont(font)
        self.px.setTextFormat(QtCore.Qt.TextFormat.PlainText)
        self.px.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight|QtCore.Qt.AlignmentFlag.AlignTrailing|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.px.setObjectName("px")
        self.FontSize = QtWidgets.QLabel(parent=self.centralwidget)
        self.FontSize.setGeometry(QtCore.QRect(310, 35, 91, 31))
        font = QtGui.QFont()
        font.setFamily("MV Boli")
        font.setPointSize(14)
        self.FontSize.setFont(font)
        self.FontSize.setTextFormat(QtCore.Qt.TextFormat.PlainText)
        self.FontSize.setObjectName("FontSize")
        self.FontColor = QtWidgets.QLabel(parent=self.centralwidget)
        self.FontColor.setGeometry(QtCore.QRect(40, 70, 91, 31))
        font = QtGui.QFont()
        font.setFamily("MV Boli")
        font.setPointSize(14)
        self.FontColor.setFont(font)
        self.FontColor.setTextFormat(QtCore.Qt.TextFormat.PlainText)
        self.FontColor.setObjectName("FontColor")
        self.Color_combo = QtWidgets.QComboBox(parent=self.centralwidget)
        self.Color_combo.setGeometry(QtCore.QRect(140, 75, 111, 22))
        font = QtGui.QFont()
        font.setFamily("MV Boli")
        self.Color_combo.setFont(font)
        self.Color_combo.setObjectName("Color_combo")
        self.Color_combo.addItem("")
        self.Color_combo.addItem("")
        self.Color_combo.addItem("")
        self.Color_combo.addItem("")
        self.Color_combo.addItem("")
        self.Color_combo.addItem("")
        self.Color_combo.addItem("")
        self.Color_combo.addItem("")
        self.Color_combo.addItem("")
        self.BG_combo = QtWidgets.QComboBox(parent=self.centralwidget)
        self.BG_combo.setGeometry(QtCore.QRect(390, 75, 111, 22))
        font = QtGui.QFont()
        font.setFamily("MV Boli")
        self.BG_combo.setFont(font)
        self.BG_combo.setObjectName("BG_combo")
        self.BG_combo.addItem("")
        self.BG_combo.addItem("")
        self.BG_combo.addItem("")
        self.BG_combo.addItem("")
        self.BG_combo.addItem("")
        self.BG_combo.addItem("")
        self.BG_combo.addItem("")
        self.BG_combo.addItem("")
        self.BG_combo.addItem("")
        self.FontSize_combo = QtWidgets.QComboBox(parent=self.centralwidget)
        self.FontSize_combo.setGeometry(QtCore.QRect(410, 40, 61, 22))
        font = QtGui.QFont()
        font.setFamily("MV Boli")
        self.FontSize_combo.setFont(font)
        self.FontSize_combo.setObjectName("FontSize_combo")
        self.FontSize_combo.addItem("")
        self.FontSize_combo.addItem("")
        self.FontSize_combo.addItem("")
        self.FontSize_combo.addItem("")
        self.FontSize_combo.addItem("")
        self.FontSize_combo.addItem("")
        self.FontSize_combo.addItem("")
        self.FontSize_combo.addItem("")
        self.FontSize_combo.addItem("")
        self.FontSize_combo.addItem("")
        self.FontSize_combo.addItem("")
        self.FontSize_combo.addItem("")
        self.FontSize_combo.addItem("")
        self.FontSize_combo.addItem("")
        self.FontSize_combo.addItem("")
        self.FontSize_combo.addItem("")
        self.FontSize_combo.addItem("")
        self.FontSize_combo.addItem("")
        self.FontSize_combo.addItem("")
        self.FontSize_combo.addItem("")
        self.FontSize_combo.addItem("")
        self.FontSize_combo.addItem("")
        self.FontSize_combo.addItem("")
        self.FontSize_combo.addItem("")
        self.FontSize_combo.addItem("")
        self.FontSize_combo.addItem("")
        self.FontSize_combo.addItem("")
        self.FontSize_combo.addItem("")
        self.FontSize_combo.addItem("")
        self.FontSize_combo.addItem("")
        self.FontSize_combo.addItem("")
        self.FontSize_combo.addItem("")
        self.FontSize_combo.addItem("")
        self.FontSize_combo.addItem("")
        self.FontSize_combo.addItem("")
        self.FontSize_combo.addItem("")
        self.FontSize_combo.addItem("")
        self.FontSize_combo.addItem("")
        self.FontSize_combo.addItem("")
        self.FontSize_combo.addItem("")
        self.Background_check = QtWidgets.QCheckBox(parent=self.centralwidget)
        self.Background_check.setGeometry(QtCore.QRect(260, 75, 121, 20))
        font = QtGui.QFont()
        font.setFamily("MV Boli")
        font.setPointSize(14)
        self.Background_check.setFont(font)
        self.Background_check.setObjectName("Background_check")
        self.info = QtWidgets.QPushButton(parent=self.centralwidget)
        self.info.setGeometry(QtCore.QRect(800, 465, 75, 24))
        font = QtGui.QFont()
        font.setFamily("MV Boli")
        self.info.setFont(font)
        self.info.setObjectName("info")
        self.volume_slider = QtWidgets.QSlider(parent=self.centralwidget)
        self.volume_slider.setGeometry(QtCore.QRect(100, 150, 151, 20))
        font = QtGui.QFont()
        font.setFamily("MV Boli")
        self.volume_slider.setFont(font)
        self.volume_slider.setOrientation(QtCore.Qt.Orientation.Horizontal)
        self.volume_slider.setObjectName("volume_slider")
        self.SrtName_text.raise_()
        self.OutName_text.raise_()
        self.Output_Video_Name.raise_()
        self.Return_btn.raise_()
        self.Finish_btn.raise_()
        self.Output_path.raise_()
        self.Embed_btn.raise_()
        self.SRT.raise_()
        self.Path_text.raise_()
        self.Folder_btn.raise_()
        self.PathFind_btn.raise_()
        self.SRT_content_plain.raise_()
        self.SaveAs_btn.raise_()
        self.Play_sounds_btn.raise_()
        self.Sub_location.raise_()
        self.Font.raise_()
        self.Font_combo.raise_()
        self.Location_combo.raise_()
        self.label.raise_()
        self.Pause_btn.raise_()
        self.Stop_btn.raise_()
        self.horizontalSlider.raise_()
        self.Choosemp4_btn.raise_()
        self.Choosemp3_btn.raise_()
        self.px.raise_()
        self.FontSize.raise_()
        self.FontColor.raise_()
        self.Color_combo.raise_()
        self.BG_combo.raise_()
        self.FontSize_combo.raise_()
        self.Background_check.raise_()
        self.info.raise_()
        self.volume_slider.raise_()
        SRT_edit_form.setCentralWidget(self.centralwidget)

        self.retranslateUi(SRT_edit_form)
        QtCore.QMetaObject.connectSlotsByName(SRT_edit_form)

    def retranslateUi(self, SRT_edit_form):
        _translate = QtCore.QCoreApplication.translate
        SRT_edit_form.setWindowTitle(_translate("SRT_edit_form", "MainWindow"))
        self.Output_Video_Name.setText(_translate("SRT_edit_form", "Output Video Name"))
        self.Return_btn.setText(_translate("SRT_edit_form", "Back"))
        self.Finish_btn.setText(_translate("SRT_edit_form", "Finish"))
        self.Finish_btn.setShortcut(_translate("SRT_edit_form", "Esc"))
        self.Output_path.setText(_translate("SRT_edit_form", "Output path"))
        self.Embed_btn.setText(_translate("SRT_edit_form", "Embed"))
        self.SRT.setText(_translate("SRT_edit_form", "SRT"))
        self.Folder_btn.setText(_translate("SRT_edit_form", "Choose"))
        self.PathFind_btn.setText(_translate("SRT_edit_form", "Choose"))
        self.SaveAs_btn.setText(_translate("SRT_edit_form", "Save"))
        self.SaveAs_btn.setShortcut(_translate("SRT_edit_form", "Ctrl+S"))
        self.Play_sounds_btn.setText(_translate("SRT_edit_form", "Play"))
        self.Play_sounds_btn.setShortcut(_translate("SRT_edit_form", "Ctrl+Q"))
        self.Sub_location.setText(_translate("SRT_edit_form", "Subtitle Location"))
        self.Font.setText(_translate("SRT_edit_form", "Font"))
        self.Location_combo.setItemText(0, _translate("SRT_edit_form", "center"))
        self.Location_combo.setItemText(1, _translate("SRT_edit_form", "top"))
        self.Location_combo.setItemText(2, _translate("SRT_edit_form", "left"))
        self.Location_combo.setItemText(3, _translate("SRT_edit_form", "bottom"))
        self.Location_combo.setItemText(4, _translate("SRT_edit_form", "right"))
        self.label.setText(_translate("SRT_edit_form", "Progress"))
        self.Pause_btn.setText(_translate("SRT_edit_form", "Pause"))
        self.Pause_btn.setShortcut(_translate("SRT_edit_form", "Ctrl+W"))
        self.Stop_btn.setText(_translate("SRT_edit_form", "Stop"))
        self.Stop_btn.setShortcut(_translate("SRT_edit_form", "Ctrl+E"))
        self.Choosemp4_btn.setText(_translate("SRT_edit_form", "Choose MP4"))
        self.Choosemp3_btn.setText(_translate("SRT_edit_form", "Choose MP3"))
        self.px.setText(_translate("SRT_edit_form", "px "))
        self.FontSize.setText(_translate("SRT_edit_form", "Font Size"))
        self.FontColor.setText(_translate("SRT_edit_form", "FontColor"))
        self.Color_combo.setItemText(0, _translate("SRT_edit_form", "black"))
        self.Color_combo.setItemText(1, _translate("SRT_edit_form", "white"))
        self.Color_combo.setItemText(2, _translate("SRT_edit_form", "red"))
        self.Color_combo.setItemText(3, _translate("SRT_edit_form", "orange"))
        self.Color_combo.setItemText(4, _translate("SRT_edit_form", "purple"))
        self.Color_combo.setItemText(5, _translate("SRT_edit_form", "pink"))
        self.Color_combo.setItemText(6, _translate("SRT_edit_form", "yellow"))
        self.Color_combo.setItemText(7, _translate("SRT_edit_form", "blue"))
        self.Color_combo.setItemText(8, _translate("SRT_edit_form", "green"))
        self.BG_combo.setItemText(0, _translate("SRT_edit_form", "white"))
        self.BG_combo.setItemText(1, _translate("SRT_edit_form", "black"))
        self.BG_combo.setItemText(2, _translate("SRT_edit_form", "red"))
        self.BG_combo.setItemText(3, _translate("SRT_edit_form", "orange"))
        self.BG_combo.setItemText(4, _translate("SRT_edit_form", "purple"))
        self.BG_combo.setItemText(5, _translate("SRT_edit_form", "pink"))
        self.BG_combo.setItemText(6, _translate("SRT_edit_form", "yellow"))
        self.BG_combo.setItemText(7, _translate("SRT_edit_form", "blue"))
        self.BG_combo.setItemText(8, _translate("SRT_edit_form", "green"))
        self.FontSize_combo.setItemText(0, _translate("SRT_edit_form", "12"))
        self.FontSize_combo.setItemText(1, _translate("SRT_edit_form", "15"))
        self.FontSize_combo.setItemText(2, _translate("SRT_edit_form", "18"))
        self.FontSize_combo.setItemText(3, _translate("SRT_edit_form", "20"))
        self.FontSize_combo.setItemText(4, _translate("SRT_edit_form", "22"))
        self.FontSize_combo.setItemText(5, _translate("SRT_edit_form", "25"))
        self.FontSize_combo.setItemText(6, _translate("SRT_edit_form", "28"))
        self.FontSize_combo.setItemText(7, _translate("SRT_edit_form", "30"))
        self.FontSize_combo.setItemText(8, _translate("SRT_edit_form", "32"))
        self.FontSize_combo.setItemText(9, _translate("SRT_edit_form", "35"))
        self.FontSize_combo.setItemText(10, _translate("SRT_edit_form", "38"))
        self.FontSize_combo.setItemText(11, _translate("SRT_edit_form", "40"))
        self.FontSize_combo.setItemText(12, _translate("SRT_edit_form", "42"))
        self.FontSize_combo.setItemText(13, _translate("SRT_edit_form", "45"))
        self.FontSize_combo.setItemText(14, _translate("SRT_edit_form", "48"))
        self.FontSize_combo.setItemText(15, _translate("SRT_edit_form", "50"))
        self.FontSize_combo.setItemText(16, _translate("SRT_edit_form", "52"))
        self.FontSize_combo.setItemText(17, _translate("SRT_edit_form", "55"))
        self.FontSize_combo.setItemText(18, _translate("SRT_edit_form", "58"))
        self.FontSize_combo.setItemText(19, _translate("SRT_edit_form", "60"))
        self.FontSize_combo.setItemText(20, _translate("SRT_edit_form", "62"))
        self.FontSize_combo.setItemText(21, _translate("SRT_edit_form", "65"))
        self.FontSize_combo.setItemText(22, _translate("SRT_edit_form", "68"))
        self.FontSize_combo.setItemText(23, _translate("SRT_edit_form", "70"))
        self.FontSize_combo.setItemText(24, _translate("SRT_edit_form", "72"))
        self.FontSize_combo.setItemText(25, _translate("SRT_edit_form", "75"))
        self.FontSize_combo.setItemText(26, _translate("SRT_edit_form", "78"))
        self.FontSize_combo.setItemText(27, _translate("SRT_edit_form", "80"))
        self.FontSize_combo.setItemText(28, _translate("SRT_edit_form", "72"))
        self.FontSize_combo.setItemText(29, _translate("SRT_edit_form", "75"))
        self.FontSize_combo.setItemText(30, _translate("SRT_edit_form", "78"))
        self.FontSize_combo.setItemText(31, _translate("SRT_edit_form", "80"))
        self.FontSize_combo.setItemText(32, _translate("SRT_edit_form", "82"))
        self.FontSize_combo.setItemText(33, _translate("SRT_edit_form", "85"))
        self.FontSize_combo.setItemText(34, _translate("SRT_edit_form", "88"))
        self.FontSize_combo.setItemText(35, _translate("SRT_edit_form", "90"))
        self.FontSize_combo.setItemText(36, _translate("SRT_edit_form", "92"))
        self.FontSize_combo.setItemText(37, _translate("SRT_edit_form", "95"))
        self.FontSize_combo.setItemText(38, _translate("SRT_edit_form", "98"))
        self.FontSize_combo.setItemText(39, _translate("SRT_edit_form", "100"))
        self.Background_check.setText(_translate("SRT_edit_form", "Background"))
        self.info.setText(_translate("SRT_edit_form", "?"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    SRT_edit_form = QtWidgets.QMainWindow()
    ui = Ui_SRT_edit_form()
    ui.setupUi(SRT_edit_form)
    SRT_edit_form.show()
    sys.exit(app.exec())
