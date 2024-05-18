# Form implementation generated from reading ui file 'SRT_export.ui'
#
# Created by: PyQt6 UI code generator 6.6.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_AI_Transcribe_SRT(object):
    def setupUi(self, AI_Transcribe_SRT):
        AI_Transcribe_SRT.setObjectName("AI_Transcribe_SRT")
        AI_Transcribe_SRT.setEnabled(True)
        AI_Transcribe_SRT.resize(827, 650)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/Images/FireFly01.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        AI_Transcribe_SRT.setWindowIcon(icon)
        AI_Transcribe_SRT.setAutoFillBackground(False)
        AI_Transcribe_SRT.setStyleSheet("BackGround-images")
        self.centralwidget = QtWidgets.QWidget(parent=AI_Transcribe_SRT)
        self.centralwidget.setObjectName("centralwidget")
        self.Language_Transcribe = QtWidgets.QLabel(parent=self.centralwidget)
        self.Language_Transcribe.setGeometry(QtCore.QRect(30, 380, 261, 31))
        font = QtGui.QFont()
        font.setFamily("MV Boli")
        font.setPointSize(14)
        self.Language_Transcribe.setFont(font)
        self.Language_Transcribe.setTextFormat(QtCore.Qt.TextFormat.PlainText)
        self.Language_Transcribe.setObjectName("Language_Transcribe")
        self.SRT_Format = QtWidgets.QLabel(parent=self.centralwidget)
        self.SRT_Format.setGeometry(QtCore.QRect(30, 430, 221, 31))
        font = QtGui.QFont()
        font.setFamily("MV Boli")
        font.setPointSize(14)
        self.SRT_Format.setFont(font)
        self.SRT_Format.setTextFormat(QtCore.Qt.TextFormat.PlainText)
        self.SRT_Format.setObjectName("SRT_Format")
        self.SRT_Prompt = QtWidgets.QLabel(parent=self.centralwidget)
        self.SRT_Prompt.setGeometry(QtCore.QRect(30, 470, 271, 31))
        font = QtGui.QFont()
        font.setFamily("MV Boli")
        font.setPointSize(14)
        self.SRT_Prompt.setFont(font)
        self.SRT_Prompt.setTextFormat(QtCore.Qt.TextFormat.PlainText)
        self.SRT_Prompt.setObjectName("SRT_Prompt")
        self.Output_Path = QtWidgets.QLabel(parent=self.centralwidget)
        self.Output_Path.setGeometry(QtCore.QRect(30, 520, 161, 31))
        font = QtGui.QFont()
        font.setFamily("MV Boli")
        font.setPointSize(14)
        self.Output_Path.setFont(font)
        self.Output_Path.setTextFormat(QtCore.Qt.TextFormat.PlainText)
        self.Output_Path.setObjectName("Output_Path")
        self.PathtextEdit = QtWidgets.QTextEdit(parent=self.centralwidget)
        self.PathtextEdit.setEnabled(False)
        self.PathtextEdit.setGeometry(QtCore.QRect(160, 520, 261, 31))
        font = QtGui.QFont()
        font.setFamily("Malgun Gothic")
        font.setPointSize(12)
        font.setBold(True)
        self.PathtextEdit.setFont(font)
        self.PathtextEdit.setReadOnly(False)
        self.PathtextEdit.setObjectName("PathtextEdit")
        self.Prompt_text = QtWidgets.QTextEdit(parent=self.centralwidget)
        self.Prompt_text.setGeometry(QtCore.QRect(125, 470, 261, 31))
        font = QtGui.QFont()
        font.setFamily("Malgun Gothic")
        font.setPointSize(12)
        font.setBold(True)
        self.Prompt_text.setFont(font)
        self.Prompt_text.setReadOnly(False)
        self.Prompt_text.setObjectName("Prompt_text")
        self.Cancel_btn = QtWidgets.QPushButton(parent=self.centralwidget)
        self.Cancel_btn.setGeometry(QtCore.QRect(25, 600, 100, 35))
        font = QtGui.QFont()
        font.setFamily("MV Boli")
        font.setPointSize(12)
        self.Cancel_btn.setFont(font)
        self.Cancel_btn.setObjectName("Cancel_btn")
        self.Transcribe_btn = QtWidgets.QPushButton(parent=self.centralwidget)
        self.Transcribe_btn.setGeometry(QtCore.QRect(690, 600, 100, 35))
        font = QtGui.QFont()
        font.setFamily("MV Boli")
        font.setPointSize(14)
        self.Transcribe_btn.setFont(font)
        self.Transcribe_btn.setObjectName("Transcribe_btn")
        self.Skip_btn = QtWidgets.QPushButton(parent=self.centralwidget)
        self.Skip_btn.setGeometry(QtCore.QRect(350, 600, 100, 35))
        font = QtGui.QFont()
        font.setFamily("MV Boli")
        font.setPointSize(14)
        self.Skip_btn.setFont(font)
        self.Skip_btn.setObjectName("Skip_btn")
        self.Choosed_File = QtWidgets.QTextEdit(parent=self.centralwidget)
        self.Choosed_File.setEnabled(False)
        self.Choosed_File.setGeometry(QtCore.QRect(210, 380, 401, 31))
        font = QtGui.QFont()
        font.setFamily("Malgun Gothic")
        font.setBold(True)
        self.Choosed_File.setFont(font)
        self.Choosed_File.setReadOnly(False)
        self.Choosed_File.setObjectName("Choosed_File")
        self.ChooseFile_btn = QtWidgets.QPushButton(parent=self.centralwidget)
        self.ChooseFile_btn.setGeometry(QtCore.QRect(620, 385, 75, 23))
        self.ChooseFile_btn.setObjectName("ChooseFile_btn")
        self.PathFind_btn = QtWidgets.QPushButton(parent=self.centralwidget)
        self.PathFind_btn.setGeometry(QtCore.QRect(430, 525, 75, 25))
        self.PathFind_btn.setObjectName("PathFind_btn")
        self.PathDefault_btn = QtWidgets.QPushButton(parent=self.centralwidget)
        self.PathDefault_btn.setGeometry(QtCore.QRect(510, 525, 75, 25))
        self.PathDefault_btn.setObjectName("PathDefault_btn")
        self.Main_Title = QtWidgets.QLabel(parent=self.centralwidget)
        self.Main_Title.setGeometry(QtCore.QRect(60, 0, 704, 154))
        font = QtGui.QFont()
        font.setFamily("MV Boli")
        font.setPointSize(72)
        self.Main_Title.setFont(font)
        self.Main_Title.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.Main_Title.setAutoFillBackground(False)
        self.Main_Title.setTextFormat(QtCore.Qt.TextFormat.PlainText)
        self.Main_Title.setObjectName("Main_Title")
        self.Format_combo = QtWidgets.QComboBox(parent=self.centralwidget)
        self.Format_combo.setGeometry(QtCore.QRect(170, 435, 75, 25))
        font = QtGui.QFont()
        font.setFamily("Malgun Gothic")
        font.setPointSize(12)
        font.setBold(True)
        self.Format_combo.setFont(font)
        self.Format_combo.setObjectName("Format_combo")
        self.background02 = QtWidgets.QLabel(parent=self.centralwidget)
        self.background02.setGeometry(QtCore.QRect(10, 350, 801, 221))
        self.background02.setText("")
        self.background02.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.background02.setObjectName("background02")
        self.tip_btn = QtWidgets.QPushButton(parent=self.centralwidget)
        self.tip_btn.setGeometry(QtCore.QRect(670, 420, 128, 128))
        self.tip_btn.setText("")
        self.tip_btn.setObjectName("tip_btn")
        self.Promt_tip = QtWidgets.QLabel(parent=self.centralwidget)
        self.Promt_tip.setGeometry(QtCore.QRect(390, 470, 21, 31))
        self.Promt_tip.setText("")
        self.Promt_tip.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.Promt_tip.setObjectName("Promt_tip")
        self.Original = QtWidgets.QGroupBox(parent=self.centralwidget)
        self.Original.setGeometry(QtCore.QRect(30, 170, 401, 171))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.Original.setFont(font)
        self.Original.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.Original.setObjectName("Original")
        self.Language_Translate = QtWidgets.QLabel(parent=self.Original)
        self.Language_Translate.setGeometry(QtCore.QRect(20, 45, 161, 31))
        font = QtGui.QFont()
        font.setFamily("MV Boli")
        font.setPointSize(14)
        self.Language_Translate.setFont(font)
        self.Language_Translate.setTextFormat(QtCore.Qt.TextFormat.PlainText)
        self.Language_Translate.setObjectName("Language_Translate")
        self.Translate_combo = QtWidgets.QComboBox(parent=self.Original)
        self.Translate_combo.setGeometry(QtCore.QRect(200, 50, 120, 25))
        font = QtGui.QFont()
        font.setFamily("Malgun Gothic")
        font.setPointSize(12)
        font.setBold(True)
        self.Translate_combo.setFont(font)
        self.Translate_combo.setObjectName("Translate_combo")
        self.Language_Translate_2 = QtWidgets.QLabel(parent=self.Original)
        self.Language_Translate_2.setGeometry(QtCore.QRect(20, 115, 71, 31))
        font = QtGui.QFont()
        font.setFamily("MV Boli")
        font.setPointSize(14)
        self.Language_Translate_2.setFont(font)
        self.Language_Translate_2.setTextFormat(QtCore.Qt.TextFormat.PlainText)
        self.Language_Translate_2.setObjectName("Language_Translate_2")
        self.Translate_combo_2 = QtWidgets.QComboBox(parent=self.Original)
        self.Translate_combo_2.setGeometry(QtCore.QRect(100, 120, 120, 25))
        font = QtGui.QFont()
        font.setFamily("Malgun Gothic")
        font.setPointSize(12)
        font.setBold(True)
        self.Translate_combo_2.setFont(font)
        self.Translate_combo_2.setObjectName("Translate_combo_2")
        self.background02.raise_()
        self.Language_Transcribe.raise_()
        self.SRT_Format.raise_()
        self.SRT_Prompt.raise_()
        self.Output_Path.raise_()
        self.PathtextEdit.raise_()
        self.Prompt_text.raise_()
        self.Cancel_btn.raise_()
        self.Transcribe_btn.raise_()
        self.Skip_btn.raise_()
        self.Choosed_File.raise_()
        self.ChooseFile_btn.raise_()
        self.PathFind_btn.raise_()
        self.PathDefault_btn.raise_()
        self.Main_Title.raise_()
        self.Format_combo.raise_()
        self.tip_btn.raise_()
        self.Promt_tip.raise_()
        self.Original.raise_()
        AI_Transcribe_SRT.setCentralWidget(self.centralwidget)

        self.retranslateUi(AI_Transcribe_SRT)
        QtCore.QMetaObject.connectSlotsByName(AI_Transcribe_SRT)

    def retranslateUi(self, AI_Transcribe_SRT):
        _translate = QtCore.QCoreApplication.translate
        AI_Transcribe_SRT.setWindowTitle(_translate("AI_Transcribe_SRT", "AI_Transcribe_SRT"))
        self.Language_Transcribe.setText(_translate("AI_Transcribe_SRT", "Audio Transcribe："))
        self.SRT_Format.setText(_translate("AI_Transcribe_SRT", "Text Format："))
        self.SRT_Prompt.setText(_translate("AI_Transcribe_SRT", "Prompt："))
        self.Output_Path.setText(_translate("AI_Transcribe_SRT", "Saved Path："))
        self.Cancel_btn.setText(_translate("AI_Transcribe_SRT", "Exit"))
        self.Transcribe_btn.setText(_translate("AI_Transcribe_SRT", "Transcribe"))
        self.Skip_btn.setText(_translate("AI_Transcribe_SRT", "Next"))
        self.ChooseFile_btn.setText(_translate("AI_Transcribe_SRT", "Choose"))
        self.PathFind_btn.setText(_translate("AI_Transcribe_SRT", "Choose"))
        self.PathDefault_btn.setText(_translate("AI_Transcribe_SRT", "Default"))
        self.Main_Title.setText(_translate("AI_Transcribe_SRT", "Speech to SRT"))
        self.Original.setTitle(_translate("AI_Transcribe_SRT", "Audio Settings"))
        self.Language_Translate.setText(_translate("AI_Transcribe_SRT", "Audio Language："))
        self.Language_Translate_2.setText(_translate("AI_Transcribe_SRT", "Model："))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    AI_Transcribe_SRT = QtWidgets.QMainWindow()
    ui = Ui_AI_Transcribe_SRT()
    ui.setupUi(AI_Transcribe_SRT)
    AI_Transcribe_SRT.show()
    sys.exit(app.exec())
