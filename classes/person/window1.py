from classes.person.people_table import *
from classes.person.window2 import *
from PyQt5.QtWidgets import QMainWindow, QMessageBox
from PyQt5 import uic

class person_window1(QMainWindow):
    def __init__(self):
        super(person_window1, self).__init__()
        uic.loadUi("ui\\person\\window1.ui", self)
        self.show()
        self.twDatabase.setColumnCount(4)
        self.twDatabase.setHorizontalHeaderLabels(("id_pessoa", "Nome", "Idade","cpf"))
        self.twDatabase.setColumnWidth(0, 70)
        self.twDatabase.setColumnWidth(1, 200)
        self.twDatabase.setColumnWidth(2, 50)
        self.twDatabase.setColumnWidth(3, 150)
        self.pbInserir.clicked.connect(self.insert)
        self.pbExibir.clicked.connect(self.show_people)
        self.pbDeletar.clicked.connect(self.delete)
        self.pbAtualizar.clicked.connect(self.update)

    def delete(self):
        try:
            id_pessoa = self.twDatabase.item(self.twDatabase.currentRow(),0).text() 
            self.person = person(None, None, None)
            self.person.delete_person(id_pessoa)
            self.twDatabase.removeRow(self.twDatabase.currentRow()) # Removes only in the widget
        except:
            QMessageBox.about(self, "Atenção!", "Nenhuma pessoa selecionada.")

        
    def insert(self):
        # Instantiate another window to make the insertion.
        self.insert_person = person_window2(None, None, None, None)

    def update(self):
        try:
            id_pessoa = self.twDatabase.item(self.twDatabase.currentRow(),0).text()
            nome = self.twDatabase.item(self.twDatabase.currentRow(),1).text()
            idade = self.twDatabase.item(self.twDatabase.currentRow(),2).text()
            cpf = self.twDatabase.item(self.twDatabase.currentRow(),3).text()
            
            self.update_window = person_window2(id_pessoa, nome, idade, cpf)
        except:
            QMessageBox.about(self, "Atenção!", "Nenhuma pessoa selecionada.")

    def show_people(self):
        person_instance = person(None, None, None)
        person_instance.show_people(self.twDatabase)
# End of Class

