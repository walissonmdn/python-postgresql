from classes.database_connection import *
from PyQt5.QtWidgets import QTableWidgetItem

# Class to represent a book and its methods related to CRUD.
class book:
    def __init__(self, nome_livro, autor, ano, quantidade):
        self.nome_livro = nome_livro
        self.autor = autor
        self.ano = ano
        self.quantidade = quantidade

    def insert_book(self):
        # Establish a connection with the database.
        connection_instance = db_connection()
        cursor = connection_instance.create_connection() # Cursor to perform operations in the database.

        # Insert a book in the database.
        cursor.execute(f"INSERT INTO livros (nome, autor, ano, qtd) VALUES ('{self.nome_livro}', '{self.autor}', {self.ano}, {self.quantidade})")

        # Close connection.
        connection_instance.close_connection()
        
    def show_books(self, twDatabase):
        # Establish a connection with the database.
        connection_instance = db_connection() 
        cursor = connection_instance.create_connection() # Cursor to perform operations in the database.

        # Get books in the database.
        cursor.execute(f"SELECT * FROM livros") # Returns a tuple with the data in the database.

        # Show data in the user interface table.
        table_row = 0 # Variable to represent the row index.
        for database_row in cursor: # Iterate to get every line in the tuple.
            twDatabase.setRowCount(table_row+1)
            # Set the informations in the user interface table.
            twDatabase.setItem(table_row, 0, QTableWidgetItem(str(database_row[0])))
            twDatabase.setItem(table_row, 1, QTableWidgetItem(database_row[1]))
            twDatabase.setItem(table_row, 2, QTableWidgetItem(database_row[2]))
            twDatabase.setItem(table_row, 3, QTableWidgetItem(str(database_row[3])))
            twDatabase.setItem(table_row, 4, QTableWidgetItem(str(database_row[4])))
            table_row+=1

        # Close connection.
        connection_instance.close_connection()

    def delete_book(self, id_livro):
        # Establish a connection with the database.
        connection_instance = db_connection()
        cursor = connection_instance.create_connection() # Cursor to perform operations in the database.
        
        # Delete a specific book in the database.
        cursor.execute(f"DELETE FROM livros where id_livro = {id_livro}")
        
        # Close connection.
        connection_instance.close_connection()

    def update_book(self, id_livro):
        # Establish a connection with the database.
        connection_instance = db_connection()
        cursor = connection_instance.create_connection() # Cursor to perform operations in the database.

        # Update informations of a book in the database.
        cursor.execute(f"UPDATE livros SET nome = '{self.nome_livro}', autor = '{self.autor}', ano = {self.ano}, qtd = {self.quantidade} where id_livro = {id_livro}")

        # Close connection.
        connection_instance.close_connection()
