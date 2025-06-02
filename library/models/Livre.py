from .GenreEnum import GenreEnum
from .EtatLivreEnum import EtatLivreEnum
from datetime import datetime, timedelta
import re


class Livre:
    """
    Classe représentant un livre dans la bibliothèque
    TODO: Ajouter système de codes-barres avec génération automatique
    TODO: Ajouter gestion des éditions multiples d'un même titre
    TODO: Ajouter système de notation et commentaires des lecteurs
    """

    def __init__(self, titre: str, auteur_nom: str, isbn: str = "", genre: GenreEnum = GenreEnum.FICTION,
                 annee_publication: int = None, nb_pages: int = 0, editeur: str = "",
                 langue: str = "Français", createur=None):
        self._titre = titre
        self._auteur_nom = auteur_nom
        self._isbn = isbn
        self._genre = genre
        self._annee_publication = annee_publication or datetime.now().year
        self._nb_pages = nb_pages
        self._editeur = editeur
        self._langue = langue
        self._createur = createur
        self._etat = EtatLivreEnum.DISPONIBLE
        self._date_acquisition = datetime.now()
        self._nb_emprunts = 0
        self._emplacement = ""
        self._resume = ""
        self._mots_cles = []
        self._valeur_achat = 0.0
        self._derniere_verification = datetime.now()

    @property
    def titre(self) -> str:
        """Obtenir le titre du livre"""
        return self._titre

    @titre.setter
    def titre(self, value: str) -> None:
        """
        Définir le titre du livre
        TODO: Ajouter validation pour éviter les titres vides ou trop courts
        """
        if not value or len(value.strip()) < 1:
            raise ValueError("Le titre ne peut pas être vide")
        if len(value) > 255:
            raise ValueError("Le titre ne peut pas dépasser 255 caractères")
        self._titre = value.strip()

    @property
    def auteur_nom(self) -> str:
        """Obtenir le nom de l'auteur"""
        return self._auteur_nom

    @auteur_nom.setter
    def auteur_nom(self, value: str) -> None:
        """Définir le nom de l'auteur"""
        if not value or len(value.strip()) < 2:
            raise ValueError("Le nom de l'auteur doit contenir au moins 2 caractères")
        self._auteur_nom = value.strip()

    @property
    def isbn(self) -> str:
        """Obtenir l'ISBN du livre"""
        return self._isbn

    @isbn.setter
    def isbn(self, value: str) -> None:
        """
        Définir l'ISBN du livre avec validation
        TODO: Améliorer la validation ISBN-13 avec checksum
        """
        if value:
            # Nettoyer l'ISBN (retirer tirets et espaces)
            isbn_clean = re.sub(r'[-\s]', '', value)

            # Vérifier le format (10 ou 13 chiffres)
            if not re.match(r'^\d{10}(\d{3})?$', isbn_clean):
                raise ValueError("ISBN invalide. Doit contenir 10 ou 13 chiffres")

            self._isbn = isbn_clean
        else:
            self._isbn = ""

    @property
    def genre(self) -> GenreEnum:
        """Obtenir le genre du livre"""
        return self._genre

    @genre.setter
    def genre(self, value: GenreEnum) -> None:
        """Définir le genre du livre"""
        if not isinstance(value, GenreEnum):
            raise ValueError("Le genre doit être une instance de GenreEnum")
        self._genre = value

    @property
    def annee_publication(self) -> int:
        """Obtenir l'année de publication"""
        return self._annee_publication

    @annee_publication.setter
    def annee_publication(self, value: int) -> None:
        """Définir l'année de publication avec validation"""
        annee_actuelle = datetime.now().year
        if value < 1000 or value > annee_actuelle + 1:
            raise ValueError(f"Année de publication invalide. Doit être entre 1000 et {annee_actuelle + 1}")
        self._annee_publication = value

    @property
    def nb_pages(self) -> int:
        """Obtenir le nombre de pages"""
        return self._nb_pages

    @nb_pages.setter
    def nb_pages(self, value: int) -> None:
        """Définir le nombre de pages"""
        if value < 0:
            raise ValueError("Le nombre de pages ne peut pas être négatif")
        if value > 10000:  # Limite raisonnable
            raise ValueError("Le nombre de pages semble excessif (max 10000)")
        self._nb_pages = value

    @property
    def editeur(self) -> str:
        """Obtenir l'éditeur"""
        return self._editeur

    @editeur.setter
    def editeur(self, value: str) -> None:
        """Définir l'éditeur"""
        self._editeur = value.strip() if value else ""

    @property
    def langue(self) -> str:
        """Obtenir la langue du livre"""
        return self._langue

    @langue.setter
    def langue(self, value: str) -> None:
        """Définir la langue du livre"""
        self._langue = value.strip() if value else "Français"

    @property
    def etat(self) -> EtatLivreEnum:
        """Obtenir l'état actuel du livre"""
        return self._etat

    @etat.setter
    def etat(self, value: EtatLivreEnum) -> None:
        """Définir l'état du livre"""
        if not isinstance(value, EtatLivreEnum):
            raise ValueError("L'état doit être une instance de EtatLivreEnum")
        self._etat = value

    @property
    def nb_emprunts(self) -> int:
        """Obtenir le nombre d'emprunts du livre"""
        return self._nb_emprunts

    @property
    def date_acquisition(self) -> datetime:
        """Obtenir la date d'acquisition du livre"""
        return self._date_acquisition

    @property
    def createur(self):
        """Obtenir le créateur de la fiche livre"""
        return self._createur

    @property
    def emplacement(self) -> str:
        """Obtenir l'emplacement physique du livre"""
        return self._emplacement

    @emplacement.setter
    def emplacement(self, value: str) -> None:
        """Définir l'emplacement physique du livre"""
        self._emplacement = value.strip() if value else ""

    @property
    def resume(self) -> str:
        """Obtenir le résumé du livre"""
        return self._resume

    @resume.setter
    def resume(self, value: str) -> None:
        """Définir le résumé du livre"""
        if len(value) > 5000:
            raise ValueError("Le résumé ne peut pas dépasser 5000 caractères")
        self._resume = value.strip() if value else ""

    @property
    def mots_cles(self) -> list:
        """Obtenir les mots-clés du livre"""
        return self._mots_cles.copy()

    @property
    def valeur_achat(self) -> float:
        """Obtenir la valeur d'achat du livre"""
        return self._valeur_achat

    @valeur_achat.setter
    def valeur_achat(self, value: float) -> None:
        """Définir la valeur d'achat du livre"""
        if value < 0:
            raise ValueError("La valeur d'achat ne peut pas être négative")
        self._valeur_achat = value

    def est_disponible(self) -> bool:
        """Vérifier si le livre est disponible pour emprunt"""
        return self._etat == EtatLivreEnum.DISPONIBLE

    def emprunter(self) -> bool:
        """
        Marquer le livre comme emprunté
        TODO: Intégrer avec le système de gestion des emprunts
        """
        if self.est_disponible():
            self._etat = EtatLivreEnum.EMPRUNTE
            self._nb_emprunts += 1
            return True
        return False

    def retourner(self) -> bool:
        """Marquer le livre comme retourné (disponible)"""
        if self._etat == EtatLivreEnum.EMPRUNTE:
            self._etat = EtatLivreEnum.DISPONIBLE
            return True
        return False

    def reserver(self) -> bool:
        """Marquer le livre comme réservé"""
        if self.est_disponible():
            self._etat = EtatLivreEnum.RESERVE
            return True
        return False

    def annuler_reservation(self) -> bool:
        """Annuler la réservation du livre"""
        if self._etat == EtatLivreEnum.RESERVE:
            self._etat = EtatLivreEnum.DISPONIBLE
            return True
        return False

    def ajouter_mot_cle(self, mot_cle: str) -> None:
        """Ajouter un mot-clé au livre"""
        mot_cle = mot_cle.strip().lower()
        if mot_cle and mot_cle not in self._mots_cles:
            self._mots_cles.append(mot_cle)

    def retirer_mot_cle(self, mot_cle: str) -> bool:
        """Retirer un mot-clé du livre"""
        mot_cle = mot_cle.strip().lower()
        if mot_cle in self._mots_cles:
            self._mots_cles.remove(mot_cle)
            return True
        return False

    def marquer_verification(self) -> None:
        """Marquer le livre comme vérifié (inventaire)"""
        self._derniere_verification = datetime.now()

    def necessite_verification(self, jours: int = 365) -> bool:
        """Vérifier si le livre nécessite une vérification d'inventaire"""
        return (datetime.now() - self._derniere_verification).days > jours

    def calculer_age(self) -> int:
        """Calculer l'âge du livre en années"""
        return datetime.now().year - self._annee_publication

    def est_recent(self, annees: int = 2) -> bool:
        """Vérifier si le livre est récent"""
        return self.calculer_age() <= annees

    def generer_cote(self) -> str:
        """
        Générer une cote de classification pour le livre
        TODO: Implémenter système de classification Dewey
        """
        # Classification simplifiée basée sur le genre
        codes_genre = {
            GenreEnum.FICTION: "F",
            GenreEnum.SCIENCE_FICTION: "SF",
            GenreEnum.FANTASY: "FY",
            GenreEnum.BIOGRAPHIE: "B",
            GenreEnum.HISTOIRE: "H",
            GenreEnum.SCIENCE: "S",
            GenreEnum.INFORMATIQUE: "I",
            GenreEnum.JEUNESSE: "J"
        }

        code = codes_genre.get(self._genre, "G")  # G pour Général

        # Ajouter les 3 premières lettres de l'auteur
        auteur_code = ''.join(c.upper() for c in self._auteur_nom if c.isalpha())[:3]

        return f"{code}{auteur_code}{self._annee_publication}"

    def rechercher_dans_contenu(self, termes: list) -> bool:
        """
        Rechercher des termes dans le titre, auteur, résumé et mots-clés
        TODO: Implémenter recherche full-text plus sophistiquée
        """
        contenu_recherche = (
                f"{self._titre} {self._auteur_nom} {self._resume} " +
                " ".join(self._mots_cles)
        ).lower()

        return all(terme.lower() in contenu_recherche for terme in termes)

    def __str__(self) -> str:
        return f"{self._titre} par {self._auteur_nom} ({self._annee_publication}) - {self._etat.value}"

    def __repr__(self) -> str:
        return f"Livre(titre='{self._titre}', auteur='{self._auteur_nom}', isbn='{self._isbn}')"

    def __eq__(self, other) -> bool:
        """Comparaison d'égalité basée sur l'ISBN ou titre+auteur"""
        if not isinstance(other, Livre):
            return False

        # Si les deux ont un ISBN, comparer par ISBN
        if self._isbn and other._isbn:
            return self._isbn == other._isbn

        # Sinon comparer par titre et auteur
        return (self._titre.lower() == other._titre.lower() and
                self._auteur_nom.lower() == other._auteur_nom.lower())

    def __hash__(self) -> int:
        """Hash basé sur l'ISBN ou titre+auteur"""
        if self._isbn:
            return hash(self._isbn)
        return hash((self._titre.lower(), self._auteur_nom.lower()))