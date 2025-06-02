from SmartCity.models.user import User

class Guest(User):
    _access = "Aucun"

    def __init__(self,name:str,password:str,type_guest:str):
        super().__init__(name,password,type_guest)

class Technician(User):
    _access = "half"

    def __init__(self,name:str,password:str,type_guest:str):
        super().__init__(name,password,type_guest)

class CityPlanner(User):
    _access = "full"
    def __init__(self,name:str,password:str,type_guest:str):
        super().__init__(name,password,type_guest)
