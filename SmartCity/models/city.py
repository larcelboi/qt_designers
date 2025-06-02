# City class definition
import jsonpickle
from SmartCity.models.district import District
from SmartCity.models.smartdevice  import SmartDevice

class City:
    def __init__(self):
        self.user_dict = {}
        self.lst_district :list[District] = []
        self.lst_device :list[SmartDevice] = []


    def add_district(self,district:District):
        "Adds a new district to the city"
        self.lst_district.append(district)
        self.save()

    def get_all_devices(self):
        "Returns a list of all smart devices in all districts"


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