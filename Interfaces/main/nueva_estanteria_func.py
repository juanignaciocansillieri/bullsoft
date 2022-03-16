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
        if columnas==0 or niveles == 0 or posicion=="":
            QtWidgets.QMessageBox.critical(self, "Error", "Llene todos los campos")
            return None
        if int(estanterias.verificar_segmentos(self.area,posicion) )== 1:
            estanterias.Estanterias(codigo,self.area,pasillo,posicion,columnas,niveles)
            self.close()
        else:
            QtWidgets.QMessageBox.critical(self, "Error", "Estanteria ya creada")
            return None


    def pasillos_cbox(self):
        pasillo = area.ver_pasillos(self.area)
        for x in range(int(pasillo)):
                self.ui.cbox_pasillo.addItem(str(x+1))

    def posicion_cbox(self):
        segmento = int(area.ver_segmentos(self.area))
        pos = estanterias.ver_posicion(self.area)
        pos2=[]
        cbox=[]
        for a in pos:
            pos2.append(int(a[0]))
        j=0
        i=0
        while i<segmento:
            j=0
            while j< len(pos2):
                if i+1==pos2[j]:
                    pos2.pop(j)
                    i=i+1
                    if(int(len(pos2))==0):
                        cbox.append(i + 1)
                    j=0
                else:
                    j=j+1
                    cbox.append(i+1)
                    j=j+1
            i=i+1

        for x in cbox:
            if x>segmento:
                cbox.remove(x)
        if len(cbox)==0:
            QtWidgets.QMessageBox.critical(self, "Error", "No hay posiciones para crear estanterias")
            return None

        for y in cbox:
            self.ui.cbox_posicion.addItem(str(y))



if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Nueva_estanteria()
    window.show()
    sys.exit(app.exec())