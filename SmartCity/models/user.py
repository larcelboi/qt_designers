# User roles and access control

class User:
    def __init__(self,name:str):
        self.name = name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self,nouv_name):
        if isinstance(nouv_name,str) and nouv_name.strip() != "":
            self._name = nouv_name
        else:
            raise ValueError("You must enter a name")


