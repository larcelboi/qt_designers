
class Personne:
    def __init__(self, name, age, role):
        super().__init__()
        self.name = name
        self._age = age
        self._role = role

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if isinstance(value, str) and value.strip():
            self._name = value
        else:
            raise ValueError("Invalid name")

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        if isinstance(value, int) and value >= 0:
            self._age = value
        else:
            raise ValueError("Invalid age")

    @property
    def role(self):
        return self._role

    @role.setter
    def role(self, value):
        if value in ["Student", "Teacher", "Admin"]:
            self._role = value
        else:
            raise ValueError("Invalid role")

    def greet(self):
        return f"Hello, I'm {self._name}, {self._age} years old, working as a {self._role}."




    def __str__(self):
        return f"Nom: {self.name} - Age: {self.age} - Role: {self.role} "

