# Main application entry
import sys

from PySide6.QtWidgets import QMainWindow, QApplication

# TODO: Load UI, handle roles, connect actions
from interface.ui_main_window import Ui_MainWindow
from interface.ui_add_device_dialog import Ui_AddDeviceDialog
from interface.ui_add_district_dialog import Ui_AddDistrictDialog
from interface.ui_malfunction_dialog import Ui_MalfunctionDialog

class RunApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)




if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = RunApp()
    window.show()
    sys.exit(app.exec())