from PySide6.QtWidgets import (QApplication, QMainWindow, QLabel, QPushButton, QVBoxLayout, QWidget,
                                     QLineEdit, QMessageBox, QListWidget, QHBoxLayout, QComboBox)
from PySide6.QtCore import Property, Signal, QObject

from personne import Personne
from information_sauvegarder import Information,information_load

# Main application window
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Advanced Person Manager")

        self.information = information_load
        self.fichier_load = information_load
        self.people = self.fichier_load.liste_personne
        self.name_input = QLineEdit()
        self.age_input = QLineEdit()
        self.role_input = QComboBox()
        self.role_input.addItems(["Student", "Teacher", "Admin"])

        self.add_button = QPushButton("Add Person")
        self.edit_button = QPushButton("Edit Selected")
        self.delete_button = QPushButton("Delete Selected")

        self.person_list = QListWidget()
        self.output_label = QLabel("")

        form_layout = QVBoxLayout()
        form_layout.addWidget(QLabel("Name:"))
        form_layout.addWidget(self.name_input)
        form_layout.addWidget(QLabel("Age:"))
        form_layout.addWidget(self.age_input)
        form_layout.addWidget(QLabel("Role:"))
        form_layout.addWidget(self.role_input)
        form_layout.addWidget(self.add_button)
        form_layout.addWidget(self.edit_button)
        form_layout.addWidget(self.delete_button)

        list_layout = QVBoxLayout()
        list_layout.addWidget(QLabel("People List:"))
        list_layout.addWidget(self.person_list)
        list_layout.addWidget(self.output_label)

        main_layout = QHBoxLayout()
        main_layout.addLayout(form_layout)
        main_layout.addLayout(list_layout)

        container = QWidget()
        container.setLayout(main_layout)
        self.setCentralWidget(container)

        # Connect buttons
        self.add_button.clicked.connect(self.add_person)
        self.edit_button.clicked.connect(self.edit_person)
        self.delete_button.clicked.connect(self.delete_person)
        self.person_list.currentRowChanged.connect(self.show_greeting)


        self.refresh_person_list()


    def add_person(self):
        try:

            name = self.name_input.text()
            age = int(self.age_input.text())
            role = self.role_input.currentText()
            new_person = Personne(name, age, role)
            self.people.append(new_person)
            self.refresh_person_list()
        except Exception as e:
            QMessageBox.critical(self, "Error", str(e))
        else:
            self.information.liste_personne.append(new_person)
            self.information.sauvegarder()

    def edit_person(self):
        row = self.person_list.currentRow()
        la_personne = self.people[row]
        if 0 <= row < len(self.people):
            try:
                la_personne.name = self.name_input.text()
                la_personne.age = int(self.age_input.text())
                la_personne.role = self.role_input.currentText()
                self.refresh_person_list()
            except Exception as e:
                QMessageBox.critical(self, "Error", str(e))
            else:
                self.information.liste_personne[row] = la_personne
                self.information.sauvegarder()


    def delete_person(self):
        row = self.person_list.currentRow()
        if 0 <= row < len(self.people):
            del self.people[row]
            self.refresh_person_list()

    def refresh_person_list(self):
        self.person_list.clear()
        try:
            for person in self.people:
                self.person_list.addItem(f"{person.name} ({person.role})")
            self.output_label.setText("")
        except Exception as e:
            print(e)

    def show_greeting(self, index):
        if 0 <= index < len(self.people):
            person = self.people[index]
            self.name_input.setText(person.name)
            self.age_input.setText(str(person.age))
            self.role_input.setCurrentText(person.role)
            self.output_label.setText(person.greet())

# TODO: Add unit tests for Person

if __name__ == '__main__':
    app = QApplication([])
    window = MainWindow()
    window.resize(800, 400)
    window.show()
    app.exec()
