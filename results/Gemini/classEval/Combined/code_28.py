import sqlite3
import pandas as pd

class DatabaseProcessor:
    """
    This is a class for processing a database, supporting to create tables, insert data into the database, search for data based on name, and delete data from the database.
    """


    def __init__(self, database_name):
        """
        Initialize database name of database processor
        """
        self.database_name = database_name


    def _execute_query(self, query, params=None):
        """
        Helper function to execute SQL queries with error handling and connection management.
        """
        conn = None
        cursor = None
        try:
            conn = sqlite3.connect(self.database_name)
            cursor = conn.cursor()
            if params:
                cursor.execute(query, params)
            else:
                cursor.execute(query)
            conn.commit()
            return cursor
        except sqlite3.Error as e:
            print(f"Database error: {e}")
            if conn:
                conn.rollback()  # Rollback in case of error
            return None
        finally:
            if cursor:
                cursor.close()
            if conn:
                conn.close()


    def create_table(self, table_name, key1, key2):
        """
        Create a new table in the database if it doesn't exist.
        And make id (INTEGER) as PRIMARY KEY, make key1 as TEXT, key2 as INTEGER
        :param table_name: str, the name of the table to create.
        :param key1: str, the name of the first column in the table.
        :param key2: str, the name of the second column in the table.
        >>> db.create_table('user', 'name', 'age')
        """
        query = f"""
            CREATE TABLE IF NOT EXISTS {table_name} (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                {key1} TEXT,
                {key2} INTEGER
            )
        """
        self._execute_query(query)


    def insert_into_database(self, table_name, data):
        """
        Insert data into the specified table in the database.
        :param table_name: str, the name of the table to insert data into.
        :param data: list, a list of dictionaries where each dictionary represents a row of data.
        >>> db.insert_into_database('user', [
                {'name': 'John', 'age': 25},
                {'name': 'Alice', 'age': 30}
            ])
        """
        for row in data:
            columns = ', '.join(row.keys())
            placeholders = ', '.join(['?'] * len(row))
            values = tuple(row.values())

            query = f"INSERT INTO {table_name} ({columns}) VALUES ({placeholders})"
            self._execute_query(query, values)


    def search_database(self, table_name, name):
        """
        Search the specified table in the database for rows with a matching name.
        :param table_name: str, the name of the table to search.
        :param name: str, the name to search for.
        :return: list, a list of tuples representing the rows with matching name, if any;
                    otherwise, returns None.
        >>> db.search_database('user', 'John')
        [(1, 'John', 25)]
        """
        query = f"SELECT * FROM {table_name} WHERE name=?"
        cursor = self._execute_query(query, (name,))

        if cursor:
            result = cursor.fetchall()
            return result if result else None
        else:
            return None


    def delete_from_database(self, table_name, name):
        """
        Delete rows from the specified table in the database with a matching name.
        :param table_name: str, the name of the table to delete rows from.
        :param name: str, the name to match for deletion.
        >>> db.delete_from_database('user', 'John')
        """
        query = f"DELETE FROM {table_name} WHERE name=?"
        self._execute_query(query, (name,))