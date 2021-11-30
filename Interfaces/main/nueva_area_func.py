from PyQt5.QtWidgets import *

from CLASES import area as a
from Interfaces.main.nueva_area import Ui_MainWindow


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

    # CREAR PRODUCTO NUEVO
    def crear_area(self):
        # RECIBIR VALORES DE LA VENTANA
        nom = self.ui.motivo_input.text()
        ide = self.ui.motivo_input_2.text()
        pasillo = self.ui.segmentos_num.value()
        segmento = self.ui.pasillos_num.value()
        longitud = self.ui.longitud_num.value()
        ancho = self.ui.ancho_num.value()
        alto = self.ui.alto_num.value()
        area = a.Area(nom, ide, pasillo, segmento, longitud, ancho, alto)
        self.close()
