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
        self.label_district_name = QLabel(AddDistrictDialog)
        self.label_district_name.setObjectName(u"label_district_name")

        self.formLayout.setWidget(0, QFormLayout.ItemRole.LabelRole, self.label_district_name)

        self.lineEdit_district_name = QLineEdit(AddDistrictDialog)
        self.lineEdit_district_name.setObjectName(u"lineEdit_district_name")

        self.formLayout.setWidget(0, QFormLayout.ItemRole.FieldRole, self.lineEdit_district_name)

        self.label_district_type = QLabel(AddDistrictDialog)
        self.label_district_type.setObjectName(u"label_district_type")

        self.formLayout.setWidget(1, QFormLayout.ItemRole.LabelRole, self.label_district_type)

        self.comboBox_district_type = QComboBox(AddDistrictDialog)
        self.comboBox_district_type.setObjectName(u"comboBox_district_type")

        self.formLayout.setWidget(1, QFormLayout.ItemRole.FieldRole, self.comboBox_district_type)

        self.btn_create = QPushButton(AddDistrictDialog)
        self.btn_create.setObjectName(u"btn_create")

        self.formLayout.setWidget(2, QFormLayout.ItemRole.FieldRole, self.btn_create)


        self.retranslateUi(AddDistrictDialog)

        QMetaObject.connectSlotsByName(AddDistrictDialog)
    # setupUi

    def retranslateUi(self, AddDistrictDialog):
        self.label_district_name.setText(QCoreApplication.translate("AddDistrictDialog", u"District Name:", None))
        self.label_district_type.setText(QCoreApplication.translate("AddDistrictDialog", u"District Type:", None))
        self.btn_create.setText(QCoreApplication.translate("AddDistrictDialog", u"Create District", None))
        pass
    # retranslateUi

