import json
import psycopg2

class db_connection:
    def __init__(self):
        # Open json to get database connection informations.
        json_file = open("parameters.json")
        connection_informations = json.load(json_file)

        # Assign values in the json to variables.
        self.dbname = connection_informations["dbname"]
        self.user = connection_informations["user"]
        self.password = connection_informations["password"]
        self.host = connection_informations["host"]
        self.port = connection_informations["port"]

        # Close json file.
        json_file.close()

    def create_connection(self):
        # Create connection string.
        self.connection_string = "dbname={0} user={1} password={2} host={3} port={4}".format(self.dbname, self.user, self.password, self.host, self.port)
        
        # Connect to the database.
        self.connection = psycopg2.connect(self.connection_string) 
        self.cursor = self.connection.cursor() # Open a cursor to perform operations.

        # Return cursor to perform operations.
        return self.cursor 

    def close_connection(self):
        # Make changes to the database persistent.
        self.connection.commit()
        
        # Close the communication with the database.
        self.cursor.close()
        self.connection.close()
