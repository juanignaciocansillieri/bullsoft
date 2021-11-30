from PIL import Image
import os
from PyQt5 import QtCore
from PyQt5 import QtGui
from PyQt5 import QtWidgets
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from CLASES import usuarios as u, productos as p, area as ar, movimientos as m, lotes as l, alojamiento as al
from DB import loginDB
from Interfaces.main.bm_producto import Ui_MainWindow as Ui_Bm
from Interfaces.main.bm_user_ui import Ui_MainWindow as Bmu
from Interfaces.main.create_user_func import UsuarioWindow
from Interfaces.main.delete_area import BorrarArea
from Interfaces.main.egreso_func import NewEgreso
from Interfaces.main.ingreso_func import NewIngreso
from Interfaces.main.modern import Ui_MainWindow
from Interfaces.main.modificar_area import ModificarArea as Ma
from Interfaces.main.nueva_area import Ui_MainWindow as Na
from Interfaces.main.nueva_area_func import NewArea
from Interfaces.main.nuevoProduct_func import ProductWindow
from Interfaces.main.posiciones_alojamiento import PosicionAlojamiento as Pa

defaultImg = ""
codigoViejo = ""
DNI_Viejo = ""
DNI = ""
globalArea = ""
nombreNuevo = ""


class Modern(QMainWindow):

    def __init__(self, admin):
        super(Modern, self).__init__()

        self.ui = Ui_MainWindow()
        self.uii = Na()
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
        self.ui.exit_btn.clicked.connect(lambda: self.close())
        self.show()
        ##########################   PAGINAS   ##################################

        ########################## PRODUCTOS ##################################

        ## Abrir Pagina Productos ##
        self.ui.products_btn.clicked.connect(
            lambda: self.ui.stackedWidget_3.setCurrentWidget(self.ui.product_subpage))
        self.ui.products_btn.clicked.connect(self.listar_productos)
        self.ui.products_btn_stock.clicked.connect(self.listar_productos)
        # Abrir Pag Stock
        self.ui.products_btn.clicked.connect(
            lambda: self.ui.stackedWidget_main.setCurrentWidget(self.ui.page_stock))
        self.ui.products_btn_stock.clicked.connect(
            lambda: self.ui.stackedWidget_main.setCurrentWidget(self.ui.page_stock))
        # Abrir Pag Movimientos
        self.ui.products_btn_movimiento.clicked.connect(
            lambda: self.ui.stackedWidget_main.setCurrentWidget(self.ui.page_movimientos))
        self.ui.products_btn_movimiento.clicked.connect(self.listar_movimientos)
        self.ui.new_egreso_btn.clicked.connect(self.mostrar_egreso)
        self.ui.new_ingreso_btn.clicked.connect(self.mostrar_ingreso)
        self.ui.btn_actualizarMov.clicked.connect(self.listar_movimientos)
        self.ui.pushButton_18.clicked.connect(self.buscar_movimiento)
        # Abrir Pag Lotes
        self.ui.products_btn_lotes.clicked.connect(
            lambda: self.ui.stackedWidget_main.setCurrentWidget(self.ui.page_lotes))
        self.ui.pushButton_19.clicked.connect(self.listar_lotes)

        # Listamos productos al iniciar la ventana

        n = p.contar_filas()

        if n > 0:
            self.listar_productos()

            # Btn para buscar
        self.ui.btn_buscarP.clicked.connect(self.buscarProducto)
        self.ui.btn_actualizarStock.clicked.connect(self.listar_productos)

        # Abrir ventana para ver el producto individual
        self.ui.tableWidget_stock_2.doubleClicked.connect(self.seleccionar_producto)
        self.ui.tableWidget_stock_2.doubleClicked.connect(self.mostrar_bm_product)

        # Abrir ventana para agregar Nuevo producto
        self.ui.product_new_btn.clicked.connect(self.mostrar_new_product)

        ########################## USUARIOS ##################################
        if admin:
            self.ui.user_new_btn.clicked.connect(self.mostrar_new_user)

            self.ui.users_btn.clicked.connect(self.listar_usuarios)
            self.ui.btn_buscarU.clicked.connect(self.buscar_usuarios)

            ## Abrir Pagina Usuarios ##
            self.ui.users_btn.clicked.connect(
                lambda: self.ui.stackedWidget_main.setCurrentWidget(self.ui.page_usuarios))
            self.ui.users_btn.clicked.connect(lambda: self.ui.stackedWidget_3.setCurrentWidget(self.ui.user_subpage))

            self.ui.btn_actualizarUsuarios.clicked.connect(self.listar_usuarios)
        else:
            self.ui.users_btn.clicked.connect(
                lambda: QtWidgets.QMessageBox.critical(self, "Error", "No tiene los permisos suficientes"))
            # Abrir ventana para ver el producto individual
        self.ui.tableWidget_usuarios.doubleClicked.connect(self.seleccionarusuario)
        self.ui.tableWidget_usuarios.doubleClicked.connect(self.mostrar_bm_user)

        ########################## DEPOSITOS ##################################

        self.ui.deposito_btn.clicked.connect(self.mostra_areas)
        ## Abrir Pagina Depositos ##
        self.ui.deposito_btn.clicked.connect(lambda: self.ui.stackedWidget_main.setCurrentWidget(self.ui.page_deposito))
        self.ui.deposito_btn.clicked.connect(lambda: self.ui.stackedWidget_3.setCurrentWidget(self.ui.deposito_subpage))
        self.ui.newArea_btn.clicked.connect(self.mostrar_new_area)
        self.ui.label_12.mousePressEvent = self.click_a
        self.ui.btn_actualizarAreas.clicked.connect(self.mostra_areas)

        self.ui.btn_actualizarAreaInd.clicked.connect(lambda: self.listar_areas(globalArea))
        self.ui.btn_newPosicion.clicked.connect(lambda: self.new_posicion(globalArea))
        self.ui.btn_modificarArea.clicked.connect(lambda: self.modificar_area(globalArea))
        self.ui.newArea_btn_2.clicked.connect(self.mostrar_borrar_area)

    def click_a(self,event):
        self.ui.stackedWidget_main.setCurrentWidget(self.ui.page_deposito)

    def mostrar_new_product(self):
        self.newProductWindow = ProductWindow()
        self.newProductWindow.show()

    def mostrar_new_user(self):
        self.newUserWindow = UsuarioWindow()
        self.newUserWindow.show()

    def mostrar_bm_product(self):
        self.newBmProduct = BMProduct()
        self.newBmProduct.show()

    def mostrar_bm_user(self):
        self.BM_Usuario = BmUsuario()
        self.BM_Usuario.show()

    def mostrar_new_area(self):
        self.newArea = NewArea()
        self.newArea.show()

    def mostrar_ingreso(self):
        self.newMovimiento = NewIngreso()
        self.newMovimiento.show()

    def mostrar_egreso(self):
        self.newEgreso = NewEgreso()
        self.newEgreso.show()

    def mostrar_borrar_area(self):
        self.borrarArea = BorrarArea()
        self.borrarArea.show()

    ## Listar Productos en la tabla
    def listar_productos(self):
        products = p.listar_prod()
        n = p.contar_filas()
        self.ui.tableWidget_stock_2.setRowCount(n)
        table_row = 0

        for row in products:
            self.ui.tableWidget_stock_2.setItem(
                table_row, 0, QtWidgets.QTableWidgetItem(row[0]))
            self.ui.tableWidget_stock_2.setItem(
                table_row, 1, QtWidgets.QTableWidgetItem(row[1]))
            self.ui.tableWidget_stock_2.setItem(
                table_row, 2, QtWidgets.QTableWidgetItem(row[2]))
            self.ui.tableWidget_stock_2.setItem(
                table_row, 3, QtWidgets.QTableWidgetItem(str(l.Lote.obtener_cantidades(row[0]))))

            self.ui.tableWidget_stock_2.setItem(
                table_row, 4, QtWidgets.QTableWidgetItem(str(l.Lote.obtener_fecha(row[0]))))

            table_row += 1

    ## Listar Movimientos en la tabla
    def listar_movimientos(self):
        movimientos = m.listar_movimientos()
        n = m.Movimientos.contar_filas()
        self.ui.tableWidget_movimientos_2.setRowCount(n)
        table_row = 0
        for row in movimientos:
            self.ui.tableWidget_movimientos_2.setItem(
                table_row, 0, QtWidgets.QTableWidgetItem(str(row[1])))
            self.ui.tableWidget_movimientos_2.setItem(
                table_row, 1, QtWidgets.QTableWidgetItem(str(row[2])))
            self.ui.tableWidget_movimientos_2.setItem(
                table_row, 2, QtWidgets.QTableWidgetItem(str(row[3])))
            self.ui.tableWidget_movimientos_2.setItem(
                table_row, 4, QtWidgets.QTableWidgetItem(str(row[5])))
            if str(row[0]) == "b'1'":
                self.ui.tableWidget_movimientos_2.setItem(
                    table_row, 3, QtWidgets.QTableWidgetItem("Egreso"))
                self.ui.tableWidget_movimientos_2.setItem(
                    table_row, 5, QtWidgets.QTableWidgetItem(str(row[4])))
            else:
                self.ui.tableWidget_movimientos_2.setItem(
                    table_row, 3, QtWidgets.QTableWidgetItem("Ingreso"))
                self.ui.tableWidget_movimientos_2.setItem(
                    table_row, 5, QtWidgets.QTableWidgetItem("-"))

            table_row += 1

    ## Listar lotes en la tabla
    def listar_lotes(self):
        id = self.ui.lineEdit_6.text()
        lotes = l.Lote.listar_lote(id)
        n = l.Lote.contar_filas_producto(id)
        self.ui.tableWidget_lotes.setRowCount(n)
        table_row = 0
        for row in lotes:
            self.ui.tableWidget_lotes.setItem(
                table_row, 0, QtWidgets.QTableWidgetItem(row[0]))
            self.ui.tableWidget_lotes.setItem(
                table_row, 1, QtWidgets.QTableWidgetItem(row[1]))
            self.ui.tableWidget_lotes.setItem(
                table_row, 2, QtWidgets.QTableWidgetItem(str(row[2])))
            self.ui.tableWidget_lotes.setItem(
                table_row, 3, QtWidgets.QTableWidgetItem(str(row[3])))
            self.ui.tableWidget_lotes.setItem(
                table_row, 4, QtWidgets.QTableWidgetItem(str(row[4])))

            table_row += 1

    # Buscar productos a traves del input, por parámetro ingresado
    def buscar_movimiento(self):
        parametro = self.ui.lineEdit_5.text()
        movimientos = m.buscar_product(parametro)
        n = m.buscar_product_rows(parametro)
        self.ui.tableWidget_movimientos_2.setRowCount(n)
        table_row = 0
        for row in movimientos:
            self.ui.tableWidget_movimientos_2.setItem(
                table_row, 0, QtWidgets.QTableWidgetItem(str(row[1])))
            self.ui.tableWidget_movimientos_2.setItem(
                table_row, 1, QtWidgets.QTableWidgetItem(str(row[2])))
            self.ui.tableWidget_movimientos_2.setItem(
                table_row, 2, QtWidgets.QTableWidgetItem(str(row[3])))
            self.ui.tableWidget_movimientos_2.setItem(
                table_row, 4, QtWidgets.QTableWidgetItem(str(row[5])))
            if str(row[0]) == "b'1'":
                self.ui.tableWidget_movimientos_2.setItem(
                    table_row, 3, QtWidgets.QTableWidgetItem("Egreso"))
                self.ui.tableWidget_movimientos_2.setItem(
                    table_row, 5, QtWidgets.QTableWidgetItem(str(row[4])))
            else:
                self.ui.tableWidget_movimientos_2.setItem(
                    table_row, 3, QtWidgets.QTableWidgetItem("Ingreso"))
                self.ui.tableWidget_movimientos_2.setItem(
                    table_row, 5, QtWidgets.QTableWidgetItem("-"))

            table_row += 1

    def buscarProducto(self):
        parametro = self.ui.buscar_input.text()
        products = p.Productos.buscar_product(parametro)
        n = p.Productos.buscar_product_rows(parametro)
        self.ui.tableWidget_stock_2.setRowCount(n)
        table_row = 0

        for row in products:
            self.ui.tableWidget_stock_2.setItem(
                table_row, 0, QtWidgets.QTableWidgetItem(row[0]))
            self.ui.tableWidget_stock_2.setItem(
                table_row, 1, QtWidgets.QTableWidgetItem(row[1]))
            self.ui.tableWidget_stock_2.setItem(
                table_row, 2, QtWidgets.QTableWidgetItem(row[2]))

            table_row += 1

    def seleccionar_producto(self):
        global productId
        global defaultImg
        lista_productos = []
        for i in range(0, 5):
            lista_productos.append(self.ui.tableWidget_stock_2.item(self.ui.tableWidget_stock_2.currentRow(), i).text())
            productId = lista_productos[0]

    def agregar_area_creada(self):

        areas = ar.Area.listar_area()
        n = ar.Area.contar_filas()
        child = self.ui.verticalLayout_7.count()
        if child == n:
            pass
        else:

            self.btn1 = QtWidgets.QPushButton(self.ui.frame_14)
            self.btn1.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
            self.btn1.setStyleSheet("QPushButton{\n"
                                    "border:none;\n"
                                    "font-family: Roboto;\n"
                                    "border-radius:5px;\n"
                                    "margin-right:20px;\n"
                                    "text-align: center;\n"
                                    "color: #000 ;\n"
                                    "padding:5px;\n"
                                    "\n"
                                    "\n"
                                    "}\n"
                                    "\n"
                                    "QPushButton:hover{\n"
                                    "    background-color: rgba(105, 105, 226, 50);\n"
                                    "}")
            self.btn1.setObjectName(areas[-1][0])
            self.btn1.setText(areas[-1][0])
            self.btn1.setMinimumSize(QtCore.QSize(128, 0))
            self.ui.verticalLayout_7.addWidget(self.btn1)
            font = QtGui.QFont()
            font.setFamily("Roboto")
            font.setPointSize(10)
            font.setBold(True)
            font.setWeight(75)
            self.btn1.setFont(font)
            self.btn1.released.connect(self.button_released)

    ## Agregar botones dinamicamente
    def agregar_btn_areas(self):

        areas = ar.Area.listar_area()
        i = 0
        n = ar.Area.contar_filas()
        child = self.ui.verticalLayout_7.count()

        for area in areas:
            self.btn1 = QtWidgets.QPushButton(self.ui.frame_14)
            self.btn1.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
            self.btn1.setStyleSheet("QPushButton{\n"
                                    "border:none;\n"
                                    "font-family: Roboto;\n"
                                    "border-radius:5px;\n"
                                    "margin-right:20px;\n"
                                    "text-align: center;\n"
                                    "color: #000 ;\n"
                                    "padding:5px;\n"
                                    "\n"
                                    "\n"
                                    "}\n"
                                    "\n"
                                    "QPushButton:hover{\n"
                                    "    background-color: rgba(105, 105, 226, 50);\n"
                                    "}")
            self.btn1.setObjectName("btn1{area[0]}")
            self.btn1.setText(area[0])
            self.btn1.setMinimumSize(QtCore.QSize(128, 0))
            self.btn1.released.connect(self.button_released)
            self.ui.verticalLayout_7.addWidget(self.btn1)
            font = QtGui.QFont()
            font.setFamily("Roboto")
            font.setPointSize(10)
            font.setBold(True)
            font.setWeight(75)
            self.btn1.setFont(font)
            i += 1

    ## Mostrar Areas graficamente

    def mostra_areas(self):
        child = self.ui.verticalLayout_7.count()
        areas = ar.Area.listar_area()
        n = ar.Area.contar_filas()
        i = 1

        for a in areas:

            frame = QtWidgets.QFrame(self.ui.frame_3)
            frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
            frame.setFrameShadow(QtWidgets.QFrame.Raised)
            frame.setObjectName(a[0])
            frame.setMaximumSize(QtCore.QSize(200, 200))
            vertical_layout = QtWidgets.QVBoxLayout(frame)
            # verticalLayout.addWidget(frame)
            self.btn = QPushButton(frame)
            self.btn.setText("Ver")
            self.btn.setObjectName('%s' % a[0])
            self.btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
            self.btn.setMinimumSize(QtCore.QSize(70, 30))
            self.btn.setMaximumSize(QtCore.QSize(100, 30))

            self.label = QtWidgets.QLabel(frame)
            self.btn.released.connect(self.button_released)

            self.ui.gridLayout.addWidget(frame, 1, i)
            font = QtGui.QFont()
            font.setFamily("Roboto")
            font.setPointSize(10)
            font.setBold(True)
            font.setWeight(75)
            self.label.setFont(font)
            self.label.setText(a[0])
            self.label.setAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter)
            self.label.setStyleSheet("QLabel{\n"  "border:none;\n""}")
            self.label.setMaximumSize(QtCore.QSize(150, 50))
            vertical_layout.addWidget(self.label, 0, QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter)
            vertical_layout.addWidget(self.btn, 0, QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter)

            if child < n:
                if child == n - 1:
                    self.agregar_area_creada()
                else:

                    self.btn2 = QtWidgets.QPushButton(self.ui.frame_14)
                    self.btn2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
                    self.btn2.setStyleSheet("QPushButton{\n"
                                            "border:none;\n"
                                            "font-family: Roboto;\n"
                                            "border-radius:5px;\n"
                                            "margin-right:20px;\n"
                                            "text-align: center;\n"
                                            "color: #000 ;\n"
                                            "padding:5px;\n"
                                            "\n"
                                            "\n"
                                            "}\n"
                                            "\n"
                                            "QPushButton:hover{\n"
                                            "    background-color: rgba(105, 105, 226, 50);\n"
                                            "}")
                    self.btn2.setObjectName(a[0])
                    self.btn2.setText(a[0])
                    self.ui.verticalLayout_7.addWidget(self.btn2)
                    font = QtGui.QFont()
                    font.setFamily("Roboto")
                    font.setPointSize(10)
                    font.setBold(True)
                    font.setWeight(75)
                    self.btn2.setFont(font)
                    self.btn2.released.connect(self.button_released)
            elif child > n:

                for i in reversed(range(self.ui.verticalLayout_7.count())):
                    self.ui.verticalLayout_7.itemAt(i).widget().deleteLater()
                for i in reversed(range(self.ui.gridLayout.count())):
                    self.ui.gridLayout.itemAt(i).widget().deleteLater()

            i += 1

    def button_released(self):
        global globalArea
        self.ui.stackedWidget_main.setCurrentWidget(self.ui.page_areas)
        sending_button = self.sender()
        nombre_area = str(sending_button.objectName())
        globalArea = nombre_area
        self.listar_areas(globalArea)

    def new_posicion(self, btn):
        self.newPosicionAlojamiento = Pa(btn)
        self.newPosicionAlojamiento.show()

    def modificar_area(self, btn):

        self.newPosicionAlojamiento = Ma(btn)
        self.newPosicionAlojamiento.show()

    def listar_areas(self, btn):
        global globalArea
        area = btn
        productos = p.Productos.buscar_productArea(area)
        n = p.Productos.buscar_product_rows_area(area)
        self.ui.tableWidget_areas.setRowCount(n)
        self.ui.label_area_mod.setText(area)
        table_row = 0
        vacio = []
        if n == 0:
            for row in vacio:
                self.ui.tableWidget_areas.setItem(
                    table_row, 0, QtWidgets.QTableWidgetItem(row[0]))
                self.ui.tableWidget_areas.setItem(
                    table_row, 1, QtWidgets.QTableWidgetItem(row[1]))
                self.ui.tableWidget_areas.setItem(
                    table_row, 2, QtWidgets.QTableWidgetItem(row[2]))
                self.ui.tableWidget_areas.setItem(
                    table_row, 3, QtWidgets.QTableWidgetItem(str(l.Lote.obtener_cantidades(row[0]))))
                self.ui.tableWidget_areas.setItem(
                    table_row, 4, QtWidgets.QTableWidgetItem(row[3]))
                self.ui.tableWidget_areas.setItem(
                    table_row, 5, QtWidgets.QTableWidgetItem(str(l.Lote.obtener_fecha(row[0]))))

                table_row += 1
        else:
            for row in productos:

                self.ui.tableWidget_areas.setItem(
                    table_row, 0, QtWidgets.QTableWidgetItem(row[0]))
                self.ui.tableWidget_areas.setItem(
                    table_row, 1, QtWidgets.QTableWidgetItem(row[1]))
                self.ui.tableWidget_areas.setItem(
                    table_row, 2, QtWidgets.QTableWidgetItem(row[2]))
                self.ui.tableWidget_areas.setItem(
                    table_row, 3, QtWidgets.QTableWidgetItem(str(l.Lote.obtener_cantidades(row[0]))))
                self.ui.tableWidget_areas.setItem(
                    table_row, 4, QtWidgets.QTableWidgetItem(str(row[3])))
                self.ui.tableWidget_areas.setItem(
                    table_row, 5, QtWidgets.QTableWidgetItem(str(l.Lote.obtener_fecha(row[0]))))

                table_row += 1

    ## Listar Usuarios en la tabla

    def listar_usuarios(self):
        usuarios = u.listar_user()
        n = u.contar_filas()
        self.ui.tableWidget_usuarios.setRowCount(n)
        table_row = 0
        for row in usuarios:
            self.ui.tableWidget_usuarios.setItem(
                table_row, 0, QtWidgets.QTableWidgetItem(row[0]))
            self.ui.tableWidget_usuarios.setItem(
                table_row, 1, QtWidgets.QTableWidgetItem(row[1]))
            self.ui.tableWidget_usuarios.setItem(
                table_row, 2, QtWidgets.QTableWidgetItem(row[2]))
            if str(row[3]) == "1":
                self.ui.tableWidget_usuarios.setItem(
                    table_row, 3, QtWidgets.QTableWidgetItem("Administrador"))
            else:
                self.ui.tableWidget_usuarios.setItem(
                    table_row, 3, QtWidgets.QTableWidgetItem("Usuario"))

            self.ui.tableWidget_usuarios.setItem(
                table_row, 4, QtWidgets.QTableWidgetItem(str(row[4])))

            table_row += 1

    # Seleccionar usuario al hacer click y abrir ventana

    def seleccionarusuario(self):
        global DNI
        seleccionarusuario = []
        for i in range(0, 5):
            seleccionarusuario.append(
                self.ui.tableWidget_usuarios.item(self.ui.tableWidget_usuarios.currentRow(), i).text())
            DNI = seleccionarusuario[0]

        ##Buscar Usuarios

    def buscar_usuarios(self):
        parametro = self.ui.lineEdit_3.text()
        products = u.Usuarios.buscar_user(parametro)
        n = u.Usuarios.buscar_user_rows(parametro)
        self.ui.tableWidget_usuarios.setRowCount(n)
        table_row = 0
        for row in products:
            self.ui.tableWidget_usuarios.setItem(table_row, 0, QtWidgets.QTableWidgetItem(row[0]))
            self.ui.tableWidget_usuarios.setItem(table_row, 1, QtWidgets.QTableWidgetItem(row[1]))
            self.ui.tableWidget_usuarios.setItem(table_row, 2, QtWidgets.QTableWidgetItem(row[2]))
            if str(row[3]) == "b'1'":
                self.ui.tableWidget_usuarios.setItem(table_row, 3, QtWidgets.QTableWidgetItem("Admin"))
            else:
                self.ui.tableWidget_usuarios.setItem(table_row, 3, QtWidgets.QTableWidgetItem("Usuario"))
            self.ui.tableWidget_usuarios.setItem(table_row, 4, QtWidgets.QTableWidgetItem(str(row[4])))

            table_row += 1

        # Seleccionar DNI al hacer click y abrir ventana

    def seleccionar_dni(self):
        global DNI
        seleccionar_dni = []
        for i in range(0, 5):
            seleccionar_dni.append(
                self.ui.tableWidget_usuarios.item(self.ui.tableWidget_usuarios.currentRow(), i).text())
            DNI = seleccionar_dni[0]


