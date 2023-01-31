from database_connection import *
from PyQt5.QtWidgets import QTableWidgetItem

class book:
    def __init__(self, nome_livro, autor, ano, qtd):
        self.nome_livro = nome_livro
        self.autor = autor
        self.ano = ano
        self.qtd = qtd
       # self.inserir_livro()

    def insert_book(self):
        # Create a connection string
        connection_instance = db_connection() # Make an instance of db_connection_string
        cursor = connection_instance.create_connection() # Call the method to create the string

        # Perform operation
        cursor.execute(f"INSERT INTO livros (nome, autor, ano, qtd) VALUES ('{self.nome_livro}', '{self.autor}', {self.ano}, {self.qtd})")

        # Close connection
        connection_instance.close_connection()
        
    def show_books(self, twDatabase):
        # Create a connection string
        connection_instance = db_connection() # Make an instance of db_connection_string
        cursor = connection_instance.create_connection() # Call the method to create the string

         # Perform operation
        cursor.execute(f"SELECT * FROM livros")
        table_row = 0
        i=0
        for database_row in cursor:
            i+=1
            twDatabase.setRowCount(i)
            print(database_row)
            twDatabase.setItem(table_row, 0, QTableWidgetItem(str(database_row[0])))
            twDatabase.setItem(table_row, 1, QTableWidgetItem(database_row[1]))
            twDatabase.setItem(table_row, 2, QTableWidgetItem(database_row[2]))
            twDatabase.setItem(table_row, 3, QTableWidgetItem(str(database_row[3])))
            twDatabase.setItem(table_row, 4, QTableWidgetItem(str(database_row[4])))
            table_row+=1

        # Close connection.
        connection_instance.close_connection()

    def delete_book(self, twDatabase):
        connection_instance = db_connection() # Make an instance of db_connection_string
        cursor = connection_instance.create_connection() # Call the method to create the string


        print(twDatabase.item(twDatabase.currentRow(),0).text())
         # Perform operation
        cursor.execute(f"DELETE FROM livros where id_livro = {twDatabase.item(twDatabase.currentRow(),0).text()}")
        twDatabase.removeRow(twDatabase.currentRow()) # Removes only in the widget

        connection_instance.close_connection()