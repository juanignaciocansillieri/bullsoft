
from PyQt5.QtWidgets import *
from Interfaces.main.posiciones_alojamiento_ui import Ui_MainWindow
from CLASES import area as a, alojamiento as al

area = ""


class PosicionAlojamiento(QMainWindow):

    def __init__(self, nombre_area):
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
        self.rellenar_campos(nombre_area)
        self.ui.modificar_btn.clicked.connect(self.crear_posicion_alojamiento)

    # CREAR POSICIONES ALOJAMIENTO
    def crear_posicion_alojamiento(self):
        # RECIBIR VALORES DE LA VENTANA
        global area
        columna = self.ui.columna_num.value()
        fila = self.ui.fila_num.value()
        nivel = self.ui.nivel_num.value()
        pasillo = str(self.ui.comboBox_pasillo.currentText())
        segmento = str(self.ui.comboBox_segmento.currentText())
        ancho = self.ui.ancho_num.value()
        alto = self.ui.alto_num.value()
        largo = self.ui.largo_num.value()
        limite = self.ui.limite_num.value()
        print()
        al.Alojamiento(largo, ancho, alto, area, pasillo, segmento, fila, nivel, limite, columna)
        self.close()

    # RELLENAR CAMPOS
    def rellenar_campos(self, id):
        global area
        area = id
        posiciones = a.Area.mostrar_area(id)
        atributos = list(posiciones[0])
        pasillos = int(atributos[2])
        segmentos = int(atributos[3])
        i = 1
        j = 1
        while i <= pasillos:
            self.ui.comboBox_pasillo.addItem('%i' % i)
            i += 1
        while j <= segmentos:
            self.ui.comboBox_segmento.addItem('%i' % j)
            j += 1
        self.ui.lineEdit.setText(id)
