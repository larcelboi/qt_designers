# District class with device list
from SmartCity.models.smartdevice  import SmartDevice

class District:
    def __init__(self,name,device_type):
        self.liste_device = []
        self.name = name
        self.device_type = device_type

    def add_device(self,device:SmartDevice):
        "Adds a smart device to the district."
        pass

    def remove_device(self,device:SmartDevice):
        "Removes a device from the district."
        pass

    def total_energy_usage(self):
        " Returns the sum of energy usage from all devices in the district."
        pass
