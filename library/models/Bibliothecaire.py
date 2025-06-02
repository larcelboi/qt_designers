from .Utilisateur import Utilisateur
from .Rayon import Rayon


class Bibliothecaire(Utilisateur):
    """
    Classe pour les bibliothécaires qui peuvent gérer les rayons et superviser
    TODO: Ajouter gestion des horaires de travail
    TODO: Ajouter système de permissions granulaires
    """

    def __init__(self, nom: str = "", email: str = "", departement: str = "", bibliotheque=None):
        super().__init__(nom, email, bibliotheque)
        self._departement = departement
        self._rayons_geres = []
        self._niveau_acces = "complet"

    @property
    def departement(self) -> str:
        """Obtenir le département du bibliothécaire"""
        return self._departement

    @departement.setter
    def departement(self, value: str) -> None:
        """Définir le département du bibliothécaire"""
        if not value or len(value.strip()) < 2:
            raise ValueError("Le département doit être spécifié")
        self._departement = value.strip()

    @property
    def rayons_geres(self) -> list:
        """Obtenir la liste des rayons gérés"""
        return self._rayons_geres.copy()  # Retourner une copie pour éviter les modifications directes

    @property
    def niveau_acces(self) -> str:
        """Obtenir le niveau d'accès du bibliothécaire"""
        return self._niveau_acces

    @niveau_acces.setter
    def niveau_acces(self, value: str) -> None:
        """Définir le niveau d'accès"""
        niveaux_valides = ["limite", "normal", "complet", "administrateur"]
        if value not in niveaux_valides:
            raise ValueError(f"Niveau d'accès invalide. Doit être: {niveaux_valides}")
        self._niveau_acces = value

    def peut_emprunter(self) -> bool:
        """Les bibliothécaires peuvent emprunter des livres"""
        return True

    def creer_rayon(self, nom: str, description: str = "") -> Rayon:
        """
        Créer un nouveau rayon et l'ajouter à la bibliothèque
        TODO: Ajouter validation des doublons de noms de rayons
        """
        if not self.bibliotheque:
            raise ValueError("Bibliothécaire non assigné à une bibliothèque")

        rayon = Rayon(nom, description)
        self.bibliotheque.rayons.append(rayon)
        self._rayons_geres.append(rayon)
        self.bibliotheque.sauvegarder()
        return rayon

    def assigner_rayon(self, rayon: Rayon) -> None:
        """Assigner un rayon à ce bibliothécaire"""
        if rayon not in self._rayons_geres:
            self._rayons_geres.append(rayon)

    def retirer_rayon(self, rayon: Rayon) -> bool:
        """Retirer un rayon de la gestion de ce bibliothécaire"""
        if rayon in self._rayons_geres:
            self._rayons_geres.remove(rayon)
            return True
        return False

    def peut_gerer_rayon(self, rayon: Rayon) -> bool:
        """Vérifier si le bibliothécaire peut gérer un rayon spécifique"""
        return (self._niveau_acces in ["complet", "administrateur"] or
                rayon in self._rayons_geres)

    def generer_rapport_rayons(self) -> dict:
        """
        Générer un rapport sur les rayons gérés
        TODO: Ajouter plus de statistiques détaillées
        """
        rapport = {
            "bibliothecaire": self.nom,
            "departement": self.departement,
            "nombre_rayons": len(self._rayons_geres),
            "rayons": []
        }

        for rayon in self._rayons_geres:
            rapport["rayons"].append({
                "nom": rayon.nom,
                "nombre_livres": len(rayon.livres),
                "description": rayon.description
            })

        return rapport

    def __str__(self) -> str:
        return f"Bibliothécaire: {self.nom} - {self.departement} ({len(self._rayons_geres)} rayons)"