class BMProduct(QMainWindow):

    def __init__(self):
        super(BMProduct, self).__init__()
        self.ui = Ui_Bm()
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
        self.rellenar_campos()
        # Subir foto btn
        self.ui.subirFoto_btn.clicked.connect(self.upload_img)

        # Modificar producto btn
        self.ui.modificarprod_btn.clicked.connect(self.modificar_producto)

        # Eliminar producto btn
        self.ui.eliminarprod_btn.clicked.connect(self.borrar_producto)

        # Mostrar Ventana
        self.show()

    # Rellenar los campos con los atributos del producto seleccionado
    def rellenar_campos(self):

        global productId
        global codigoViejo
        global defaultImg
        producto = p.Productos.mostrar_product(productId)
        atributos = list(producto[0])
        self.ui.codigo_input.setText(atributos[0])
        codigoViejo = atributos[0]
        self.ui.descripcion_input.setPlainText(atributos[3])
        self.ui.marca_input.setText(atributos[1])
        self.productImg = self.ui.label
        self.img = QPixmap('../main/img/{0}'.format(atributos[8]))
        self.productImg.setPixmap(self.img)
        defaultImg = atributos[8]

        if str(atributos[7]) == "b'1'":
            self.ui.fragil_si.setChecked(1)
        else:
            self.ui.fragil_no.setChecked(1)

        self.ui.peso_num.setValue(atributos[9])
        self.ui.largo_num.setValue(atributos[10])
        self.ui.ancho_num.setValue(atributos[11])
        self.ui.altura_num.setValue(atributos[12])
        self.cbox()
        self.ui.estado_cbox.setCurrentText(atributos[13])
        self.ui.ubicacion_cbox.setCurrentText(atributos[4])

    def modificar_producto(self):
        global productId
        global codigoViejo
        global defaultImg
        codigo = self.ui.codigo_input.text()
        descripcion = self.ui.descripcion_input.toPlainText()
        marca = self.ui.marca_input.text()
        ubicacion = self.ui.ubicacion_cbox.currentText()
        condicion = self.ui.estado_cbox.currentText()
        if self.ui.fragil_si.isChecked():
            fragil = "1"
        else:
            fragil = "0"

        peso = self.ui.peso_num.value()
        ancho = self.ui.ancho_num.value()
        altura = self.ui.altura_num.value()
        largo = self.ui.largo_num.value()
        foto = defaultImg
        p.Productos.modificar_produc(codigoViejo, codigo, marca, descripcion, ubicacion, condicion, fragil, foto, peso,
                                     largo, ancho, altura)
        self.close()

    def borrar_producto(self):
        global productId
        qm = QMessageBox

        ret = qm.warning(self, 'Esta acción es irreversible', "¿Estás seguro que quieres eliminar el producto?",
                         qm.Yes | qm.No)
        if ret == qm.Yes:
            p.Productos.borrar_producto(productId)
            self.close()

    def upload_img(self):
        global defaultImg
        size = (256, 256)
        self.filename, ok = QFileDialog.getOpenFileName(self, 'Upload Image', '', 'Image files (*.jpg *.png)')
        if ok:
            defaultImg = os.path.basename(self.filename)
            img = Image.open(self.filename)
            img = img.resize(size)
            img.save('../main/img/{0}'.format(defaultImg))

    def cbox(self):
        areas = ar.Area.listar_area()
        for a in areas:
            self.ui.estado_cbox.addItem(a[0])
        pos = al.Alojamiento.listar_alojamiento()
        for p in pos:
            self.ui.ubicacion_cbox.addItem(p[0])
        self.ui.estado_cbox.currentIndexChanged.connect(self.clear_combo)
        self.ui.estado_cbox.currentIndexChanged.connect(self.update_combo)

    def update_combo(self):
        area_seleccionada = self.ui.estado_cbox.currentText()
        posiciones = al.Alojamiento.listar_alojamiento_disponibles_area(area_seleccionada)
        for pos in posiciones:
            self.ui.ubicacion_cbox.addItem(pos[0])

    def clear_combo(self):
        self.ui.ubicacion_cbox.clear()


