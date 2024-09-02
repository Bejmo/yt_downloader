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
        Form.resize(620, 615)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_4.addWidget(self.label_2, 0, QtCore.Qt.AlignHCenter)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.url_tag = QtWidgets.QLabel(Form)
        self.url_tag.setObjectName("url_tag")
        self.verticalLayout_3.addWidget(self.url_tag, 0, QtCore.Qt.AlignHCenter)
        self.carpeta_descarga_tag = QtWidgets.QLabel(Form)
        self.carpeta_descarga_tag.setObjectName("carpeta_descarga_tag")
        self.verticalLayout_3.addWidget(self.carpeta_descarga_tag)
        self.horizontalLayout_3.addLayout(self.verticalLayout_3)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.url_line = QtWidgets.QLineEdit(Form)
        self.url_line.setObjectName("url_line")
        self.verticalLayout.addWidget(self.url_line)
        self.carpeta_line = QtWidgets.QLineEdit(Form)
        self.carpeta_line.setObjectName("carpeta_line")
        self.verticalLayout.addWidget(self.carpeta_line)
        self.horizontalLayout_3.addLayout(self.verticalLayout)
        self.horizontalLayout_5.addLayout(self.horizontalLayout_3)
        self.MP3 = QtWidgets.QComboBox(Form)
        self.MP3.setMinimumSize(QtCore.QSize(50, 50))
        self.MP3.setObjectName("MP3")
        self.MP3.addItem("")
        self.MP3.addItem("")
        self.horizontalLayout_5.addWidget(self.MP3)
        self.borrar_button = QtWidgets.QPushButton(Form)
        self.borrar_button.setMinimumSize(QtCore.QSize(0, 50))
        self.borrar_button.setObjectName("borrar_button")
        self.horizontalLayout_5.addWidget(self.borrar_button)
        self.verticalLayout_4.addLayout(self.horizontalLayout_5)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.descargar_button = QtWidgets.QPushButton(Form)
        self.descargar_button.setObjectName("descargar_button")
        self.horizontalLayout.addWidget(self.descargar_button)
        self.verticalLayout_4.addLayout(self.horizontalLayout)
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
        self.actualizar_playlist_radio_button.setToolTipDuration(-1)
        self.actualizar_playlist_radio_button.setObjectName("actualizar_playlist_radio_button")
        self.verticalLayout_2.addWidget(self.actualizar_playlist_radio_button)
        self.horizontalLayout_4.addLayout(self.verticalLayout_2)
        self.download_whole_playlist = QtWidgets.QCheckBox(Form)
        self.download_whole_playlist.setEnabled(True)
        self.download_whole_playlist.setAcceptDrops(False)
        self.download_whole_playlist.setChecked(True)
        self.download_whole_playlist.setObjectName("download_whole_playlist")
        self.horizontalLayout_4.addWidget(self.download_whole_playlist)
        self.numero_descargas = QtWidgets.QSpinBox(Form)
        self.numero_descargas.setEnabled(False)
        self.numero_descargas.setWrapping(False)
        self.numero_descargas.setProperty("showGroupSeparator", False)
        self.numero_descargas.setMaximum(999)
        self.numero_descargas.setObjectName("numero_descargas")
        self.horizontalLayout_4.addWidget(self.numero_descargas, 0, QtCore.Qt.AlignRight)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem1)
        self.verticalLayout_4.addLayout(self.horizontalLayout_4)
        self.mejorar_nombres = QtWidgets.QCheckBox(Form)
        self.mejorar_nombres.setChecked(True)
        self.mejorar_nombres.setObjectName("mejorar_nombres")
        self.verticalLayout_4.addWidget(self.mejorar_nombres, 0, QtCore.Qt.AlignHCenter)
        spacerItem2 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacerItem2)
        self.label = QtWidgets.QLabel(Form)
        self.label.setObjectName("label")
        self.verticalLayout_4.addWidget(self.label, 0, QtCore.Qt.AlignHCenter)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.verticalLayout_4.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.modificar_root_line = QtWidgets.QLineEdit(Form)
        self.modificar_root_line.setObjectName("modificar_root_line")
        self.horizontalLayout_2.addWidget(self.modificar_root_line)
        self.modificar_root_button = QtWidgets.QPushButton(Form)
        self.modificar_root_button.setMinimumSize(QtCore.QSize(120, 23))
        self.modificar_root_button.setObjectName("modificar_root_button")
        self.horizontalLayout_2.addWidget(self.modificar_root_button)
        self.set_default_root_button = QtWidgets.QPushButton(Form)
        self.set_default_root_button.setObjectName("set_default_root_button")
        self.horizontalLayout_2.addWidget(self.set_default_root_button)
        self.verticalLayout_4.addLayout(self.horizontalLayout_2)
        self.imprimir_root_actual_button = QtWidgets.QPushButton(Form)
        self.imprimir_root_actual_button.setObjectName("imprimir_root_actual_button")
        self.verticalLayout_4.addWidget(self.imprimir_root_actual_button)
        spacerItem3 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacerItem3)
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_4.addWidget(self.label_3, 0, QtCore.Qt.AlignHCenter)
        self.usage_button = QtWidgets.QPushButton(Form)
        self.usage_button.setObjectName("usage_button")
        self.verticalLayout_4.addWidget(self.usage_button)
        self.terminal = QtWidgets.QTextBrowser(Form)
        self.terminal.setMinimumSize(QtCore.QSize(0, 0))
        self.terminal.setObjectName("terminal")
        self.verticalLayout_4.addWidget(self.terminal)
        self.clear_button = QtWidgets.QPushButton(Form)
        self.clear_button.setObjectName("clear_button")
        self.verticalLayout_4.addWidget(self.clear_button)

        self.retranslateUi(Form)
        self.clear_button.pressed.connect(self.terminal.clear) # type: ignore
        self.borrar_button.pressed.connect(self.url_line.clear) # type: ignore
        self.borrar_button.pressed.connect(self.carpeta_line.clear) # type: ignore
        self.descargar_playlist_radio_button.toggled['bool'].connect(self.download_whole_playlist.setVisible) # type: ignore
        self.descargar_playlist_radio_button.toggled['bool'].connect(self.numero_descargas.setVisible) # type: ignore
        self.download_whole_playlist.toggled['bool'].connect(self.numero_descargas.setDisabled) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label_2.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">DESCARGAR</span></p></body></html>"))
        self.url_tag.setText(_translate("Form", "URL YouTube"))
        self.carpeta_descarga_tag.setText(_translate("Form", "Carpeta de Descarga"))
        self.carpeta_line.setToolTip(_translate("Form", "<html><head/><body><p>Carpeta de descarga dentro del ROOT.</p></body></html>"))
        self.MP3.setItemText(0, _translate("Form", "MP3"))
        self.MP3.setItemText(1, _translate("Form", "MP4"))
        self.borrar_button.setText(_translate("Form", "BORRAR"))
        self.descargar_button.setText(_translate("Form", "DESCARGAR"))
        self.descargar_video_radio_button.setToolTip(_translate("Form", "<html><head/><body><p>Descarga el audio del vídeo de la &quot;URL YouTube&quot; y lo guarda en &quot;Carpeta Descarga&quot;, dentro del root.</p></body></html>"))
        self.descargar_video_radio_button.setText(_translate("Form", "DESCARGAR VÍDEO"))
        self.descargar_playlist_radio_button.setToolTip(_translate("Form", "<html><head/><body><p>Descarga la playlist de la &quot;URL YouTube&quot; y lo guarda en &quot;Carpeta Descarga&quot;, dentro del root.</p></body></html>"))
        self.descargar_playlist_radio_button.setText(_translate("Form", "DESCARGAR PLAYLIST"))
        self.actualizar_playlist_radio_button.setToolTip(_translate("Form", "<html><head/><body><p>Actualiza la playlist que está en la &quot;Carpeta Descarga&quot; y le añade las canciones que no tiene de la &quot;URL YouTube&quot;.</p><p>ATENCIÓN: Solo funciona si la playlist de YouTube está ordenada con los vídeos recientemente añadidos primero.</p></body></html>"))
        self.actualizar_playlist_radio_button.setText(_translate("Form", "ACTUALIZAR PLAYLIST"))
        self.download_whole_playlist.setToolTip(_translate("Form", "<html><head/><body><p>Descargar toda la playlist.</p></body></html>"))
        self.download_whole_playlist.setText(_translate("Form", "TODA LA PLAYLIST"))
        self.numero_descargas.setToolTip(_translate("Form", "<html><head/><body><p>Número de vídeos que se quieren descargar.</p></body></html>"))
        self.mejorar_nombres.setToolTip(_translate("Form", "<html><head/><body><p>Mejora el nombre de los archivos descargados, dándoles el siguiente formato:</p><p>AUTOR + TÍTULO CANCIÓN</p></body></html>"))
        self.mejorar_nombres.setText(_translate("Form", "MEJORAR NOMBRES"))
        self.label.setToolTip(_translate("Form", "<html><head/><body><p>El &quot;ROOT&quot; es el directorio en el que se guardan las descargas.</p></body></html>"))
        self.label.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">MODIFICAR ROOT</span></p></body></html>"))
        self.modificar_root_button.setText(_translate("Form", "MODIFICAR ROOT"))
        self.set_default_root_button.setText(_translate("Form", "SET DEFAULT ROOT"))
        self.imprimir_root_actual_button.setText(_translate("Form", "IMPRIMIR ROOT ACTUAL"))
        self.label_3.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">IMPRIMIR</span></p></body></html>"))
        self.usage_button.setToolTip(_translate("Form", "<html><head/><body><p>Imprime cómo funciona el programa.</p></body></html>"))
        self.usage_button.setText(_translate("Form", "USAGE"))
        self.clear_button.setText(_translate("Form", "CLEAR"))
