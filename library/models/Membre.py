from .Utilisateur import Utilisateur
from datetime import datetime, timedelta


class Membre(Utilisateur):
    """
    Classe pour les membres de la bibliothèque qui peuvent emprunter des livres
    TODO: Ajouter système d'abonnement payant
    TODO: Ajouter gestion des notifications par email
    """

    def __init__(self, nom: str = "", email: str = "", type_adhesion: str = "standard", bibliotheque=None):
        super().__init__(nom, email, bibliotheque)
        self._type_adhesion = type_adhesion
        self._livres_empruntes = []
        self._historique_emprunts = []
        self._amendes = 0.0
        self._date_expiration_adhesion = datetime.now() + timedelta(days=365)
        self._limite_emprunts = self._determiner_limite_emprunts()
        self._nb_emprunts_total = 0

    @property
    def type_adhesion(self) -> str:
        """Obtenir le type d'adhésion du membre"""
        return self._type_adhesion

    @type_adhesion.setter
    def type_adhesion(self, value: str) -> None:
        """Définir le type d'adhésion"""
        types_valides = ["etudiant", "standard", "premium", "famille"]
        if value not in types_valides:
            raise ValueError(f"Type d'adhésion invalide. Doit être: {types_valides}")
        self._type_adhesion = value
        self._limite_emprunts = self._determiner_limite_emprunts()

    @property
    def livres_empruntes(self) -> list:
        """Obtenir la liste des livres actuellement empruntés"""
        return self._livres_empruntes.copy()

    @property
    def historique_emprunts(self) -> list:
        """Obtenir l'historique complet des emprunts"""
        return self._historique_emprunts.copy()

    @property
    def amendes(self) -> float:
        """Obtenir le montant des amendes dues"""
        return self._amendes

    @amendes.setter
    def amendes(self, value: float) -> None:
        """Définir le montant des amendes"""
        if value < 0:
            raise ValueError("Le montant des amendes ne peut pas être négatif")
        self._amendes = value

    @property
    def date_expiration_adhesion(self) -> datetime:
        """Obtenir la date d'expiration de l'adhésion"""
        return self._date_expiration_adhesion

    @property
    def limite_emprunts(self) -> int:
        """Obtenir la limite d'emprunts simultanés"""
        return self._limite_emprunts

    @property
    def nb_emprunts_total(self) -> int:
        """Obtenir le nombre total d'emprunts effectués"""
        return self._nb_emprunts_total

    def _determiner_limite_emprunts(self) -> int:
        """Déterminer la limite d'emprunts selon le type d'adhésion"""
        limites = {
            "etudiant": 3,
            "standard": 5,
            "premium": 10,
            "famille": 8
        }
        return limites.get(self._type_adhesion, 5)

    def peut_emprunter(self) -> bool:
        """Vérifier si le membre peut emprunter un livre"""
        return (self.actif and
                len(self._livres_empruntes) < self._limite_emprunts and
                self._amendes < 50.0 and  # Limite d'amendes
                datetime.now() < self._date_expiration_adhesion)

    def emprunter_livre(self, livre=None) -> bool:
        """
        Emprunter un livre
        TODO: Intégrer avec la classe Livre pour la gestion des états
        """
        if not self.peut_emprunter():
            return False

        emprunt = {
            "livre": livre,
            "date_emprunt": datetime.now(),
            "date_retour_prevue": datetime.now() + timedelta(days=21),  # 3 semaines
            "retourne": False
        }

        self._livres_empruntes.append(emprunt)
        self._historique_emprunts.append(emprunt)
        self._nb_emprunts_total += 1

        if self.bibliotheque:
            self.bibliotheque.sauvegarder()

        return True

    def retourner_livre(self, livre=None) -> bool:
        """
        Retourner un livre emprunté
        TODO: Calculer automatiquement les amendes de retard
        """
        for emprunt in self._livres_empruntes:
            if emprunt["livre"] == livre:
                emprunt["retourne"] = True
                emprunt["date_retour_effective"] = datetime.now()

                # Calculer amende si retard
                if datetime.now() > emprunt["date_retour_prevue"]:
                    jours_retard = (datetime.now() - emprunt["date_retour_prevue"]).days
                    amende = jours_retard * 0.50  # 50 cents par jour
                    self._amendes += amende

                self._livres_empruntes.remove(emprunt)

                if self.bibliotheque:
                    self.bibliotheque.sauvegarder()

                return True
        return False

    def payer_amendes(self, montant: float) -> float:
        """
        Payer les amendes
        Retourne le montant restant dû
        """
        if montant <= 0:
            raise ValueError("Le montant doit être positif")

        self._amendes -= montant
        if self._amendes < 0:
            self._amendes = 0

        return self._amendes

    def renouveler_adhesion(self, duree_mois: int = 12) -> None:
        """Renouveler l'adhésion pour une durée donnée"""
        self._date_expiration_adhesion = datetime.now() + timedelta(days=duree_mois * 30)

    def obtenir_livres_en_retard(self) -> list:
        """Obtenir la liste des livres en retard"""
        livres_retard = []
        for emprunt in self._livres_empruntes:
            if datetime.now() > emprunt["date_retour_prevue"]:
                livres_retard.append(emprunt)
        return livres_retard

    def adhesion_expiree(self) -> bool:
        """Vérifier si l'adhésion a expiré"""
        return datetime.now() > self._date_expiration_adhesion

    def generer_rapport_membre(self) -> dict:
        """
        Générer un rapport détaillé du membre
        TODO: Ajouter graphiques de statistiques d'emprunt
        """
        return {
            "nom": self.nom,
            "email": self.email,
            "type_adhesion": self._type_adhesion,
            "emprunts_actuels": len(self._livres_empruntes),
            "limite_emprunts": self._limite_emprunts,
            "total_emprunts": self._nb_emprunts_total,
            "amendes_dues": self._amendes,
            "adhesion_expire": self.adhesion_expiree(),
            "livres_en_retard": len(self.obtenir_livres_en_retard()),
            "peut_emprunter": self.peut_emprunter()
        }

    def __str__(self) -> str:
        return f"Membre: {self.nom} ({self._type_adhesion}) - {len(self._livres_empruntes)}/{self._limite_emprunts} emprunts"