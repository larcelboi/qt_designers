# User roles and access control
from SmartCity.models.district  import District
from SmartCity.models.smartdevice  import SmartDevice



class User:
    _access = ""
    def __init__(self,name:str,password:str,type_guest):
        self.lst_erreur = []
        self.name = name
        self.password = password
        self.type_guest = type_guest
        self.district: list[District] = []
        self.device: list[SmartDevice] = []

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self,nouv_name):
        try:
            if isinstance(nouv_name,str) and nouv_name.strip() != "":
                self._name = nouv_name.capitalize()
            else:
                raise ValueError("You must enter a name")
        except Exception as e:
            self.lst_erreur.append(e)

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, nouv_password):
        try:
            if isinstance(nouv_password, str) and nouv_password.strip() != "":
                self._password = nouv_password
            else:
                raise ValueError("You must enter a password")
        except Exception as e:
            self.lst_erreur.append(e)





