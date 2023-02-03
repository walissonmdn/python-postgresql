from classes.initial_window import *
from PyQt5.QtWidgets import QApplication
import sys

app = QApplication(sys.argv)
window = initialwindow()
app.exec_()
