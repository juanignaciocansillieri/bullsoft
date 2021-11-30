# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'bm_user.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(597, 618)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setMinimumSize(QtCore.QSize(0, 0))
        self.frame.setMaximumSize(QtCore.QSize(16777215, 209))
        self.frame.setStyleSheet("background: #fff;\n"
                                 "")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(190, 20, 221, 181))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap(":/cct/Alimento.png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.frame)
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setMinimumSize(QtCore.QSize(0, 300))
        self.frame_2.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.frame_2.setStyleSheet("background: #fff;\n"
                                   "\n"
                                   "\n"
                                   "")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.frame_3 = QtWidgets.QFrame(self.frame_2)
        self.frame_3.setGeometry(QtCore.QRect(50, 10, 491, 331))
        self.frame_3.setMaximumSize(QtCore.QSize(16777215, 400))
        self.frame_3.setStyleSheet("border-radius: 10px;\n"
                                   "background-color: rgb(240, 242, 255);\n"
                                   "")
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.label_mail = QtWidgets.QLabel(self.frame_3)
        self.label_mail.setGeometry(QtCore.QRect(259, 70, 90, 27))
        self.label_mail.setMaximumSize(QtCore.QSize(90, 16777215))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(0)
        self.label_mail.setFont(font)
        self.label_mail.setStyleSheet("font-family: Roboto;\n"
                                      "font-size: 14px;\n"
                                      "margin-top:10px;\n"
                                      "margin-left:10px\n"
                                      "\n"
                                      "")
        self.label_mail.setObjectName("label_mail")
        self.apellido_input = QtWidgets.QLineEdit(self.frame_3)
        self.apellido_input.setGeometry(QtCore.QRect(50, 100, 170, 25))
        self.apellido_input.setMinimumSize(QtCore.QSize(0, 0))
        self.apellido_input.setMaximumSize(QtCore.QSize(16777215, 25))
        self.apellido_input.setStyleSheet("QLineEdit{\n"
                                          "background-color: #fff;\n"
                                          "border: 0.5px solid #c1c1c1;\n"
                                          "border-radius: 3px;\n"
                                          "padding: 4 5px;\n"
                                          "font-family:Roboto;\n"
                                          "font-size:13px;\n"
                                          "font-weight: 400;\n"
                                          "margin-left: 10px;\n"
                                          "\n"
                                          "}")
        self.apellido_input.setPlaceholderText("")
        self.apellido_input.setObjectName("apellido_input")
        self.label_apellido = QtWidgets.QLabel(self.frame_3)
        self.label_apellido.setGeometry(QtCore.QRect(50, 70, 67, 27))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(0)
        self.label_apellido.setFont(font)
        self.label_apellido.setStyleSheet("font-family: Roboto;\n"
                                          "font-size: 14px;\n"
                                          "margin-top:10px;\n"
                                          "margin-left:10px\n"
                                          "\n"
                                          "")
        self.label_apellido.setObjectName("label_apellido")
        self.label_tipo = QtWidgets.QLabel(self.frame_3)
        self.label_tipo.setGeometry(QtCore.QRect(259, 10, 90, 27))
        self.label_tipo.setMaximumSize(QtCore.QSize(90, 16777215))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(0)
        self.label_tipo.setFont(font)
        self.label_tipo.setStyleSheet("font-family: Roboto;\n"
                                      "font-size: 14px;\n"
                                      "margin-top:10px;\n"
                                      "margin-left:10px\n"
                                      "\n"
                                      "")
        self.label_tipo.setObjectName("label_tipo")
        self.label_nombre = QtWidgets.QLabel(self.frame_3)
        self.label_nombre.setGeometry(QtCore.QRect(50, 10, 71, 27))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(0)
        self.label_nombre.setFont(font)
        self.label_nombre.setStyleSheet("font-family: Roboto;\n"
                                        "font-size: 14px;\n"
                                        "margin-top:10px;\n"
                                        "margin-left:10px\n"
                                        "\n"
                                        "")
        self.label_nombre.setObjectName("label_nombre")
        self.nombre_input_2 = QtWidgets.QLineEdit(self.frame_3)
        self.nombre_input_2.setGeometry(QtCore.QRect(50, 40, 170, 25))
        self.nombre_input_2.setMinimumSize(QtCore.QSize(0, 0))
        self.nombre_input_2.setMaximumSize(QtCore.QSize(16777215, 25))
        self.nombre_input_2.setStyleSheet("QLineEdit{\n"
                                          "background-color: #fff;\n"
                                          "border: 0.5px solid #c1c1c1;\n"
                                          "border-radius: 3px;\n"
                                          "padding: 4 5px;\n"
                                          "font-family:Roboto;\n"
                                          "font-size:13px;\n"
                                          "font-weight: 400;\n"
                                          "margin-left: 10px;\n"
                                          "\n"
                                          "}")
        self.nombre_input_2.setText("")
        self.nombre_input_2.setPlaceholderText("")
        self.nombre_input_2.setObjectName("nombre_input_2")
        self.label_password = QtWidgets.QLabel(self.frame_3)
        self.label_password.setGeometry(QtCore.QRect(259, 190, 154, 27))
        self.label_password.setMaximumSize(QtCore.QSize(154, 16777215))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(0)
        self.label_password.setFont(font)
        self.label_password.setStyleSheet("font-family: Roboto;\n"
                                          "font-size: 14px;\n"
                                          "margin-top:10px;\n"
                                          "margin-left:10px\n"
                                          "\n"
                                          "")
        self.label_password.setObjectName("label_password")
        self.label_dni = QtWidgets.QLabel(self.frame_3)
        self.label_dni.setGeometry(QtCore.QRect(50, 250, 71, 27))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(0)
        self.label_dni.setFont(font)
        self.label_dni.setStyleSheet("font-family: Roboto;\n"
                                     "font-size: 14px;\n"
                                     "margin-top:10px;\n"
                                     "margin-left:10px\n"
                                     "\n"
                                     "")
        self.label_dni.setObjectName("label_dni")
        self.label_nacimiento = QtWidgets.QLabel(self.frame_3)
        self.label_nacimiento.setGeometry(QtCore.QRect(50, 130, 91, 27))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(0)
        self.label_nacimiento.setFont(font)
        self.label_nacimiento.setStyleSheet("font-family: Roboto;\n"
                                            "font-size: 14px;\n"
                                            "margin-top:10px;\n"
                                            "margin-left:10px\n"
                                            "\n"
                                            "")
        self.label_nacimiento.setObjectName("label_nacimiento")
        self.label_rep_mail = QtWidgets.QLabel(self.frame_3)
        self.label_rep_mail.setGeometry(QtCore.QRect(259, 130, 90, 27))
        self.label_rep_mail.setMaximumSize(QtCore.QSize(90, 16777215))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(0)
        self.label_rep_mail.setFont(font)
        self.label_rep_mail.setStyleSheet("font-family: Roboto;\n"
                                          "font-size: 14px;\n"
                                          "margin-top:10px;\n"
                                          "margin-left:10px\n"
                                          "\n"
                                          "")
        self.label_rep_mail.setObjectName("label_rep_mail")
        self.puesto_input = QtWidgets.QLineEdit(self.frame_3)
        self.puesto_input.setGeometry(QtCore.QRect(50, 220, 170, 25))
        self.puesto_input.setMinimumSize(QtCore.QSize(0, 0))
        self.puesto_input.setMaximumSize(QtCore.QSize(16777215, 25))
        self.puesto_input.setStyleSheet("QLineEdit{\n"
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
                                        "}")
        self.puesto_input.setPlaceholderText("")
        self.puesto_input.setObjectName("puesto_input")
        self.label_puesto = QtWidgets.QLabel(self.frame_3)
        self.label_puesto.setGeometry(QtCore.QRect(50, 190, 84, 27))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(0)
        self.label_puesto.setFont(font)
        self.label_puesto.setStyleSheet("font-family: Roboto;\n"
                                        "font-size: 14px;\n"
                                        "margin-top:10px;\n"
                                        "margin-left:10px\n"
                                        "\n"
                                        "")
        self.label_puesto.setObjectName("label_puesto")
        self.nacimiento_date = QtWidgets.QDateEdit(self.frame_3)
        self.nacimiento_date.setGeometry(QtCore.QRect(50, 160, 170, 25))
        self.nacimiento_date.setStyleSheet("\n"
                                           "background-color: #fff;\n"
                                           "border: 0.5px solid #c1c1c1;\n"
                                           "border-radius: 3px;\n"
                                           "padding: 4 5px;\n"
                                           "font-family:Roboto;\n"
                                           "font-size:13px;\n"
                                           "font-weight: 400;\n"
                                           "margin-left: 10px;\n"
                                           "\n"
                                           "")
        self.nacimiento_date.setDateTime(QtCore.QDateTime(QtCore.QDate(2021, 1, 1), QtCore.QTime(0, 0, 0)))
        self.nacimiento_date.setObjectName("nacimiento_date")
        self.dni_input = QtWidgets.QLineEdit(self.frame_3)
        self.dni_input.setGeometry(QtCore.QRect(50, 280, 170, 25))
        self.dni_input.setMinimumSize(QtCore.QSize(0, 0))
        self.dni_input.setMaximumSize(QtCore.QSize(16777215, 25))
        self.dni_input.setStyleSheet("QLineEdit{\n"
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
                                     "}")
        self.dni_input.setPlaceholderText("")
        self.dni_input.setObjectName("dni_input")
        self.mail_input = QtWidgets.QLineEdit(self.frame_3)
        self.mail_input.setGeometry(QtCore.QRect(260, 100, 170, 25))
        self.mail_input.setMinimumSize(QtCore.QSize(0, 0))
        self.mail_input.setMaximumSize(QtCore.QSize(16777215, 25))
        self.mail_input.setStyleSheet("QLineEdit{\n"
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
                                      "}")
        self.mail_input.setPlaceholderText("")
        self.mail_input.setObjectName("mail_input")
        self.mail_rep_input = QtWidgets.QLineEdit(self.frame_3)
        self.mail_rep_input.setGeometry(QtCore.QRect(260, 160, 170, 25))
        self.mail_rep_input.setMinimumSize(QtCore.QSize(0, 0))
        self.mail_rep_input.setMaximumSize(QtCore.QSize(16777215, 25))
        self.mail_rep_input.setStyleSheet("QLineEdit{\n"
                                          "background-color: #fff;\n"
                                          "border: 0.5px solid #c1c1c1;\n"
                                          "border-radius: 3px;\n"
                                          "padding: 4 5px;\n"
                                          "font-family:Roboto;\n"
                                          "font-size:13px;\n"
                                          "font-weight: 400;\n"
                                          "margin-left: 10px;\n"
                                          "\n"
                                          "}")
        self.mail_rep_input.setPlaceholderText("")
        self.mail_rep_input.setObjectName("mail_rep_input")
        self.label_rep_password = QtWidgets.QLabel(self.frame_3)
        self.label_rep_password.setGeometry(QtCore.QRect(260, 250, 158, 27))
        self.label_rep_password.setMaximumSize(QtCore.QSize(500, 16777215))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(0)
        self.label_rep_password.setFont(font)
        self.label_rep_password.setStyleSheet("font-family: Roboto;\n"
                                              "font-size: 14px;\n"
                                              "margin-top:10px;\n"
                                              "margin-left:10px\n"
                                              "\n"
                                              "")
        self.label_rep_password.setObjectName("label_rep_password")
        self.pass_input = QtWidgets.QLineEdit(self.frame_3)
        self.pass_input.setGeometry(QtCore.QRect(260, 220, 170, 25))
        self.pass_input.setMinimumSize(QtCore.QSize(0, 0))
        self.pass_input.setMaximumSize(QtCore.QSize(16777215, 25))
        self.pass_input.setStyleSheet("QLineEdit{\n"
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
        self.pass_input.setEchoMode(QtWidgets.QLineEdit.Password)
        self.pass_input.setPlaceholderText("")
        self.pass_input.setObjectName("pass_input")
        self.pass_rep_input = QtWidgets.QLineEdit(self.frame_3)
        self.pass_rep_input.setGeometry(QtCore.QRect(260, 280, 170, 25))
        self.pass_rep_input.setMinimumSize(QtCore.QSize(0, 0))
        self.pass_rep_input.setMaximumSize(QtCore.QSize(16777215, 25))
        self.pass_rep_input.setStyleSheet("QLineEdit{\n"
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
                                          "}")
        self.pass_rep_input.setEchoMode(QtWidgets.QLineEdit.Password)
        self.pass_rep_input.setPlaceholderText("")
        self.pass_rep_input.setObjectName("pass_rep_input")
        self.tipo_cb = QtWidgets.QComboBox(self.frame_3)
        self.tipo_cb.setGeometry(QtCore.QRect(260, 40, 171, 29))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tipo_cb.sizePolicy().hasHeightForWidth())
        self.tipo_cb.setSizePolicy(sizePolicy)
        self.tipo_cb.setMinimumSize(QtCore.QSize(120, 0))
        self.tipo_cb.setStyleSheet("\n"
                                   "background-color: #fff;\n"
                                   "border: 0.5px solid #c1c1c1;\n"
                                   "border-radius: 3px;\n"
                                   "padding: 4 5px;\n"
                                   "font-family:Roboto;\n"
                                   "font-size:13px;\n"
                                   "font-weight: 400;\n"
                                   "margin-left: 10px;\n"
                                   "\n"
                                   "")
        self.tipo_cb.setMaxVisibleItems(2)
        self.tipo_cb.setInsertPolicy(QtWidgets.QComboBox.InsertAfterCurrent)
        self.tipo_cb.setDuplicatesEnabled(False)
        self.tipo_cb.setFrame(True)
        self.tipo_cb.setObjectName("tipo_cb")
        self.tipo_cb.addItem("")
        self.tipo_cb.addItem("")
        self.tipo_cb.addItem("")
        self.tipo_cb.setItemText(2, "")
        self.modificarprod_btn = QtWidgets.QPushButton(self.frame_2)
        self.modificarprod_btn.setGeometry(QtCore.QRect(280, 360, 121, 26))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(0)
        font.setBold(True)
        font.setWeight(75)
        self.modificarprod_btn.setFont(font)
        self.modificarprod_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.modificarprod_btn.setStyleSheet("QPushButton{\n"
                                             "background-color: rgb(71, 71, 103);\n"
                                             "color: #fff;\n"
                                             "border-radius:10px;\n"
                                             "font-family:Roboto;\n"
                                             "font-size: 13px\n"
                                             "\n"
                                             "}\n"
                                             "QPushButton:hover{\n"
                                             "background-color: background-color: rgba(71, 71, 103,180);\n"
                                             "}")
        self.modificarprod_btn.setObjectName("modificarprod_btn")
        self.eliminarprod_btn = QtWidgets.QPushButton(self.frame_2)
        self.eliminarprod_btn.setGeometry(QtCore.QRect(420, 360, 121, 26))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(0)
        font.setBold(True)
        font.setWeight(75)
        self.eliminarprod_btn.setFont(font)
        self.eliminarprod_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.eliminarprod_btn.setToolTipDuration(1)
        self.eliminarprod_btn.setStyleSheet("QPushButton{\n"
                                            "background-color: rgb(71, 71, 103);\n"
                                            "color: #fff;\n"
                                            "border-radius:10px;\n"
                                            "font-family:Roboto;\n"
                                            "font-size: 13px\n"
                                            "\n"
                                            "}\n"
                                            "QPushButton:hover{\n"
                                            "background-color: rgba(71, 71, 103,180);\n"
                                            "}")
        self.eliminarprod_btn.setObjectName("eliminarprod_btn")
        self.subirFoto_btn_2 = QtWidgets.QPushButton(self.frame_2)
        self.subirFoto_btn_2.setGeometry(QtCore.QRect(130, 360, 131, 25))
        self.subirFoto_btn_2.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.subirFoto_btn_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.subirFoto_btn_2.setStyleSheet("QPushButton{\n"
                                           "background-color: #b3b3b3;\n"
                                           "border-radius: 7px;\n"
                                           "padding: 4 10px;\n"
                                           "color: #12151a;\n"
                                           "font-family:Roboto;\n"
                                           "border: none;\n"
                                           "font-size:13px;\n"
                                           "font-weight: 500;\n"
                                           "}\n"
                                           "QPushButton:hover{\n"
                                           "background-color: rgba(179,179,179,110);\n"
                                           "\n"
                                           "\n"
                                           "}")
        self.subirFoto_btn_2.setObjectName("subirFoto_btn_2")
        self.verticalLayout.addWidget(self.frame_2)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.tipo_cb.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Usuario"))
        self.label_mail.setText(_translate("MainWindow", "Mail"))
        self.label_apellido.setText(_translate("MainWindow", "Apellido"))
        self.label_tipo.setText(_translate("MainWindow", "Tipo"))
        self.label_nombre.setText(_translate("MainWindow", "Nombre"))
        self.label_password.setText(_translate("MainWindow", "Contraseña"))
        self.label_dni.setText(_translate("MainWindow", "DNI"))
        self.label_nacimiento.setText(_translate("MainWindow", "Nacimiento"))
        self.label_rep_mail.setText(_translate("MainWindow", "Repetir Mail"))
        self.label_puesto.setText(_translate("MainWindow", "Puesto"))
        self.label_rep_password.setText(_translate("MainWindow", "Repetir Contraseña"))
        self.tipo_cb.setCurrentText(_translate("MainWindow", "Usuario"))
        self.tipo_cb.setItemText(0, _translate("MainWindow", "Usuario"))
        self.tipo_cb.setItemText(1, _translate("MainWindow", "Administrador"))
        self.modificarprod_btn.setText(_translate("MainWindow", "Modificar Usuario"))
        self.eliminarprod_btn.setText(_translate("MainWindow", "Dar De Baja"))
        self.subirFoto_btn_2.setText(_translate("MainWindow", "Actualizar Imagen"))

from Interfaces.main import img_oficiales_rc

if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
