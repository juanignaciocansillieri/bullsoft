import sys

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *

from Interfaces.main.nueva_estanteria import Ui_MainWindow
from CLASES import estanterias,area


class Nueva_estanteria(QMainWindow):

    def __init__(self,area):
        self.area=area
        super(Nueva_estanteria, self).__init__()
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
        self.posicion_cbox()
        self.pasillos_cbox()
        self.ui.btn_nueva_estanteria.clicked.connect(self.crear_estanteria)

    def crear_estanteria(self):
        columnas = self.ui.num_columnas.value()
        niveles=self.ui.num_niveles.value()
        pasillo = self.ui.cbox_pasillo.currentText()
        posicion= self.ui.cbox_posicion.currentText()
        codigo=str(str(self.area)+"-"+str(pasillo)+"-"+str(posicion))
        if int(estanterias.verificar_segmentos(self.area,posicion) )== 1:
            estanterias.Estanterias(codigo,self.area,pasillo,posicion,columnas,niveles)
        else:
            QtWidgets.QMessageBox.critical(self, "Error", "Estanteria ya creada")
            return None


        self.close()

    def pasillos_cbox(self):
        pasillo = area.ver_pasillos(self.area)
        for x in range(int(pasillo[0][0])):
                self.ui.cbox_pasillo.addItem(str(x+1))

    def posicion_cbox(self):
        segmento = area.ver_segmentos(self.area)
        for x in range(int(segmento[0][0])):
                self.ui.cbox_posicion.addItem(str(x+1))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Nueva_estanteria()
    window.show()
    sys.exit(app.exec())