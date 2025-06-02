from user import User

class Guest(User):
    _access = "Aucun"

    def __init__(self,name:str):
        super().__init__(name)

class Technician(User):
    _access = "half"

    def __init__(self,name:str):
        super().__init__(name)

class CityPlanner(User):
    _access = "full"
    def __init__(self,name:str):
        super().__init__(name)
