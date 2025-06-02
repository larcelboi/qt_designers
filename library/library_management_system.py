import sys
from pathlib import Path
import jsonpickle
from PySide6.QtCore import QTimer, Qt
from PySide6.QtWidgets import (QApplication, QMainWindow, QDialog, QVBoxLayout,
                               QHBoxLayout, QLabel, QPushButton, QComboBox,
                               QStackedWidget, QFrame, QGridLayout, QWidget,
                               QLineEdit, QTextEdit, QSpinBox, QDateEdit)
from PySide6.QtCore import QDate
from models import Bibliothecaire, Membre, Auteur, Livre, Rayon, Utilisateur, Bibliotheque
from interface.ajouter_livre_dialogue import AjouterLivreDialogue
from interface.ajouter_rayon_dialogue import AjouterRayonDialogue
from interface.emprunter_livre_dialogue import EmprunterLivreDialogue
from interface import LivreWidget

# Désactive l'échappement ASCII et conserve l'UTF‑8 «tel quel»
jsonpickle.set_encoder_options('json', ensure_ascii=False, indent=4)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi()

        # Préparer les fenêtres secondaires
        self.fenetre_ajouter_livre = None
        self.fenetre_ajouter_rayon = None
        self.fenetre_emprunter_livre = None

        # Variables globales
        self.bibliotheque: Bibliotheque = Bibliotheque()
        self.bibliotheque.charger()
        self.rayon_actuel_index: int = -1
        self.rayon_actuel: Rayon | None = None
        self.utilisateur_actuel: Utilisateur | None = None

        # Préparer affichage initial
        self.rafraichir_choix_utilisateurs()
        self.rafraichir_choix_rayons()
        self.rafraichir_contenu_rayon()
        self.lbl_message_emprunt.hide()

        # Événements
        self.btn_connexion.clicked.connect(self.connexion)
        self.btn_deconnexion.clicked.connect(self.deconnexion)
        self.btn_ajouter_rayon.clicked.connect(self.ajouter_rayon)
        self.btn_ajouter_livre.clicked.connect(self.ajouter_livre)
        self.cb_choix_rayon.currentIndexChanged.connect(self.rafraichir_contenu_rayon)
        self.btn_emprunter_livre.clicked.connect(self.emprunter_livre)
        self.btn_retourner_livre.clicked.connect(self.retourner_livre)
        self.btn_voir_statistiques.clicked.connect(self.voir_statistiques)
        self.cb_choix_rayon.currentIndexChanged.connect(self.cacher_message_emprunt)

        # TODO: Ajouter recherche par auteur
        # TODO: Ajouter système de réservation
        # TODO: Ajouter gestion des amendes

    def setupUi(self):
        """Configure l'interface utilisateur"""
        self.setWindowTitle("Système de Gestion de Bibliothèque")
        self.setGeometry(100, 100, 1200, 800)

        # Widget central et layout principal
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        # Stacked widget pour les pages
        self.stackedWidget = QStackedWidget()
        layout_principal = QVBoxLayout(central_widget)
        layout_principal.addWidget(self.stackedWidget)

        # Page de connexion
        self.page_connexion = QWidget()
        self.setupPageConnexion()
        self.stackedWidget.addWidget(self.page_connexion)

        # Page principale
        self.page_principale = QWidget()
        self.setupPagePrincipale()
        self.stackedWidget.addWidget(self.page_principale)

        self.stackedWidget.setCurrentWidget(self.page_connexion)

    def setupPageConnexion(self):
        """Configure la page de connexion"""
        layout = QVBoxLayout(self.page_connexion)

        self.lbl_titre = QLabel("📚 Système de Gestion de Bibliothèque")
        self.lbl_titre.setAlignment(Qt.AlignCenter)
        self.lbl_titre.setObjectName("lbl_titre")

        self.cb_connexion = QComboBox()
        self.btn_connexion = QPushButton("Se Connecter")

        layout.addStretch()
        layout.addWidget(self.lbl_titre)
        layout.addWidget(QLabel("Choisir un utilisateur:"))
        layout.addWidget(self.cb_connexion)
        layout.addWidget(self.btn_connexion)
        layout.addStretch()

    def setupPagePrincipale(self):
        """Configure la page principale"""
        layout = QVBoxLayout(self.page_principale)

        # Header avec déconnexion
        header_layout = QHBoxLayout()
        self.lbl_utilisateur_connecte = QLabel("Utilisateur: Non connecté")
        self.btn_deconnexion = QPushButton("Se Déconnecter")
        header_layout.addWidget(self.lbl_utilisateur_connecte)
        header_layout.addStretch()
        header_layout.addWidget(self.btn_deconnexion)

        # Sélection de rayon
        rayon_layout = QHBoxLayout()
        self.lbl_choix_rayon = QLabel("Choisir un rayon:")
        self.lbl_choix_rayon.setObjectName("lbl_choix_rayon")
        self.cb_choix_rayon = QComboBox()
        rayon_layout.addWidget(self.lbl_choix_rayon)
        rayon_layout.addWidget(self.cb_choix_rayon)
        rayon_layout.addStretch()

        # Boutons d'action (seront cachés/montrés selon l'utilisateur)
        actions_layout = QHBoxLayout()
        self.btn_ajouter_rayon = QPushButton("Ajouter Rayon")
        self.btn_ajouter_livre = QPushButton("Ajouter Livre")
        self.btn_emprunter_livre = QPushButton("Emprunter Livre")
        self.btn_retourner_livre = QPushButton("Retourner Livre")
        self.btn_voir_statistiques = QPushButton("Voir Statistiques")

        actions_layout.addWidget(self.btn_ajouter_rayon)
        actions_layout.addWidget(self.btn_ajouter_livre)
        actions_layout.addWidget(self.btn_emprunter_livre)
        actions_layout.addWidget(self.btn_retourner_livre)
        actions_layout.addWidget(self.btn_voir_statistiques)
        actions_layout.addStretch()

        # Message d'emprunt
        self.lbl_message_emprunt = QLabel("✅ Livre emprunté avec succès!")
        self.lbl_message_emprunt.setObjectName("lbl_message_emprunt")

        # Zone d'affichage des livres
        self.rayon_frame = QFrame()
        self.rayon_frame.setObjectName("rayon_frame")
        self.rayon_frame.setLayout(QGridLayout())

        layout.addLayout(header_layout)
        layout.addLayout(rayon_layout)
        layout.addLayout(actions_layout)
        layout.addWidget(self.lbl_message_emprunt)
        layout.addWidget(self.rayon_frame)

    def cacher_message_emprunt(self):
        """Cache le message d'emprunt"""
        self.lbl_message_emprunt.hide()

    def emprunter_livre(self):
        """Gère l'emprunt de livre avec effet visuel"""
        if self.lbl_message_emprunt.isVisible():
            self.lbl_message_emprunt.hide()
            QTimer.singleShot(300, self.lbl_message_emprunt.show)
        else:
            self.lbl_message_emprunt.show()

        rayon_actuel = self.cb_choix_rayon.currentData()
        if rayon_actuel and isinstance(self.utilisateur_actuel, Membre):
            # TODO: Implémenter la logique d'emprunt complète
            self.utilisateur_actuel.emprunter_livre()
            self.bibliotheque.sauvegarder()

        self.btn_emprunter_livre.setChecked(False)

    def retourner_livre(self):
        """Gère le retour de livre"""
        # TODO: Implémenter la logique de retour de livre
        if isinstance(self.utilisateur_actuel, Membre):
            # Logique de retour
            pass

    def voir_statistiques(self):
        """Affiche les statistiques de la bibliothèque"""
        # TODO: Créer une fenêtre de statistiques
        pass

    def rafraichir_choix_rayons(self):
        """Remplit le combobox des rayons"""
        self.rayon_actuel_index = self.cb_choix_rayon.currentIndex()
        self.rayon_actuel = self.cb_choix_rayon.currentData()
        self.cb_choix_rayon.clear()

        for rayon in self.bibliotheque.rayons:
            self.cb_choix_rayon.addItem(rayon.nom, rayon)

        if self.rayon_actuel_index == -1 and self.bibliotheque.rayons:
            self.cb_choix_rayon.setCurrentIndex(0)
            self.rayon_actuel_index = self.cb_choix_rayon.currentIndex()
            self.rayon_actuel = self.cb_choix_rayon.currentData()

        self.cb_choix_rayon.setCurrentIndex(self.rayon_actuel_index)

    def rafraichir_choix_utilisateurs(self):
        """Remplit le combobox de connexion"""
        self.cb_connexion.clear()
        for utilisateur in self.bibliotheque.utilisateurs:
            type_utilisateur = utilisateur.__class__.__name__
            self.cb_connexion.addItem(f"{utilisateur.nom} ({type_utilisateur})", utilisateur)

    def rafraichir_contenu_rayon(self):
        """Rafraîchit l'affichage du rayon sélectionné"""
        self.rayon_actuel = self.cb_choix_rayon.currentData()

        # Effacer les widgets existants
        while self.rayon_frame.layout().count():
            item = self.rayon_frame.layout().takeAt(0)
            if item.widget():
                item.widget().deleteLater()

        # Créer les cartes de livres
        row, col = 0, 0
        cols_per_row = 4

        if self.rayon_actuel is not None:
            for livre in self.rayon_actuel.livres:
                livre_widget = LivreWidget(livre)
                self.rayon_frame.layout().addWidget(livre_widget, row, col)

                col += 1
                if col >= cols_per_row:
                    col = 0
                    row += 1

    def connexion(self):
        """Connexion à l'application selon l'utilisateur sélectionné"""
        self.utilisateur_actuel = self.cb_connexion.currentData()

        # Cacher tous les boutons d'actions
        self.cacher_boutons_utilisateurs()

        # Afficher les boutons appropriés selon le type d'utilisateur
        if isinstance(self.utilisateur_actuel, Bibliothecaire):
            self.btn_ajouter_rayon.show()
            self.btn_ajouter_livre.show()
            self.btn_voir_statistiques.show()
            self.btn_retourner_livre.show()
        elif isinstance(self.utilisateur_actuel, Auteur):
            self.btn_ajouter_livre.show()
            self.btn_voir_statistiques.show()
        elif isinstance(self.utilisateur_actuel, Membre):
            self.btn_emprunter_livre.show()
            self.btn_retourner_livre.show()
        else:
            print("Type d'utilisateur inconnu")
            return

        # Mettre à jour le label et changer de page
        self.lbl_utilisateur_connecte.setText(f"Utilisateur: {self.utilisateur_actuel.nom}")
        self.stackedWidget.setCurrentWidget(self.page_principale)

    def cacher_boutons_utilisateurs(self):
        """Cache tous les boutons d'actions utilisateurs"""
        self.btn_ajouter_rayon.hide()
        self.btn_ajouter_livre.hide()
        self.btn_emprunter_livre.hide()
        self.btn_retourner_livre.hide()
        self.btn_voir_statistiques.hide()

    def deconnexion(self):
        """Retour à la page de connexion"""
        self.stackedWidget.setCurrentWidget(self.page_connexion)
        self.lbl_message_emprunt.hide()
        self.rafraichir_choix_utilisateurs()

    def ajouter_rayon(self):
        """Ouvre la fenêtre pour ajouter un rayon"""
        if isinstance(self.utilisateur_actuel, Bibliothecaire):
            self.fenetre_ajouter_rayon = AjouterRayonDialogue(self.utilisateur_actuel)
            self.fenetre_ajouter_rayon.exec()
            self.rafraichir_choix_rayons()

    def ajouter_livre(self):
        """Ouvre la fenêtre pour ajouter un livre"""
        self.fenetre_ajouter_livre = AjouterLivreDialogue(self.utilisateur_actuel)
        if self.fenetre_ajouter_livre.exec() == QDialog.Accepted:
            rayon_actuel = self.cb_choix_rayon.currentData()
            if rayon_actuel:
                self.bibliotheque.ajouter_livre(self.fenetre_ajouter_livre.nouveau_livre)
                self.bibliotheque.ajouter_livre_rayon(
                    self.fenetre_ajouter_livre.nouveau_livre,
                    rayon_actuel
                )

        self.rafraichir_contenu_rayon()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setStyleSheet("""
        * {
            color: #2c3e50;
            font-size: 12px;
            font-family: 'Segoe UI', Arial, sans-serif;
        }
        #lbl_titre {
            font-size: 32px;
            font-weight: bold;
            color: #3498db;
            margin: 20px;
        }
        #lbl_choix_rayon {
            font-size: 18px;
            font-weight: bold;
            color: #2c3e50;
        }
        #lbl_message_emprunt {
            font-size: 16px;
            color: #27ae60;
            font-weight: bold;
            padding: 10px;
            background-color: #d5f4e6;
            border-radius: 5px;
        }
        QMainWindow {
            background-color: #ecf0f1;
        }
        #rayon_frame {
            background-color: rgba(255, 255, 255, 180);
            border-radius: 10px;
            padding: 15px;
        }
        QPushButton {
            background-color: #3498db;
            color: white;
            border: none;
            padding: 8px 16px;
            border-radius: 6px;
            font-weight: bold;
        }
        QPushButton:hover {
            background-color: #2980b9;
        }
        QPushButton:pressed {
            background-color: #21618c;
        }
        QComboBox {
            padding: 5px;
            border: 2px solid #bdc3c7;
            border-radius: 4px;
            background-color: white;
        }
        QComboBox:focus {
            border-color: #3498db;
        }
    """)

    window = MainWindow()
    window.show()
    sys.exit(app.exec())