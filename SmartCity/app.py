# Main application entry
import sys

from PySide6.QtWidgets import QMainWindow, QApplication, QSizePolicy, QMessageBox, QListWidgetItem

from SmartCity.models.city import ville_load
# TODO: Load UI, handle roles, connect actions
from interface.ui_code.ui_main_window import Ui_MainWindow
from interface.code_ui.code_login_page import Login
from interface.code_ui.code_add_device import AddDeviceDialog
from interface.code_ui.code_add_district import AddDistrict


class RunApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.user = None

        self.ui.stackedWidget.setCurrentIndex(0)


        # les autres widgets
        self.login_page = Login(self)
        self.add_device = AddDeviceDialog(self)
        self.add_district = AddDistrict(self)

        # cahcer
        self.ui.btn_logout.hide()
        self.ui.label.hide()

        self.ui.startpushButton.clicked.connect(self.ouvrir_login)
        self.ui.btn_logout.clicked.connect(self.sortir)
        self.ui.btn_add_device.clicked.connect(self.ouvrir_add_device)
        self.ui.btn_add_district.clicked.connect(self.ouvrir_add_district)
        self.ui.btn_refresh.clicked.connect(self.refresh)
        self.ui.btn_settings.clicked.connect(self.settings)

    def afficher_district_devices(self):
        personne = ville_load.user_dict[self.user.name]
        self.ui.list_districts.clear()
        for district in personne.district_device:
            for device in district.liste_device:
                self.ui.list_districts.addItem(f"Distract: {district.name}\nDevice: {device}\n")

    def ajouter_district(self,device,district):
        personne = ville_load.user_dict[self.user.name]
        personne.district_device.append(district)
        ville_load.user_dict[self.user.name] = personne
        ville_load.save()
        self.ajouter_device(district,device)

    def ajouter_device(self,district,device):
        personne = ville_load.user_dict[self.user.name]
        for les_districts in personne.district_device:
            if les_districts.name == district.name:
                les_districts.liste_device.append(device)
                ville_load.lst_district.remove(district)
                break
        ville_load.user_dict[self.user.name] = personne
        ville_load.save()
        self.afficher_district_devices()

    def settings(self):
        self.ui.stackedWidget.setCurrentIndex(2)
    def refresh(self):
        self.add_device.refresh_district()
        QMessageBox.information(self,"Refresh","Everything got refresh")
    def sortir(self):
        self.ui.stackedWidget.setCurrentIndex(0)
        self.user = None
        self.cacher_montrer()
        self.ui.list_districts.clear()


    def ouvrir_login(self):
        self.login_page.show()

    def ouvrir_add_device(self):
        self.add_device.show()

    def ouvrir_add_district(self):
        self.add_district.show()

    def cacher_montrer(self):
        if self.user is not None:
            self.login_page.close()
            self.ui.btn_logout.show()
            self.ui.btn_logout.show()
            self.ui.verticalSpacer.changeSize(20, 1, QSizePolicy.Minimum, QSizePolicy.Fixed)
            self.ui.verticalLayout.update()
            self.ui.startpushButton.hide()
            self.ui.stackedWidget.setCurrentIndex(1)
            self.ui.label.setText(f"City of {self.user.name}\nType user: {self.user.type_guest}")
            self.ui.label.show()
        else:
            self.ui.startpushButton.show()
            self.ui.label.hide()
            self.ui.btn_logout.hide()
            self.ui.verticalSpacer.changeSize(20, 150, QSizePolicy.Minimum, QSizePolicy.Fixed)
            self.ui.verticalLayout.update()

    def obtenir_login_information(self,information_client):
        self.user = information_client
        if self.user is not None:
            self.cacher_montrer()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = RunApp()
    window.show()
    sys.exit(app.exec())