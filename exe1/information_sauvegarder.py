import jsonpickle

class Information:
    def __init__(self):
        self.liste_personne = []

    def sauvegarder(self):
        with open("informations.json", "w", encoding="utf-8") as file:
            file.write(jsonpickle.encode(self, indent=4))

    @staticmethod
    def load():
        try:
            with open("informations.json", "r", encoding="utf-8") as file:
                return jsonpickle.decode(file.read())
        except FileNotFoundError:
            return Information()

information_load = Information.load()