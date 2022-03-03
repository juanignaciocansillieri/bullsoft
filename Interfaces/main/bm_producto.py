# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'bm_producto_ui.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(678, 578)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setMinimumSize(QtCore.QSize(0, 0))
        self.frame.setMaximumSize(QtCore.QSize(16777215, 209))
        self.frame.setStyleSheet("background: #f5f5f5;\n"
"")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(210, 10, 231, 191))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap(":/cct/Alimento.png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.frame)
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setMinimumSize(QtCore.QSize(0, 300))
        self.frame_2.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.frame_2.setStyleSheet("background: #f5f5f5;\n"
"")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.modificarprod_btn = QtWidgets.QPushButton(self.frame_2)
        self.modificarprod_btn.setGeometry(QtCore.QRect(380, 320, 121, 26))
        font = QtGui.QFont()
        font.setFamily("Cairo")
        font.setBold(True)
        font.setWeight(75)
        self.modificarprod_btn.setFont(font)
        self.modificarprod_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.modificarprod_btn.setStyleSheet("QPushButton{\n"
"background-color: #055ffc;\n"
"color:#fff;\n"
"border-radius: 5px;\n"
"text-align:center;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"\n"
"}")
        self.modificarprod_btn.setObjectName("modificarprod_btn")
        self.eliminarprod_btn = QtWidgets.QPushButton(self.frame_2)
        self.eliminarprod_btn.setGeometry(QtCore.QRect(520, 320, 121, 26))
        font = QtGui.QFont()
        font.setFamily("Cairo")
        font.setBold(True)
        font.setWeight(75)
        self.eliminarprod_btn.setFont(font)
        self.eliminarprod_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.eliminarprod_btn.setStyleSheet("QPushButton{\n"
"background-color: #055ffc;\n"
"color:#fff;\n"
"border-radius: 5px;\n"
"text-align:center;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"\n"
"}")
        self.eliminarprod_btn.setObjectName("eliminarprod_btn")
        self.codigo_label = QtWidgets.QLabel(self.frame_2)
        self.codigo_label.setGeometry(QtCore.QRect(51, 30, 91, 27))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(-1)
        self.codigo_label.setFont(font)
        self.codigo_label.setStyleSheet("font-family: Roboto;\n"
"font-size: 14px;\n"
"margin-top:10px;\n"
"margin-left:10px\n"
"\n"
"")
        self.codigo_label.setObjectName("codigo_label")
        self.ubicacion_label = QtWidgets.QLabel(self.frame_2)
        self.ubicacion_label.setGeometry(QtCore.QRect(460, 150, 171, 27))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(-1)
        self.ubicacion_label.setFont(font)
        self.ubicacion_label.setStyleSheet("font-family: Roboto;\n"
"font-size: 14px;\n"
"margin-top:10px;\n"
"margin-left:10px\n"
"\n"
"")
        self.ubicacion_label.setObjectName("ubicacion_label")
        self.descripcion_input = QtWidgets.QTextEdit(self.frame_2)
        self.descripcion_input.setGeometry(QtCore.QRect(51, 120, 170, 85))
        self.descripcion_input.setStyleSheet("border: 1px solid #b8b9bd ;\n"
"border-radius: 3px;\n"
"padding: 4 5px;\n"
"color: #e9e9;\n"
"font-family:Roboto;\n"
"font-size:13px;\n"
"font-weight: 400;\n"
"margin-left: 10px;\n"
"")
        self.descripcion_input.setObjectName("descripcion_input")
        self.estado_cbox = QtWidgets.QComboBox(self.frame_2)
        self.estado_cbox.setGeometry(QtCore.QRect(460, 120, 171, 25))
        self.estado_cbox.setStyleSheet("border: 1px solid #b8b9bd ;\n"
"border-radius: 3px;\n"
"padding: 4 5px;\n"
"color: rgb(0, 0, 0);\n"
"font-family:Roboto;\n"
"font-size:13px;\n"
"font-weight: 400;\n"
"margin-left: 10px;\n"
"")
        self.estado_cbox.setCurrentText("")
        self.estado_cbox.setMaxVisibleItems(10)
        self.estado_cbox.setMaxCount(10)
        self.estado_cbox.setInsertPolicy(QtWidgets.QComboBox.InsertAfterCurrent)
        self.estado_cbox.setIconSize(QtCore.QSize(16, 0))
        self.estado_cbox.setDuplicatesEnabled(False)
        self.estado_cbox.setFrame(False)
        self.estado_cbox.setObjectName("estado_cbox")
        self.label_lote_2 = QtWidgets.QLabel(self.frame_2)
        self.label_lote_2.setGeometry(QtCore.QRect(251, 30, 154, 27))
        self.label_lote_2.setMaximumSize(QtCore.QSize(154, 16777215))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(-1)
        self.label_lote_2.setFont(font)
        self.label_lote_2.setStyleSheet("font-family: Roboto;\n"
"font-size: 14px;\n"
"margin-top:10px;\n"
"margin-left:10px\n"
"\n"
"")
        self.label_lote_2.setObjectName("label_lote_2")
        self.estado_label = QtWidgets.QLabel(self.frame_2)
        self.estado_label.setGeometry(QtCore.QRect(460, 90, 57, 27))
        self.estado_label.setMaximumSize(QtCore.QSize(75, 16777215))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(-1)
        self.estado_label.setFont(font)
        self.estado_label.setStyleSheet("font-family: Roboto;\n"
"font-size: 14px;\n"
"margin-top:10px;\n"
"margin-left:10px\n"
"\n"
"")
        self.estado_label.setObjectName("estado_label")
        self.peso_label = QtWidgets.QLabel(self.frame_2)
        self.peso_label.setGeometry(QtCore.QRect(251, 90, 71, 27))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(-1)
        self.peso_label.setFont(font)
        self.peso_label.setStyleSheet("font-family: Roboto;\n"
"font-size: 14px;\n"
"margin-top:10px;\n"
"margin-left:10px\n"
"\n"
"")
        self.peso_label.setObjectName("peso_label")
        self.marca_label = QtWidgets.QLabel(self.frame_2)
        self.marca_label.setGeometry(QtCore.QRect(251, 150, 57, 27))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(-1)
        self.marca_label.setFont(font)
        self.marca_label.setStyleSheet("font-family: Roboto;\n"
"font-size: 14px;\n"
"margin-top:10px;\n"
"margin-left:10px\n"
"\n"
"")
        self.marca_label.setObjectName("marca_label")
        self.codigo_input = QtWidgets.QLineEdit(self.frame_2)
        self.codigo_input.setGeometry(QtCore.QRect(50, 60, 170, 25))
        self.codigo_input.setMinimumSize(QtCore.QSize(0, 0))
        self.codigo_input.setMaximumSize(QtCore.QSize(16777215, 25))
        self.codigo_input.setStyleSheet("QLineEdit{\n"
"border: 1px solid #b8b9bd;\n"
"border-radius: 3px;\n"
"padding: 4 5px;\n"
"color: #e9e9;\n"
"font-family:Roboto;\n"
"font-size:13px;\n"
"font-weight: 400;\n"
"margin-left: 10px;\n"
"\n"
"}")
        self.codigo_input.setText("")
        self.codigo_input.setPlaceholderText("")
        self.codigo_input.setObjectName("codigo_input")
        self.subirFoto_btn = QtWidgets.QPushButton(self.frame_2)
        self.subirFoto_btn.setGeometry(QtCore.QRect(471, 240, 160, 25))
        self.subirFoto_btn.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily("Cairo")
        font.setBold(True)
        font.setWeight(75)
        self.subirFoto_btn.setFont(font)
        self.subirFoto_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.subirFoto_btn.setStyleSheet("QPushButton{\n"
"background-color: #055ffc;\n"
"color:#fff;\n"
"border-radius: 5px;\n"
"text-align:center;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"\n"
"}")
        self.subirFoto_btn.setObjectName("subirFoto_btn")
        self.peso_num = QtWidgets.QSpinBox(self.frame_2)
        self.peso_num.setGeometry(QtCore.QRect(251, 120, 170, 25))
        self.peso_num.setStyleSheet("border-radius: 3px;\n"
"padding: 4 5px;\n"
"color: rgb(0, 0, 0);\n"
"font-family:Roboto;\n"
"border: none;\n"
"font-size:13px;\n"
"font-weight: 400;\n"
"margin-left: 10px;\n"
"border: 1px solid #b8b9bd ;\n"
"")
        self.peso_num.setMaximum(9999)
        self.peso_num.setObjectName("peso_num")
        self.ubicacion_cbox = QtWidgets.QComboBox(self.frame_2)
        self.ubicacion_cbox.setGeometry(QtCore.QRect(461, 180, 171, 25))
        self.ubicacion_cbox.setStyleSheet("border: 1px solid #b8b9bd ;\n"
"border-radius: 3px;\n"
"padding: 4 5px;\n"
"color: rgb(0, 0, 0);\n"
"font-family:Roboto;\n"
"font-size:13px;\n"
"font-weight: 400;\n"
"margin-left: 10px;\n"
"")
        self.ubicacion_cbox.setCurrentText("")
        self.ubicacion_cbox.setMaxVisibleItems(10)
        self.ubicacion_cbox.setMaxCount(10)
        self.ubicacion_cbox.setInsertPolicy(QtWidgets.QComboBox.InsertAfterCurrent)
        self.ubicacion_cbox.setIconSize(QtCore.QSize(16, 0))
        self.ubicacion_cbox.setDuplicatesEnabled(False)
        self.ubicacion_cbox.setFrame(False)
        self.ubicacion_cbox.setObjectName("ubicacion_cbox")
        self.fragil_label = QtWidgets.QLabel(self.frame_2)
        self.fragil_label.setGeometry(QtCore.QRect(460, 30, 56, 27))
        self.fragil_label.setMaximumSize(QtCore.QSize(75, 16777215))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(-1)
        self.fragil_label.setFont(font)
        self.fragil_label.setStyleSheet("font-family: Roboto;\n"
"font-size: 14px;\n"
"margin-top:10px;\n"
"margin-left:10px\n"
"\n"
"")
        self.fragil_label.setObjectName("fragil_label")
        self.marca_input = QtWidgets.QLineEdit(self.frame_2)
        self.marca_input.setGeometry(QtCore.QRect(251, 180, 170, 25))
        self.marca_input.setMinimumSize(QtCore.QSize(0, 0))
        self.marca_input.setMaximumSize(QtCore.QSize(16777215, 25))
        self.marca_input.setStyleSheet("QLineEdit{\n"
"border: 1px solid #b8b9bd ;\n"
"border-radius: 3px;\n"
"padding: 4 5px;\n"
"color: #e9e9;\n"
"font-family:Roboto;\n"
"font-size:13px;\n"
"font-weight: 400;\n"
"margin-left: 10px;\n"
"\n"
"}")
        self.marca_input.setPlaceholderText("")
        self.marca_input.setObjectName("marca_input")
        self.descripcion_label = QtWidgets.QLabel(self.frame_2)
        self.descripcion_label.setGeometry(QtCore.QRect(51, 90, 99, 27))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(-1)
        self.descripcion_label.setFont(font)
        self.descripcion_label.setStyleSheet("font-family: Roboto;\n"
"font-size: 14px;\n"
"margin-top:10px;\n"
"margin-left:10px\n"
"\n"
"")
        self.descripcion_label.setObjectName("descripcion_label")
        self.fragil_si = QtWidgets.QRadioButton(self.frame_2)
        self.fragil_si.setGeometry(QtCore.QRect(473, 50, 41, 31))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(-1)
        font.setBold(False)
        font.setWeight(50)
        self.fragil_si.setFont(font)
        self.fragil_si.setStyleSheet("QRadioButton{\n"
"border-radius: 3px;\n"
"font-family: Roboto;\n"
"font-size: 12px;\n"
"border: none;\n"
"font-weight: 400;\n"
"margin-top:15px\n"
"}\n"
"")
        self.fragil_si.setObjectName("fragil_si")
        self.num_volumen = QtWidgets.QSpinBox(self.frame_2)
        self.num_volumen.setGeometry(QtCore.QRect(251, 60, 170, 25))
        self.num_volumen.setStyleSheet("border-radius: 3px;\n"
"padding: 4 5px;\n"
"color: rgb(0, 0, 0);\n"
"font-family:Roboto;\n"
"border: 1px solid #b8b9bd;font-size:13px;\n"
"font-weight: 400;\n"
"margin-left: 10px;\n"
"")
        self.num_volumen.setMinimum(0)
        self.num_volumen.setMaximum(9999)
        self.num_volumen.setObjectName("num_volumen")
        self.fragil_no = QtWidgets.QRadioButton(self.frame_2)
        self.fragil_no.setGeometry(QtCore.QRect(520, 50, 41, 31))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(-1)
        font.setBold(False)
        font.setWeight(50)
        self.fragil_no.setFont(font)
        self.fragil_no.setStyleSheet("QRadioButton{\n"
"border-radius: 3px;\n"
"font-family: Roboto;\n"
"font-size: 12px;\n"
"border: none;\n"
"font-weight: 400;\n"
"margin-top:15px\n"
"}\n"
"")
        self.fragil_no.setObjectName("fragil_no")
        self.num_precio = QtWidgets.QSpinBox(self.frame_2)
        self.num_precio.setGeometry(QtCore.QRect(250, 240, 170, 25))
        self.num_precio.setStyleSheet("border-radius: 3px;\n"
"padding: 4 5px;\n"
"color: rgb(0, 0, 0);\n"
"font-family:Roboto;\n"
"border: none;\n"
"font-size:13px;\n"
"font-weight: 400;\n"
"margin-left: 10px;\n"
"border: 1px solid #b8b9bd ;\n"
"")
        self.num_precio.setMaximum(9999)
        self.num_precio.setObjectName("num_precio")
        self.peso_label_2 = QtWidgets.QLabel(self.frame_2)
        self.peso_label_2.setGeometry(QtCore.QRect(250, 210, 71, 27))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(-1)
        self.peso_label_2.setFont(font)
        self.peso_label_2.setStyleSheet("font-family: Roboto;\n"
"font-size: 14px;\n"
"margin-top:10px;\n"
"margin-left:10px\n"
"\n"
"")
        self.peso_label_2.setObjectName("peso_label_2")
        self.verticalLayout.addWidget(self.frame_2)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.estado_cbox.setCurrentIndex(-1)
        self.ubicacion_cbox.setCurrentIndex(-1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Producto"))
        self.modificarprod_btn.setText(_translate("MainWindow", "Modificar Producto"))
        self.eliminarprod_btn.setText(_translate("MainWindow", "Eliminar Producto"))
        self.codigo_label.setText(_translate("MainWindow", "Código EAN"))
        self.ubicacion_label.setText(_translate("MainWindow", "Posición de alojamiento"))
        self.label_lote_2.setText(_translate("MainWindow", "Volumen"))
        self.estado_label.setText(_translate("MainWindow", "Área"))
        self.peso_label.setText(_translate("MainWindow", "Peso (gr)"))
        self.marca_label.setText(_translate("MainWindow", "Marca"))
        self.subirFoto_btn.setText(_translate("MainWindow", "Actualizar Imagen"))
        self.fragil_label.setText(_translate("MainWindow", "Fragil"))
        self.descripcion_label.setText(_translate("MainWindow", "Descripción"))
        self.fragil_si.setText(_translate("MainWindow", "Si"))
        self.fragil_no.setText(_translate("MainWindow", "No"))
        self.peso_label_2.setText(_translate("MainWindow", "Precio"))
import img_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
