import sqlite3

class DatabaseProcessor:
    """
    A class for processing a SQLite database, supporting table creation, data insertion, 
    searching, and deletion.
    """

    def __init__(self, database_name):
        """
        Initialize the DatabaseProcessor with the specified database name.
        
        :param database_name: str, the name of the SQLite database file.
        """
        self.database_name = database_name

    def create_table(self, table_name, key1, key2):
        """
        Create a new table in the database if it doesn't exist.
        
        :param table_name: str, the name of the table to create.
        :param key1: str, the name of the first column in the table (TEXT).
        :param key2: str, the name of the second column in the table (INTEGER).
        """
        with sqlite3.connect(self.database_name) as conn:
            cursor = conn.cursor()
            cursor.execute(f"""
                CREATE TABLE IF NOT EXISTS {table_name} (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    {key1} TEXT,
                    {key2} INTEGER
                )
            """)

    def insert_into_database(self, table_name, data):
        """
        Insert data into the specified table in the database.
        
        :param table_name: str, the name of the table to insert data into.
        :param data: list of dicts, where each dict represents a row of data.
        """
        with sqlite3.connect(self.database_name) as conn:
            cursor = conn.cursor()
            for entry in data:
                cursor.execute(f"""
                    INSERT INTO {table_name} ({', '.join(entry.keys())}) 
                    VALUES ({', '.join(['?' for _ in entry])})
                """, tuple(entry.values()))

    def search_database(self, table_name, name):
        """
        Search the specified table for rows with a matching name.
        
        :param table_name: str, the name of the table to search.
        :param name: str, the name to search for.
        :return: list of tuples representing the rows with matching name, or None if not found.
        """
        with sqlite3.connect(self.database_name) as conn:
            cursor = conn.cursor()
            cursor.execute(f"SELECT * FROM {table_name} WHERE {name}=?", (name,))
            result = cursor.fetchall()
            return result if result else None

    def delete_from_database(self, table_name, name):
        """
        Delete rows from the specified table with a matching name.
        
        :param table_name: str, the name of the table to delete from.
        :param name: str, the name to match for deletion.
        """
        with sqlite3.connect(self.database_name) as conn:
            cursor = conn.cursor()
            cursor.execute(f"DELETE FROM {table_name} WHERE name=?", (name,))