import sys
import os
import time

from PyQt6.QtGui import QPixmap
from PyQt6.QtWidgets import QApplication, QMainWindow, QDialog, QInputDialog
from ui_dialog import Ui_Dialog
from ui_Main import Ui_MainWindow
import threading

# event = threading.Event()
# path = ''

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
            # self.dialog = Dialog()
            # self.dialog.show()
            self.path, ok = QInputDialog.getText(self, 'Выбор папки', 'Введите адрес папки: ')
            self.set_folder()
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

    def set_folder(self):
        os.chdir(self.path)
        self.link.setText(os.getcwd())
        self.im_list = os.listdir()  # лист со всеми названиями изображений
        print(self.im_list)
        self.list_l = len(self.im_list) - 1
        self.btn_disable()
        self.setpix(self.im_list[self.list_i])
        self.show()

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

    # ставит изображение по названию
    def setpix(self, filename):
        print(f"Изображение {filename} поставлено")
        self.pixmap = QPixmap(filename)
        # self.pixmap.scaled(1260, 601, transformMode=)
        # self.pixmap.transformed(transform=)
        self.image.setPixmap(self.pixmap)
        self.name.setText(filename)


# class Dialog(QDialog, Ui_Dialog):
#     def __init__(self):
#         super().__init__()
#         self.setupUi(self)
#
#
#         self.ok.clicked.connect(self.buttons)
#         self.cancel.clicked.connect(self.buttons)
#
#     def buttons(self):
#         if self.sender() == self.ok:
#             path = self.line.text()
#             self.close()
#
#         if self.sender() == self.cancel:
#             self.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MainWindow()
    ex.show()
    sys.exit(app.exec())
