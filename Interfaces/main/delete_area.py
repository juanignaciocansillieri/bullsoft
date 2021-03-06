# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'delete_area.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5.QtWidgets import *
# -*- coding: utf-8 -*-

from CLASES import area as ar,estanterias as es,alojamiento as al
from DB import  conexion as c
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
        posicion= ar.ver_posicion(area)

        ret = qm.warning(self, 'Esta acción es irreversible', "¿Estás seguro que quieres eliminar ésta área ?",
                         qm.Yes | qm.No)
        if ret == qm.Yes:
            es.Estanterias.borrar_estanteria(area)
            al.Alojamiento.elim_pos_area(area)
            a = c.start_connection()
            cursor = a.cursor()
            query = "UPDATE area SET nombre=%s WHERE posicion=%s"
            values = (posicion, posicion)
            cursor.execute(query, values)
            a.commit()
            query = "UPDATE area SET identificador=%s WHERE posicion=%s"
            values = (posicion, posicion)
            cursor.execute(query, values)
            a.commit()
            query = "UPDATE area SET pasillos=%s WHERE posicion=%s"
            values = (0, posicion)
            cursor.execute(query, values)
            a.commit()
            query = "UPDATE area SET segmentos=%s WHERE posicion=%s"
            values = (0, posicion)
            cursor.execute(query, values)
            a.commit()
            query = "UPDATE area SET disponibilidad=%s WHERE posicion=%s"
            values = (100, posicion)
            cursor.execute(query, values)
            a.commit()


            self.close()

    def rellenar_campo(self):
        areas = ar.Area.listar_area()
        for area in areas:
            self.ui.comboBox.addItem(area[0])
        self.close()
