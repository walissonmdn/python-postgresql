from classes.lent.lent_books_table import *
from classes.lent.window1 import *
from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QMessageBox

class lent_book_window2(QMainWindow):
    def __init__(self, cod_emprestimo, id_pessoa, id_livro):
        super(lent_book_window2, self).__init__()
        uic.loadUi("ui\\lent\\window2.ui", self)
        self.show()
        self.cod_emprestimo = cod_emprestimo

        if self.cod_emprestimo == None:
            self.pbInserirAtualizar.clicked.connect(self.insert)
        else:
            self.lbAdicionarAtualizar.setText("Atualizar")
            self.pbInserirAtualizar.setText("Atualizar")
            self.setWindowTitle("Atualizar")
            self.leId_pessoa.setText(id_pessoa)
            self.leId_livro.setText(id_livro)
            self.pbInserirAtualizar.clicked.connect(self.atualizar)
              
    def insert(self):
        # try-except block to validate data type.
        try:
            leId_pessoa = int(self.leId_pessoa.text())
            leId_livro = int(self.leId_livro.text())
            conversion_success = True # Variable to identify if the IDs are integers.
        except:
            conversion_success = False
            QMessageBox.about(self, "Alerta", 'Os campos só aceitam números inteiros como entrada.')

        if conversion_success == True:
            self.lent_book = lent_book(leId_pessoa, leId_livro)
            insert_success = self.lent_book.insert_lent_book()
            if insert_success == True:
                QMessageBox.about(self, "Sucesso", "Dados inseridos no banco de dados.")
                self.close()

    def atualizar(self):
        # try-except block to validate data type.
        try:
            leId_pessoa = int(self.leId_pessoa.text())
            leId_livro = int(self.leId_livro.text())
            conversion_success = True # Variable to identify if the IDs are integers.
        except:
            conversion_success = False
            QMessageBox.about(self, "Alerta", 'Os campos só aceitam números inteiros como entrada.')

        if conversion_success == True:      
            self.lent_book = lent_book(leId_pessoa, leId_livro)
            update_sucess = self.lent_book.update_lent_book(self.cod_emprestimo)
            if update_sucess == True:
                QMessageBox.about(self, "Sucesso", "Dados modificados no banco de dados.")
                self.close()
# End of Class
