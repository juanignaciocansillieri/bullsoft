# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'movimiento_ui.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(475, 270)
        MainWindow.setMaximumSize(QtCore.QSize(475, 296))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setMinimumSize(QtCore.QSize(0, 237))
        self.frame_2.setMaximumSize(QtCore.QSize(16777215, 300))
        self.frame_2.setStyleSheet("background: #fff;\n"
                                   "")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.frame_3 = QtWidgets.QFrame(self.frame_2)
        self.frame_3.setGeometry(QtCore.QRect(10, 10, 455, 242))
        self.frame_3.setMinimumSize(QtCore.QSize(435, 242))
        self.frame_3.setMaximumSize(QtCore.QSize(16777215, 400))
        self.frame_3.setStyleSheet("border-radius: 10px;\n"
                                   "background-color: rgb(240, 242, 255);\n"
                                   "")
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.label_fecha = QtWidgets.QLabel(self.frame_3)
        self.label_fecha.setGeometry(QtCore.QRect(230, 20, 131, 27))
        self.label_fecha.setMaximumSize(QtCore.QSize(174, 16777215))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(-1)
        self.label_fecha.setFont(font)
        self.label_fecha.setStyleSheet("font-family: Roboto;\n"
                                       "font-size: 14px;\n"
                                       "margin-top:10px;\n"
                                       "margin-left:10px\n"
                                       "\n"
                                       "")
        self.label_fecha.setObjectName("label_fecha")
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
        self.codigo_producto_input = QtWidgets.QLineEdit(self.frame_3)
        self.codigo_producto_input.setGeometry(QtCore.QRect(20, 50, 170, 25))
        self.codigo_producto_input.setMinimumSize(QtCore.QSize(0, 0))
        self.codigo_producto_input.setMaximumSize(QtCore.QSize(16777215, 25))
        self.codigo_producto_input.setStyleSheet("QLineEdit{\n"
                                                 "background-color: #fff;\n"
                                                 "border: 0.5px solid #c1c1c1;\n"
                                                 "border-radius: 3px;\n"
                                                 "padding: 4 5px;\n"
                                                 "font-family:Roboto;\n"
                                                 "font-size:13px;\n"
                                                 "font-weight: 400;\n"
                                                 "margin-left: 10px;\n"
                                                 "\n"
                                                 "}\n"
                                                 "")
        self.codigo_producto_input.setPlaceholderText("")
        self.codigo_producto_input.setObjectName("codigo_producto_input")
        self.label_codigo_producto = QtWidgets.QLabel(self.frame_3)
        self.label_codigo_producto.setGeometry(QtCore.QRect(20, 20, 141, 27))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(-1)
        self.label_codigo_producto.setFont(font)
        self.label_codigo_producto.setStyleSheet("font-family: Roboto;\n"
                                                 "font-size: 14px;\n"
                                                 "margin-top:10px;\n"
                                                 "margin-left:10px\n"
                                                 "\n"
                                                 "")
        self.label_codigo_producto.setObjectName("label_codigo_producto")
        self.label_motivo = QtWidgets.QLabel(self.frame_3)
        self.label_motivo.setGeometry(QtCore.QRect(20, 90, 71, 27))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(-1)
        self.label_motivo.setFont(font)
        self.label_motivo.setStyleSheet("font-family: Roboto;\n"
                                        "font-size: 14px;\n"
                                        "margin-top:10px;\n"
                                        "margin-left:10px\n"
                                        "\n"
                                        "")
        self.label_motivo.setObjectName("label_motivo")
        self.motivo_input = QtWidgets.QLineEdit(self.frame_3)
        self.motivo_input.setGeometry(QtCore.QRect(20, 120, 170, 25))
        self.motivo_input.setMinimumSize(QtCore.QSize(0, 0))
        self.motivo_input.setMaximumSize(QtCore.QSize(16777215, 25))
        self.motivo_input.setStyleSheet("QLineEdit{\n"
                                        "background-color: #fff;\n"
                                        "border: 0.5px solid #c1c1c1;\n"
                                        "border-radius: 3px;\n"
                                        "padding: 4 5px;\n"
                                        "\n"
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
        self.crearprod_btn.setGeometry(QtCore.QRect(240, 180, 161, 26))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(-1)
        self.crearprod_btn.setFont(font)
        self.crearprod_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.crearprod_btn.setStyleSheet("QPushButton{\n"
                                         "background-color: rgba(71, 71, 103);\n"
                                         "color: #fff;\n"
                                         "border-radius:5px;\n"
                                         "font-family:Roboto;\n"
                                         "font-size: 13px\n"
                                         "\n"
                                         "}\n"
                                         "QPushButton:hover{\n"
                                         "background-color: rgba(71, 71, 103,180);\n"
                                         "}")
        self.crearprod_btn.setObjectName("crearprod_btn")
        self.fecha_date = QtWidgets.QDateEdit(self.frame_3)
        self.fecha_date.setGeometry(QtCore.QRect(230, 50, 170, 25))
        self.fecha_date.setStyleSheet("\n"
                                      "background-color: #fff;\n"
                                      "border: 0.5px solid #c1c1c1;\n"
                                      "border-radius: 3px;\n"
                                      "padding: 4 5px;\n"
                                      "color: #000;\n"
                                      "font-family:Roboto;\n"
                                      "font-size:13px;\n"
                                      "font-weight: 400;\n"
                                      "margin-left: 10px;\n"
                                      "\n"
                                      "")
        self.fecha_date.setDateTime(QtCore.QDateTime(QtCore.QDate(2021, 1, 1), QtCore.QTime(0, 0, 0)))
        self.fecha_date.setObjectName("fecha_date")
        self.label_cantidad = QtWidgets.QLabel(self.frame_3)
        self.label_cantidad.setGeometry(QtCore.QRect(20, 150, 141, 27))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(-1)
        self.label_cantidad.setFont(font)
        self.label_cantidad.setStyleSheet("font-family: Roboto;\n"
                                          "font-size: 14px;\n"
                                          "margin-top:10px;\n"
                                          "margin-left:10px\n"
                                          "\n"
                                          "")
        self.label_cantidad.setObjectName("label_cantidad")
        self.fecha_date_2 = QtWidgets.QDateEdit(self.frame_3)
        self.fecha_date_2.setGeometry(QtCore.QRect(230, 120, 170, 25))
        self.fecha_date_2.setStyleSheet("\n"
                                        "background-color: #fff;\n"
                                        "border: 0.5px solid #c1c1c1;\n"
                                        "border-radius: 3px;\n"
                                        "padding: 4 5px;\n"
                                        "color: #000;\n"
                                        "font-family:Roboto;\n"
                                        "font-size:13px;\n"
                                        "font-weight: 400;\n"
                                        "margin-left: 10px;\n"
                                        "\n"
                                        "")
        self.fecha_date_2.setDateTime(QtCore.QDateTime(QtCore.QDate(2021, 1, 1), QtCore.QTime(0, 0, 0)))
        self.fecha_date_2.setObjectName("fecha_date_2")
        self.label_fecha_2 = QtWidgets.QLabel(self.frame_3)
        self.label_fecha_2.setGeometry(QtCore.QRect(230, 90, 151, 27))
        self.label_fecha_2.setMaximumSize(QtCore.QSize(174, 16777215))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(-1)
        self.label_fecha_2.setFont(font)
        self.label_fecha_2.setStyleSheet("font-family: Roboto;\n"
                                         "font-size: 14px;\n"
                                         "margin-top:10px;\n"
                                         "margin-left:10px\n"
                                         "\n"
                                         "")
        self.label_fecha_2.setObjectName("label_fecha_2")
        self.spinBox = QtWidgets.QSpinBox(self.frame_3)
        self.spinBox.setGeometry(QtCore.QRect(20, 180, 170, 25))
        self.spinBox.setStyleSheet("\n"
                                   "background-color: #fff;\n"
                                   "border: 0.5px solid #c1c1c1;\n"
                                   "border-radius: 3px;\n"
                                   "padding: 4 5px;\n"
                                   "font-family:Roboto;\n"
                                   "font-size:13px;\n"
                                   "font-weight: 400;\n"
                                   "margin-left: 10px;\n"
                                   "\n"
                                   "\n"
                                   "")
        self.spinBox.setObjectName("spinBox")
        self.verticalLayout.addWidget(self.frame_2)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Nuevo Ingreso"))
        self.label_fecha.setText(_translate("MainWindow", "Fecha de Ingreso"))
        self.label_codigo_producto.setText(_translate("MainWindow", "Código de producto"))
        self.label_motivo.setText(_translate("MainWindow", "Lote"))
        self.crearprod_btn.setText(_translate("MainWindow", "Confirmar"))
        self.label_cantidad.setText(_translate("MainWindow", "Cantidad"))
        self.label_fecha_2.setText(_translate("MainWindow", "Fecha de Vencimiento"))
from Interfaces.main import img_rc


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
