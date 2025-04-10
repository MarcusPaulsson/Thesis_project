import sqlite3


class DatabaseProcessor:
    """
    A class for processing a SQLite database, supporting table creation, data insertion,
    searching, and deletion.
    """

    def __init__(self, database_name):
        """
        Initialize the DatabaseProcessor with the specified database name.
        :param database_name: str, the name of the SQLite database.
        """
        self.database_name = database_name

    def _execute_query(self, query, params=(), fetch=False):
        """Execute a query and optionally fetch results."""
        with sqlite3.connect(self.database_name) as conn:
            cursor = conn.cursor()
            cursor.execute(query, params)
            if fetch:
                return cursor.fetchall()

    def create_table(self, table_name, key1, key2):
        """
        Create a new table in the database if it doesn't exist.
        :param table_name: str, the name of the table to create.
        :param key1: str, the name of the first column in the table.
        :param key2: str, the name of the second column in the table.
        """
        create_table_query = f"""
        CREATE TABLE IF NOT EXISTS {table_name} (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            {key1} TEXT NOT NULL,
            {key2} INTEGER NOT NULL
        );
        """
        self._execute_query(create_table_query)

    def insert_into_database(self, table_name, data):
        """
        Insert data into the specified table in the database.
        :param table_name: str, the name of the table to insert data into.
        :param data: list, a list of dictionaries where each dictionary represents a row of data.
        """
        insert_query = f"INSERT INTO {table_name} (name, age) VALUES (?, ?)"
        for item in data:
            self._execute_query(insert_query, (item['name'], item['age']))

    def search_database(self, table_name, name):
        """
        Search the specified table in the database for rows with a matching name.
        :param table_name: str, the name of the table to search.
        :param name: str, the name to search for.
        :return: list or None, a list of tuples representing the rows with matching name, if any.
        """
        search_query = f"SELECT * FROM {table_name} WHERE name = ?"
        result = self._execute_query(search_query, (name,), fetch=True)
        return result if result else None

    def delete_from_database(self, table_name, name):
        """
        Delete rows from the specified table in the database with a matching name.
        :param table_name: str, the name of the table to delete rows from.
        :param name: str, the name to match for deletion.
        """
        delete_query = f"DELETE FROM {table_name} WHERE name = ?"
        self._execute_query(delete_query, (name,))