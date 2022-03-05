# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'posiciones_alojamiento.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(535, 301)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setMinimumSize(QtCore.QSize(0, 300))
        self.frame_2.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.frame_2.setStyleSheet("background: #f5f5f5")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.largo_num = QtWidgets.QSpinBox(self.frame_2)
        self.largo_num.setGeometry(QtCore.QRect(110, 130, 121, 25))
        self.largo_num.setStyleSheet("background:#fff;border-radius: 3px;\n"
"padding: 4 5px;\n"
"color: rgb(0, 0, 0);\n"
"font-family:Roboto;\n"
"border: none;\n"
"font-size:13px;\n"
"font-weight: 400;\n"
"margin-left: 10px;\n"
"border: 1px solid #b8b9bd")
        self.largo_num.setMinimum(0)
        self.largo_num.setMaximum(999)
        self.largo_num.setObjectName("largo_num")
        self.label_segmento = QtWidgets.QLabel(self.frame_2)
        self.label_segmento.setGeometry(QtCore.QRect(110, 100, 131, 27))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(-1)
        self.label_segmento.setFont(font)
        self.label_segmento.setStyleSheet("font-family: Roboto;\n"
"font-size: 14px;\n"
"margin-top:10px;\n"
"margin-left:10px\n"
"\n"
"")
        self.label_segmento.setObjectName("label_segmento")
        self.alto_num = QtWidgets.QSpinBox(self.frame_2)
        self.alto_num.setGeometry(QtCore.QRect(320, 190, 121, 25))
        self.alto_num.setStyleSheet("background-color: #fff;\n"
"border-radius: 3px;\n"
"padding: 4 5px;\n"
"color: rgb(0, 0, 0);\n"
"font-family:Roboto;\n"
"border: none;\n"
"font-size:13px;\n"
"font-weight: 400;\n"
"margin-left: 10px;\n"
"border: 1px solid #b8b9bd")
        self.alto_num.setMinimum(0)
        self.alto_num.setMaximum(999)
        self.alto_num.setObjectName("alto_num")
        self.limite_num = QtWidgets.QSpinBox(self.frame_2)
        self.limite_num.setGeometry(QtCore.QRect(110, 190, 121, 25))
        self.limite_num.setStyleSheet("background-color: #fff;\n"
"border-radius: 3px;\n"
"padding: 4 5px;\n"
"color: rgb(0, 0, 0);\n"
"font-family:Roboto;\n"
"border: none;\n"
"font-size:13px;\n"
"font-weight: 400;\n"
"margin-left: 10px;\n"
"border: 1px solid #b8b9bd\n"
"")
        self.limite_num.setMinimum(0)
        self.limite_num.setMaximum(999)
        self.limite_num.setObjectName("limite_num")
        self.ancho_num = QtWidgets.QSpinBox(self.frame_2)
        self.ancho_num.setGeometry(QtCore.QRect(110, 250, 121, 25))
        self.ancho_num.setStyleSheet("background-color: #fff;\n"
"border-radius: 3px;\n"
"padding: 4 5px;\n"
"color: rgb(0, 0, 0);\n"
"font-family:Roboto;\n"
"border: none;\n"
"font-size:13px;\n"
"font-weight: 400;\n"
"margin-left: 10px;\n"
"border: 1px solid #b8b9bd")
        self.ancho_num.setMinimum(0)
        self.ancho_num.setMaximum(999)
        self.ancho_num.setObjectName("ancho_num")
        self.modificar_btn = QtWidgets.QPushButton(self.frame_2)
        self.modificar_btn.setGeometry(QtCore.QRect(330, 250, 111, 26))
        font = QtGui.QFont()
        font.setFamily("Cairo")
        font.setPointSize(10)
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
        self.comboBox_area = QtWidgets.QComboBox(self.frame_2)
        self.comboBox_area.setGeometry(QtCore.QRect(320, 130, 151, 25))
        self.comboBox_area.setStyleSheet("background-color: #fff;\n"
"border-radius: 3px;\n"
"padding: 4 5px;\n"
"color: rgb(0, 0, 0);\n"
"font-family:Roboto;\n"
"border: none;\n"
"font-size:13px;\n"
"font-weight: 400;\n"
"margin-left: 10px;\n"
"border: 1px solid #b8b9bd")
        self.comboBox_area.setObjectName("comboBox_area")
        self.label_alto = QtWidgets.QLabel(self.frame_2)
        self.label_alto.setGeometry(QtCore.QRect(110, 160, 131, 27))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(-1)
        self.label_alto.setFont(font)
        self.label_alto.setStyleSheet("font-family: Roboto;\n"
"font-size: 14px;\n"
"margin-top:10px;\n"
"margin-left:10px\n"
"\n"
"")
        self.label_alto.setObjectName("label_alto")
        self.label_Area = QtWidgets.QLabel(self.frame_2)
        self.label_Area.setGeometry(QtCore.QRect(320, 100, 131, 27))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(-1)
        self.label_Area.setFont(font)
        self.label_Area.setStyleSheet("font-family: Roboto;\n"
"font-size: 14px;\n"
"margin-top:10px;\n"
"margin-left:10px\n"
"\n"
"")
        self.label_Area.setObjectName("label_Area")
        self.label_ancho = QtWidgets.QLabel(self.frame_2)
        self.label_ancho.setGeometry(QtCore.QRect(110, 220, 131, 27))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(-1)
        self.label_ancho.setFont(font)
        self.label_ancho.setStyleSheet("font-family: Roboto;\n"
"font-size: 14px;\n"
"margin-top:10px;\n"
"margin-left:10px\n"
"\n"
"")
        self.label_ancho.setObjectName("label_ancho")
        self.label_limite = QtWidgets.QLabel(self.frame_2)
        self.label_limite.setGeometry(QtCore.QRect(320, 160, 131, 27))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(-1)
        self.label_limite.setFont(font)
        self.label_limite.setStyleSheet("font-family: Roboto;\n"
"font-size: 14px;\n"
"margin-top:10px;\n"
"margin-left:10px\n"
"\n"
"")
        self.label_limite.setObjectName("label_limite")
        self.label_5 = QtWidgets.QLabel(self.frame_2)
        self.label_5.setGeometry(QtCore.QRect(90, 20, 371, 61))
        font = QtGui.QFont()
        font.setFamily("Cairo")
        font.setPointSize(16)
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
        self.label_segmento.setText(_translate("MainWindow", "Largo"))
        self.modificar_btn.setText(_translate("MainWindow", "Crear Posición"))
        self.label_alto.setText(_translate("MainWindow", "Alto"))
        self.label_Area.setText(_translate("MainWindow", "Posición"))
        self.label_ancho.setText(_translate("MainWindow", "Ancho"))
        self.label_limite.setText(_translate("MainWindow", "Peso Maximo"))
        self.label_5.setText(_translate("MainWindow", "Nueva Posición de Alojamiento"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
