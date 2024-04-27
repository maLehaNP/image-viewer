import sys
import os, os.path, shutil

from PyQt6.QtGui import QPixmap
from PyQt6.QtWidgets import QApplication, QWidget, QMainWindow, QDialog
from ui_widget import Ui_Form
from ui_dialog import Ui_Dialog
from ui_Main import Ui_MainWindow


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.im_list = []
        self.list_i = 0
        self.list_l = 0
        self.btn_disable()

        # кнопки
        self.folder_btn.clicked.connect(self.buttons)
        self.prev_btn.clicked.connect(self.buttons)
        self.next_btn.clicked.connect(self.buttons)
        self.first_btn.clicked.connect(self.buttons)
        self.last_btn.clicked.connect(self.buttons)
        self.slide_show_btn.clicked.connect(self.buttons)
        self.turn_l_btn.clicked.connect(self.buttons)
        self.turn_r_btn.clicked.connect(self.buttons)
        self.del_bnt.clicked.connect(self.buttons)

    def buttons(self):
        if self.sender() == self.folder_btn:
            self.dialog = Dialog()
            self.dialog.show()
        if self.sender() == self.prev_btn:
            self.list_i -= 1
            self.setpix(self.im_list[self.list_i])
            self.btn_disable()
        if self.sender() == self.next_btn:
            self.list_i += 1
            self.setpix(self.im_list[self.list_i])
            self.btn_disable()
        if self.sender() == self.first_btn:
            self.list_i = 0
            self.setpix(self.im_list[0])
            self.btn_disable()
        if self.sender() == self.last_btn:
            self.list_i = self.list_l
            self.setpix(self.im_list[self.list_l])
            self.btn_disable()

    def set_folder(self, path):
        os.chdir(path)
        self.link.setText(os.getcwd())
        self.im_list = os.listdir()  # лист со всеми названиями изображений
        self.list_l = len(self.im_list) - 1
        self.btn_disable()
        self.setpix(self.im_list[self.list_i])

    def btn_disable(self):
        if self.list_i == 0:
            self.prev_btn.setDisabled(1)
            self.first_btn.setDisabled(1)
        else:
            self.prev_btn.setDisabled(0)
            self.first_btn.setDisabled(0)
        if self.list_i == self.list_l:
            self.next_btn.setDisabled(1)
            self.last_btn.setDisabled(1)
        else:
            self.next_btn.setDisabled(0)
            self.last_btn.setDisabled(0)

    # ставит изображение по навванию
    def setpix(self, filename):
        self.pixmap = QPixmap(filename)
        # self.pixmap.scaled(1260, 601, transformMode=)
        # self.pixmap.transformed(transform=)
        self.image.setPixmap(self.pixmap)
        self.name.setText(filename)


class Dialog(QDialog, Ui_Dialog):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.buttonBox.clicked.connect(self.buttons)
    def buttons(self):
        if self.buttonBox.sender() == self.buttonBox.standardButton().Yes:
            path = self.line.text()
            MainWindow.set_folder(path)
            self.close()
        else:
            self.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MainWindow()
    ex.show()
    sys.exit(app.exec())
