from books_table import *
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5 import uic
import sys

class main_window(QMainWindow):
    def __init__(self):
        super(main_window, self).__init__()
        uic.loadUi("ui\\book_window.ui", self)
        self.show()
        self.twDatabase.setColumnCount(5)
        self.twDatabase.setHorizontalHeaderLabels(("id_livro", "Nome", "Autor","Ano","QTD"))
        self.twDatabase.setColumnWidth(0, 50)
        self.twDatabase.setColumnWidth(1, 50)
        self.twDatabase.setColumnWidth(2, 50)
        self.twDatabase.setColumnWidth(3, 50)
        self.twDatabase.setColumnWidth(4, 50)
        self.pbInserir.clicked.connect(self.inserir)
        self.pbExibir.clicked.connect(self.exibir)
        self.pbLimpar.clicked.connect(self.limpar)

    def limpar(self):
        self.book = book(None, None, None, None)
        self.book.delete_book(self.twDatabase)
        
    def inserir(self):
        self.book = book(self.leNome.text(), self.leAutor.text(), int(self.leAno.text()), int(self.leQuantidade.text()))
        self.book.insert_book()

    def exibir(self):
        self.book = book(None, None, None, None)
        self.book.show_books(self.twDatabase)

# End of Class

app = QApplication(sys.argv)
window = main_window()
app.exec_()
