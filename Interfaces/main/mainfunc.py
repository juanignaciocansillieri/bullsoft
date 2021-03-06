from PIL import Image
import os
from PyQt5 import QtCore
from PyQt5 import QtGui
from PyQt5 import QtWidgets
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from CLASES import usuarios as u, productos as p, area as ar, movimientos as m, lotes as l, alojamiento as al,estanterias as es
from DB import loginDB,conexion as conex
from Interfaces.main.bm_producto import Ui_MainWindow as Ui_Bm
from Interfaces.main.bm_user_ui import Ui_MainWindow as Bmu
from Interfaces.main.create_user_func import UsuarioWindow
from Interfaces.main.delete_area import BorrarArea
from Interfaces.main.egreso_func import NewEgreso
from Interfaces.main.ingreso_func import NewIngreso
from Interfaces.main.main import Ui_MainWindow
from Interfaces.main.modificar_area import ModificarArea as Ma
from Interfaces.main.nueva_area import Ui_MainWindow as Na
from Interfaces.main.nueva_area_func import NewArea
from Interfaces.main.nuevoProduct_func import ProductWindow
from Interfaces.main.posiciones_alojamiento import PosicionAlojamiento as Pa
from Interfaces.main.nueva_estanteria_func import Nueva_estanteria as ne
from CLASES import matriz as mz
from CLASES import  estanterias
from fpdf import FPDF

globalPosicion = ""
defaultImg = ""
codigoViejo = ""
DNI_Viejo = ""
DNI = ""
globalArea = ""
nombreNuevo = ""
n_egreso=0
nivelId = ""
tupla_egreso=[]
admin=False
nombre_user=""
tupla_pdf=[]

