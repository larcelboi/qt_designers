from PySide6.QtWidgets import QDialog, QMessageBox

from SmartCity.interface.ui_code.ui_add_device_dialog import Ui_AddDeviceDialog
from SmartCity.models.enum_device_type import DeviceType,DistrictType,TrafficLightMode
from SmartCity.models.subclasses_user import Technician,Guest,CityPlanner
from SmartCity.models.subclasses_district import Camera,Sensor,TrafficLight

from SmartCity.models.city import ville_load

class AddDeviceDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__()
        self.ui = Ui_AddDeviceDialog()
        self.ui.setupUi(self)
        self.parent = parent

        self.ui.btn_add_device.clicked.connect(self.ajouter_device)

        liste_type_device = [DeviceType]
        for type_class in liste_type_device:
            for value in type_class:
                self.ui.cb_type.addItem(str(value.value))

        for type_class in ville_load.lst_district:
            self.ui.cb_district.addItem(type_class.name,type_class)

    def refresh_district(self):
        self.ui.cb_district.clear()
        for type_class in ville_load.lst_district:
            self.ui.cb_district.addItem(type_class.name,type_class)

    def ajouter_device(self):
        nom = self.ui.le_name.text()
        device_type = self.ui.cb_type.currentText()
        energy = self.ui.le_energy.text()
        status = self.ui.cb_status.currentText()
        malfunction = self.ui.cb_malfunction.currentText()
        district = self.ui.cb_district.currentText()

        if not any([nom.strip()=="",device_type,energy=="",status,malfunction,district]):
            QMessageBox.warning(self,"Erreur","Vous avez des casses vides")
            return
        if status == "ON":
            bool_status = True
        else:
            bool_status = False

        if malfunction == "False":
            bool_malfunction = False
        else:
            bool_malfunction = True
        verification = Camera(nom,int(energy),bool_status,bool_malfunction,recording=True)
        QMessageBox.information(self, "Valide!", "Informations entrées valies")
        le_district = None
        for name_district in ville_load.lst_district:
            if name_district.name == district:
                le_district = name_district
                break
        if hasattr(self.parent,'ajouter_district'):
            self.parent.ajouter_district(verification,le_district)