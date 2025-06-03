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

        self.login.cb_user_role.hide()
        self.login.label.hide()
        self.login.label_4.setText("Login")
        # ajouter class dans combobox
        self.login.cb_user_role.addItems(["Guest","Technician","CityPlanner"])
        # Connecter les bouttons
        self.login.sign_up.clicked.connect(self.entrer_informations)
        self.login.btn_login.clicked.connect(self.obtenir_login)
        self.login.pushButton.clicked.connect(self.changer_page)

    def changer_page(self):
        if self.login.label_4.text() == "Login":
            self.login.label_4.setText("Guest")
            self.login.cb_user_role.show()
            self.login.label.show()
        elif self.login.label_4.text() == "Guest":
            self.login.label_4.setText("Login")
            self.login.cb_user_role.hide()
            self.login.label.hide()

    def entrer_informations(self):
        if self.login.label_4.text() == "Login":
            QMessageBox.warning(self, "Attention", f"Veuillez changer la page avec Login/Signup")
            return

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
            QMessageBox.warning(self, "Invalide", message_erreur)
            return None

        if verification_class.name in ville_load.user_dict.keys():
            print(ville_load.user_dict)
            QMessageBox.warning(self, "Invalide", f"Ce nom {nom} à déjà été crée")
            return

        ville_load.user_dict[nom] = verification_class
        ville_load.save()
        QMessageBox.information(self, "Information",f"{nom} a été crée")
        if hasattr(self.parent,"obtenir_login_information"):
            self.parent.obtenir_login_information(verification_class)
            self.login.lineEdit.clear()
            self.login.lineEdit_2.clear()

    def obtenir_login(self):
        if not self.login.label_4.text() == "Login":
            QMessageBox.warning(self, "Attention", f"Veuillez changer la page avec Login/Signup")
            return
        nom = self.login.lineEdit.text().capitalize().capitalize()
        password = self.login.lineEdit_2.text()

        if nom.strip() =="" or password.strip() =="":
            QMessageBox.warning(self, "Attention", f"Vous avez une ou des casses vides")
            return
        for les_noms,attributes in ville_load.user_dict.items():
            if nom == les_noms and password == attributes.password:
                personne = ville_load.user_dict[nom]
                if hasattr(self.parent, "obtenir_login_information"):
                    QMessageBox.information(self, "En cours..", f"Ouverture de la ville de {nom}..")

                    self.parent.obtenir_login_information(personne)
                    self.login.lineEdit.clear()
                    self.login.lineEdit_2.clear()
                    if hasattr(self.parent, "afficher_district_devices"):
                        self.parent.afficher_district_devices()

                return
        else:
            QMessageBox.warning(self, "Invalie", f"nom et mot de passe invalide")
