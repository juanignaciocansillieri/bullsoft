import os
from PIL import Image
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *
from CLASES import usuarios as us
from DB import loginDB as log
from Interfaces.main.create_user import Ui_MainWindow

defaultImg = "Error.png"


class UsuarioWindow(QMainWindow):

    def __init__(self):
        super(UsuarioWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        ############# RECIBIMOS PROPORCIONES DE LA PANTALLA ###########
        qt_rectangle = self.frameGeometry()
        center_point = QDesktopWidget().availableGeometry().center()
        qt_rectangle.moveCenter(center_point)
        self.move(qt_rectangle.topLeft())
        ############## CENTRAMOS LA VENTANA #############
        center_point = QDesktopWidget().availableGeometry().center()
        qt_rectangle.moveCenter(center_point)
        self.move(qt_rectangle.topLeft())

        self.ui.subirFoto_btn.clicked.connect(self.upload_img)

        self.ui.crearprod_btn.clicked.connect(self.crear_user)

    # CREAR PRODUCTO NUEVO
    def crear_user(self):

        # RECIBIR VALORES DE LA VENTANA
        apellido = self.ui.apellido_input.text()
        nom = self.ui.nombre_input_2.text()
        mail = self.ui.mail_input.text()
        mail_rep = self.ui.mail_rep_input.text()
        dni = self.ui.dni_input.text()
        nacimiento = self.ui.nacimiento_date.date().toString("yyyy/MM/dd")
        puesto = self.ui.puesto_input.text()
        tipo = self.ui.tipo_cb.currentText()
        contrasena = self.ui.pass_input.text()
        contrasena_rep = self.ui.pass_rep_input.text()
        foto = defaultImg

        if nom == "" or apellido == "" or dni == "" or tipo == "" or puesto == "" or nacimiento == "" or contrasena == "" or contrasena_rep == "":
            QtWidgets.QMessageBox.critical(self, "Error", "Ingrese todos los datos")
            return None

        if len(dni) != 8:
            QtWidgets.QMessageBox.critical(self, "Error", "Ingrese un dni existente")
            return None

        if tipo == "Administrador":
            tipo = "1"
        else:
            tipo = "0"

        if mail != mail_rep:
            QtWidgets.QMessageBox.critical(self, "Error", "Mails diferentes")
            return None

        if contrasena != contrasena_rep:
            QtWidgets.QMessageBox.critical(self, "Error", "Contraseñas diferentes")
            return None

        if us.Usuarios.verificar(dni) == 1:
            QtWidgets.QMessageBox.critical(self, "Error", "DNI Existente")
            return None
        else:

            us.Usuarios(nom, apellido, dni, tipo, puesto, nacimiento, mail, foto)
            log.alta_login(dni, contrasena)
            self.close()
        self.clear_input()
        # return(codigo,nombre,desc,cantidad,marca,venc,condicion,lote,fragil)

    def upload_img(self):
        global defaultImg
        size = (256, 256)
        self.filename, ok = QFileDialog.getOpenFileName(self, "Upload Image", "", "Image Files (*.jpg *.png)")
        if ok:
            print(self.filename)
            defaultImg = os.path.basename(self.filename)
            print(defaultImg)
            img = Image.open(self.filename)
            img = img.resize(size)
            img.save('../main/img/{0}'.format(defaultImg))

    def clear_input(self):
        self.ui.apellido_input.setText("")
        self.ui.nombre_input_2.setText("")
        self.ui.mail_input.setText("")
        self.ui.puesto_input.setText("")
        self.ui.pass_input.setText("")
