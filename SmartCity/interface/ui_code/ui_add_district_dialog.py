# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'add_district_dialog.ui'
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

class Ui_AddDistrictDialog(object):
    def setupUi(self, AddDistrictDialog):
        if not AddDistrictDialog.objectName():
            AddDistrictDialog.setObjectName(u"AddDistrictDialog")
        AddDistrictDialog.resize(400, 200)
        self.formLayout = QFormLayout(AddDistrictDialog)
        self.formLayout.setObjectName(u"formLayout")
        self.lbl_name = QLabel(AddDistrictDialog)
        self.lbl_name.setObjectName(u"lbl_name")

        self.formLayout.setWidget(0, QFormLayout.ItemRole.LabelRole, self.lbl_name)

        self.le_name = QLineEdit(AddDistrictDialog)
        self.le_name.setObjectName(u"le_name")

        self.formLayout.setWidget(0, QFormLayout.ItemRole.FieldRole, self.le_name)

        self.lbl_type = QLabel(AddDistrictDialog)
        self.lbl_type.setObjectName(u"lbl_type")

        self.formLayout.setWidget(1, QFormLayout.ItemRole.LabelRole, self.lbl_type)

        self.cb_type = QComboBox(AddDistrictDialog)
        self.cb_type.setObjectName(u"cb_type")

        self.formLayout.setWidget(1, QFormLayout.ItemRole.FieldRole, self.cb_type)

        self.btn_create_district = QPushButton(AddDistrictDialog)
        self.btn_create_district.setObjectName(u"btn_create_district")

        self.formLayout.setWidget(2, QFormLayout.ItemRole.FieldRole, self.btn_create_district)


        self.retranslateUi(AddDistrictDialog)

        QMetaObject.connectSlotsByName(AddDistrictDialog)
    # setupUi

    def retranslateUi(self, AddDistrictDialog):
        self.lbl_name.setText(QCoreApplication.translate("AddDistrictDialog", u"District Name:", None))
        self.lbl_type.setText(QCoreApplication.translate("AddDistrictDialog", u"District Type:", None))
        self.btn_create_district.setText(QCoreApplication.translate("AddDistrictDialog", u"Create District", None))
        pass
    # retranslateUi

