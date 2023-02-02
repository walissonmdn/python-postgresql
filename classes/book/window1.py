from classes.book.books_table import *
from classes.book.window2 import *
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from PyQt5 import uic

class book_window1(QMainWindow):
    def __init__(self):
        super(book_window1, self).__init__()
        uic.loadUi("ui\\book\\window1.ui", self)
        self.show()
        self.twDatabase.setColumnCount(5)
        self.twDatabase.setHorizontalHeaderLabels(("id_livro", "Nome", "Autor","Ano","Qtd"))
        self.twDatabase.setColumnWidth(0, 50)
        self.twDatabase.setColumnWidth(1, 160)
        self.twDatabase.setColumnWidth(2, 160)
        self.twDatabase.setColumnWidth(3, 50)
        self.twDatabase.setColumnWidth(4, 50)
        self.pbInserir.clicked.connect(self.insert)
        self.pbExibir.clicked.connect(self.show_books)
        self.pbDeletar.clicked.connect(self.delete)
        self.pbAtualizar.clicked.connect(self.update)

    def delete(self):
        try:
            id_livro = self.twDatabase.item(self.twDatabase.currentRow(),0).text() 
            self.book = book(None, None, None, None)
            self.book.delete_book(id_livro)
            self.twDatabase.removeRow(self.twDatabase.currentRow()) # Removes only in the widget
        except:
            QMessageBox.about(self, "Atenção!", "Nenhum livro selecionado.")

        
    def insert(self):
        # Instantiate another window to make the insertion.
        self.insert_book = book_window2(None, None, None, None, None)

    def update(self):
        try:
            id_livro = self.twDatabase.item(self.twDatabase.currentRow(),0).text()
            nome = self.twDatabase.item(self.twDatabase.currentRow(),1).text()
            autor = self.twDatabase.item(self.twDatabase.currentRow(),2).text()
            ano = self.twDatabase.item(self.twDatabase.currentRow(),3).text()
            quantidade = self.twDatabase.item(self.twDatabase.currentRow(),4).text()
            
            self.update_window = book_window2(id_livro, nome, autor, ano, quantidade)
        except:
            QMessageBox.about(self, "Atenção!", "Nenhum livro selecionado.")

    def show_books(self):
        book_instance = book(None, None, None, None)
        book_instance.show_books(self.twDatabase)
# End of Class

