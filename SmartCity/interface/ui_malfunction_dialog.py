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
from PySide6.QtWidgets import (QApplication, QDialog, QLabel, QPushButton,
    QSizePolicy, QTextEdit, QVBoxLayout, QWidget)

class Ui_MalfunctionDialog(object):
    def setupUi(self, MalfunctionDialog):
        if not MalfunctionDialog.objectName():
            MalfunctionDialog.setObjectName(u"MalfunctionDialog")
        MalfunctionDialog.resize(400, 200)
        self.verticalLayout = QVBoxLayout(MalfunctionDialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(MalfunctionDialog)
        self.label.setObjectName(u"label")

        self.verticalLayout.addWidget(self.label)

        self.textEdit_description = QTextEdit(MalfunctionDialog)
        self.textEdit_description.setObjectName(u"textEdit_description")

        self.verticalLayout.addWidget(self.textEdit_description)

        self.btn_report = QPushButton(MalfunctionDialog)
        self.btn_report.setObjectName(u"btn_report")

        self.verticalLayout.addWidget(self.btn_report)


        self.retranslateUi(MalfunctionDialog)

        QMetaObject.connectSlotsByName(MalfunctionDialog)
    # setupUi

    def retranslateUi(self, MalfunctionDialog):
        self.label.setText(QCoreApplication.translate("MalfunctionDialog", u"Describe the malfunction:", None))
        self.btn_report.setText(QCoreApplication.translate("MalfunctionDialog", u"Report", None))
        pass
    # retranslateUi

