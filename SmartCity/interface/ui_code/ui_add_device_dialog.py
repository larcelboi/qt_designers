# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'add_device_dialog.ui'
##
## Created by: Qt User Interface Compiler version 6.9.0
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
from PySide6.QtWidgets import (QApplication, QComboBox, QDialog, QFormLayout,
    QLabel, QLineEdit, QPushButton, QSizePolicy,
    QWidget)

class Ui_AddDeviceDialog(object):
    def setupUi(self, AddDeviceDialog):
        if not AddDeviceDialog.objectName():
            AddDeviceDialog.setObjectName(u"AddDeviceDialog")
        AddDeviceDialog.resize(500, 350)
        self.formLayout = QFormLayout(AddDeviceDialog)
        self.formLayout.setObjectName(u"formLayout")
        self.lbl_name = QLabel(AddDeviceDialog)
        self.lbl_name.setObjectName(u"lbl_name")

        self.formLayout.setWidget(0, QFormLayout.ItemRole.LabelRole, self.lbl_name)

        self.le_name = QLineEdit(AddDeviceDialog)
        self.le_name.setObjectName(u"le_name")

        self.formLayout.setWidget(0, QFormLayout.ItemRole.FieldRole, self.le_name)

        self.lbl_type = QLabel(AddDeviceDialog)
        self.lbl_type.setObjectName(u"lbl_type")

        self.formLayout.setWidget(1, QFormLayout.ItemRole.LabelRole, self.lbl_type)

        self.cb_type = QComboBox(AddDeviceDialog)
        self.cb_type.setObjectName(u"cb_type")

        self.formLayout.setWidget(1, QFormLayout.ItemRole.FieldRole, self.cb_type)

        self.lbl_energy = QLabel(AddDeviceDialog)
        self.lbl_energy.setObjectName(u"lbl_energy")

        self.formLayout.setWidget(2, QFormLayout.ItemRole.LabelRole, self.lbl_energy)

        self.le_energy = QLineEdit(AddDeviceDialog)
        self.le_energy.setObjectName(u"le_energy")

        self.formLayout.setWidget(2, QFormLayout.ItemRole.FieldRole, self.le_energy)

        self.lbl_status = QLabel(AddDeviceDialog)
        self.lbl_status.setObjectName(u"lbl_status")

        self.formLayout.setWidget(3, QFormLayout.ItemRole.LabelRole, self.lbl_status)

        self.cb_status = QComboBox(AddDeviceDialog)
        self.cb_status.addItem("")
        self.cb_status.addItem("")
        self.cb_status.setObjectName(u"cb_status")

        self.formLayout.setWidget(3, QFormLayout.ItemRole.FieldRole, self.cb_status)

        self.lbl_malfunction = QLabel(AddDeviceDialog)
        self.lbl_malfunction.setObjectName(u"lbl_malfunction")

        self.formLayout.setWidget(4, QFormLayout.ItemRole.LabelRole, self.lbl_malfunction)

        self.cb_malfunction = QComboBox(AddDeviceDialog)
        self.cb_malfunction.addItem("")
        self.cb_malfunction.addItem("")
        self.cb_malfunction.setObjectName(u"cb_malfunction")

        self.formLayout.setWidget(4, QFormLayout.ItemRole.FieldRole, self.cb_malfunction)

        self.lbl_district = QLabel(AddDeviceDialog)
        self.lbl_district.setObjectName(u"lbl_district")

        self.formLayout.setWidget(5, QFormLayout.ItemRole.LabelRole, self.lbl_district)

        self.cb_district = QComboBox(AddDeviceDialog)
        self.cb_district.setObjectName(u"cb_district")

        self.formLayout.setWidget(5, QFormLayout.ItemRole.FieldRole, self.cb_district)

        self.btn_add_device = QPushButton(AddDeviceDialog)
        self.btn_add_device.setObjectName(u"btn_add_device")

        self.formLayout.setWidget(6, QFormLayout.ItemRole.FieldRole, self.btn_add_device)


        self.retranslateUi(AddDeviceDialog)

        QMetaObject.connectSlotsByName(AddDeviceDialog)
    # setupUi

    def retranslateUi(self, AddDeviceDialog):
        self.lbl_name.setText(QCoreApplication.translate("AddDeviceDialog", u"Device Name:", None))
        self.lbl_type.setText(QCoreApplication.translate("AddDeviceDialog", u"Device Type:", None))
        self.lbl_energy.setText(QCoreApplication.translate("AddDeviceDialog", u"Energy Usage:", None))
        self.lbl_status.setText(QCoreApplication.translate("AddDeviceDialog", u"Status:", None))
        self.cb_status.setItemText(0, QCoreApplication.translate("AddDeviceDialog", u"ON", None))
        self.cb_status.setItemText(1, QCoreApplication.translate("AddDeviceDialog", u"OFF", None))

        self.lbl_malfunction.setText(QCoreApplication.translate("AddDeviceDialog", u"Malfunction:", None))
        self.cb_malfunction.setItemText(0, QCoreApplication.translate("AddDeviceDialog", u"False", None))
        self.cb_malfunction.setItemText(1, QCoreApplication.translate("AddDeviceDialog", u"True", None))

        self.lbl_district.setText(QCoreApplication.translate("AddDeviceDialog", u"Assign to District:", None))
        self.btn_add_device.setText(QCoreApplication.translate("AddDeviceDialog", u"Add Device", None))
        pass
    # retranslateUi