class Modern(QMainWindow):

    def __init__(self, admF,nombre):
        super(Modern, self).__init__()
        global admin
        admin=admF
        nombreNuevo=nombre
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
        self.ui.label_nombre_usuario.setText(nombreNuevo)
        ##########################   PAGINAS   ##################################

        ########################## PRODUCTOS ##################################

        ## Abrir Pagina Productos ##
        self.ui.products_btn.clicked.connect(
            lambda: self.ui.stackedWidget_3.setCurrentWidget(self.ui.product_subpage))
        self.ui.products_btn_2.clicked.connect(
            lambda: self.ui.stackedWidget_3.setCurrentWidget(self.ui.product_subpage))
        self.ui.products_btn.clicked.connect(self.listar_productos)
        self.ui.products_btn_stock.clicked.connect(self.listar_productos)
        # Abrir Pag Stock
        self.ui.products_btn.clicked.connect(
            lambda: self.ui.stackedWidget_main.setCurrentWidget(self.ui.page_stock))
        self.ui.products_btn_2.clicked.connect(
            lambda: self.ui.stackedWidget_main.setCurrentWidget(self.ui.page_stock))
        self.ui.products_btn_stock.clicked.connect(
            lambda: self.ui.stackedWidget_main.setCurrentWidget(self.ui.page_stock))
        self.ui.products_btn_stock_2.clicked.connect(
            lambda: self.ui.stackedWidget_main.setCurrentWidget(self.ui.page_stock))
        # Abrir Pag Movimientos
        self.ui.products_btn_movimiento.clicked.connect(
            lambda: self.ui.stackedWidget_main.setCurrentWidget(self.ui.page_movimientos))
        self.ui.products_btn_movimientos_2.clicked.connect(
            lambda: self.ui.stackedWidget_main.setCurrentWidget(self.ui.page_movimientos))
        self.ui.products_btn_movimiento.clicked.connect(self.listar_movimientos)
        self.ui.new_egreso_btn.clicked.connect(self.mostrar_egreso)
        self.ui.btn_agregarProdEgreso.clicked.connect(self.guardar_egreso)
        self.ui.btn_actualizarProdEgreso.clicked.connect(self.act_egreso)
        self.ui.btn_eliminarProdEgreso.clicked.connect(self.borrar_egreso)
        self.ui.btn_confirmarPicking.clicked.connect(self.confirmar_egreso)
        self.ui.new_ingreso_btn.clicked.connect(self.mostrar_ingreso)
        self.ui.btn_actualizarMov.clicked.connect(self.listar_movimientos)
        self.ui.pushButton_21.clicked.connect(self.buscar_movimiento)
        # Abrir Pag Lotes
        self.ui.products_btn_lotes.clicked.connect(
            lambda: self.ui.stackedWidget_main.setCurrentWidget(self.ui.page_lotes))
        self.ui.products_btn_lotes_2.clicked.connect(
            lambda: self.ui.stackedWidget_main.setCurrentWidget(self.ui.page_lotes))
        self.ui.pushButton_20.clicked.connect(self.listar_lotes)
        self.ui.btn_volver_niveles.clicked.connect(lambda: self.ui.stackedWidget_main.setCurrentWidget(self.ui.page_areaIndividual))
        #self.ui.users_btn_2.clicked.connect(lambda: self.ui.stackedWidget_3.setCurrentWidget(self.ui.user_subpage) )
        self.ui.users_btn_2.clicked.connect(self.listar_usuarios)
        self.ui.users_btn.clicked.connect(self.listar_usuarios)
        self.ui.label_inicio_stock.mousePressEvent = self.click_label_stock
        self.ui.label_inicio_stock_2.mousePressEvent = self.click_label_stock
        self.ui.label_inicio_stock_3.mousePressEvent = self.click_label_stock
        self.ui.label_inicio_lotes_2.mousePressEvent = self.click_label_lotes
        self.ui.label_inicio_lotes_3.mousePressEvent = self.click_label_lotes
        self.ui.label_inicio_lotes.mousePressEvent = self.click_label_lotes
        self.ui.label_inicio_movimientos.mousePressEvent = self.click_label_mov
        self.ui.label_inicio_movimientos_2.mousePressEvent = self.click_label_mov
        self.ui.label_inicio_movimientos_3.mousePressEvent = self.click_label_mov
        self.ui.label_inicio_areas.mousePressEvent = self.click_label_areas
        self.ui.label_inicio_areas_2.mousePressEvent = self.click_label_areas
        self.ui.label_inicio_usuarios.mousePressEvent = self.click_label_usuarios
        self.ui.label_inicio_usuarios_2.mousePressEvent = self.click_label_usuarios
        self.ui.btn_inicio_lotes.clicked.connect(lambda: self.ui.stackedWidget_main)
        self.shadow = QGraphicsDropShadowEffect()
        self.shadow1= QGraphicsDropShadowEffect()
        self.shadow2 = QGraphicsDropShadowEffect()
        self.shadow3 = QGraphicsDropShadowEffect()
        self.shadow4 = QGraphicsDropShadowEffect()

        self.shadow.setBlurRadius(80)
        self.shadow1.setBlurRadius(80)
        self.shadow2.setBlurRadius(80)
        self.shadow3.setBlurRadius(80)
        self.shadow4.setBlurRadius(80)

        self.ui.btn_inicio_usuarios.setGraphicsEffect(self.shadow)
        self.ui.btn_inicio_areas.setGraphicsEffect(self.shadow1)
        self.ui.btn_inicio_stock.setGraphicsEffect(self.shadow2)
        self.ui.btn_inicio_movimientos.setGraphicsEffect(self.shadow3)
        self.ui.btn_inicio_lotes.setGraphicsEffect(self.shadow4)

        self.ui.inicio_btn.setChecked(True)
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
        """
        if admin:
            self.ui.user_new_btn.clicked.connect(self.mostrar_new_user)

            self.ui.users_btn.clicked.connect(self.listar_usuarios)
            self.ui.btn_buscarU.clicked.connect(self.buscar_usuarios)

            ## Abrir Pagina Usuarios ##
            self.ui.users_btn.clicked.connect(
                lambda: self.ui.stackedWidget_main.setCurrentWidget(self.ui.page_usuarios))

            self.ui.users_btn.clicked.connect(
                lambda: self.ui.stackedWidget_3.setCurrentWidget(self.ui.user_subpage))

            self.ui.users_btn_2.clicked.connect(
                lambda: self.ui.stackedWidget_main.setCurrentWidget(self.ui.page_usuarios))

            self.ui.users_btn_2.clicked.connect(lambda: self.ui.stackedWidget_3.setCurrentWidget(self.ui.user_subpage))

            self.ui.btn_actualizarUsuarios.clicked.connect(self.listar_usuarios)
        else:
            self.ui.users_btn.clicked.connect(
                lambda: QtWidgets.QMessageBox.critical(self, "Error", "No tiene los permisos suficientes"))
            self.ui.users_btn_2.clicked.connect(
                lambda: QtWidgets.QMessageBox.critical(self, "Error", "No tiene los permisos suficientes"))
        """
        self.ui.tableWidget_usuarios.doubleClicked.connect(self.seleccionarusuario)
        self.ui.tableWidget_usuarios.doubleClicked.connect(self.mostrar_bm_user)


        ########################## DEPOSITOS ##################################

        self.ui.deposito_btn.clicked.connect(self.mostra_areas)
        ## Abrir Pagina Depositos ##
        """if (verificar_deposito== 0):
           self.ui.deposito_btn.clicked.connect(lambda: self.ui.stackedWidget_main.setCurrentWidget(self.ui.page_area))
            self.ui.deposito_btn_2.clicked.connect(lambda: self.ui.stackedWidget_main.setCurrentWidget(self.ui.page_area))
            print("dep0", verificar_deposito)
            self.mostra_areas()
        else:
            print("dep1", verificar_deposito)
            self.mostra_areas()
            self.ui.deposito_btn.clicked.connect(lambda: self.ui.stackedWidget_main.setCurrentWidget(self.ui.page_deposito))
            self.ui.deposito_btn_2.clicked.connect(lambda: self.ui.stackedWidget_main.setCurrentWidget(self.ui.page_deposito))
"""
        self.ui.btn_confirmarPicking.clicked.connect(self.width_tabla)

        self.ui.deposito_btn.clicked.connect(self.click_label_areas)
        self.ui.deposito_btn_2.clicked.connect(self.click_label_areas)
        self.ui.newArea_btn.clicked.connect(self.mostrar_new_area)
        self.ui.label_12.mousePressEvent = self.click_a
        self.ui.btn_actualizarAreas.clicked.connect(self.mostra_areas)
        self.ui.btn_actualizar_estanteria.clicked.connect(lambda: self.listar_segmentos(globalArea))
        #self.ui.btn_actualizarAreas.clicked.connect(self.crear_deposito)
        self.ui.btn_crearDeposito.clicked.connect(lambda: self.ui.stackedWidget_main.setCurrentWidget(self.ui.page_deposito))
        self.ui.inicio_btn.clicked.connect(lambda: self.ui.stackedWidget_main.setCurrentWidget(self.ui.page_inicio))
        self.ui.inicio_btn_2.clicked.connect(lambda: self.ui.stackedWidget_main.setCurrentWidget(self.ui.page_inicio))
        self.ui.inicio_btn.clicked.connect(lambda: self.ui.stackedWidget_3.setCurrentWidget(self.ui.user_subpage))
        self.ui.inicio_btn_2.clicked.connect(lambda: self.ui.stackedWidget_3.setCurrentWidget(self.ui.user_subpage))
        self.ui.btn_crearDeposito.clicked.connect(self.crear_deposito)
        self.ui.btn_crearDeposito.clicked.connect(self.mostra_areas)
        self.ui.btn_newPosicion.clicked.connect(lambda: self.new_posicion(globalArea))
        self.ui.newArea_btn_2.clicked.connect(self.mostrar_borrar_area)
        self.ui.btn_nuevaEstanteria.clicked.connect(self.mostrar_nueva_estanteria)
        self.ui.btn_actualizarNiveles.clicked.connect(self.listar_niveles)
        self.ui.tableWidget_niveles.doubleClicked.connect(self.seleccionar_niveles)
        self.ui.tableWidget_niveles.doubleClicked.connect(self.listar_productos_niveles)
        self.ui.products_btn.clicked.connect(self.checkear_boton_prod)
        self.ui.products_btn_2.clicked.connect(self.checkear_boton_prod)
        self.ui.users_btn_2.clicked.connect(self.checkear_boton_users)
        self.ui.users_btn.clicked.connect(self.checkear_boton_users)
        self.ui.inicio_btn.clicked.connect(self.checkear_boton_inicio)
        self.ui.inicio_btn_2.clicked.connect(self.checkear_boton_inicio)
        self.ui.deposito_btn.clicked.connect(self.checkear_boton_areas)
        self.ui.deposito_btn_2.clicked.connect(self.checkear_boton_areas)
        self.ui.products_btn_stock.clicked.connect(self.checkear_boton_stock)
        self.ui.products_btn_stock_2.clicked.connect(self.checkear_boton_stock)
        self.ui.products_btn_movimiento.clicked.connect(self.checkear_boton_movimientos)
        self.ui.products_btn_movimientos_2.clicked.connect(self.checkear_boton_movimientos)
        self.ui.products_btn_lotes.clicked.connect(self.checkear_boton_lotes)
        self.ui.products_btn_lotes_2.clicked.connect(self.checkear_boton_lotes)
        self.ui.btn_inicio_stock.clicked.connect(self.click_label_stock)
        self.ui.btn_inicio_areas.clicked.connect(self.click_label_areas)
        self.ui.btn_inicio_lotes.clicked.connect(self.click_label_lotes)
        self.ui.btn_inicio_movimientos.clicked.connect(self.click_label_mov)
        self.ui.btn_inicio_usuarios.clicked.connect(self.click_label_usuarios)
        self.ui.users_btn.clicked.connect(self.click_label_usuarios)
        self.ui.users_btn_2.clicked.connect(self.click_label_usuarios)
        self.ui.btn_volver_egreso.clicked.connect(lambda : self.ui.stackedWidget_main.setCurrentWidget(self.ui.page_movimientos))
        self.ui.btn_confirmarPicking_2.clicked.connect(self.table_to_pdf)

        ##########################       ##################################

    def click_label_stock(self,event):
        self.ui.stackedWidget_main.setCurrentWidget(self.ui.page_stock)
        self.ui.stackedWidget_3.setCurrentWidget(self.ui.product_subpage)
        self.checkear_boton_stock()
        self.listar_productos()
        self.checkear_boton_prod()
    def click_label_mov(self,event):
        self.ui.stackedWidget_main.setCurrentWidget(self.ui.page_movimientos)
        self.ui.stackedWidget_3.setCurrentWidget(self.ui.product_subpage)
        self.checkear_boton_prod()
        self.listar_movimientos()
        self.checkear_boton_movimientos()

    def click_label_lotes(self,event):
        self.ui.stackedWidget_main.setCurrentWidget(self.ui.page_lotes)
        self.ui.stackedWidget_3.setCurrentWidget(self.ui.product_subpage)
        self.checkear_boton_prod()
        self.listar_lotes()
        self.checkear_boton_lotes()
    def click_label_usuarios(self,event):
        admin
        if admin:
            self.ui.user_new_btn.clicked.connect(self.mostrar_new_user)
            self.listar_usuarios()
            self.ui.btn_buscarU.clicked.connect(self.buscar_usuarios)

            self.ui.stackedWidget_main.setCurrentWidget(self.ui.page_usuarios)
            self.ui.stackedWidget_3.setCurrentWidget(self.ui.user_subpage)
            self.ui.btn_actualizarUsuarios.clicked.connect(self.listar_usuarios)
        else:
            QtWidgets.QMessageBox.critical(self, "Error", "No tiene los permisos suficientes")
            return None
        self.listar_usuarios()
        self.checkear_boton_users()

    def click_label_areas(self,event):

        if admin:
            self.ui.stackedWidget_main.setCurrentWidget(self.ui.page_area)

        else:
            QtWidgets.QMessageBox.critical(self, "Error", "No tiene los permisos suficientes")
            return None
        self.verificar_deposito_creado()
        self.checkear_boton_areas()
    def checkear_boton_prod(self):

            self.ui.users_btn.setChecked(False)
            self.ui.users_btn_2.setChecked(False)
            self.ui.inicio_btn.setChecked(False)
            self.ui.inicio_btn_2.setChecked(False)
            self.ui.deposito_btn.setChecked(False)
            self.ui.deposito_btn_2.setChecked(False)
            self.ui.products_btn.setChecked(True)
            self.ui.products_btn_2.setChecked(True)
            self.ui.products_btn_stock_2.setChecked(True)
            self.ui.products_btn_lotes.setChecked(False)
            self.ui.products_btn_lotes_2.setChecked(False)
            self.ui.products_btn_movimientos_2.setChecked(False)
            self.ui.products_btn_movimiento.setChecked(False)
            self.ui.buscar_input.setText("")

    def checkear_boton_stock(self):
        self.ui.products_btn_stock.setChecked(True)
        self.ui.products_btn_stock_2.setChecked(True)
        self.ui.products_btn_movimiento.setChecked(False)
        self.ui.products_btn_movimientos_2.setChecked(False)
        self.ui.products_btn_lotes.setChecked(False)
        self.ui.products_btn_lotes_2.setChecked(False)
        self.ui.buscar_input.setText("")
    def checkear_boton_movimientos(self):
        self.ui.products_btn_stock.setChecked(False)
        self.ui.products_btn_stock_2.setChecked(False)
        self.ui.products_btn_movimiento.setChecked(True)
        self.ui.products_btn_movimientos_2.setChecked(True)
        self.ui.products_btn_lotes.setChecked(False)
        self.ui.products_btn_lotes_2.setChecked(False)
        self.ui.lineEdit_5.setText("")
    def checkear_boton_lotes(self):
        self.ui.products_btn_stock.setChecked(False)
        self.ui.products_btn_stock_2.setChecked(False)
        self.ui.products_btn_movimiento.setChecked(False)
        self.ui.products_btn_movimientos_2.setChecked(False)
        self.ui.products_btn_lotes.setChecked(True)
        self.ui.products_btn_lotes_2.setChecked(True)
        self.ui.lineEdit_6.setText("")
        self.ui.tableWidget_lotes.setRowCount(0)


    def checkear_boton_areas(self):
            self.ui.products_btn.setChecked(False)
            self.ui.products_btn_2.setChecked(False)
            self.ui.products_btn_stock_2.setChecked(False)
            self.ui.users_btn.setChecked(False)
            self.ui.users_btn_2.setChecked(False)
            self.ui.inicio_btn.setChecked(False)
            self.ui.inicio_btn_2.setChecked(False)
            self.ui.deposito_btn.setChecked(True)
            self.ui.deposito_btn_2.setChecked(True)
    def checkear_boton_users(self):
            self.ui.products_btn.setChecked(False)
            self.ui.products_btn_2.setChecked(False)
            self.ui.products_btn_stock_2.setChecked(False)
            self.ui.users_btn.setChecked(True)
            self.ui.users_btn_2.setChecked(True)
            self.ui.inicio_btn.setChecked(False)
            self.ui.inicio_btn_2.setChecked(False)
            self.ui.deposito_btn.setChecked(False)
            self.ui.deposito_btn_2.setChecked(False)
            self.ui.lineEdit_3.setText("")
    def checkear_boton_inicio(self):
            self.ui.products_btn.setChecked(False)
            self.ui.products_btn_2.setChecked(False)
            self.ui.products_btn_stock_2.setChecked(False)
            self.ui.users_btn.setChecked(False)
            self.ui.users_btn_2.setChecked(False)
            self.ui.inicio_btn.setChecked(True)
            self.ui.inicio_btn_2.setChecked(True)
            self.ui.deposito_btn.setChecked(False)
            self.ui.deposito_btn_2.setChecked(False)

    def verificar_deposito_creado(self):
        verificar_deposito = conex.verificar_deposito()
        if (verificar_deposito == 0):
            self.ui.stackedWidget_main.setCurrentWidget(self.ui.page_area)
            print("dep0", verificar_deposito)
            self.mostra_areas()
        else:
            print("dep1", verificar_deposito)
            self.ui.stackedWidget_main.setCurrentWidget(self.ui.page_deposito)
            self.mostra_areas()
        self.ui.stackedWidget_3.setCurrentWidget(self.ui.deposito_subpage)



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
        self.mostra_areas()

    def mostrar_ingreso(self):
        self.newMovimiento = NewIngreso()
        self.newMovimiento.show()

    def mostrar_egreso(self):
        global  n_egreso
        global tupla_egreso
        n_egreso=0
        tupla_egreso=[]
        self.ui.stackedWidget_main.setCurrentWidget(self.ui.page_egreso)
        self.act_egreso()
        self.ui.input_codigoProdEgreso.setText("")
        self.ui.input_motivo_egreso.setText("")
        self.ui.num_cantidadEgreso.setValue(0)

    def mostrar_borrar_area(self):
        self.borrarArea = BorrarArea()
        self.borrarArea.show()

    def mostrar_nueva_estanteria(self):
        self.nueva_estanteria = ne(globalArea)
        self.nueva_estanteria.show()

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
                table_row, 3, QtWidgets.QTableWidgetItem(str(l.obtener_cantidades(row[0]))))

            self.ui.tableWidget_stock_2.setItem(
                table_row, 4, QtWidgets.QTableWidgetItem(str(l.obtener_fecha(row[0]))))

            table_row += 1

            #   MOVIMIENTO EGRESO

    def guardar_egreso(self):
        global  n_egreso
        global tupla_egreso
        codigo=self.ui.input_codigoProdEgreso.text()
        if codigo=="":
            QtWidgets.QMessageBox.critical(self, "Error", "Ingrese un codigo")
            return None
        if p.ver_desc(codigo)==0:
            QtWidgets.QMessageBox.critical(self, "Error", "Producto no encontrado")
            return None
        cantidad=self.ui.num_cantidadEgreso.text()
        if int(cantidad)<=0:
            QtWidgets.QMessageBox.critical(self, "Error", "Ingrese una cantidad correcta")
            return None
        #if cantidad<l.Lote.obtener_cantidades(codigo):
        #    QtWidgets.QMessageBox.critical(self, "Error", "Cantidad no disponible")
        #    return None
        desc=p.ver_desc(codigo)
        t = [str(codigo), desc, str(cantidad)]
        tupla_egreso.append(t)
        #print(tupla_egreso)
        self.ui.input_codigoProdEgreso.setText("")
        self.ui.num_cantidadEgreso.setValue(0)
        n_egreso=n_egreso+1
        self.act_egreso()

    def borrar_egreso(self):
        global n_egreso
        global tupla_egreso
        codigo = self.ui.input_codigoProdEgreso.text()
        if codigo=="":
            QtWidgets.QMessageBox.critical(self, "Error", "Ingrese un codigo")
            return None
        n=len(tupla_egreso)
        print(tupla_egreso)
        i=0
        while i<n:
            if tupla_egreso[i][0] ==codigo:
                print(i)
                print(tupla_egreso[i][0],codigo)
                tupla_egreso.pop(i)
                i=n+1
            else: i=i+1
        if i==n:
            QtWidgets.QMessageBox.critical(self, "Error", "Producto no encontrado")
            return None

        print(tupla_egreso)
        self.ui.input_codigoProdEgreso.setText("")
        self.ui.num_cantidadEgreso.setValue(0)
        n_egreso = n_egreso - 1
        self.act_egreso()

    def act_egreso(self):
        #print("actualizar")
        global tupla_egreso
        global n_egreso
        self.ui.tableWidget_egreso.setRowCount(n_egreso)
        table_row = 0
        print("n greso",n_egreso)
        for row in tupla_egreso:
            self.ui.tableWidget_egreso.setItem(
                table_row, 0, QtWidgets.QTableWidgetItem(str(row[0])))
            self.ui.tableWidget_egreso.setItem(
                table_row, 1, QtWidgets.QTableWidgetItem(str(row[1])))
            self.ui.tableWidget_egreso.setItem(
                table_row, 2, QtWidgets.QTableWidgetItem(str(row[2])))
            table_row = table_row + 1


    def confirmar_egreso(self):
        global tupla_egreso
        global n_egreso
        fecha=self.ui.fecha_vencimiento_egreso.date().toString("yyyy/MM/dd")
        motivo=self.ui.input_motivo_egreso.text()
        if motivo=="":
            QtWidgets.QMessageBox.critical(self, "Error", "Agregue motivo antes de confirmar")
            return None
        if n_egreso==0:
            QtWidgets.QMessageBox.critical(self, "Error", "Agregue productos antes de confirmar")
            return None
        n = len(tupla_egreso)
        i = 0
        lc=[]
        while i < n:
            codigo = tupla_egreso[i][0]
            lc.append(codigo)
            cantidad = tupla_egreso[i][2]
            fifo=l.fifo(codigo, cantidad)
            if fifo==1 :
                QtWidgets.QMessageBox.critical(self, "Error", "No hay esa cantidad disponible")
                return None
            if fifo==0:
                QtWidgets.QMessageBox.critical(self, "Error", "No hay lo del producto disponible")
                return None

            if(al.modificar_dispo_egreso(codigo,cantidad)==0):
                QtWidgets.QMessageBox.critical(self, "Error", "No hay esa disponibilidad")
                return None
            else: m.Movimientos(1,codigo,cantidad,motivo,fecha)

            i = i +1

        rp=p.pick_posiciones(lc)
        #print("rp",rp)
        pick = al.pick_(rp)
        #print(pick)
        self.listar_pick(pick,lc)
        tupla_egreso=[]
        n_egreso=0
        self.act_egreso()
        return 0

    def listar_pick(self,pick,lc):
        global tupla_pdf
        tupla_pdf=[]
        lc2=p.pick_productos(lc,pick)
        self.ui.tableWidget_picking.setRowCount(n_egreso)
        n=n_egreso
        t=[]
        table_row = 0
        for row in lc2:
            t=[]
            codigo=p.ver_posicion(row).split(sep="-")
            self.ui.tableWidget_picking.setItem(
                table_row, 0, QtWidgets.QTableWidgetItem(str(codigo[0])))
            t.append(str(codigo[0]))
            self.ui.tableWidget_picking.setItem(
                table_row, 1, QtWidgets.QTableWidgetItem(str(codigo[1])))
            t.append(str(codigo[1]))
            self.ui.tableWidget_picking.setItem(
                table_row, 2, QtWidgets.QTableWidgetItem(str(codigo[2])))
            t.append(str(codigo[2]))
            self.ui.tableWidget_picking.setItem(
                table_row, 3, QtWidgets.QTableWidgetItem(str(codigo[3])))
            t.append(str(codigo[3]))
            self.ui.tableWidget_picking.setItem(
                table_row, 4, QtWidgets.QTableWidgetItem(str(codigo[4])))
            t.append(str(codigo[4]))
            self.ui.tableWidget_picking.setItem(
                table_row, 5, QtWidgets.QTableWidgetItem(str(row)))
            t.append(str(row))
            self.ui.tableWidget_picking.setItem(
                table_row, 6, QtWidgets.QTableWidgetItem(str(p.ver_desc(row))))
            t.append(str(p.ver_desc(row)))

            fechalote=l.lote_codigo(row)
            if fechalote==0:
                fechalote="-"
            self.ui.tableWidget_picking.setItem(
                table_row, 7, QtWidgets.QTableWidgetItem(fechalote))
            t.append(str(l.lote_codigo(row)))

            i=0
            while i < n:
                codigo = tupla_egreso[i][0]
                cantidad = tupla_egreso[i][2]
                print(codigo,cantidad)
                if codigo==row:
                    cantidad2=cantidad

                    i=n+1
                i = i + 1
            #print(cantidad2)

            self.ui.tableWidget_picking.setItem(
                table_row, 8, QtWidgets.QTableWidgetItem(str(cantidad2)))
            t.append(str(cantidad2))

            print("t, ",t )

            tupla_pdf.append(t)

            table_row+=1
        return 0

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
        lotes = l.listar_lote(id)
        n = l.contar_filas_producto(id)
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

    # Buscar productos a traves del input, por par??metro ingresado
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
        products = p.buscar_product(parametro)
        n = p.buscar_product_rows(parametro)
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
        n = ar.contar_filas()
        child = self.ui.verticalLayout_7.count()
        print("areacreada")
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
        print("mostrar areas")
        child = self.ui.verticalLayout_7.count()
        areas = ar.Area.listar_area()
        n = ar.contar_filas()
        print(n,child)

        for i in reversed(range(self.ui.verticalLayout_7.count())):
            self.ui.verticalLayout_7.itemAt(i).widget().deleteLater()

        for a in areas:
                    frame = QtWidgets.QFrame(self.ui.frame_3)
                    frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
                    frame.setFrameShadow(QtWidgets.QFrame.Raised)
                    frame.setObjectName(a[0])
                    frame.setMaximumSize(QtCore.QSize(200, 200))
                    vertical_layout = QtWidgets.QVBoxLayout(frame)
                    self.btn = QPushButton(frame)
                    self.btn.setText("Ver")
                    self.btn.setObjectName('%s' % a[0])
                    self.btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
                    self.btn.setMinimumSize(QtCore.QSize(70, 30))
                    self.btn.setMaximumSize(QtCore.QSize(100, 30))
                    self.label = QtWidgets.QLabel(frame)
                    self.btn.released.connect(self.button_released)
                    p=a[2].split(sep="x")
                    x=int(p[0])
                    y=int(p[1])
                    self.ui.gridLayout.addWidget(frame, x, y)
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


                    self.btn2 = QtWidgets.QPushButton(self.ui.frame_14)
                    self.btn2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
                    self.btn2.setStyleSheet("QPushButton{\n"
                                            "border:none;\n"
                                            "font-family: Cairo;\n"
                                            "font-weight: Regular;\n"
                                            "border-radius:5px;\n"
                                            #"margin-right:20px;\n"
                                            "text-align: center;\n"
                                            "color: #818489 ;\n"
                                            #"padding:5px;\n"

                                            "}\n"
                                            "\n"
                                            "QPushButton:hover{\n"
                                            "font-weight: bold;\n"
                                            "background:rgba(129, 132, 137, 20);\n"
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
                    if child > n:
                        for i in reversed(range(self.ui.verticalLayout_7.count())):
                            self.ui.verticalLayout_7.itemAt(i).widget().deleteLater()
                        for i in reversed(range(self.ui.gridLayout.count())):
                            self.ui.gridLayout.itemAt(i).widget().deleteLater()


    def button_released(self):
        global globalArea
        sending_button = self.sender()
        nombre_area = str(sending_button.objectName())
        if ar.ver_posicion(nombre_area)==0:
            QtWidgets.QMessageBox.critical(self, "Error", "Actualice para poder ingresar")
            return None
        if ar.ver_pasillos(nombre_area)==0 or ar.ver_nombre(nombre_area)==0:
            QtWidgets.QMessageBox.critical(self, "Error", "Cree el area para poder ingresar")
            return None
        else:
            self.ui.stackedWidget_main.setCurrentWidget(self.ui.page_areaIndividual)
            globalArea = nombre_area
            self.listar_segmentos(globalArea)

    def new_posicion(self, btn):
        self.newPosicionAlojamiento = Pa(globalArea)
        self.newPosicionAlojamiento.show()

    def modificar_area(self, btn):

        self.newPosicionAlojamiento = Ma(btn)
        self.newPosicionAlojamiento.show()



    def listar_segmentos(self, btn):
        global globalArea
        global globalPosicion
        nombreArea = btn
        self.ui.label_nombre_area.setText(nombreArea)
        self.ui.pushButton.clicked.connect(lambda :self.ui.stackedWidget_main.setCurrentWidget(self.ui.page_deposito))
        area = ar.Area.mostrar_area(nombreArea)
        child = self.ui.gridLayout_2.count()

        pasillos = int(area[0][3])
        segmentos = estanterias.contar_estanterias_area(globalArea) ##cuantas estanterias tiene el area

        total_segmentos = int(area[0][4])
        print(total_segmentos)
        vacio = 0
        i = 1
        if child >0:
            for i in reversed(range(self.ui.gridLayout_2.count())):
                self.ui.gridLayout_2.itemAt(i).widget().deleteLater()
        i=1
        j=1
        if pasillos == 2 and total_segmentos == 4:
            for x in range(segmentos):
                if x==1 or x==4:
                    j+=1
                frame = QtWidgets.QFrame(self.ui.frame_area)
                frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
                frame.setFrameShadow(QtWidgets.QFrame.Raised)
                frame.setMaximumSize(QtCore.QSize(190, 428))
                frame2 = QtWidgets.QFrame(self.ui.frame_area)
                frame2.setFrameShape(QtWidgets.QFrame.StyledPanel)
                frame2.setFrameShadow(QtWidgets.QFrame.Raised)
                frame2.setMaximumSize(QtCore.QSize(190, 428))
                frame_pasillo = QtWidgets.QFrame(self.ui.frame_area)
                frame_pasillo.setFrameShape(QtWidgets.QFrame.StyledPanel)
                frame_pasillo.setFrameShadow(QtWidgets.QFrame.Raised)
                frame_pasillo.setMaximumSize(QtCore.QSize(190, 428))
                frame_pasillo.setStyleSheet("border:1px solid white")
                frame_pasillo2 = QtWidgets.QFrame(self.ui.frame_area)
                frame_pasillo2.setFrameShape(QtWidgets.QFrame.StyledPanel)
                frame_pasillo2.setFrameShadow(QtWidgets.QFrame.Raised)
                frame_pasillo2.setMaximumSize(QtCore.QSize(190, 428))
                frame_pasillo2.setStyleSheet("border:1px solid white")
                vertical_layout = QtWidgets.QVBoxLayout(frame)
                vertical_layout2 = QtWidgets.QVBoxLayout(frame2)
                vertical_layout1 = QtWidgets.QVBoxLayout(frame_pasillo)
                self.ui.gridLayout_2.addWidget(frame, 1, j)
                if segmentos == 4:
                    self.ui.gridLayout_2.addWidget(frame2,1,6)
                    self.ui.gridLayout_2.addWidget(frame_pasillo, 1, 2)
                    self.ui.gridLayout_2.addWidget(frame_pasillo2, 1, 5)


                niveles = estanterias.mostrar_columnas(globalArea, i)
                nivel=int(niveles[0])
                print("col")
                for y in range(nivel):
                    btn_area = QtWidgets.QPushButton()
                    btn_area2 = QtWidgets.QPushButton()
                    btn_area.setMinimumSize(QtCore.QSize(55, 55))
                    btn_area2.setMinimumSize(QtCore.QSize(55, 55))
                    if x==0:
                        btn_area.setObjectName(globalArea + "-" + str(x + 1) + "-" + str(y + 1))
                    else:
                        btn_area.setObjectName(globalArea + "-" + str(x) + "-" + str(y + 1))
                        btn_area2.setObjectName(globalArea + "-" + str(x+1) + "-" + str(y + 1))
                    vertical_layout.addWidget(btn_area, 0, QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter)
                    vertical_layout2.addWidget(btn_area2, 0, QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter)
                    btn_area.released.connect(self.button_released2)
                    btn_area2.released.connect(self.button_released2)
                i=niveles[1]+1
                j+=1


        else:
            for x in range(segmentos):
                frame = QtWidgets.QFrame(self.ui.frame_area)
                frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
                frame.setFrameShadow(QtWidgets.QFrame.Raised)
                frame.setMaximumSize(QtCore.QSize(190, 428))
                vertical_layout = QtWidgets.QVBoxLayout(frame)
                self.ui.gridLayout_2.addWidget(frame,1,i)
                niveles=estanterias.mostrar_columnas(globalArea,i)
                nivel = int(niveles[0])
                for y in range(nivel):
                    btn_area = QtWidgets.QPushButton(self.ui.frame)
                    btn_area.setMinimumSize(QtCore.QSize(55, 55))
                    btn_area.setObjectName(globalArea + "-" + str(x+1) + "-" + str(y+1))
                    btn_area.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
                    vertical_layout.addWidget(btn_area, 0, QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter)
                    btn_area.released.connect(self.button_released2)
                i=niveles[1]+1

    def width_tabla(self):
        header = self.ui.tableWidget_picking.horizontalHeader()
        header.setStretchLastSection(False)
        self.ui.tableWidget_picking.setColumnWidth(0, 68)
        self.ui.tableWidget_picking.setColumnWidth(1, 25)
        self.ui.tableWidget_picking.setColumnWidth(2, 25)
        self.ui.tableWidget_picking.setColumnWidth(3, 25)
        self.ui.tableWidget_picking.setColumnWidth(4, 35)
        self.ui.tableWidget_picking.setColumnWidth(5, 92)
        self.ui.tableWidget_picking.setColumnWidth(6, 115)
        self.ui.tableWidget_picking.setColumnWidth(7, 90)
        self.ui.tableWidget_picking.setColumnWidth(8, 25)


    def button_released2(self):
        global globalPosicion
        sending_button = self.sender()
        nombre_posicion = str(sending_button.objectName())
        self.ui.stackedWidget_main.setCurrentWidget(self.ui.page_posicionesAlojamiento)
        print(nombre_posicion)
        globalPosicion = nombre_posicion
        print(globalPosicion)
        self.listar_productos_posicion()
        self.listar_niveles()



    def listar_productos_posicion(self):
        global globalPosicion
        self.ui.label_posicion.setText(globalPosicion)

    def listar_productos_niveles(self):
        global nivelId
        print(nivelId)
        products = p.listar_productos_ubicacion(nivelId)
        print(products)
        n = p.contar_productos_ubicacion(nivelId)
        print(n)
        self.ui.tableWidget_prodNiveles.setRowCount(n)
        table_row = 0

        for row in products:
            print("row",row)
            self.ui.tableWidget_prodNiveles.setItem(
                table_row, 0, QtWidgets.QTableWidgetItem(row[0]))
            self.ui.tableWidget_prodNiveles.setItem(
                table_row, 1, QtWidgets.QTableWidgetItem(row[1]))
            self.ui.tableWidget_prodNiveles.setItem(
                table_row, 2, QtWidgets.QTableWidgetItem(row[2]))
            self.ui.tableWidget_prodNiveles.setItem(
                table_row, 3, QtWidgets.QTableWidgetItem(str(l.obtener_cantidades(row[0]))))

            self.ui.tableWidget_prodNiveles.setItem(
                table_row, 4, QtWidgets.QTableWidgetItem(str(l.obtener_fecha(row[0]))))

            table_row += 1
    def listar_niveles(self):
        global globalPosicion
        global globalArea
        table_row_i = 0
        posicion = globalPosicion.split(sep="-")
        area=posicion[0]
        segmento=posicion[1]
        columna=posicion[2]
        niveles = int(es.contar_niveles(globalArea,segmento))
        self.ui.tableWidget_niveles.setRowCount(niveles)
        data = al.mostrar_al(area, segmento, columna)

        for n in data:
            self.ui.tableWidget_niveles.setItem(
                table_row_i, 0, QtWidgets.QTableWidgetItem(n[0]))
            self.ui.tableWidget_niveles.setItem(
                table_row_i, 1, QtWidgets.QTableWidgetItem(n[1]))
            self.ui.tableWidget_niveles.setItem(
                table_row_i, 2, QtWidgets.QTableWidgetItem(n[2]))
            self.ui.tableWidget_niveles.setItem(
                table_row_i, 3, QtWidgets.QTableWidgetItem(n[3]))
            table_row_i+=1

        for x in range(niveles):
            item = QtWidgets.QTableWidgetItem()
            item.setText("Nivel " + str(x+1))
            self.ui.tableWidget_niveles.verticalHeader().setVisible(True)
            self.ui.tableWidget_niveles.setVerticalHeaderItem(x,item)

    def seleccionar_niveles(self):
        global nivelId
        lista_niveles = []
        lista_niveles.append(self.ui.tableWidget_niveles.item(self.ui.tableWidget_niveles.currentRow(), 0).text())
        nivelId = lista_niveles[0]
    # CREAR DEP??SITO
    def crear_deposito(self):
        ancho_area = self.ui.spinBox_anchoarea.value()
        largo_area = self.ui.spinBox_largoarea.value()
        mz.alta_datos_matriz(ancho_area,largo_area)
        for x in range(largo_area):
            for y in range(ancho_area):
                mz.crear_matriz_areas(x+1,y+1)


    # LISTAR USUARIOS EN TABLA

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

    def table_to_pdf(self):
        global tupla_pdf
        data=[]
        pdf = FPDF(format='letter', unit='in')

        pdf.add_page()

        pdf.set_font('Times', '', 10.0)

        epw = pdf.w - 2 * pdf.l_margin

        col_width = epw / 9


        dat = ['??rea','Pasillo', 'Estanter??a','Columna','Nivel', 'C??digo', 'Descripci??n','Lote','Cantidad']
        data.append(dat)

        for x in tupla_pdf:
            data.append(x)


        th = pdf.font_size

        pdf.set_font('Times', 'B', 20.0)
        pdf.cell(epw, 0.0, 'Picking', align='C')
        pdf.set_font('Times', '', 10.5)
        pdf.ln(0.5)

        for row in data:
            print ("row, ",row)
            for datum in row:
                print("datum, ",datum)
                pdf.cell(col_width, 2 * th, str(datum), border=1)

            pdf.ln(2 * th)

        pdf.output('picking.pdf','F')




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
        self.cbox()
        global productId
        global codigoViejo
        global defaultImg
        producto = p.mostrar_product(productId)
        print(producto)
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

        area=atributos[4].split(sep="-")
        self.ui.estado_cbox.setCurrentText(str(area[0]))
        self.ui.ubicacion_cbox.setCurrentText(atributos[4])
        self.ui.peso_num.setValue(atributos[9])
        self.ui.num_volumen.setValue(atributos[10])
        self.ui.num_precio.setValue(atributos[11])

    def modificar_producto(self):
        global productId
        global codigoViejo
        global defaultImg
        cantidad_total = 0
        codigo = self.ui.codigo_input.text()
        descripcion = self.ui.descripcion_input.toPlainText()
        marca = self.ui.marca_input.text()
        ubicacion = self.ui.ubicacion_cbox.currentText()
        if self.ui.fragil_si.isChecked():
            fragil = "1"
        else:
            fragil = "0"

        peso = self.ui.peso_num.value()
        volumen = self.ui.num_volumen.value()
        precio = self.ui.num_precio.value()
        foto = defaultImg

        if p.ver_posicion(codigo)!=ubicacion or volumen!=p.ver_vol(codigo):
            a = conex.start_connection()
            cursor = a.cursor()
            query = "SELECT cantidad FROM lote WHERE idproducto=%s ORDER BY vencimiento"
            cursor.execute(query, codigoViejo)
            data = cursor.fetchall()
            data = data
            conex.close_connection(a)
            cantidad_total=0
            print(data)
            for x in data:
                cantidad_total = cantidad_total + x[0]
            al.modificar_dispo_egreso(codigo,cantidad_total)
            p.modificar_produc(codigoViejo, codigo, marca, descripcion, ubicacion, fragil, foto, peso,
                               volumen, precio)
            al.modificar_dispo_ingreso(codigo,cantidad_total)

        else:
            p.modificar_produc(codigoViejo, codigo, marca, descripcion, ubicacion, fragil, foto, peso,volumen, precio)
        self.close()
    def borrar_producto(self):
        global productId
        qm = QMessageBox

        ret = qm.warning(self, 'Esta acci??n es irreversible', "??Est??s seguro que quieres eliminar el producto?",
                         qm.Yes | qm.No)
        if ret == qm.Yes:
            p.borrar_producto(productId)
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
        posicion = self.ui.estado_cbox.currentText()
        pos = al.listar_alojamiento_disponibles_area(posicion)
        for p in pos:
            self.ui.ubicacion_cbox.addItem(p[0])

        self.ui.estado_cbox.currentIndexChanged.connect(self.clear_combo)
        self.ui.estado_cbox.currentIndexChanged.connect(self.update_combo)

    def update_combo(self):
        area_seleccionada = self.ui.estado_cbox.currentText()
        posiciones = al.listar_alojamiento_disponibles_area(area_seleccionada)
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

        # CAMBIAR BOT??N PARA QUE INFORME SI SE DA DE ALTA O NO

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
            QtWidgets.QMessageBox.critical(self, "Error", "Contrase??as diferentes")
            return None

        else:

            u.Usuarios.modificar_datos_user(DNI_Viejo, dni, nombre, apellido, tipo, puesto, nacimiento, mail, foto)
            loginDB.cambiar_contrasena(DNI_Viejo, dni, contrasena)

        self.close()

    def dar_baja_usuario(self):
        global DNI
        qm = QMessageBox

        ret = qm.warning(self, 'Advertencia', "??Est?? seguro que quieres dar de baja el usuario?", qm.Yes | qm.No)
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





if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    window = Modern(1,"nombre")
    window.show()
    window.ui.stackedWidget_main.setCurrentWidget(window.ui.page_inicio)
    window.ui.stackedWidget_3.setCurrentWidget(window.ui.user_subpage)

    sys.exit(app.exec())
