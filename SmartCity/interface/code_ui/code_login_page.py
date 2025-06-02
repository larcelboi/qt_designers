from PySide6.QtWidgets import QMainWindow, QWidget, QMessageBox

from SmartCity.interface.ui_code.ui_login_page import Ui_Form
from SmartCity.models.subclasses_user import Technician,Guest,CityPlanner
from SmartCity.models.city import ville_load

class Login(QWidget):
    def __init__(self,parent=None):
        super().__init__()
        self.login = Ui_Form()
        self.login.setupUi(self)
        self.parent = parent

        # ajouter class dans combobox
        self.login.cb_user_role.addItems(["Guest","Technician","CityPlanner"])
        # Connecter les bouttons
        self.login.pushButton.clicked.connect(self.close)
        self.login.btn_login.clicked.connect(self.entrer_informations)

    def entrer_informations(self):
        nom = self.login.lineEdit.text().capitalize()
        type_guest = self.login.cb_user_role.currentText()
        password = self.login.lineEdit_2.text()

        verification_class = None
        if type_guest == "Guest":
            verification_class = Guest(nom,password,type_guest)
        elif type_guest == "Technician":
            verification_class = Technician(nom, password,type_guest)
        elif type_guest == "CityPlanner":
            verification_class = CityPlanner(nom, password,type_guest)

        message_erreur = ""
        if len(verification_class.lst_erreur) >= 1:
            for chiffre,erreur in enumerate(verification_class.lst_erreur,start=1):
                message_erreur += f"{chiffre}.{erreur}\n"
            QMessageBox.warning(self, "Information", message_erreur)
            return None

        if verification_class.name in ville_load.user_dict.keys():
            print(ville_load.user_dict)
            QMessageBox.warning(self, "Information", f"Ce nom {nom} à déjà été crée")
            return

        ville_load.user_dict[nom] = verification_class
        ville_load.save()
        QMessageBox.information(self, "Information",f"{nom} a été crée")
        if hasattr(self.parent,"obtenir_login_information"):
            self.parent.obtenir_login_information(verification_class)
            self.login.lineEdit.clear()
            self.login.lineEdit_2.clear()

