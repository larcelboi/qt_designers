# Main application entry
import sys

from PySide6.QtWidgets import QMainWindow, QApplication

# TODO: Load UI, handle roles, connect actions
from interface.ui_code.ui_main_window import Ui_MainWindow


class RunApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        #self.ui.cb_user_role.addItem()# todo ajouter le nom des personnes
        #self.ui.btn_login.clicked.connect() # todo
        #self.ui.btn_logout.clicked.connect() # todo



if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = RunApp()
    window.show()
    sys.exit(app.exec())