import sqlite3
from contextlib import closing

class DatabaseProcessor:
    """
    A class for processing a SQLite database, supporting creating tables, inserting data,
    searching for data by name, and deleting data from the database.
    """

    def __init__(self, database_name):
        """
        Initialize the database processor with the specified database name.
        """
        self.database_name = database_name

    def __enter__(self):
        """Enable use of 'with' statement for automatic resource management."""
        self.connection = sqlite3.connect(self.database_name)
        self.cursor = self.connection.cursor()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        """Ensure the database connection is closed properly."""
        self.close()

    def create_table(self, table_name, key1, key2):
        """
        Create a new table in the database if it doesn't exist.
        :param table_name: str, the name of the table to create.
        :param key1: str, the name of the first column in the table.
        :param key2: str, the name of the second column in the table.
        """
        self.cursor.execute(f"""
            CREATE TABLE IF NOT EXISTS {table_name} (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                {key1} TEXT,
                {key2} INTEGER
            )
        """)
        self.connection.commit()

    def insert_into_database(self, table_name, data):
        """
        Insert data into the specified table in the database.
        :param table_name: str, the name of the table to insert data into.
        :param data: list, a list of dictionaries where each dictionary represents a row of data.
        """
        if not data:
            return

        columns = data[0].keys()
        placeholders = ', '.join('?' * len(columns))
        self.cursor.executemany(f"""
            INSERT INTO {table_name} ({', '.join(columns)})
            VALUES ({placeholders})
        """, [tuple(entry.values()) for entry in data])
        self.connection.commit()

    def search_database(self, table_name, name):
        """
        Search the specified table in the database for rows with a matching name.
        :param table_name: str, the name of the table to search.
        :param name: str, the name to search for.
        :return: list, a list of tuples representing the rows with matching name, or an empty list if none found.
        """
        self.cursor.execute(f"SELECT * FROM {table_name} WHERE name = ?", (name,))
        return self.cursor.fetchall() or []

    def delete_from_database(self, table_name, name):
        """
        Delete rows from the specified table in the database with a matching name.
        :param table_name: str, the name of the table to delete rows from.
        :param name: str, the name to match for deletion.
        """
        self.cursor.execute(f"DELETE FROM {table_name} WHERE name = ?", (name,))
        self.connection.commit()

    def close(self):
        """Close the database connection."""
        if self.connection:
            self.connection.close()