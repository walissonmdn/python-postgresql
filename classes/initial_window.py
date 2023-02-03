from classes.book.window1 import *
from classes.lent.window1 import *
from classes.person.window1 import *
from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow

class initialwindow(QMainWindow):
    def __init__(self):
        super(initialwindow, self).__init__()
        uic.loadUi("ui\\initial_window.ui", self)
        self.show()
        self.pbLivros.clicked.connect(self.book_window1)
        self.pbPessoas.clicked.connect(self.person_window1)
        self.pbEmprestimos.clicked.connect(self.lent_book_window1)

    def book_window1(self):
        self.book_window1_object = book_window1()

    def person_window1(self):
        self.person_window1_object = person_window1()

    def lent_book_window1(self):
        self.lent_book_window1_object = lent_books_window1()
        