from .Utilisateur import Utilisateur
from .GenreEnum import GenreEnum
from datetime import datetime


class Auteur(Utilisateur):
    """
    Classe pour les auteurs qui peuvent consulter leurs livres et statistiques
    TODO: Ajouter système de royalties
    TODO: Ajouter notifications pour nouveaux emprunts de leurs livres
    """

    def __init__(self, nom: str = "", email: str = "", pseudonyme: str = "", bibliotheque=None):
        super().__init__(nom, email, bibliotheque)
        self._pseudonyme = pseudonyme
        self._biographie = ""
        self._genres_preferes = []
        self._livres_publies = []
        self._date_premiere_publication = None
        self._nationalite = ""
        self._site_web = ""
        self._actif_publication = True

    @property
    def pseudonyme(self) -> str:
        """Obtenir le pseudonyme de l'auteur"""
        return self._pseudonyme if self._pseudonyme else self.nom

    @pseudonyme.setter
    def pseudonyme(self, value: str) -> None:
        """Définir le pseudonyme de l'auteur"""
        self._pseudonyme = value.strip() if value else ""

    @property
    def biographie(self) -> str:
        """Obtenir la biographie de l'auteur"""
        return self._biographie

    @biographie.setter
    def biographie(self, value: str) -> None:
        """Définir la biographie de l'auteur"""
        if len(value) > 2000:
            raise ValueError("La biographie ne peut pas dépasser 2000 caractères")
        self._biographie = value.strip()

    @property
    def genres_preferes(self) -> list:
        """Obtenir la liste des genres préférés"""
        return self._genres_preferes.copy()

    @property
    def livres_publies(self) -> list:
        """Obtenir la liste des livres publiés par cet auteur"""
        return self._livres_publies.copy()

    @property
    def date_premiere_publication(self) -> datetime:
        """Obtenir la date de première publication"""
        return self._date_premiere_publication

    @property
    def nationalite(self) -> str:
        """Obtenir la nationalité de l'auteur"""
        return self._nationalite

    @nationalite.setter
    def nationalite(self, value: str) -> None:
        """Définir la nationalité de l'auteur"""
        self._nationalite = value.strip()

    @property
    def site_web(self) -> str:
        """Obtenir le site web de l'auteur"""
        return self._site_web

    @site_web.setter
    def site_web(self, value: str) -> None:
        """
        Définir le site web de l'auteur
        TODO: Ajouter validation d'URL
        """
        self._site_web = value.strip()

    @property
    def actif_publication(self) -> bool:
        """Vérifier si l'auteur publie encore activement"""
        return self._actif_publication

    @actif_publication.setter
    def actif_publication(self, value: bool) -> None:
        """Définir le statut de publication actif"""
        self._actif_publication = value

    def peut_emprunter(self) -> bool:
        """Les auteurs peuvent emprunter des livres (recherche, inspiration)"""
        return True

    def ajouter_genre_prefere(self, genre: GenreEnum) -> None:
        """Ajouter un genre à la liste des préférés"""
        if genre not in self._genres_preferes:
            self._genres_preferes.append(genre)

    def retirer_genre_prefere(self, genre: GenreEnum) -> bool:
        """Retirer un genre de la liste des préférés"""
        if genre in self._genres_preferes:
            self._genres_preferes.remove(genre)
            return True
        return False

    def ajouter_livre_publie(self, livre) -> None:
        """
        Ajouter un livre à la liste des publications
        TODO: Vérifier que l'auteur correspond
        """
        if livre not in self._livres_publies:
            self._livres_publies.append(livre)

            # Mettre à jour la date de première publication
            if (self._date_premiere_publication is None or
                    livre.date_publication < self._date_premiere_publication):
                self._date_premiere_publication = livre.date_publication

    def retirer_livre_publie(self, livre) -> bool:
        """Retirer un livre de la liste des publications"""
        if livre in self._livres_publies:
            self._livres_publies.remove(livre)
            return True
        return False

    def obtenir_livres_par_genre(self, genre: GenreEnum) -> list:
        """Obtenir les livres de l'auteur dans un genre spécifique"""
        return [livre for livre in self._livres_publies if livre.genre == genre]

    def calculer_nb_emprunts_total(self) -> int:
        """
        Calculer le nombre total d'emprunts de tous les livres de l'auteur
        TODO: Implémenter avec les statistiques réelles de la bibliothèque
        """
        total = 0
        for livre in self._livres_publies:
            total += livre.nb_emprunts if hasattr(livre, 'nb_emprunts') else 0
        return total

    def obtenir_livre_plus_populaire(self):
        """Obtenir le livre le plus emprunté de l'auteur"""
        if not self._livres_publies:
            return None

        livre_populaire = None
        max_emprunts = -1

        for livre in self._livres_publies:
            nb_emprunts = livre.nb_emprunts if hasattr(livre, 'nb_emprunts') else 0
            if nb_emprunts > max_emprunts:
                max_emprunts = nb_emprunts
                livre_populaire = livre

        return livre_populaire

    def generer_rapport_auteur(self) -> dict:
        """
        Générer un rapport détaillé de l'auteur
        TODO: Ajouter statistiques de popularité par période
        """
        return {
            "nom": self.nom,
            "pseudonyme": self.pseudonyme,
            "email": self.email,
            "nationalite": self._nationalite,
            "nb_livres_publies": len(self._livres_publies),
            "genres_preferes": [genre.value for genre in self._genres_preferes],
            "total_emprunts": self.calculer_nb_emprunts_total(),
            "livre_plus_populaire": (self.obtenir_livre_plus_populaire().titre
                                     if self.obtenir_livre_plus_populaire() else None),
            "premiere_publication": (self._date_premiere_publication.strftime("%Y-%m-%d")
                                     if self._date_premiere_publication else None),
            "actif": self._actif_publication,
            "site_web": self._site_web
        }

    def rechercher_livres_similaires(self) -> list:
        """
        Rechercher des livres similaires dans la bibliothèque
        TODO: Implémenter algorithme de recommandation
        """
        if not self.bibliotheque:
            return []

        livres_similaires = []
        for genre in self._genres_preferes:
            # Recherche simplifiée par genre
            for rayon in self.bibliotheque.rayons:
                for livre in rayon.livres:
                    if (livre.genre == genre and
                            livre not in self._livres_publies and
                            livre not in livres_similaires):
                        livres_similaires.append(livre)

        return livres_similaires[:10]  # Limiter à 10 suggestions

    def __str__(self) -> str:
        return f"Auteur: {self.pseudonyme} ({len(self._livres_publies)} livres publiés)"