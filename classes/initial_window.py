from classes.book.window1 import *
from PyQt5.QtWidgets import QMainWindow
from PyQt5 import uic

class initialwindow(QMainWindow):
    def __init__(self):
        super(initialwindow, self).__init__()
        uic.loadUi("ui\\initial_window.ui", self)
        self.show()
        self.pbLivros.clicked.connect(self.book_window1)

    def book_window1(self):
        self.book_window1_object = book_window1()
        self.close()