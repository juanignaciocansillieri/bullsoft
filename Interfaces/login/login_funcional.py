from PyQt5 import QtWidgets
import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QMainWindow, QDesktopWidget


from Interfaces.login.login import Ui_MainWindow


from DB import loginDB as l

from CLASES import usuarios as u

from Interfaces.main import mainfunc as m

admin_user = True


class LoginWindow(QMainWindow):
    def __init__(self):
        super(LoginWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowFlag(Qt.FramelessWindowHint)

        ############# RECIBIMOS PROPORCIONES DE LA PANTALLA ###########
        qt_rectangle = self.frameGeometry()
        center_point = QDesktopWidget().availableGeometry().center()
        qt_rectangle.moveCenter(center_point)
        self.move(qt_rectangle.topLeft())
        ############## CENTRAMOS LA VENTANA #############
        center_point = QDesktopWidget().availableGeometry().center()
        qt_rectangle.moveCenter(center_point)
        self.move(qt_rectangle.topLeft())
        ### BOTON INGRESAR ####
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.ui.login_btn.clicked.connect(self.verificacion)

        ## MOSTRAR ##
        self.show()

    ### VERIFICAR DATOS INGRESADOS LA DB ####
    def verificacion(self):
        global admin_user
        user = self.ui.user_login_input.text()
        password = self.ui.pass_login_input.text()
        usuario = l.log_in(user, password)

        if usuario == 1:
            # inicia
            admin_user = u.ver_tipo(user)
            nombre=u.Usuarios.mostrar_user(user)
            nombre=str(nombre[0][1])+" "+str(nombre[0][1])
            self.main = m.Modern(admin_user,nombre)
            self.main.show()
            self.main.ui.stackedWidget_main.setCurrentWidget(self.main.ui.page_inicio)
            self.close()

        if usuario == 2:
            # no se encuentra dni
            if user == "admin":
                pass
            else:
                QtWidgets.QMessageBox.critical(self, "Error", "DNI Incorrecto")
                self.ui.user_login_input.setText("")
                self.ui.pass_login_input.setText("")
        if usuario == 3:
            # contraseña incorrecta
            QtWidgets.QMessageBox.critical(self, "Error", "Contraseña Incorrecta")
            self.ui.pass_login_input.setText("")

