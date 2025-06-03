from PySide6.QtWidgets import QDialog, QMessageBox

from SmartCity.interface.ui_code.ui_add_district_dialog import Ui_AddDistrictDialog
from SmartCity.models.subclasses_district import Camera,Sensor,TrafficLight
from SmartCity.models.enum_device_type import DeviceType,DistrictType,TrafficLightMode

from SmartCity.models.district import District
from SmartCity.models.city import ville_load

class AddDistrict(QDialog):
    def __init__(self, parent=None):
        super().__init__()
        self.ui = Ui_AddDistrictDialog()
        self.ui.setupUi(self)
        self.parent = parent

        self.ui.btn_create_district.clicked.connect(self.create_district)
        liste_district = [DistrictType]
        for type_class in liste_district:
            for value in type_class:
                self.ui.cb_type.addItem(value.value,value)

    def create_district(self):
        name = self.ui.le_name.text()
        type_district = self.ui.cb_type.currentData()
        verification = District(name,type_district.name)
        ville_load.lst_district.append(verification)
        ville_load.save()
        QMessageBox.information(self,"Valide",f"Création de {name}")
        self.ui.le_name.clear()


