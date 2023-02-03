from classes.lent.lent_books_table import *
from classes.lent.window2 import *
from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QMessageBox

class lent_books_window1(QMainWindow):
    def __init__(self):
        super(lent_books_window1, self).__init__()
        uic.loadUi("ui\\lent\\window1.ui", self)
        self.show()
        self.twDatabase.setColumnCount(5)
        self.twDatabase.setHorizontalHeaderLabels(("cod_emprestimo", "id_pessoa", "id_livro", "Pessoa", "Livro"))
        self.twDatabase.setColumnWidth(0, 100)
        self.twDatabase.setColumnWidth(1, 60)
        self.twDatabase.setColumnWidth(2, 60)
        self.twDatabase.setColumnWidth(3, 150)
        self.twDatabase.setColumnWidth(4, 150)


        self.pbInserir.clicked.connect(self.insert)
        self.pbExibir.clicked.connect(self.show_people)
        self.pbDeletar.clicked.connect(self.delete)
        self.pbAtualizar.clicked.connect(self.update)

    def insert(self):
        # Instantiate another window to make the insertion.
        self.insert_lent_book = lent_book_window2(None, None, None)

    def update(self):
        # try-except block to verify if a row was selected in the widget.
        try:
            cod_emprestimo = self.twDatabase.item(self.twDatabase.currentRow(),0).text()
            id_pessoa = self.twDatabase.item(self.twDatabase.currentRow(),1).text()
            id_livro = self.twDatabase.item(self.twDatabase.currentRow(),2).text()
            self.update_window = lent_book_window2(cod_emprestimo, id_pessoa, id_livro)
        except:
            QMessageBox.about(self, "Atenção!", "Nenhum empréstimo selecionado.")

    def delete(self):
        # try-except block to verify if a row was selected in the widget.
        try:
            cod_emprestimo = self.twDatabase.item(self.twDatabase.currentRow(),0).text() 
            self.lent_book = lent_book(None, None)
            self.lent_book.delete_lent_book(cod_emprestimo)
            self.twDatabase.removeRow(self.twDatabase.currentRow()) # Removes only in the widget
        except:
            QMessageBox.about(self, "Atenção!", "Nenhum empréstimo selecionado.")

    def show_people(self):
        lent_book_instance = lent_book(None, None)
        lent_book_instance.show_lent_books(self.twDatabase)
# End of Class

