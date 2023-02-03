from classes.database_connection import *
from psycopg2.errors import ForeignKeyViolation
from PyQt5.QtWidgets import QTableWidgetItem, QMainWindow, QMessageBox

# Class to represent lent books and methods related to CRUD.
class lent_book(QMainWindow):
    def __init__(self, id_pessoa, id_livro):
        super(lent_book, self).__init__()
        self.id_pessoa = id_pessoa
        self.id_livro = id_livro

    def insert_lent_book(self):
        # Establish a connection with the database.
        connection_instance = db_connection()
        cursor = connection_instance.create_connection() # Cursor to perform operations in the database.

        # try-except block, because it won't be possible to insert in the database if IDs don't exit.
        try:
            # Insert informations in the database if a book is lent.
            cursor.execute(f"INSERT INTO emprestimos (id_pessoa, id_livro) VALUES ({self.id_pessoa}, {self.id_livro})")
            success = True # Variable to indicate if the operation was executed successfully.
        except ForeignKeyViolation:
            # Return a message if one or both ID's don't exit.
            QMessageBox.about(self, "Atenção!", "id da pessoa ou/e do livro não encontrado(s).")
            success = False
        finally:
            # Close connection with the database.
            connection_instance.close_connection()

        return success
        
    def update_lent_book(self, cod_emprestimo):
        # Establish a connection with the database.
        connection_instance = db_connection()
        cursor = connection_instance.create_connection() # Cursor to perform operations in the database.

         # try-except block, because it won't be possible to insert in the database if IDs don't exit.
        try:
            # Update informations of IDs in the database.
            cursor.execute(f"UPDATE emprestimos SET id_pessoa = {self.id_pessoa}, id_livro = {self.id_livro} WHERE cod_emprestimo = {cod_emprestimo}")
            success = True # Variable to indicate if the operation was executed successfully.
        except ForeignKeyViolation:
            # Return a message if one or both ID's don't exit.
            QMessageBox.about(self, "Atenção!", "id da pessoa ou/e do livro não encontrado(s).")
            success = False
        finally:
            # Close connection with the database.
            connection_instance.close_connection()

        return success
    
    def delete_lent_book(self, cod_emprestimo):
        # Establish a connection with the database.
        connection_instance = db_connection()
        cursor = connection_instance.create_connection() # Cursor to perform operations in the database.
        
        # Delete a specific person from the database.
        cursor.execute(f"DELETE FROM emprestimos WHERE cod_emprestimo = {cod_emprestimo}")
        
        # Close connection.
        connection_instance.close_connection()

    def show_lent_books(self, twDatabase):
        # Establish a connection with the database.
        connection_instance = db_connection() 
        cursor = connection_instance.create_connection() # Cursor to perform operations in the database.
        cursor2 = cursor
        cursor3 = cursor
        # Get people informations in the database.
        cursor.execute(f"SELECT * FROM emprestimos") # Returns a tuple with the data in the database.

        # Show data in the user interface table.
        table_row = 0 # Variable to represent the row index.
        for database_row in cursor: # Iterate to get every line in the tuple.
            twDatabase.setRowCount(table_row+1)
            # Set the informations in the user interface table.
            twDatabase.setItem(table_row, 0, QTableWidgetItem(str(database_row[0])))
            twDatabase.setItem(table_row, 1, QTableWidgetItem(str(database_row[1])))
            twDatabase.setItem(table_row, 2, QTableWidgetItem(str(database_row[2])))
            cursor2.execute(f"SELECT nome FROM pessoas WHERE id_pessoa = '{database_row[1]}'")
            for select_row in cursor2:
                twDatabase.setItem(table_row, 3, QTableWidgetItem(str(select_row[0])))
            cursor3.execute(f"SELECT nome FROM livros WHERE id_livro = '{database_row[2]}'")
            for select_row in cursor2:
                twDatabase.setItem(table_row, 4, QTableWidgetItem(str(select_row[0])))
            table_row+=1

        # Close connection.
        connection_instance.close_connection()
