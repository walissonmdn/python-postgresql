from classes.book.books_table import *
from classes.book.window1 import *
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from PyQt5 import uic

class book_window2(QMainWindow):
    def __init__(self, id_livro, nome, autor, ano, quantidade):
        super(book_window2, self).__init__()
        uic.loadUi("ui\\book\\window2.ui", self)
        self.show()
        self.id_livro = id_livro

        if self.id_livro == None:
            self.pbInserirAtualizar.clicked.connect(self.insert)
        else:
            self.lbAdicionarAtualizar.setText("Atualizar")
            self.pbInserirAtualizar.setText("Atualizar")
            self.setWindowTitle("Atualizar")
            self.leNome.setText(nome)
            self.leAutor.setText(autor)
            self.leAno.setText(ano)
            self.leQuantidade.setText(quantidade)
            self.pbInserirAtualizar.clicked.connect(self.atualizar)
            
        
    def insert(self):
        self.book = book(self.leNome.text(), self.leAutor.text(), int(self.leAno.text()), int(self.leQuantidade.text()))
        self.book.insert_book()
        QMessageBox.about(self, "Alerta", "Livro inserido no banco de dados.")
        self.close()

    def atualizar(self):
        self.book = book(self.leNome.text(), self.leAutor.text(), int(self.leAno.text()), int(self.leQuantidade.text()))
        self.book.update_book(self.id_livro)
        QMessageBox.about(self, "Alerta", "Dados modificados no banco de dados.")
        self.close()


    


# End of Class
