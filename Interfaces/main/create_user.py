# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'create_user.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(490, 485)
        MainWindow.setMinimumSize(QtCore.QSize(490, 485))
        MainWindow.setMaximumSize(QtCore.QSize(490, 485))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setMinimumSize(QtCore.QSize(0, 300))
        self.frame_2.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.frame_2.setStyleSheet("background: #f5f5f5;\n"
"")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.crearprod_btn = QtWidgets.QPushButton(self.frame_2)
        self.crearprod_btn.setGeometry(QtCore.QRect(280, 430, 161, 26))
        font = QtGui.QFont()
        font.setFamily("Roboto")
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
        self.dni_input = QtWidgets.QLineEdit(self.frame_2)
        self.dni_input.setGeometry(QtCore.QRect(60, 380, 170, 25))
        self.dni_input.setMinimumSize(QtCore.QSize(0, 0))
        self.dni_input.setMaximumSize(QtCore.QSize(16777215, 25))
        self.dni_input.setStyleSheet("QLineEdit{\n"
"background-color: #fff;\n"
"border: 0.5px solid #c1c1c1;\n"
"border-radius: 3px;\n"
"padding: 4 5px;\n"
"color: #e9e9;\n"
"font-family:Roboto;\n"
"font-size:13px;\n"
"font-weight: 400;\n"
"margin-left: 10px;\n"
"\n"
"}\n"
"")
        self.dni_input.setPlaceholderText("")
        self.dni_input.setObjectName("dni_input")
        self.label_rep_password = QtWidgets.QLabel(self.frame_2)
        self.label_rep_password.setGeometry(QtCore.QRect(270, 350, 158, 27))
        self.label_rep_password.setMaximumSize(QtCore.QSize(500, 16777215))
        font = QtGui.QFont()
        font.setPointSize(-1)
        self.label_rep_password.setFont(font)
        self.label_rep_password.setStyleSheet("font-size: 14px;\n"
"margin-top:10px;\n"
"margin-left:10px\n"
"\n"
"")
        self.label_rep_password.setObjectName("label_rep_password")
        self.label_mail = QtWidgets.QLabel(self.frame_2)
        self.label_mail.setGeometry(QtCore.QRect(269, 170, 90, 27))
        self.label_mail.setMaximumSize(QtCore.QSize(90, 16777215))
        font = QtGui.QFont()
        font.setPointSize(-1)
        self.label_mail.setFont(font)
        self.label_mail.setStyleSheet("font-size: 14px;\n"
"color: #000;\n"
"margin-top:10px;\n"
"margin-left:10px\n"
"\n"
"")
        self.label_mail.setObjectName("label_mail")
        self.mail_input = QtWidgets.QLineEdit(self.frame_2)
        self.mail_input.setGeometry(QtCore.QRect(270, 200, 170, 25))
        self.mail_input.setMinimumSize(QtCore.QSize(0, 0))
        self.mail_input.setMaximumSize(QtCore.QSize(16777215, 25))
        self.mail_input.setStyleSheet("QLineEdit{\n"
"background-color: #fff;\n"
"border: 0.5px solid #c1c1c1;\n"
"border-radius: 3px;\n"
"padding: 4 5px;\n"
"color: #e9e9;\n"
"font-family:Roboto;\n"
"font-size:13px;\n"
"font-weight: 400;\n"
"margin-left: 10px;\n"
"\n"
"}\n"
"")
        self.mail_input.setPlaceholderText("")
        self.mail_input.setObjectName("mail_input")
        self.tipo_cb = QtWidgets.QComboBox(self.frame_2)
        self.tipo_cb.setGeometry(QtCore.QRect(280, 140, 161, 25))
        self.tipo_cb.setStyleSheet("padding:0 5px;\n"
"border-radius: 3px;\n"
"font-family:Roboto Lt;\n"
"border: none;\n"
"font-size:13px;\n"
"font-weight: 400;\n"
"background-color: #fff;\n"
"border: 0.5px solid #c1c1c1;\n"
"color: #000;\n"
"\n"
"")
        self.tipo_cb.setMaxVisibleItems(3)
        self.tipo_cb.setMaxCount(3)
        self.tipo_cb.setInsertPolicy(QtWidgets.QComboBox.InsertAfterCurrent)
        self.tipo_cb.setIconSize(QtCore.QSize(16, 0))
        self.tipo_cb.setDuplicatesEnabled(False)
        self.tipo_cb.setFrame(False)
        self.tipo_cb.setObjectName("tipo_cb")
        self.tipo_cb.addItem("")
        self.tipo_cb.addItem("")
        self.pass_input = QtWidgets.QLineEdit(self.frame_2)
        self.pass_input.setGeometry(QtCore.QRect(270, 320, 170, 25))
        self.pass_input.setMinimumSize(QtCore.QSize(0, 0))
        self.pass_input.setMaximumSize(QtCore.QSize(16777215, 25))
        self.pass_input.setStyleSheet("QLineEdit{\n"
"background-color: #fff;\n"
"border: 0.5px solid #c1c1c1;\n"
"border-radius: 3px;\n"
"padding: 4 5px;\n"
"color: #e9e9;\n"
"font-family:Roboto;\n"
"font-size:13px;\n"
"font-weight: 400;\n"
"margin-left: 10px;\n"
"\n"
"}\n"
"")
        self.pass_input.setInputMethodHints(QtCore.Qt.ImhHiddenText|QtCore.Qt.ImhNoAutoUppercase|QtCore.Qt.ImhNoPredictiveText|QtCore.Qt.ImhSensitiveData)
        self.pass_input.setEchoMode(QtWidgets.QLineEdit.Password)
        self.pass_input.setPlaceholderText("")
        self.pass_input.setObjectName("pass_input")
        self.label_nombre = QtWidgets.QLabel(self.frame_2)
        self.label_nombre.setGeometry(QtCore.QRect(60, 110, 71, 27))
        font = QtGui.QFont()
        font.setPointSize(-1)
        self.label_nombre.setFont(font)
        self.label_nombre.setStyleSheet("font-size: 14px;\n"
"margin-top:10px;\n"
"margin-left:10px\n"
"\n"
"")
        self.label_nombre.setObjectName("label_nombre")
        self.nombre_input_2 = QtWidgets.QLineEdit(self.frame_2)
        self.nombre_input_2.setGeometry(QtCore.QRect(60, 140, 170, 25))
        self.nombre_input_2.setMinimumSize(QtCore.QSize(0, 0))
        self.nombre_input_2.setMaximumSize(QtCore.QSize(16777215, 25))
        self.nombre_input_2.setStyleSheet("QLineEdit{\n"
"background-color: #fff;\n"
"border: 0.5px solid #c1c1c1;\n"
"border-radius: 3px;\n"
"padding: 4 5px;\n"
"color: #e9e9;\n"
"font-family:Roboto;\n"
"font-size:13px;\n"
"font-weight: 400;\n"
"margin-left: 10px;\n"
"\n"
"}\n"
"")
        self.nombre_input_2.setText("")
        self.nombre_input_2.setPlaceholderText("")
        self.nombre_input_2.setObjectName("nombre_input_2")
        self.apellido_input = QtWidgets.QLineEdit(self.frame_2)
        self.apellido_input.setGeometry(QtCore.QRect(60, 200, 170, 25))
        self.apellido_input.setMinimumSize(QtCore.QSize(0, 0))
        self.apellido_input.setMaximumSize(QtCore.QSize(16777215, 25))
        self.apellido_input.setStyleSheet("QLineEdit{\n"
"background-color: #fff;\n"
"border: 0.5px solid #c1c1c1;\n"
"border-radius: 3px;\n"
"padding: 4 5px;\n"
"color: #e9e9;\n"
"font-family:Roboto;\n"
"font-size:13px;\n"
"font-weight: 400;\n"
"margin-left: 10px;\n"
"\n"
"}\n"
"")
        self.apellido_input.setPlaceholderText("")
        self.apellido_input.setObjectName("apellido_input")
        self.label_nacimiento = QtWidgets.QLabel(self.frame_2)
        self.label_nacimiento.setGeometry(QtCore.QRect(60, 230, 91, 27))
        font = QtGui.QFont()
        font.setPointSize(-1)
        self.label_nacimiento.setFont(font)
        self.label_nacimiento.setStyleSheet("font-size: 14px;\n"
"margin-top:10px;\n"
"margin-left:10px\n"
"\n"
"")
        self.label_nacimiento.setObjectName("label_nacimiento")
        self.nacimiento_date = QtWidgets.QDateEdit(self.frame_2)
        self.nacimiento_date.setGeometry(QtCore.QRect(60, 260, 170, 25))
        self.nacimiento_date.setStyleSheet("\n"
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
        self.nacimiento_date.setDateTime(QtCore.QDateTime(QtCore.QDate(2021, 1, 1), QtCore.QTime(0, 0, 0)))
        self.nacimiento_date.setObjectName("nacimiento_date")
        self.label_password = QtWidgets.QLabel(self.frame_2)
        self.label_password.setGeometry(QtCore.QRect(270, 290, 154, 27))
        self.label_password.setMaximumSize(QtCore.QSize(154, 16777215))
        font = QtGui.QFont()
        font.setPointSize(-1)
        self.label_password.setFont(font)
        self.label_password.setStyleSheet("font-size: 14px;\n"
"margin-top:10px;\n"
"margin-left:10px\n"
"\n"
"")
        self.label_password.setObjectName("label_password")
        self.label_puesto = QtWidgets.QLabel(self.frame_2)
        self.label_puesto.setGeometry(QtCore.QRect(60, 290, 84, 27))
        font = QtGui.QFont()
        font.setPointSize(-1)
        self.label_puesto.setFont(font)
        self.label_puesto.setStyleSheet("font-size: 14px;\n"
"margin-top:10px;\n"
"margin-left:10px\n"
"\n"
"")
        self.label_puesto.setObjectName("label_puesto")
        self.subirFoto_btn = QtWidgets.QPushButton(self.frame_2)
        self.subirFoto_btn.setGeometry(QtCore.QRect(70, 430, 160, 25))
        self.subirFoto_btn.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.subirFoto_btn.setFont(font)
        self.subirFoto_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.subirFoto_btn.setStyleSheet("QPushButton{\n"
"background-color: #055ffc;\n"
"color:#fff;\n"
"border-radius: 5px;\n"
"text-align:center;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"\n"
"}")
        self.subirFoto_btn.setObjectName("subirFoto_btn")
        self.pass_rep_input = QtWidgets.QLineEdit(self.frame_2)
        self.pass_rep_input.setGeometry(QtCore.QRect(270, 380, 170, 25))
        self.pass_rep_input.setMinimumSize(QtCore.QSize(0, 0))
        self.pass_rep_input.setMaximumSize(QtCore.QSize(16777215, 25))
        self.pass_rep_input.setStyleSheet("QLineEdit{\n"
"background-color: #fff;\n"
"border: 0.5px solid #c1c1c1;\n"
"border-radius: 3px;\n"
"padding: 4 5px;\n"
"color: #e9e9;\n"
"font-family:Roboto;\n"
"font-size:13px;\n"
"font-weight: 400;\n"
"margin-left: 10px;\n"
"\n"
"}\n"
"")
        self.pass_rep_input.setEchoMode(QtWidgets.QLineEdit.Password)
        self.pass_rep_input.setPlaceholderText("")
        self.pass_rep_input.setObjectName("pass_rep_input")
        self.label_rep_mail = QtWidgets.QLabel(self.frame_2)
        self.label_rep_mail.setGeometry(QtCore.QRect(269, 230, 90, 27))
        self.label_rep_mail.setMaximumSize(QtCore.QSize(90, 16777215))
        font = QtGui.QFont()
        font.setPointSize(-1)
        self.label_rep_mail.setFont(font)
        self.label_rep_mail.setStyleSheet("font-size: 14px;\n"
"margin-top:10px;\n"
"margin-left:10px\n"
"\n"
"")
        self.label_rep_mail.setObjectName("label_rep_mail")
        self.mail_rep_input = QtWidgets.QLineEdit(self.frame_2)
        self.mail_rep_input.setGeometry(QtCore.QRect(270, 260, 170, 25))
        self.mail_rep_input.setMinimumSize(QtCore.QSize(0, 0))
        self.mail_rep_input.setMaximumSize(QtCore.QSize(16777215, 25))
        self.mail_rep_input.setStyleSheet("QLineEdit{\n"
"background-color: #fff;\n"
"border: 0.5px solid #c1c1c1;\n"
"border-radius: 3px;\n"
"padding: 4 5px;\n"
"color: #e9e9;\n"
"font-family:Roboto;\n"
"font-size:13px;\n"
"font-weight: 400;\n"
"margin-left: 10px;\n"
"\n"
"}\n"
"")
        self.mail_rep_input.setPlaceholderText("")
        self.mail_rep_input.setObjectName("mail_rep_input")
        self.label_tipo = QtWidgets.QLabel(self.frame_2)
        self.label_tipo.setGeometry(QtCore.QRect(269, 110, 90, 27))
        self.label_tipo.setMaximumSize(QtCore.QSize(90, 16777215))
        font = QtGui.QFont()
        font.setPointSize(-1)
        self.label_tipo.setFont(font)
        self.label_tipo.setStyleSheet("font-size: 14px;\n"
"margin-top:10px;\n"
"margin-left:10px\n"
"\n"
"")
        self.label_tipo.setObjectName("label_tipo")
        self.label_dni = QtWidgets.QLabel(self.frame_2)
        self.label_dni.setGeometry(QtCore.QRect(60, 350, 71, 27))
        font = QtGui.QFont()
        font.setPointSize(-1)
        self.label_dni.setFont(font)
        self.label_dni.setStyleSheet("font-size: 14px;\n"
"margin-top:10px;\n"
"margin-left:10px\n"
"\n"
"")
        self.label_dni.setObjectName("label_dni")
        self.label_apellido = QtWidgets.QLabel(self.frame_2)
        self.label_apellido.setGeometry(QtCore.QRect(60, 170, 67, 27))
        font = QtGui.QFont()
        font.setPointSize(-1)
        self.label_apellido.setFont(font)
        self.label_apellido.setStyleSheet("font-size: 14px;\n"
"margin-top:10px;\n"
"margin-left:10px\n"
"\n"
"")
        self.label_apellido.setObjectName("label_apellido")
        self.puesto_input = QtWidgets.QLineEdit(self.frame_2)
        self.puesto_input.setGeometry(QtCore.QRect(60, 320, 170, 25))
        self.puesto_input.setMinimumSize(QtCore.QSize(0, 0))
        self.puesto_input.setMaximumSize(QtCore.QSize(16777215, 25))
        self.puesto_input.setStyleSheet("QLineEdit{\n"
"background-color: #fff;\n"
"border: 0.5px solid #c1c1c1;\n"
"border-radius: 3px;\n"
"padding: 4 5px;\n"
"color: #e9e9;\n"
"font-family:Roboto;\n"
"font-size:13px;\n"
"font-weight: 400;\n"
"margin-left: 10px;\n"
"\n"
"}\n"
"")
        self.puesto_input.setPlaceholderText("")
        self.puesto_input.setObjectName("puesto_input")
        self.label_5 = QtWidgets.QLabel(self.frame_2)
        self.label_5.setGeometry(QtCore.QRect(0, 30, 491, 61))
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
        self.verticalLayout.addWidget(self.frame_2)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.tipo_cb.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.crearprod_btn.setText(_translate("MainWindow", "Crear Usuario"))
        self.label_rep_password.setText(_translate("MainWindow", "Repetir Contraseña"))
        self.label_mail.setText(_translate("MainWindow", "Mail"))
        self.tipo_cb.setCurrentText(_translate("MainWindow", "Usuario"))
        self.tipo_cb.setItemText(0, _translate("MainWindow", "Usuario"))
        self.tipo_cb.setItemText(1, _translate("MainWindow", "Administrador"))
        self.label_nombre.setText(_translate("MainWindow", "Nombre"))
        self.label_nacimiento.setText(_translate("MainWindow", "Nacimiento"))
        self.label_password.setText(_translate("MainWindow", "Contraseña"))
        self.label_puesto.setText(_translate("MainWindow", "Puesto"))
        self.subirFoto_btn.setText(_translate("MainWindow", "Subir Imagen"))
        self.label_rep_mail.setText(_translate("MainWindow", "Repetir Mail"))
        self.label_tipo.setText(_translate("MainWindow", "Tipo"))
        self.label_dni.setText(_translate("MainWindow", "DNI"))
        self.label_apellido.setText(_translate("MainWindow", "Apellido"))
        self.label_5.setText(_translate("MainWindow", "Nuevo Usuario"))
from  Interfaces.main import img_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
