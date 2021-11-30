import sys

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *

from Interfaces.main.ingreso import Ui_MainWindow
from CLASES import movimientos as m, lotes as l, productos as p


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
        codigo = p.Productos.mostrar_product(cod)
        lote_v = l.Lote.verificar(lote)

        if codigo == "":
            QtWidgets.QMessageBox.critical(self, "Error", "Código Inexistente")
        if lote_v == 1:
            QtWidgets.QMessageBox.critical(self, "Error", "Lote Existente")
        else:
            l.Lote(cod, cantidad, lote, venc)
            m.Movimientos(tipo, cod, cantidad, "Ingreso", fecha_igreso)
            self.close()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = NewIngreso()
    window.show()
    sys.exit(app.exec())
