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
        Form.resize(571, 674)
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.url_tag = QtWidgets.QLabel(Form)
        self.url_tag.setObjectName("url_tag")
        self.horizontalLayout_5.addWidget(self.url_tag)
        self.url_line = QtWidgets.QLineEdit(Form)
        self.url_line.setObjectName("url_line")
        self.horizontalLayout_5.addWidget(self.url_line)
        self.verticalLayout.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.carpeta_descarga_tag = QtWidgets.QLabel(Form)
        self.carpeta_descarga_tag.setObjectName("carpeta_descarga_tag")
        self.horizontalLayout_3.addWidget(self.carpeta_descarga_tag)
        self.carpeta_line = QtWidgets.QLineEdit(Form)
        self.carpeta_line.setObjectName("carpeta_line")
        self.horizontalLayout_3.addWidget(self.carpeta_line)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.enviar_button = QtWidgets.QPushButton(Form)
        self.enviar_button.setObjectName("enviar_button")
        self.horizontalLayout.addWidget(self.enviar_button)
        self.borrar_button = QtWidgets.QPushButton(Form)
        self.borrar_button.setObjectName("borrar_button")
        self.horizontalLayout.addWidget(self.borrar_button)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.descargar_video_radio_button = QtWidgets.QRadioButton(Form)
        self.descargar_video_radio_button.setObjectName("descargar_video_radio_button")
        self.verticalLayout_2.addWidget(self.descargar_video_radio_button)
        self.descargar_playlist_radio_button = QtWidgets.QRadioButton(Form)
        self.descargar_playlist_radio_button.setObjectName("descargar_playlist_radio_button")
        self.verticalLayout_2.addWidget(self.descargar_playlist_radio_button)
        self.actualizar_playlist_radio_button = QtWidgets.QRadioButton(Form)
        self.actualizar_playlist_radio_button.setObjectName("actualizar_playlist_radio_button")
        self.verticalLayout_2.addWidget(self.actualizar_playlist_radio_button)
        self.horizontalLayout_4.addLayout(self.verticalLayout_2)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem1)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        spacerItem2 = QtWidgets.QSpacerItem(20, 39, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem2)
        self.set_default_root = QtWidgets.QPushButton(Form)
        self.set_default_root.setObjectName("set_default_root")
        self.verticalLayout.addWidget(self.set_default_root)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.cambiar_root_line = QtWidgets.QLineEdit(Form)
        self.cambiar_root_line.setObjectName("cambiar_root_line")
        self.horizontalLayout_2.addWidget(self.cambiar_root_line)
        self.cambiar_root_button = QtWidgets.QPushButton(Form)
        self.cambiar_root_button.setObjectName("cambiar_root_button")
        self.horizontalLayout_2.addWidget(self.cambiar_root_button)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        spacerItem3 = QtWidgets.QSpacerItem(20, 38, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem3)
        self.terminal = QtWidgets.QTextBrowser(Form)
        self.terminal.setObjectName("terminal")
        self.verticalLayout.addWidget(self.terminal)
        self.clear_button = QtWidgets.QPushButton(Form)
        self.clear_button.setObjectName("clear_button")
        self.verticalLayout.addWidget(self.clear_button)

        self.retranslateUi(Form)
        self.clear_button.pressed.connect(self.terminal.clear) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.url_tag.setText(_translate("Form", "URL YouTube"))
        self.carpeta_descarga_tag.setText(_translate("Form", "Carpeta Descarga"))
        self.enviar_button.setText(_translate("Form", "Enviar"))
        self.borrar_button.setText(_translate("Form", "Borrar"))
        self.descargar_video_radio_button.setText(_translate("Form", "Descargar Vídeo"))
        self.descargar_playlist_radio_button.setText(_translate("Form", "Descargar Playlist"))
        self.actualizar_playlist_radio_button.setText(_translate("Form", "Actualizar Playlist"))
        self.set_default_root.setText(_translate("Form", "Set Default Root"))
        self.cambiar_root_button.setText(_translate("Form", "Cambiar Root"))
        self.clear_button.setText(_translate("Form", "Clear"))
