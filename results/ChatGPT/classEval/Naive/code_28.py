import sqlite3
import pandas as pd

class DatabaseProcessor:
    """
    A class for processing a database, supporting table creation, data insertion,
    data searching by name, and data deletion.
    """

    def __init__(self, database_name):
        """
        Initialize the database processor with the specified database name.
        :param database_name: str, the name of the database file.
        """
        self.database_name = database_name
        self.connection = sqlite3.connect(self.database_name)
        self.cursor = self.connection.cursor()

    def create_table(self, table_name, key1, key2):
        """
        Create a new table in the database if it doesn't exist.
        :param table_name: str, the name of the table to create.
        :param key1: str, the name of the first column in the table.
        :param key2: str, the name of the second column in the table.
        """
        create_table_query = f"""
        CREATE TABLE IF NOT EXISTS {table_name} (
            id INTEGER PRIMARY KEY,
            {key1} TEXT,
            {key2} INTEGER
        );
        """
        self.cursor.execute(create_table_query)
        self.connection.commit()

    def insert_into_database(self, table_name, data):
        """
        Insert data into the specified table in the database.
        :param table_name: str, the name of the table to insert data into.
        :param data: list, a list of dictionaries where each dictionary represents a row of data.
        """
        for entry in data:
            columns = ', '.join(entry.keys())
            placeholders = ', '.join('?' * len(entry))
            insert_query = f"INSERT INTO {table_name} ({columns}) VALUES ({placeholders})"
            self.cursor.execute(insert_query, tuple(entry.values()))
        self.connection.commit()

    def search_database(self, table_name, name):
        """
        Search the specified table in the database for rows with a matching name.
        :param table_name: str, the name of the table to search.
        :param name: str, the name to search for.
        :return: list, a list of tuples representing the rows with the matching name, if any;
                otherwise, returns None.
        """
        search_query = f"SELECT * FROM {table_name} WHERE name = ?"
        self.cursor.execute(search_query, (name,))
        results = self.cursor.fetchall()
        return results if results else None

    def delete_from_database(self, table_name, name):
        """
        Delete rows from the specified table in the database with a matching name.
        :param table_name: str, the name of the table to delete rows from.
        :param name: str, the name to match for deletion.
        """
        delete_query = f"DELETE FROM {table_name} WHERE name = ?"
        self.cursor.execute(delete_query, (name,))
        self.connection.commit()

    def close(self):
        """Close the database connection."""
        self.connection.close()