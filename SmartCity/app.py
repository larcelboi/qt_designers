# Main application entry
import sys

from PySide6.QtWidgets import QMainWindow, QApplication, QSizePolicy

# TODO: Load UI, handle roles, connect actions
from interface.ui_code.ui_main_window import Ui_MainWindow
from interface.code_ui.code_login_page import Login

class RunApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.user = None

        self.ui.stackedWidget.setCurrentIndex(0)

        # les autres widgets
        self.login_page = Login(self)

        # cahcer
        self.ui.btn_logout.hide()
        self.ui.label.hide()

        #self.ui.cb_user_role.addItem()# todo ajouter le nom des personnes
        self.ui.startpushButton.clicked.connect(self.ouvrir_login) # todo
        self.ui.btn_logout.clicked.connect(self.sortir) # todo

    def sortir(self):
        self.ui.stackedWidget.setCurrentIndex(0)
        self.user = None
        self.cacher_montrer()
    def ouvrir_login(self):
        self.login_page.show()

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