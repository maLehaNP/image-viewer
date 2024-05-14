import sys
import os
import time
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QPixmap, QTransform
from PyQt6.QtWidgets import QApplication, QMainWindow, QInputDialog
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
        self.turn_btn.clicked.connect(self.buttons)
        self.del_bnt.clicked.connect(self.buttons)

    # функция кнопок
    def buttons(self):
        if self.sender() == self.folder_btn:
            path, ok = QInputDialog.getText(self, 'Выбор папки', 'Введите адрес папки: ')
            self.set_folder(path)
        if self.sender() == self.prev_btn:
            self.list_i -= 1
            self.change_image()
        if self.sender() == self.next_btn:
            self.list_i += 1
            self.change_image()
        if self.sender() == self.first_btn:
            self.list_i = 0
            self.change_image()
        if self.sender() == self.last_btn:
            self.list_i = self.list_l
            self.change_image()
        if self.sender() == self.slide_show_btn:  # слайд-шоу
            while self.list_i != self.list_l + 1:
                self.setpix(self.im_list[self.list_i])
                self.btn_disable()
                self.list_i += 1
                time.sleep(5)  # из-за этого зависает, нужно завести таймер как переменную...
        if self.sender() == self.turn_btn:
            self.turnpix()
        if self.sender() == self.del_bnt:  # удаление
            del_filename = self.filename
            if self.list_i != 0:
                self.prev_btn.click()
            else:
                self.next_btn.click()
            os.remove(del_filename)
            self.im_list = os.listdir()
            self.list_l = len(self.im_list) - 1

    # установить папку и 1-ое изображение
    def set_folder(self, path):
        os.chdir(path)
        self.link.setText(os.getcwd())
        self.im_list = os.listdir()  # лист со всеми названиями изображений
        self.list_l = len(self.im_list) - 1
        self.btn_disable()
        self.setpix(self.im_list[self.list_i])

    # сменить изображение на list_i
    def change_image(self):
        self.safepix()
        self.setpix(self.im_list[self.list_i])
        self.btn_disable()

    # отключение кнопок
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
            self.slide_show_btn.setDisabled(1)
        else:
            self.next_btn.setDisabled(0)
            self.last_btn.setDisabled(0)
            self.slide_show_btn.setDisabled(0)

    # ставит изображение по названию
    def setpix(self, filename):
        self.filename = filename
        self.pixmap = QPixmap(filename)
        self.image.setPixmap(self.pixmap.scaled(self.pixmap.size(), Qt.AspectRatioMode.IgnoreAspectRatio))
        self.name.setText(filename)

    # поворот изображения
    def turnpix(self):
        transform90 = QTransform().rotate(90)
        # mode = Qt.TransformationMode.SmoothTransformation
        rotated = self.pixmap.transformed(transform90)
        self.pixmap = QPixmap(rotated)
        self.image.setPixmap(self.pixmap)

    # сохранение изображения
    def safepix(self):
        self.pixmap.save(self.filename)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MainWindow()
    ex.show()
    sys.exit(app.exec())
