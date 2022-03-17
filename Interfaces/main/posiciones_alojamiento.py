
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *
from Interfaces.main.posiciones_alojamiento_ui import Ui_MainWindow
from CLASES import area as a, alojamiento as al

area = ""


class PosicionAlojamiento(QMainWindow):

    def __init__(self, nombre_area):
        self.area=nombre_area
        super(PosicionAlojamiento, self).__init__()
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
        self.cbox_posicion()
        self.ui.modificar_btn.clicked.connect(self.crear_posicion_alojamiento)

    # CREAR POSICIONES ALOJAMIENTO
    def crear_posicion_alojamiento(self):
        # RECIBIR VALORES DE LA VENTANA
        global area
        ancho = self.ui.ancho_num.value()
        limite = self.ui.alto_num.value()#
        largo = self.ui.largo_num.value()
        alto  = self.ui.limite_num.value()#
        posicion=self.ui.comboBox_area.currentText()
        if (posicion == ""):
            QtWidgets.QMessageBox.critical(self, "Error", "Llene todos los campos")
            return None
        if (ancho == 0 or alto == 0 or largo == 0 or limite==0):
            QtWidgets.QMessageBox.critical(self, "Error", "Llene todos los campos")
            return None
        if al.verificar_posicion(posicion)==1:
            print(largo,ancho,alto)
            al.Alojamiento.modificar_alojamiento(posicion,largo,ancho,alto,limite)
        else:
            QtWidgets.QMessageBox.critical(self, "Error", "posicion ya creada")
            return None
        self.close()

    # RELLENAR CAMPOS
    def cbox_posicion(self):
        data=al.mostrar_filas_area(self.area)
        for codigos in data:
            self.ui.comboBox_area.addItem(codigos[0])
