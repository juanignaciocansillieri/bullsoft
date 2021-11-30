from PyQt5.QtWidgets import *

from CLASES import area as a
from Interfaces.main.delete_area_ui import Ui_MainWindow

nombreViejo = ""


class BorrarArea(QMainWindow):

    def __init__(self):
        super(BorrarArea, self).__init__()
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
        self.ui.modificar_btn.clicked.connect(lambda: self.eliminar_area())
        self.rellenar_campo()

    def eliminar_area(self):

        area = self.ui.comboBox.currentText()
        qm = QMessageBox

        ret = qm.warning(self, 'Esta acción es irreversible', "¿Estás seguro que quieres eliminar ésta área ?",
                         qm.Yes | qm.No)
        if ret == qm.Yes:
            a.Area.eliminar_area(area)
            self.close()

    def rellenar_campo(self):
        areas = a.Area.listar_area()
        for area in areas:
            self.ui.comboBox.addItem(area[0])
        self.close()
