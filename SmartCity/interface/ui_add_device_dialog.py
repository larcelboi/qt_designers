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
        AddDeviceDialog.resize(400, 300)
        self.formLayout = QFormLayout(AddDeviceDialog)
        self.formLayout.setObjectName(u"formLayout")
        self.label_name = QLabel(AddDeviceDialog)
        self.label_name.setObjectName(u"label_name")

        self.formLayout.setWidget(0, QFormLayout.ItemRole.LabelRole, self.label_name)

        self.lineEdit_name = QLineEdit(AddDeviceDialog)
        self.lineEdit_name.setObjectName(u"lineEdit_name")

        self.formLayout.setWidget(0, QFormLayout.ItemRole.FieldRole, self.lineEdit_name)

        self.label_type = QLabel(AddDeviceDialog)
        self.label_type.setObjectName(u"label_type")

        self.formLayout.setWidget(1, QFormLayout.ItemRole.LabelRole, self.label_type)

        self.comboBox_type = QComboBox(AddDeviceDialog)
        self.comboBox_type.setObjectName(u"comboBox_type")

        self.formLayout.setWidget(1, QFormLayout.ItemRole.FieldRole, self.comboBox_type)

        self.btn_add = QPushButton(AddDeviceDialog)
        self.btn_add.setObjectName(u"btn_add")

        self.formLayout.setWidget(2, QFormLayout.ItemRole.FieldRole, self.btn_add)


        self.retranslateUi(AddDeviceDialog)

        QMetaObject.connectSlotsByName(AddDeviceDialog)
    # setupUi

    def retranslateUi(self, AddDeviceDialog):
        self.label_name.setText(QCoreApplication.translate("AddDeviceDialog", u"Device Name:", None))
        self.label_type.setText(QCoreApplication.translate("AddDeviceDialog", u"Device Type:", None))
        self.btn_add.setText(QCoreApplication.translate("AddDeviceDialog", u"Add Device", None))
        pass
    # retranslateUi

