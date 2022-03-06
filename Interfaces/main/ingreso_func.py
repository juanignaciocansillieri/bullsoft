import sys

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *

from Interfaces.main.ingreso import Ui_MainWindow
from CLASES import movimientos as m, lotes as l, productos as p, alojamiento as al


class NewIngreso(QMainWindow):

    def __init__(self):
        super(NewIngreso, self).__init__()
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
        self.ui.crearprod_btn.clicked.connect(self.crear_ingreso)

    def crear_ingreso(self):
        tipo = False
        cantidad = self.ui.spinBox.value()
        lote = self.ui.motivo_input.text()
        cod = self.ui.codigo_producto_input.text()
        fecha_igreso = self.ui.fecha_date.date().toString("yyyy/MM/dd")
        venc = self.ui.fecha_date_2.date().toString("yyyy/MM/dd")
        if cod == "" or p.ver_desc(cod) ==0:
            QtWidgets.QMessageBox.critical(self, "Error", "Código Inexistente")
            return None
        if lote=="" or cantidad==0:
            QtWidgets.QMessageBox.critical(self, "Error", "Ingrese todos los datos")
            return None
        if l.verificar(lote) == 0:
            QtWidgets.QMessageBox.critical(self, "Error", "Lote ya existe")
            return None
        l.Lote(cod, cantidad, lote, venc)
        m.Movimientos(tipo, cod, cantidad, "Ingreso", fecha_igreso)
        if al.modificar_dispo_ingreso(cod,cantidad) == 0 or al.modificar_dispo_ingreso(cod,cantidad)==1:
            QtWidgets.QMessageBox.critical(self, "Error", "No hay disponibilidad disponible")
            return None
        self.close()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = NewIngreso()
    window.show()
    sys.exit(app.exec())
