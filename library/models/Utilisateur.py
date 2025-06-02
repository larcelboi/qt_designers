from abc import ABC, abstractmethod
from datetime import datetime


class Utilisateur(ABC):
    """
    Classe abstraite pour tous les types d'utilisateurs de la bibliothèque
    TODO: Ajouter système d'authentification avec mot de passe
    TODO: Ajouter validation d'email avec regex
    """

    def __init__(self, nom: str = "", email: str = "", bibliotheque=None):
        self._nom = nom
        self._email = email
        self._date_inscription = datetime.now()
        self._bibliotheque = bibliotheque
        self._actif = True

    @property
    def nom(self) -> str:
        """Obtenir le nom de l'utilisateur"""
        return self._nom

    @nom.setter
    def nom(self, value: str) -> None:
        """
        Définir le nom de l'utilisateur
        TODO: Ajouter validation (longueur minimale, caractères autorisés)
        """
        if not value or len(value.strip()) < 2:
            raise ValueError("Le nom doit contenir au moins 2 caractères")
        self._nom = value.strip()

    @property
    def email(self) -> str:
        """Obtenir l'email de l'utilisateur"""
        return self._email

    @email.setter
    def email(self, value: str) -> None:
        """
        Définir l'email de l'utilisateur
        TODO: Ajouter validation d'email complète
        """
        if not value or "@" not in value:
            raise ValueError("Email invalide")
        self._email = value.lower().strip()

    @property
    def date_inscription(self) -> datetime:
        """Obtenir la date d'inscription"""
        return self._date_inscription

    @property
    def bibliotheque(self):
        """Obtenir la référence à la bibliothèque"""
        return self._bibliotheque

    @bibliotheque.setter
    def bibliotheque(self, value) -> None:
        """Définir la référence à la bibliothèque"""
        self._bibliotheque = value

    @property
    def actif(self) -> bool:
        """Vérifier si l'utilisateur est actif"""
        return self._actif

    @actif.setter
    def actif(self, value: bool) -> None:
        """Activer/désactiver l'utilisateur"""
        self._actif = value

    def desactiver(self) -> None:
        """Désactiver l'utilisateur"""
        self._actif = False

    def activer(self) -> None:
        """Activer l'utilisateur"""
        self._actif = True

    @abstractmethod
    def peut_emprunter(self) -> bool:
        """Méthode abstraite pour vérifier si l'utilisateur peut emprunter"""
        pass

    def __str__(self) -> str:
        return f"{self.__class__.__name__}: {self._nom} ({self._email})"

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(nom='{self._nom}', email='{self._email}')"