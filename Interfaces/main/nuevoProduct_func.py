import os
from PIL import Image
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *
from Interfaces.main.nuevo_producto_ui import Ui_MainWindow
from CLASES import productos as pr, area as a, alojamiento as p

defaultImg = "Error.png"


class ProductWindow(QMainWindow):

    def __init__(self):
        super(ProductWindow, self).__init__()
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
        # Agregar Producto
        self.ui.crearprod_btn.clicked.connect(self.crear_producto)
        self.ui.subirFoto_btn.clicked.connect(self.upload_img)
        self.cbox()

    # CREAR PRODUCTO NUEVO
    def crear_producto(self):
        global defaultImg
        # RECIBIR VALORES DE LA VENTANA
        codigo = self.ui.codigo_input.text()
        descripcion = self.ui.descripcion_input.toPlainText()
        cantidad = self.ui.cantidad_num.value()
        marca = self.ui.marca_input.text()
        venc = self.ui.venc_date.date().toString("yyyy/MM/dd")
        lote = self.ui.lote_input.text()
        imagen = defaultImg
        if self.ui.fragil_si.isChecked():
            fragil = "1"
        else:
            fragil = "0"

        condicion = self.ui.area_comboBox.currentText()
        posicion = self.ui.posicion_comboBox.currentText()

        peso = self.ui.peso_num.value()
        ancho = self.ui.ancho_num.value()
        altura = self.ui.altura_num.value()
        largo = self.ui.largo_num.value()

        if codigo == "" or descripcion == "" or cantidad == 0 or marca == "" or venc == "" or lote == "" or peso == "" or ancho == "" or largo == "" or altura == "":
            QtWidgets.QMessageBox.critical(self, "Error", "Ingrese todos los datos")
            return None
        data = pr.Productos.verificar(codigo)
        if data == 1:

            QtWidgets.QMessageBox.critical(self, "Error", "Codigo Existente")
            return None
        else:
            pr.Productos(codigo, marca, cantidad, descripcion, posicion, lote, venc, condicion, fragil, defaultImg,
                         peso, largo, ancho, altura)

        self.close()

    def upload_img(self):
        global defaultImg
        size = (256, 256)
        filename, ok = QFileDialog.getOpenFileName(self, "Upload Image", "", "Image Files (*.jpg *.png)")
        if ok:
            defaultImg = os.path.basename(filename)
            img = Image.open(filename)
            img = img.resize(size)
            img.save('../main/img/{0}'.format(defaultImg))

    def clear_input(self):
        self.ui.codigo_input.setText("")
        self.ui.descripcion_input.setText("")
        self.ui.cantidad_num.setValue("")
        self.ui.lote_input.setText("")
        self.ui.peso_num.setValue("")
        self.ui.ancho_num.setValue("")
        self.ui.largo_num.setValue("")
        self.ui.altura_num.setValue("")
        self.ui.marca_input.setText("")
        self.ui.venc_date.setDate("")
        self.ui.descripcion_input.setText("")
        self.ui.ubicacion_input.setText("")

    def cbox(self):
        areas = a.Area.listar_area()
        for ar in areas:
            self.ui.area_comboBox.addItem(ar[0])
        area_seleccionada = self.ui.area_comboBox.currentText()
        posiciones = p.Alojamiento.listar_alojamiento_disponibles_area(area_seleccionada)
        for pos in posiciones:
            self.ui.posicion_comboBox.addItem(pos[0])

        self.ui.area_comboBox.currentIndexChanged.connect(self.clear_combo)
        self.ui.area_comboBox.currentIndexChanged.connect(self.update_combo)

    def update_combo(self):
        area_seleccionada = self.ui.area_comboBox.currentText()
        posiciones = p.Alojamiento.listar_alojamiento_disponibles_area(area_seleccionada)
        for pos in posiciones:
            self.ui.posicion_comboBox.addItem(pos[0])

    def clear_combo(self):
        self.ui.posicion_comboBox.clear()
