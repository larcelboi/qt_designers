# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'malfunction_dialog.ui'
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
    QLabel, QPushButton, QSizePolicy, QTextEdit,
    QWidget)

class Ui_MalfunctionDialog(object):
    def setupUi(self, MalfunctionDialog):
        if not MalfunctionDialog.objectName():
            MalfunctionDialog.setObjectName(u"MalfunctionDialog")
        MalfunctionDialog.resize(450, 250)
        self.formLayout = QFormLayout(MalfunctionDialog)
        self.formLayout.setObjectName(u"formLayout")
        self.lbl_device = QLabel(MalfunctionDialog)
        self.lbl_device.setObjectName(u"lbl_device")

        self.formLayout.setWidget(0, QFormLayout.ItemRole.LabelRole, self.lbl_device)

        self.cb_devices = QComboBox(MalfunctionDialog)
        self.cb_devices.setObjectName(u"cb_devices")

        self.formLayout.setWidget(0, QFormLayout.ItemRole.FieldRole, self.cb_devices)

        self.lbl_description = QLabel(MalfunctionDialog)
        self.lbl_description.setObjectName(u"lbl_description")

        self.formLayout.setWidget(1, QFormLayout.ItemRole.LabelRole, self.lbl_description)

        self.te_description = QTextEdit(MalfunctionDialog)
        self.te_description.setObjectName(u"te_description")

        self.formLayout.setWidget(1, QFormLayout.ItemRole.FieldRole, self.te_description)

        self.btn_report = QPushButton(MalfunctionDialog)
        self.btn_report.setObjectName(u"btn_report")

        self.formLayout.setWidget(2, QFormLayout.ItemRole.FieldRole, self.btn_report)


        self.retranslateUi(MalfunctionDialog)

        QMetaObject.connectSlotsByName(MalfunctionDialog)
    # setupUi

    def retranslateUi(self, MalfunctionDialog):
        self.lbl_device.setText(QCoreApplication.translate("MalfunctionDialog", u"Select Device:", None))
        self.lbl_description.setText(QCoreApplication.translate("MalfunctionDialog", u"Description:", None))
        self.btn_report.setText(QCoreApplication.translate("MalfunctionDialog", u"Report Malfunction", None))
        pass
    # retranslateUi

