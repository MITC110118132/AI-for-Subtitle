from PyQt6 import QtWidgets, QtCore, QtGui
from PyQt6.QtWidgets import *
from PyQt6.QtGui import *

import sys, os
import Qt_ui.SRT_export, Qt_ui.SRT_edit_form, Qt_ui.AISRT

class AISRT(QtWidgets.QMainWindow, Qt_ui.AISRT.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.w = None
        self.pushButton.clicked.connect(self.Start)

    def Start(self):
        if  self.w is None:
            self.w = SRT_export()
            self.w.show()
            self.hide()

        else:
            self.w.hide()  # Close window.
            self.w = None  # Discard reference.

class SRT_export(QtWidgets.QMainWindow, Qt_ui.SRT_export.Ui_AI_Transcribe_SRT):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.w = None
        self.Skip_btn.clicked.connect(self.NextPage)
        self.Transcribe_btn.clicked.connect(self.NextPage)
        self.Cancel_btn.clicked.connect(self.UpPage)

    def NextPage(self):
        if self.w is None:
            self.w = SRT_edit_form()
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

class SRT_edit_form(QtWidgets.QMainWindow, Qt_ui.SRT_edit_form.Ui_SRT_edit_form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.w = None
        self.Finish_btn.clicked.connect(Functions.Finish)
        self.Return_btn.clicked.connect(self.UpPage)
        self.Folder_btn.clicked.connect(self.OpenFolder)
        self.PathFind_btn.clicked.connect(self.ChoosePath)
        self.populate_fonts() # 在初始化时填充字体列表
        validator = QtGui.QIntValidator()
        self.FontSize_line.setValidator(validator)

    def UpPage(self):
        if self.w is None:
            self.w = SRT_export()
            self.w.show()
            self.hide()
        else:
            self.w.hide()  # Close window.
            self.w = None  # Discard reference.

    def OpenFolder(self):
        filePath , _ = QtWidgets.QFileDialog.getOpenFileName(filter="Subtitle Files (*.srt)")
        if filePath:  # 检查是否选择了文件
            fileName = os.path.basename(filePath)
            self.SrtName_text.setText(fileName)

    def ChoosePath(self):
        folderPath = QtWidgets.QFileDialog.getExistingDirectory()
        if folderPath:  # 检查是否选择了文件夹
            fileName = self.SrtName_text.toPlainText().strip()  # 获取SrtName的文本内容作为文件名
            if fileName:  # 检查文件名是否非空
                # 在此处执行您想要进行的操作，例如创建文件等
                self.Path_text.setText(folderPath)
                self.FileName_text.setText(fileName)
            else:
                QMessageBox.warning(None, "注意", "請選擇要轉換的文件")

    def populate_fonts(self):
        # 获取系统中的字体列表
        font_families = QtGui.QFontDatabase.families()

        # 将字体列表添加到 font_combo 中
        self.Font_combo.addItems(font_families)


class Functions:
    def __init__(self, main):
        self.main = main

    def Finish(form):
        form.close()

############################################
if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = AISRT()
    window.show()
    sys.exit(app.exec())