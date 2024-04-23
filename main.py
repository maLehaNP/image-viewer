import sys
import os, os.path, shutil

from PyQt6.QtGui import QPixmap
from PyQt6.QtWidgets import QApplication, QWidget
from ui_widget import Ui_Form


class MyWidget(QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.im_list = []
        self.list_i = 0

        # кнопки
        self.ok_btn.clicked.connect(self.buttons)
        self.prev_btn.clicked.connect(self.buttons)
        self.next_btn.clicked.connect(self.buttons)
        self.first_btn.clicked.connect(self.buttons)
        self.last_btn.clicked.connect(self.buttons)
        self.slide_show_btn.clicked.connect(self.buttons)
        self.turn_l_btn.clicked.connect(self.buttons)
        self.turn_r_btn.clicked.connect(self.buttons)
        self.del_bnt.clicked.connect(self.buttons)

    def buttons(self):
        if self.sender() == self.ok_btn:
            os.chdir(self.line.text())
            self.link.setText(self.line.text())
            self.im_list = os.listdir()
            self.setpix(self.im_list[self.list_i])
            print(self.im_list)
        if self.sender() == self.next_btn:
            # self.setpix(self.im_list.index(self.image.text()))

    def setpix(self, filename):
        self.pixmap = QPixmap(filename)
        self.image.setPixmap(self.pixmap)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec())
