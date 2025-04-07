import sqlite3

class DatabaseProcessor:
    """
    This is a class for processing a database, supporting to create tables, insert data into the database, 
    search for data based on name, and delete data from the database.
    """

    def __init__(self, database_name):
        """
        Initialize database name of database processor.
        """
        self.database_name = database_name

    def create_table(self, table_name, key1, key2):
        """
        Create a new table in the database if it doesn't exist.
        Make id (INTEGER) as PRIMARY KEY, make key1 as TEXT, key2 as INTEGER.
        
        :param table_name: str, the name of the table to create.
        :param key1: str, the name of the first column in the table.
        :param key2: str, the name of the second column in the table.
        """
        with sqlite3.connect(self.database_name) as conn:
            cursor = conn.cursor()
            cursor.execute(f'''
                CREATE TABLE IF NOT EXISTS {table_name} (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    {key1} TEXT,
                    {key2} INTEGER
                )
            ''')
            conn.commit()

    def insert_into_database(self, table_name, data):
        """
        Insert data into the specified table in the database.
        
        :param table_name: str, the name of the table to insert data into.
        :param data: list, a list of dictionaries where each dictionary represents a row of data.
        """
        with sqlite3.connect(self.database_name) as conn:
            cursor = conn.cursor()
            for row in data:
                cursor.execute(f'''
                    INSERT INTO {table_name} ({', '.join(row.keys())})
                    VALUES ({', '.join(['?'] * len(row))})
                ''', tuple(row.values()))
            conn.commit()

    def search_database(self, table_name, name):
        """
        Search the specified table in the database for rows with a matching name.
        
        :param table_name: str, the name of the table to search.
        :param name: str, the name to search for.
        :return: list, a list of tuples representing the rows with matching name, if any; otherwise, returns None.
        """
        with sqlite3.connect(self.database_name) as conn:
            cursor = conn.cursor()
            cursor.execute(f'SELECT * FROM {table_name} WHERE {table_name.split("_")[0]} = ?', (name,))
            results = cursor.fetchall()
            return results if results else None

    def delete_from_database(self, table_name, name):
        """
        Delete rows from the specified table in the database with a matching name.
        
        :param table_name: str, the name of the table to delete rows from.
        :param name: str, the name to match for deletion.
        """
        with sqlite3.connect(self.database_name) as conn:
            cursor = conn.cursor()
            cursor.execute(f'DELETE FROM {table_name} WHERE {table_name.split("_")[0]} = ?', (name,))
            conn.commit()