# GenreEnum.py
from enum import Enum


class GenreEnum(Enum):
    """Énumération des genres de livres disponibles"""
    FICTION = "Fiction"
    SCIENCE_FICTION = "Science-Fiction"
    FANTASY = "Fantasy"
    ROMANCE = "Romance"
    THRILLER = "Thriller"
    MYSTERE = "Mystère"
    HORREUR = "Horreur"
    BIOGRAPHIE = "Biographie"
    HISTOIRE = "Histoire"
    SCIENCE = "Science"
    PHILOSOPHIE = "Philosophie"
    PSYCHOLOGIE = "Psychologie"
    ART = "Art"
    CUISINE = "Cuisine"
    VOYAGE = "Voyage"
    INFORMATIQUE = "Informatique"
    MATHEMATIQUES = "Mathématiques"
    MEDECINE = "Médecine"
    JEUNESSE = "Jeunesse"
    BANDE_DESSINEE = "Bande Dessinée"
    POESIE = "Poésie"
    THEATRE = "Théâtre"
    ESSAI = "Essai"
    MANUEL_SCOLAIRE = "Manuel Scolaire"
    REFERENCE = "Référence"


# EtatLivreEnum.py
from enum import Enum


class EtatLivreEnum(Enum):
    """Énumération des états possibles d'un livre"""
    DISPONIBLE = "Disponible"
    EMPRUNTE = "Emprunté"
    RESERVE = "Réservé"
    EN_REPARATION = "En Réparation"
    EN_COMMANDE = "En Commande"
    PERDU = "Perdu"
    ENDOMMAGE = "Endommagé"
    RETIRE = "Retiré"
    EN_TRAITEMENT = "En Traitement"
    QUARANTAINE = "Quarantaine"  # Pour les protocoles sanitaires