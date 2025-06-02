
class SmartDevice:
    def __init__(self,name : str,energy_usage:int,status:bool,malfunctioning:bool):
        self.name = name
        self.energy_usage = energy_usage
        self.status = status
        self.malfunctioning = malfunctioning

    @property
    def name(self):
        return self._name
    @name.setter
    def name(self,nouv_name):
        if isinstance(nouv_name,str) and nouv_name.strip() != "":
            self._name = nouv_name
        else:
            raise ValueError("you must enter a name")

    @property
    def energy_usage(self):
        return self._energy_usage

    @energy_usage.setter
    def energy_usage(self, nouv_energy_usage):
        if isinstance(nouv_energy_usage, int):
            self._energy_usage = nouv_energy_usage
        else:
            raise ValueError("the energy needs to be an integer")

    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, nouv_status):
        if isinstance(nouv_status, bool):
            self._status = nouv_status
        else:
            raise ValueError("the status must be a bool")

    @property
    def malfunctioning(self):
        return self._malfunctioning

    @malfunctioning.setter
    def malfunctioning(self, nouv_malfunctioning):
        if isinstance(nouv_malfunctioning, bool):
            self._malfunctioning = nouv_malfunctioning
        else:
            raise ValueError("malfunctioning needs to be a bool")

    def toggle_status(self):
        "Turns the device on or off."
        if self.status:
            self.status = False
        elif not self.status:
            self.status = True

    def report_malfunction(self):
        "Flags the device as malfunctioning."
        pass

    def reset_malfunction(self):
        "Clears the malfunction flag."
