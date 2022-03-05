# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'nueva_area.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(657, 289)
        MainWindow.setMaximumSize(QtCore.QSize(16777215, 300))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setMinimumSize(QtCore.QSize(0, 0))
        self.frame_2.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.frame_2.setStyleSheet("background: #fff;\n"
"")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.frame_3 = QtWidgets.QFrame(self.frame_2)
        self.frame_3.setGeometry(QtCore.QRect(0, 0, 771, 291))
        self.frame_3.setMaximumSize(QtCore.QSize(16777215, 400))
        self.frame_3.setStyleSheet("border-radius: 10px;\n"
"background-color: #f5f5f5;\n"
"")
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.label_3 = QtWidgets.QLabel(self.frame_3)
        self.label_3.setGeometry(QtCore.QRect(20, 10, 62, 27))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(-1)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("font-family: Roboto;\n"
"font-size: 14px;\n"
"margin-top:10px;\n"
"margin-left:10px\n"
"\n"
"\n"
"")
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")
        self.motivo_input = QtWidgets.QLineEdit(self.frame_3)
        self.motivo_input.setGeometry(QtCore.QRect(30, 100, 170, 25))
        self.motivo_input.setMinimumSize(QtCore.QSize(0, 0))
        self.motivo_input.setMaximumSize(QtCore.QSize(16777215, 25))
        self.motivo_input.setStyleSheet("QLineEdit{\n"
"background-color: #fff;\n"
"border: 0.5px solid #c1c1c1;\n"
"border-radius: 3px;\n"
"padding: 4 5px;\n"
"color: rgb(0, 0, 0);\n"
"font-family:Roboto;\n"
"font-size:13px;\n"
"font-weight: 400;\n"
"margin-left: 10px;\n"
"\n"
"}\n"
"")
        self.motivo_input.setPlaceholderText("")
        self.motivo_input.setObjectName("motivo_input")
        self.crearprod_btn = QtWidgets.QPushButton(self.frame_3)
        self.crearprod_btn.setGeometry(QtCore.QRect(290, 240, 141, 26))
        font = QtGui.QFont()
        font.setFamily("Cairo")
        font.setPointSize(10)
        self.crearprod_btn.setFont(font)
        self.crearprod_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.crearprod_btn.setStyleSheet("QPushButton{\n"
"background-color: #055ffc;\n"
"color:#fff;\n"
"border-radius: 5px;\n"
"text-align:center;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"\n"
"}")
        self.crearprod_btn.setObjectName("crearprod_btn")
        self.label_egr_ing = QtWidgets.QLabel(self.frame_3)
        self.label_egr_ing.setGeometry(QtCore.QRect(30, 70, 131, 27))
        font = QtGui.QFont()
        font.setFamily("Cairo")
        font.setPointSize(-1)
        font.setBold(True)
        font.setWeight(75)
        self.label_egr_ing.setFont(font)
        self.label_egr_ing.setStyleSheet("font-size: 14px;\n"
"margin-top:10px;\n"
"margin-left:10px\n"
"\n"
"")
        self.label_egr_ing.setObjectName("label_egr_ing")
        self.label_egr_ing_2 = QtWidgets.QLabel(self.frame_3)
        self.label_egr_ing_2.setGeometry(QtCore.QRect(30, 150, 131, 27))
        font = QtGui.QFont()
        font.setFamily("Cairo")
        font.setPointSize(-1)
        font.setBold(True)
        font.setWeight(75)
        self.label_egr_ing_2.setFont(font)
        self.label_egr_ing_2.setStyleSheet("\n"
"font-size: 14px;\n"
"margin-top:10px;\n"
"margin-left:10px\n"
"\n"
"")
        self.label_egr_ing_2.setObjectName("label_egr_ing_2")
        self.motivo_input_2 = QtWidgets.QLineEdit(self.frame_3)
        self.motivo_input_2.setGeometry(QtCore.QRect(30, 180, 170, 25))
        self.motivo_input_2.setMinimumSize(QtCore.QSize(0, 0))
        self.motivo_input_2.setMaximumSize(QtCore.QSize(16777215, 25))
        self.motivo_input_2.setStyleSheet("QLineEdit{\n"
"background-color: #fff;\n"
"border: 0.5px solid #c1c1c1;\n"
"border-radius: 3px;\n"
"padding: 4 5px;\n"
"color: rgb(0, 0, 0);\n"
"font-family:Roboto;\n"
"font-size:13px;\n"
"font-weight: 400;\n"
"margin-left: 10px;\n"
"\n"
"}\n"
"")
        self.motivo_input_2.setPlaceholderText("")
        self.motivo_input_2.setObjectName("motivo_input_2")
        self.label_pasillos = QtWidgets.QLabel(self.frame_3)
        self.label_pasillos.setGeometry(QtCore.QRect(290, 70, 131, 27))
        font = QtGui.QFont()
        font.setFamily("Cairo")
        font.setPointSize(-1)
        font.setBold(True)
        font.setWeight(75)
        self.label_pasillos.setFont(font)
        self.label_pasillos.setStyleSheet("\n"
"font-size: 14px;\n"
"margin-top:10px;\n"
"margin-left:10px\n"
"\n"
"")
        self.label_pasillos.setObjectName("label_pasillos")
        self.label_pasillos_2 = QtWidgets.QLabel(self.frame_3)
        self.label_pasillos_2.setGeometry(QtCore.QRect(290, 150, 131, 27))
        font = QtGui.QFont()
        font.setFamily("Cairo")
        font.setPointSize(-1)
        font.setBold(True)
        font.setWeight(75)
        self.label_pasillos_2.setFont(font)
        self.label_pasillos_2.setStyleSheet("\n"
"font-size: 14px;\n"
"margin-top:10px;\n"
"margin-left:10px\n"
"\n"
"")
        self.label_pasillos_2.setObjectName("label_pasillos_2")
        self.segmentos_num = QtWidgets.QSpinBox(self.frame_3)
        self.segmentos_num.setGeometry(QtCore.QRect(290, 180, 121, 25))
        self.segmentos_num.setStyleSheet("background-color: #fff;\n"
"border-radius: 3px;\n"
"padding: 4 5px;\n"
"color: rgb(0, 0, 0);\n"
"border: 0.5px solid #c1c1c1;\n"
"\n"
"font-size:13px;\n"
"font-weight: 400;\n"
"margin-left: 10px;\n"
"")
        self.segmentos_num.setMinimum(0)
        self.segmentos_num.setMaximum(999)
        self.segmentos_num.setObjectName("segmentos_num")
        self.pasillos_num = QtWidgets.QSpinBox(self.frame_3)
        self.pasillos_num.setGeometry(QtCore.QRect(290, 100, 121, 25))
        self.pasillos_num.setStyleSheet("background-color: #fff;\n"
"border-radius: 3px;\n"
"padding: 4 5px;\n"
"color: rgb(0, 0, 0);\n"
"border: 0.5px solid #c1c1c1;\n"
"font-size:13px;\n"
"font-weight: 400;\n"
"margin-left: 10px;\n"
"")
        self.pasillos_num.setMaximum(999)
        self.pasillos_num.setObjectName("pasillos_num")
        self.comboBox = QtWidgets.QComboBox(self.frame_3)
        self.comboBox.setGeometry(QtCore.QRect(500, 100, 121, 25))
        self.comboBox.setStyleSheet("background-color: #fff;\n"
"border-radius: 3px;\n"
"padding: 4 5px;\n"
"color: rgb(0, 0, 0);\n"
"border: 0.5px solid #c1c1c1;\n"
"font-size:13px;\n"
"font-weight: 400;\n"
"margin-left: 10px;\n"
"")
        self.comboBox.setObjectName("comboBox")
        self.label_pasillos_3 = QtWidgets.QLabel(self.frame_3)
        self.label_pasillos_3.setGeometry(QtCore.QRect(500, 70, 131, 27))
        font = QtGui.QFont()
        font.setFamily("Cairo")
        font.setPointSize(-1)
        font.setBold(True)
        font.setWeight(75)
        self.label_pasillos_3.setFont(font)
        self.label_pasillos_3.setStyleSheet("\n"
"font-size: 14px;\n"
"margin-top:10px;\n"
"margin-left:10px\n"
"\n"
"")
        self.label_pasillos_3.setObjectName("label_pasillos_3")
        self.radioButton = QtWidgets.QRadioButton(self.frame_3)
        self.radioButton.setGeometry(QtCore.QRect(510, 170, 82, 21))
        font = QtGui.QFont()
        font.setFamily("Cairo")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.radioButton.setFont(font)
        self.radioButton.setIconSize(QtCore.QSize(25, 24))
        self.radioButton.setCheckable(True)
        self.radioButton.setChecked(False)
        self.radioButton.setObjectName("radioButton")
        self.radioButton_2 = QtWidgets.QRadioButton(self.frame_3)
        self.radioButton_2.setGeometry(QtCore.QRect(510, 190, 82, 21))
        font = QtGui.QFont()
        font.setFamily("Cairo")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.radioButton_2.setFont(font)
        self.radioButton_2.setAutoExclusive(False)
        self.radioButton_2.setObjectName("radioButton_2")
        self.label_5 = QtWidgets.QLabel(self.frame_3)
        self.label_5.setGeometry(QtCore.QRect(-20, 0, 741, 61))
        font = QtGui.QFont()
        font.setFamily("Cairo")
        font.setPointSize(17)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("color: #212325;\n"
"margin-bottom: 5px")
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.verticalLayout.addWidget(self.frame_2)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.crearprod_btn.setText(_translate("MainWindow", "Crear Área"))
        self.label_egr_ing.setText(_translate("MainWindow", "Nombre"))
        self.label_egr_ing_2.setText(_translate("MainWindow", "Identifcador"))
        self.label_pasillos.setText(_translate("MainWindow", "Pasilllos"))
        self.label_pasillos_2.setText(_translate("MainWindow", "Estanterías"))
        self.label_pasillos_3.setText(_translate("MainWindow", "Posición"))
        self.radioButton.setText(_translate("MainWindow", "Entrada"))
        self.radioButton_2.setText(_translate("MainWindow", "Salida"))
        self.label_5.setText(_translate("MainWindow", "Nueva Área"))
import img_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
