# Form implementation generated from reading ui file 'ui_Main.ui'
#
# Created by: PyQt6 UI code generator 6.7.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1280, 720)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.name = QtWidgets.QLabel(parent=self.centralwidget)
        self.name.setGeometry(QtCore.QRect(10, 30, 1261, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        font.setKerning(False)
        self.name.setFont(font)
        self.name.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.name.setObjectName("name")
        self.turn_l_btn = QtWidgets.QPushButton(parent=self.centralwidget)
        self.turn_l_btn.setGeometry(QtCore.QRect(840, 650, 51, 41))
        self.turn_l_btn.setObjectName("turn_l_btn")
        self.last_btn = QtWidgets.QPushButton(parent=self.centralwidget)
        self.last_btn.setGeometry(QtCore.QRect(760, 660, 71, 21))
        self.last_btn.setObjectName("last_btn")
        self.del_bnt = QtWidgets.QPushButton(parent=self.centralwidget)
        self.del_bnt.setGeometry(QtCore.QRect(960, 660, 61, 23))
        self.del_bnt.setObjectName("del_bnt")
        self.image = QtWidgets.QLabel(parent=self.centralwidget)
        self.image.setGeometry(QtCore.QRect(10, 50, 1261, 591))
        self.image.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.image.setObjectName("image")
        self.folder_btn = QtWidgets.QPushButton(parent=self.centralwidget)
        self.folder_btn.setGeometry(QtCore.QRect(10, 0, 91, 31))
        self.folder_btn.setObjectName("folder_btn")
        self.prev_btn = QtWidgets.QPushButton(parent=self.centralwidget)
        self.prev_btn.setGeometry(QtCore.QRect(520, 650, 71, 41))
        font = QtGui.QFont()
        font.setFamily("Courier New")
        font.setPointSize(16)
        self.prev_btn.setFont(font)
        self.prev_btn.setObjectName("prev_btn")
        self.link = QtWidgets.QLabel(parent=self.centralwidget)
        self.link.setGeometry(QtCore.QRect(200, 0, 1071, 31))
        self.link.setText("")
        self.link.setObjectName("link")
        self.label = QtWidgets.QLabel(parent=self.centralwidget)
        self.label.setGeometry(QtCore.QRect(110, 0, 91, 31))
        self.label.setObjectName("label")
        self.turn_r_btn = QtWidgets.QPushButton(parent=self.centralwidget)
        self.turn_r_btn.setGeometry(QtCore.QRect(900, 650, 51, 41))
        self.turn_r_btn.setObjectName("turn_r_btn")
        self.next_btn = QtWidgets.QPushButton(parent=self.centralwidget)
        self.next_btn.setGeometry(QtCore.QRect(680, 650, 71, 41))
        font = QtGui.QFont()
        font.setFamily("Courier New")
        font.setPointSize(16)
        self.next_btn.setFont(font)
        self.next_btn.setObjectName("next_btn")
        self.first_btn = QtWidgets.QPushButton(parent=self.centralwidget)
        self.first_btn.setGeometry(QtCore.QRect(440, 660, 71, 21))
        self.first_btn.setObjectName("first_btn")
        self.slide_show_btn = QtWidgets.QPushButton(parent=self.centralwidget)
        self.slide_show_btn.setGeometry(QtCore.QRect(600, 650, 71, 41))
        self.slide_show_btn.setObjectName("slide_show_btn")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1280, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Просмотрщик изображений"))
        self.name.setText(_translate("MainWindow", "name"))
        self.turn_l_btn.setText(_translate("MainWindow", "Против"))
        self.last_btn.setText(_translate("MainWindow", "Последний"))
        self.del_bnt.setText(_translate("MainWindow", "Удалить"))
        self.image.setText(_translate("MainWindow", "Изображение"))
        self.folder_btn.setText(_translate("MainWindow", "Выбрать папку"))
        self.prev_btn.setText(_translate("MainWindow", "←"))
        self.label.setText(_translate("MainWindow", "Текущая папка:"))
        self.turn_r_btn.setText(_translate("MainWindow", "По час."))
        self.next_btn.setText(_translate("MainWindow", "→"))
        self.first_btn.setText(_translate("MainWindow", "Первый"))
        self.slide_show_btn.setText(_translate("MainWindow", "Слайд-шоу"))
