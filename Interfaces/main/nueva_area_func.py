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
        pasillo = self.ui.segmentos_num.value()
        segmento = self.ui.pasillos_num.value()
        posicion = self.ui.comboBox.currentText()
        if self.ui.radioButton.isChecked()==True and ar.ver_e()==0:
            QtWidgets.QMessageBox.critical(self, "Error", "Entrada ya ocupada")
            return None
        if self.ui.radioButton_2.isChecked() == True and ar.ver_s()==0:
            QtWidgets.QMessageBox.critical(self, "Error", "Salida ya ocupada")
            return None
        if ar.ver_area_posicion(posicion) == 1:
            a.Area.modificar_area(nom, ide , posicion, pasillo, segmento, 0, 0, 0)
        else:
            QtWidgets.QMessageBox.critical(self, "Error", "Espacio ya ocupado")
            return None
        self.close()


    def posicion_cbox(self):
        medidas = mz.importar_datos_matriz()
        for x in range(medidas[0][0]):
            for y in range(medidas[0][1]):
                self.ui.comboBox.addItem('{}x{}'.format(x+1, y+1))

