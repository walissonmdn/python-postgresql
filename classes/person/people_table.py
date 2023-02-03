from classes.database_connection import *
from psycopg2.errors import ForeignKeyViolation
from PyQt5.QtWidgets import QTableWidgetItem, QMainWindow, QMessageBox

# Class to represent a person and methods related to CRUD.
class person(QMainWindow):
    def __init__(self, nome, idade, cpf):
        super(person, self).__init__()
        self.nome = nome
        self.idade = idade
        self.cpf = cpf

    def insert_person(self):
        # Establish a connection with the database.
        connection_instance = db_connection()
        cursor = connection_instance.create_connection() # Cursor to perform operations in the database.

        # Insert a person in the database.
        cursor.execute(f"INSERT INTO pessoas (nome, idade, cpf) VALUES ('{self.nome}', {self.idade}, '{self.cpf}')")

        # Close connection.
        connection_instance.close_connection()
        
    def update_person(self, id_pessoa):
        # Establish a connection with the database.
        connection_instance = db_connection()
        cursor = connection_instance.create_connection() # Cursor to perform operations in the database.

        # Update informations of a person in the database.
        cursor.execute(f"UPDATE pessoas SET nome = '{self.nome}', idade = '{self.idade}', cpf = '{self.cpf}' where id_pessoa = {id_pessoa}")

        # Close connection.
        connection_instance.close_connection()

    def delete_person(self, id_pessoa):
        # Establish a connection with the database.
        connection_instance = db_connection()
        cursor = connection_instance.create_connection() # Cursor to perform operations in the database.
        
        # try-except block, because it won't be possible to delete the register of a person if she's borrowed a book.
        try:
            # Delete a specific person from the database.
            cursor.execute(f"DELETE FROM pessoas where id_pessoa = {id_pessoa}")
            success = True # Variable to indicate if the operation was executed successfully.
        except ForeignKeyViolation:
            # Return a message if the person's borrowed a book.
            QMessageBox.about(self, "Atenção!", "Não é possível deletar o registro da pessoa, pois existe um empréstimo realizado.")
            success = False
        finally:
            # Close connection with the database.
            connection_instance.close_connection()

        return success

    def show_people(self, twDatabase):
        # Establish a connection with the database.
        connection_instance = db_connection() 
        cursor = connection_instance.create_connection() # Cursor to perform operations in the database.

        # Get people informations in the database.
        cursor.execute(f"SELECT * FROM pessoas") # Returns a tuple with the data in the database.

        # Show data in the user interface table.
        table_row = 0 # Variable to represent the row index.
        for database_row in cursor: # Iterate to get every line in the tuple.
            twDatabase.setRowCount(table_row+1)
            # Set the informations in the user interface table.
            twDatabase.setItem(table_row, 0, QTableWidgetItem(str(database_row[0])))
            twDatabase.setItem(table_row, 1, QTableWidgetItem(database_row[1]))
            twDatabase.setItem(table_row, 2, QTableWidgetItem(str(database_row[2])))
            twDatabase.setItem(table_row, 3, QTableWidgetItem(database_row[3]))
            table_row+=1

        # Close connection.
        connection_instance.close_connection()


    