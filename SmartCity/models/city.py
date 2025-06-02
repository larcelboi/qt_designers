# City class definition
import jsonpickle
from district import District

class City:
    def __init__(self):
        self.lst_city = []


    def add_district(self,district):
        "Adds a new district to the city"
        pass

    def get_all_devices(self):
        "Returns a list of all smart devices in all districts"
        pass

    def save(self):
        with open("LaVille.json", 'w',encoding="utf-8") as file:
            file.write(jsonpickle.encode(self, indent=4))

    @staticmethod
    def load():
        try:
            with open("LaVille.json", 'r', encoding="utf-8") as file:
                return jsonpickle.decode(file.read())
        except FileNotFoundError:
            return City()

ville_load = City.load()