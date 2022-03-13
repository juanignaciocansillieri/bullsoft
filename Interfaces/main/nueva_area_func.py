import time

from PyQt5.QtWidgets import *

from CLASES import area as a
from Interfaces.main.nueva_area import Ui_MainWindow
from CLASES import  matriz as mz
from CLASES import  area as ar
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *


class NewArea(QMainWindow):

    def __init__(self):
        super(NewArea, self).__init__()
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
        self.ui.crearprod_btn.clicked.connect(self.crear_area)
        self.posicion_cbox()

    # CREAR ÁREA
    def crear_area(self):
        # RECIBIR VALORES DE LA VENTANA
        nom = self.ui.motivo_input.text()
        ide = self.ui.motivo_input_2.text()
        segmento = self.ui.segmentos_num.value()
        pasillo = self.ui.pasillos_num.value()
        posicion = self.ui.comboBox.currentText()
        print(posicion)
        entrada=0
        salida=0
        if a.ver_nombre(nom)==1:
            QtWidgets.QMessageBox.critical(self, "Error", "Nombre existente")
            return None
        if(nom=="" or ide=="" or posicion==""):
            QtWidgets.QMessageBox.critical(self, "Error", "Llene todos los campos")
            return None
        if segmento<(pasillo*2)-1 or segmento>pasillo*2:
            QtWidgets.QMessageBox.critical(self, "Error", "Para esa cantidad de pasillos solo puede tener "+str((pasillo*2)-1)+" o "+str(pasillo*2)+" estanterias")
            return None
        if self.ui.radioButton.isChecked()==True:
            if ar.ver_e()!=0:
                QtWidgets.QMessageBox.critical(self, "Error", "Entrada ya ocupada")
                return None
            else:
                entrada=1
                salida=0
        if self.ui.radioButton_2.isChecked() == True:
            if ar.ver_s()!=0:
                QtWidgets.QMessageBox.critical(self, "Error", "Salida ya ocupada")

                return None
            else:
                entrada=0
                salida=1
        if ar.confirmar_area_disponible(posicion) == 1:
            a.Area.modificar_area(nom, ide , posicion, pasillo, segmento,entrada,salida)

        else:
            QtWidgets.QMessageBox.critical(self, "Error", "Espacio ya ocupado")
            return None

        self.close()


    def posicion_cbox(self):
        areas=a.Area.listar_area()
        print("AREAS: ",areas)
        medidas = mz.importar_datos_matriz()
        i=0
        for x in areas:
            if x[0]==x[2]:
                self.ui.comboBox.addItem(x[2])
                i+=1
        if i==0:
            QtWidgets.QMessageBox.critical(self, "Error", "No hay posiciones para crear areas")
            return 0