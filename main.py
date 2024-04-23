import sys
import json
from PyQt6.QtWidgets import QApplication, QWidget, QTableWidgetItem
from ui_widget import Ui_Form

class MyWidget(QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        # кнопки
        self.ok_btn.clicked.connect(self.buttons)

        self.pixmap = QPixmap('image.jpg')
        self.image = QLabel(self)
        # Отображаем содержимое QPixmap в объекте QLabel
        self.image.setPixmap(self.pixmap)

    def buttons(self):
        if self.sender() == self.ok_btn:




if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec())