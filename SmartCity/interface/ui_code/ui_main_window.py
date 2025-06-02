# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_window.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QFormLayout, QHBoxLayout,
    QLabel, QLineEdit, QListWidget, QListWidgetItem,
    QMainWindow, QPushButton, QSizePolicy, QSpacerItem,
    QStackedWidget, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(553, 452)
        MainWindow.setMinimumSize(QSize(553, 0))
        MainWindow.setMaximumSize(QSize(553, 452))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.mainLayout = QVBoxLayout(self.centralwidget)
        self.mainLayout.setObjectName(u"mainLayout")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setPointSize(12)
        self.label.setFont(font)

        self.mainLayout.addWidget(self.label)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(450, -1, -1, -1)
        self.btn_logout = QPushButton(self.centralwidget)
        self.btn_logout.setObjectName(u"btn_logout")
        self.btn_logout.setLayoutDirection(Qt.LayoutDirection.LeftToRight)

        self.verticalLayout.addWidget(self.btn_logout)


        self.mainLayout.addLayout(self.verticalLayout)

        self.stackedWidget = QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.page_home = QWidget()
        self.page_home.setObjectName(u"page_home")
        self.homeLayout = QVBoxLayout(self.page_home)
        self.homeLayout.setObjectName(u"homeLayout")
        self.lbl_welcome = QLabel(self.page_home)
        self.lbl_welcome.setObjectName(u"lbl_welcome")
        self.lbl_welcome.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.homeLayout.addWidget(self.lbl_welcome)

        self.stackedWidget.addWidget(self.page_home)
        self.page_dashboard = QWidget()
        self.page_dashboard.setObjectName(u"page_dashboard")
        self.dashboardLayout = QVBoxLayout(self.page_dashboard)
        self.dashboardLayout.setObjectName(u"dashboardLayout")
        self.dashboardControls = QHBoxLayout()
        self.dashboardControls.setObjectName(u"dashboardControls")
        self.btn_add_district = QPushButton(self.page_dashboard)
        self.btn_add_district.setObjectName(u"btn_add_district")

        self.dashboardControls.addWidget(self.btn_add_district)

        self.btn_add_device = QPushButton(self.page_dashboard)
        self.btn_add_device.setObjectName(u"btn_add_device")

        self.dashboardControls.addWidget(self.btn_add_device)

        self.btn_report_malfunction = QPushButton(self.page_dashboard)
        self.btn_report_malfunction.setObjectName(u"btn_report_malfunction")

        self.dashboardControls.addWidget(self.btn_report_malfunction)

        self.btn_refresh = QPushButton(self.page_dashboard)
        self.btn_refresh.setObjectName(u"btn_refresh")

        self.dashboardControls.addWidget(self.btn_refresh)

        self.btn_settings = QPushButton(self.page_dashboard)
        self.btn_settings.setObjectName(u"btn_settings")

        self.dashboardControls.addWidget(self.btn_settings)


        self.dashboardLayout.addLayout(self.dashboardControls)

        self.list_districts = QListWidget(self.page_dashboard)
        self.list_districts.setObjectName(u"list_districts")

        self.dashboardLayout.addWidget(self.list_districts)

        self.stackedWidget.addWidget(self.page_dashboard)
        self.page_settings = QWidget()
        self.page_settings.setObjectName(u"page_settings")
        self.settingsLayout = QFormLayout(self.page_settings)
        self.settingsLayout.setObjectName(u"settingsLayout")
        self.lbl_select_district = QLabel(self.page_settings)
        self.lbl_select_district.setObjectName(u"lbl_select_district")

        self.settingsLayout.setWidget(0, QFormLayout.ItemRole.LabelRole, self.lbl_select_district)

        self.cb_settings_district = QComboBox(self.page_settings)
        self.cb_settings_district.setObjectName(u"cb_settings_district")

        self.settingsLayout.setWidget(0, QFormLayout.ItemRole.FieldRole, self.cb_settings_district)

        self.lbl_select_device = QLabel(self.page_settings)
        self.lbl_select_device.setObjectName(u"lbl_select_device")

        self.settingsLayout.setWidget(1, QFormLayout.ItemRole.LabelRole, self.lbl_select_device)

        self.cb_settings_device = QComboBox(self.page_settings)
        self.cb_settings_device.setObjectName(u"cb_settings_device")

        self.settingsLayout.setWidget(1, QFormLayout.ItemRole.FieldRole, self.cb_settings_device)

        self.lbl_update_name = QLabel(self.page_settings)
        self.lbl_update_name.setObjectName(u"lbl_update_name")

        self.settingsLayout.setWidget(2, QFormLayout.ItemRole.LabelRole, self.lbl_update_name)

        self.le_update_name = QLineEdit(self.page_settings)
        self.le_update_name.setObjectName(u"le_update_name")

        self.settingsLayout.setWidget(2, QFormLayout.ItemRole.FieldRole, self.le_update_name)

        self.lbl_update_energy = QLabel(self.page_settings)
        self.lbl_update_energy.setObjectName(u"lbl_update_energy")

        self.settingsLayout.setWidget(3, QFormLayout.ItemRole.LabelRole, self.lbl_update_energy)

        self.le_update_energy = QLineEdit(self.page_settings)
        self.le_update_energy.setObjectName(u"le_update_energy")

        self.settingsLayout.setWidget(3, QFormLayout.ItemRole.FieldRole, self.le_update_energy)

        self.lbl_device_status = QLabel(self.page_settings)
        self.lbl_device_status.setObjectName(u"lbl_device_status")

        self.settingsLayout.setWidget(4, QFormLayout.ItemRole.LabelRole, self.lbl_device_status)

        self.cb_device_status = QComboBox(self.page_settings)
        self.cb_device_status.addItem("")
        self.cb_device_status.addItem("")
        self.cb_device_status.setObjectName(u"cb_device_status")

        self.settingsLayout.setWidget(4, QFormLayout.ItemRole.FieldRole, self.cb_device_status)

        self.btn_apply_changes = QPushButton(self.page_settings)
        self.btn_apply_changes.setObjectName(u"btn_apply_changes")

        self.settingsLayout.setWidget(5, QFormLayout.ItemRole.FieldRole, self.btn_apply_changes)

        self.stackedWidget.addWidget(self.page_settings)

        self.mainLayout.addWidget(self.stackedWidget)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(150, -1, 150, -1)
        self.startpushButton = QPushButton(self.centralwidget)
        self.startpushButton.setObjectName(u"startpushButton")

        self.horizontalLayout.addWidget(self.startpushButton)


        self.mainLayout.addLayout(self.horizontalLayout)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.mainLayout.addItem(self.verticalSpacer)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        self.label.setText(QCoreApplication.translate("MainWindow", u"City of : Nom", None))
        self.btn_logout.setText(QCoreApplication.translate("MainWindow", u"Logout", None))
        self.lbl_welcome.setText(QCoreApplication.translate("MainWindow", u"Welcome! Please login to manage the Smart City.", None))
        self.btn_add_district.setText(QCoreApplication.translate("MainWindow", u"Add District", None))
        self.btn_add_device.setText(QCoreApplication.translate("MainWindow", u"Add Device", None))
        self.btn_report_malfunction.setText(QCoreApplication.translate("MainWindow", u"Report Malfunction", None))
        self.btn_refresh.setText(QCoreApplication.translate("MainWindow", u"Refresh", None))
        self.btn_settings.setText(QCoreApplication.translate("MainWindow", u"Settings", None))
        self.lbl_select_district.setText(QCoreApplication.translate("MainWindow", u"Select District:", None))
        self.lbl_select_device.setText(QCoreApplication.translate("MainWindow", u"Select Device:", None))
        self.lbl_update_name.setText(QCoreApplication.translate("MainWindow", u"New Name:", None))
        self.lbl_update_energy.setText(QCoreApplication.translate("MainWindow", u"New Energy Usage:", None))
        self.lbl_device_status.setText(QCoreApplication.translate("MainWindow", u"Device Status:", None))
        self.cb_device_status.setItemText(0, QCoreApplication.translate("MainWindow", u"ON", None))
        self.cb_device_status.setItemText(1, QCoreApplication.translate("MainWindow", u"OFF", None))

        self.btn_apply_changes.setText(QCoreApplication.translate("MainWindow", u"Apply Changes", None))
        self.startpushButton.setText(QCoreApplication.translate("MainWindow", u"Start", None))
        pass
    # retranslateUi

