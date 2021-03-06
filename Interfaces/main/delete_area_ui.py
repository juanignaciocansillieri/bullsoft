# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'delete_area.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(312, 244)
        MainWindow.setMaximumSize(QtCore.QSize(312, 244))
        MainWindow.setSizeIncrement(QtCore.QSize(312, 244))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setGeometry(QtCore.QRect(-30, 0, 461, 311))
        self.frame_2.setMinimumSize(QtCore.QSize(0, 300))
        self.frame_2.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.frame_2.setStyleSheet("background: #f5f5f5;\n"
"")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.comboBox = QtWidgets.QComboBox(self.frame_2)
        self.comboBox.setGeometry(QtCore.QRect(110, 120, 151, 27))
        self.comboBox.setStyleSheet("background-color: #fff;\n"
"border-radius: 3px;\n"
"padding: 4 5px;\n"
"color: rgb(0, 0, 0);\n"
"font-family:Roboto;\n"
"border: none;\n"
"font-size:13px;\n"
"margin-left: 10px;\n"
"")
        self.comboBox.setObjectName("comboBox")
        self.label_Area = QtWidgets.QLabel(self.frame_2)
        self.label_Area.setGeometry(QtCore.QRect(110, 80, 111, 31))
        font = QtGui.QFont()
        font.setFamily("Cairo")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_Area.setFont(font)
        self.label_Area.setStyleSheet("\n"
"margin-top:10px;\n"
"margin-left:10px\n"
"\n"
"")
        self.label_Area.setObjectName("label_Area")
        self.modificar_btn = QtWidgets.QPushButton(self.frame_2)
        self.modificar_btn.setGeometry(QtCore.QRect(120, 170, 141, 26))
        font = QtGui.QFont()
        font.setFamily("Cairo")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.modificar_btn.setFont(font)
        self.modificar_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.modificar_btn.setStyleSheet("QPushButton{\n"
"background-color: #055ffc;\n"
"color:#fff;\n"
"border-radius: 5px;\n"
"text-align:center;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"\n"
"}")
        self.modificar_btn.setObjectName("modificar_btn")
        self.label_5 = QtWidgets.QLabel(self.frame_2)
        self.label_5.setGeometry(QtCore.QRect(30, 10, 311, 61))
        font = QtGui.QFont()
        font.setFamily("Cairo")
        font.setPointSize(17)
        font.setBold(True)
        font.setWeight(75)
        font.setKerning(True)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("color: #212325;\n"
"margin-bottom: 5px")
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_Area.setText(_translate("MainWindow", "Elegir ??rea"))
        self.modificar_btn.setText(_translate("MainWindow", "Eliminar"))
        self.label_5.setText(_translate("MainWindow", "Eliminar ??rea"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
