import sqlite3

class DatabaseProcessor:
    """
    A class for processing a SQLite database, supporting the creation of tables, 
    inserting data, searching for data based on name, and deleting data from the database.
    """

    def __init__(self, database_name):
        """
        Initialize the database processor with a specified database name.
        """
        self.database_name = database_name

    def create_table(self, table_name: str, key1: str, key2: str):
        """ 
        Create a new table in the database if it doesn't exist.
        Each table will have an id (INTEGER) as PRIMARY KEY, key1 as TEXT, and key2 as INTEGER.
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

    def insert_into_database(self, table_name: str, data: list):
        """ 
        Insert data into the specified table in the database.
        Each entry in data should be a dictionary with keys matching the table columns.
        """
        with sqlite3.connect(self.database_name) as conn:
            cursor = conn.cursor()
            cursor.executemany(f"""
                INSERT INTO {table_name} (name, age) 
                VALUES (?, ?)
            """, [(entry['name'], entry['age']) for entry in data])

    def search_database(self, table_name: str, name: str):
        """ 
        Search the specified table for rows with a matching name.
        Returns a list of tuples representing the rows or None if not found.
        """
        with sqlite3.connect(self.database_name) as conn:
            cursor = conn.cursor()
            cursor.execute(f"SELECT * FROM {table_name} WHERE name = ?", (name,))
            result = cursor.fetchall()
            return result if result else None

    def delete_from_database(self, table_name: str, name: str):
        """ 
        Delete rows from the specified table with a matching name.
        """
        with sqlite3.connect(self.database_name) as conn:
            cursor = conn.cursor()
            cursor.execute(f"DELETE FROM {table_name} WHERE name = ?", (name,))