import sys

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *

from CLASES import movimientos as m, lotes as l
from Interfaces.main.egreso import Ui_MainWindow


class NewEgreso(QMainWindow):

    def __init__(self):
        super(NewEgreso, self).__init__()
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
        self.ui.crear_egreso.clicked.connect(self.crear_egreso)

    def crear_egreso(self):
        tipo = True
        cantidad = self.ui.cantidad.value()
        motivo = self.ui.motivo_input_2.text()
        cod = self.ui.codigo_producto_input_2.text()
        fecha_egreso = self.ui.fecha_egreso.date().toString("yyyy/MM/dd")
        codigo = l.Lote.obtener_cantidades(cod)
        if codigo == "":
            QtWidgets.QMessageBox.critical(self, "Error", "Código Inexistente o Lote Inexistente")
        else:
            cant = l.Lote.obtener_cantidades(cod)
            print("CANTIDAD", cant)
            if cant > cantidad:
                m.Movimientos(tipo, cod, cantidad, motivo, fecha_egreso)
                l.Lote.fifo(cod, cantidad)
                self.close()
            else:
                QtWidgets.QMessageBox.critical(self, "Error",
                                               "Cantidad Insuficiente, quedan: " + str(cant) + " productos")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = NewEgreso()
    window.show()
    sys.exit(app.exec())
