from classes.person.people_table import *
from classes.person.window1 import *
from PyQt5.QtWidgets import QMainWindow, QMessageBox
from PyQt5 import uic

class person_window2(QMainWindow):
    def __init__(self, id_pessoa, nome, idade, cpf):
        super(person_window2, self).__init__()
        uic.loadUi("ui\\person\\window2.ui", self)
        self.show()
        self.id_pessoa = id_pessoa

        if self.id_pessoa == None:
            self.pbInserirAtualizar.clicked.connect(self.insert)
        else:
            self.lbAdicionarAtualizar.setText("Atualizar")
            self.pbInserirAtualizar.setText("Atualizar")
            self.setWindowTitle("Atualizar")
            self.leNome.setText(nome)
            self.leIdade.setText(idade)
            self.leCpf.setText(cpf)
            self.pbInserirAtualizar.clicked.connect(self.atualizar)
            
        
    def insert(self):
        self.person = person(self.leNome.text(), int(self.leIdade.text()), self.leCpf.text())
        self.person.insert_person()
        QMessageBox.about(self, "Alerta", "Dados inseridos no banco de dados.")
        self.close()

    def atualizar(self):
        self.person = person(self.leNome.text(), int(self.leIdade.text()), self.leCpf.text())
        self.person.update_person(self.id_pessoa)
        QMessageBox.about(self, "Alerta", "Dados modificados no banco de dados.")
        self.close()


    


# End of Class
