# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'vtn_principal.ui'
##
## Created by: Qt User Interface Compiler version 6.5.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QLabel, QLineEdit,
    QMainWindow, QMenuBar, QPushButton, QSizePolicy,
    QSpinBox, QStatusBar, QWidget)

class Ui_vtn_principal(object):
    def setupUi(self, vtn_principal):
        if not vtn_principal.objectName():
            vtn_principal.setObjectName(u"vtn_principal")
        vtn_principal.resize(448, 454)
        self.centralwidget = QWidget(vtn_principal)
        self.centralwidget.setObjectName(u"centralwidget")
        self.line_nombre = QLineEdit(self.centralwidget)
        self.line_nombre.setObjectName(u"line_nombre")
        self.line_nombre.setGeometry(QRect(190, 80, 113, 20))
        self.line_nombre.setMaxLength(50)
        self.line_apellido = QLineEdit(self.centralwidget)
        self.line_apellido.setObjectName(u"line_apellido")
        self.line_apellido.setGeometry(QRect(190, 110, 113, 20))
        self.line_apellido.setMaxLength(50)
        self.lbl_Nombre = QLabel(self.centralwidget)
        self.lbl_Nombre.setObjectName(u"lbl_Nombre")
        self.lbl_Nombre.setGeometry(QRect(60, 80, 51, 16))
        self.lbl_Apellido = QLabel(self.centralwidget)
        self.lbl_Apellido.setObjectName(u"lbl_Apellido")
        self.lbl_Apellido.setGeometry(QRect(60, 110, 51, 16))
        self.pBtton_Grabar = QPushButton(self.centralwidget)
        self.pBtton_Grabar.setObjectName(u"pBtton_Grabar")
        self.pBtton_Grabar.setGeometry(QRect(190, 370, 75, 23))
        self.cb_tipo_persona = QComboBox(self.centralwidget)
        self.cb_tipo_persona.addItem("")
        self.cb_tipo_persona.addItem("")
        self.cb_tipo_persona.setObjectName(u"cb_tipo_persona")
        self.cb_tipo_persona.setGeometry(QRect(190, 20, 121, 21))
        self.lbl_tipo_persona = QLabel(self.centralwidget)
        self.lbl_tipo_persona.setObjectName(u"lbl_tipo_persona")
        self.lbl_tipo_persona.setGeometry(QRect(130, 20, 51, 16))
        self.lbl_cedula = QLabel(self.centralwidget)
        self.lbl_cedula.setObjectName(u"lbl_cedula")
        self.lbl_cedula.setGeometry(QRect(60, 140, 51, 16))
        self.lbl_correo = QLabel(self.centralwidget)
        self.lbl_correo.setObjectName(u"lbl_correo")
        self.lbl_correo.setGeometry(QRect(60, 170, 51, 16))
        self.line_cedula = QLineEdit(self.centralwidget)
        self.line_cedula.setObjectName(u"line_cedula")
        self.line_cedula.setGeometry(QRect(190, 140, 113, 20))
        self.line_cedula.setMaxLength(10)
        self.line_email = QLineEdit(self.centralwidget)
        self.line_email.setObjectName(u"line_email")
        self.line_email.setGeometry(QRect(190, 170, 113, 20))
        self.line_email.setMaxLength(100)
        self.pBtton_buscar_cedula = QPushButton(self.centralwidget)
        self.pBtton_buscar_cedula.setObjectName(u"pBtton_buscar_cedula")
        self.pBtton_buscar_cedula.setGeometry(QRect(320, 140, 111, 21))
        self.lbl_estatura = QLabel(self.centralwidget)
        self.lbl_estatura.setObjectName(u"lbl_estatura")
        self.lbl_estatura.setGeometry(QRect(60, 290, 71, 20))
        self.sp_estatura = QSpinBox(self.centralwidget)
        self.sp_estatura.setObjectName(u"sp_estatura")
        self.sp_estatura.setGeometry(QRect(190, 290, 42, 22))
        self.sp_estatura.setMaximum(300)
        self.line_Fnacimiento = QLineEdit(self.centralwidget)
        self.line_Fnacimiento.setObjectName(u"line_Fnacimiento")
        self.line_Fnacimiento.setGeometry(QRect(190, 210, 113, 20))
        self.line_Fnacimiento.setMaxLength(100)
        self.line_peso = QLineEdit(self.centralwidget)
        self.line_peso.setObjectName(u"line_peso")
        self.line_peso.setGeometry(QRect(190, 250, 61, 20))
        self.line_peso.setMaxLength(100)
        self.lbl_Fnacimiento = QLabel(self.centralwidget)
        self.lbl_Fnacimiento.setObjectName(u"lbl_Fnacimiento")
        self.lbl_Fnacimiento.setGeometry(QRect(60, 210, 101, 20))
        self.lbl_peso = QLabel(self.centralwidget)
        self.lbl_peso.setObjectName(u"lbl_peso")
        self.lbl_peso.setGeometry(QRect(60, 250, 51, 16))
        self.pBtton_peso = QPushButton(self.centralwidget)
        self.pBtton_peso.setObjectName(u"pBtton_peso")
        self.pBtton_peso.setGeometry(QRect(260, 250, 81, 21))
        self.pBtton_estatura = QPushButton(self.centralwidget)
        self.pBtton_estatura.setObjectName(u"pBtton_estatura")
        self.pBtton_estatura.setGeometry(QRect(260, 290, 101, 21))
        self.pBtton_edad = QPushButton(self.centralwidget)
        self.pBtton_edad.setObjectName(u"pBtton_edad")
        self.pBtton_edad.setGeometry(QRect(310, 210, 51, 21))
        vtn_principal.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(vtn_principal)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 448, 21))
        vtn_principal.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(vtn_principal)
        self.statusbar.setObjectName(u"statusbar")
        vtn_principal.setStatusBar(self.statusbar)

        self.retranslateUi(vtn_principal)

        QMetaObject.connectSlotsByName(vtn_principal)
    # setupUi

    def retranslateUi(self, vtn_principal):
        vtn_principal.setWindowTitle(QCoreApplication.translate("vtn_principal", u"vtn_principal", None))
        self.lbl_Nombre.setText(QCoreApplication.translate("vtn_principal", u"Nombre", None))
        self.lbl_Apellido.setText(QCoreApplication.translate("vtn_principal", u"Apellido", None))
        self.pBtton_Grabar.setText(QCoreApplication.translate("vtn_principal", u"Grabar", None))
        self.cb_tipo_persona.setItemText(0, QCoreApplication.translate("vtn_principal", u"Docente", None))
        self.cb_tipo_persona.setItemText(1, QCoreApplication.translate("vtn_principal", u"Estudiante", None))

        self.lbl_tipo_persona.setText(QCoreApplication.translate("vtn_principal", u"Tipo", None))
        self.lbl_cedula.setText(QCoreApplication.translate("vtn_principal", u"Cedula", None))
        self.lbl_correo.setText(QCoreApplication.translate("vtn_principal", u"Email", None))
        self.pBtton_buscar_cedula.setText(QCoreApplication.translate("vtn_principal", u"Buscar por Cedula", None))
        self.lbl_estatura.setText(QCoreApplication.translate("vtn_principal", u"Estatura (cm)", None))
        self.lbl_Fnacimiento.setText(QCoreApplication.translate("vtn_principal", u"Fecha de Nacimiento", None))
        self.lbl_peso.setText(QCoreApplication.translate("vtn_principal", u"Peso (kg)", None))
        self.pBtton_peso.setText(QCoreApplication.translate("vtn_principal", u"Calculos Peso", None))
        self.pBtton_estatura.setText(QCoreApplication.translate("vtn_principal", u"Calculos Estatura", None))
        self.pBtton_edad.setText(QCoreApplication.translate("vtn_principal", u"Edad", None))
    # retranslateUi