#############################################################  CLASS BM_USUARIOS ######################################################


class BmUsuario(QMainWindow):

    def __init__(self):
        super(BmUsuario, self).__init__()
        self.ui = Bmu()
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
        self.rellenar_campos()

        # Subir foto btn
        self.ui.subirFoto_btn_2.clicked.connect(self.upload_img)

        # Modificar usuario btn
        self.ui.modificarprod_btn.clicked.connect(self.modificar_usuario)

        # Eliminar usuario btn
        self.ui.eliminarprod_btn.clicked.connect(self.dar_baja_usuario)

        # Mostrar Ventana
        self.show()

    # Rellenar los campos con los atributos del producto seleccionado
    def rellenar_campos(self):
        global userid
        global DNI
        global DNI_Viejo
        global defaultImg
        # global defaultImg
        usuario = u.Usuarios.mostrar_user(DNI)
        atributos = list(usuario[0])
        DNI_Viejo = atributos[0]
        self.ui.dni_input.setText(atributos[0])
        self.ui.nombre_input_2.setText(atributos[1])
        self.ui.apellido_input.setText(atributos[2])
        self.ui.nacimiento_date.setDate(atributos[4])
        self.ui.puesto_input.setText(atributos[5])
        self.ui.mail_input.setText(atributos[7])
        self.ui.mail_rep_input.setText(atributos[7])
        contra = loginDB.mostrar_pass(DNI_Viejo)
        contra = str(contra[0][0])
        self.ui.pass_input.setText(contra)
        self.ui.pass_rep_input.setText(contra)
        ###Img###
        self.usuarioImg = self.ui.label
        self.img = QPixmap('../main/img/{0}'.format(atributos[8]))
        self.usuarioImg.setPixmap(self.img)
        defaultImg = atributos[8]
        ########

        if str(atributos[3]) == "1":
            self.ui.tipo_cb.setCurrentText("Administrador")

        else:
            self.ui.tipo_cb.setCurrentText("Usuario")

        # CAMBIAR BOTÓN PARA QUE INFORME SI SE DA DE ALTA O NO

    def modificar_usuario(self):
        global DNI_Viejo
        global defaultImg
        dni = self.ui.dni_input.text()
        nombre = self.ui.nombre_input_2.text()
        apellido = self.ui.apellido_input.text()
        tipo = self.ui.tipo_cb.currentText()
        foto = defaultImg
        contrasena = self.ui.pass_input.text()
        contrasena_rep = self.ui.pass_rep_input.text()
        mail_rep = self.ui.mail_rep_input.text()
        if tipo == "Administrador":
            tipo = 1
        else:
            tipo = 0
        nacimiento = self.ui.nacimiento_date.date().toString("yyyy/MM/dd")
        puesto = self.ui.puesto_input.text()
        mail = self.ui.mail_input.text()
        if nombre == "" or apellido == "" or dni == "" or tipo == "" or puesto == "" or nacimiento == "" or contrasena == "" or contrasena_rep == "":
            QtWidgets.QMessageBox.critical(self, "Error", "Ingrese todos los datos")
            return None

        if len(dni) != 8:
            QtWidgets.QMessageBox.critical(self, "Error", "Ingrese un dni existente")
            return None

        if mail != mail_rep:
            QtWidgets.QMessageBox.critical(self, "Error", "Mails diferentes")
            return None

        if contrasena != contrasena_rep:
            QtWidgets.QMessageBox.critical(self, "Error", "Contraseñas diferentes")
            return None

        else:

            u.Usuarios.modificar_datos_user(DNI_Viejo, dni, nombre, apellido, tipo, puesto, nacimiento, mail, foto)
            loginDB.cambiar_contrasena(DNI_Viejo, dni, contrasena)

        self.close()

    def dar_baja_usuario(self):
        global DNI
        qm = QMessageBox

        ret = qm.warning(self, 'Advertencia', "¿Está seguro que quieres dar de baja el usuario?", qm.Yes | qm.No)
        if ret == qm.Yes:
            u.Usuarios.ab_usuario(DNI)
            self.close()

    def upload_img(self):
        global defaultImg
        size = (256, 256)
        self.filename, ok = QFileDialog.getOpenFileName(self, 'Upload Image', '', 'Image files (*.jpg *.png)')
        if ok:
            defaultImg = os.path.basename(self.filename)
            img = Image.open(self.filename)
            img = img.resize(size)
            img.save('../main/img/{0}'.format(defaultImg))
