from PyQt5.QtWidgets import *
from CLASES import area as a
from Interfaces.main.modificar_area_ui import Ui_MainWindow

nombreViejo = ""


class ModificarArea(QMainWindow):

    def __init__(self, id):
        super(ModificarArea, self).__init__()
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
        self.rellenar_campos(id)
        self.ui.modificar_btn.clicked.connect(lambda: self.modificar_area(id))

    # CREAR PRODUCTO NUEVO
    def modificar_area(self, id):
        nombre = id
        # RECIBIR VALORES DE LA VENTANA
        identificador = self.ui.identificador_input.text()
        longitud = self.ui.largo_num.value()
        pasillos = self.ui.pasillo_num.value()
        segmentos = self.ui.segmento_num.value()
        ancho = self.ui.ancho_num.value()
        alto = self.ui.alto_num.value()
        print(nombre, identificador, pasillos, segmentos, longitud, ancho, alto)
        a.Area.modificar_area(nombre, identificador, pasillos, segmentos, longitud, ancho, alto)
        self.close()
        return (nombre)

    def rellenar_campos(self, id):
        areas = a.Area.mostrar_area(id)
        print("area", id)
        atributos = list(areas[0])
        self.ui.nombre_input.setText(atributos[0])
        self.ui.identificador_input.setText(atributos[1])
        self.ui.pasillo_num.setValue(int(atributos[2]))
        self.ui.segmento_num.setValue(int(atributos[3]))
        self.ui.largo_num.setValue(int(atributos[4]))
        self.ui.ancho_num.setValue(int(atributos[5]))
        self.ui.alto_num.setValue(int(atributos[6]))
