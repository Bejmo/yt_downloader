# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'interface.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(539, 464)
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.URL = QtWidgets.QLabel(Form)
        self.URL.setObjectName("URL")
        self.horizontalLayout_5.addWidget(self.URL)
        self.URL_text = QtWidgets.QLineEdit(Form)
        self.URL_text.setObjectName("URL_text")
        self.horizontalLayout_5.addWidget(self.URL_text)
        self.verticalLayout.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.carpeta_descarga = QtWidgets.QLabel(Form)
        self.carpeta_descarga.setObjectName("carpeta_descarga")
        self.horizontalLayout_3.addWidget(self.carpeta_descarga)
        self.carpeta = QtWidgets.QLineEdit(Form)
        self.carpeta.setObjectName("carpeta")
        self.horizontalLayout_3.addWidget(self.carpeta)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.Enviar = QtWidgets.QPushButton(Form)
        self.Enviar.setObjectName("Enviar")
        self.horizontalLayout.addWidget(self.Enviar)
        self.Borrar = QtWidgets.QPushButton(Form)
        self.Borrar.setObjectName("Borrar")
        self.horizontalLayout.addWidget(self.Borrar)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.DescargarVideo = QtWidgets.QRadioButton(Form)
        self.DescargarVideo.setObjectName("DescargarVideo")
        self.verticalLayout_2.addWidget(self.DescargarVideo)
        self.DescargarPlaylist = QtWidgets.QRadioButton(Form)
        self.DescargarPlaylist.setObjectName("DescargarPlaylist")
        self.verticalLayout_2.addWidget(self.DescargarPlaylist)
        self.ActualizarPlaylist = QtWidgets.QRadioButton(Form)
        self.ActualizarPlaylist.setObjectName("ActualizarPlaylist")
        self.verticalLayout_2.addWidget(self.ActualizarPlaylist)
        self.horizontalLayout_4.addLayout(self.verticalLayout_2)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem1)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.lineEdit = QtWidgets.QLineEdit(Form)
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout_2.addWidget(self.lineEdit)
        self.Cambiar_root = QtWidgets.QPushButton(Form)
        self.Cambiar_root.setObjectName("Cambiar_root")
        self.horizontalLayout_2.addWidget(self.Cambiar_root)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.terminal = QtWidgets.QTextBrowser(Form)
        self.terminal.setObjectName("terminal")
        self.verticalLayout.addWidget(self.terminal)
        self.Clear = QtWidgets.QPushButton(Form)
        self.Clear.setObjectName("Clear")
        self.verticalLayout.addWidget(self.Clear)

        self.retranslateUi(Form)
        self.Clear.pressed.connect(self.terminal.clear) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.URL.setText(_translate("Form", "URL YouTube"))
        self.carpeta_descarga.setText(_translate("Form", "Carpeta Descarga"))
        self.Enviar.setText(_translate("Form", "Enviar"))
        self.Borrar.setText(_translate("Form", "Borrar"))
        self.DescargarVideo.setText(_translate("Form", "Descargar Vídeo"))
        self.DescargarPlaylist.setText(_translate("Form", "Descargar Playlist"))
        self.ActualizarPlaylist.setText(_translate("Form", "Actualizar Playlist"))
        self.Cambiar_root.setText(_translate("Form", "Cambiar Root"))
        self.Clear.setText(_translate("Form", "Clear"))
