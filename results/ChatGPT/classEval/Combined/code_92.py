import sqlite3
from contextlib import closing

class UserLoginDB:
    """
    A database management class for user login verification,
    providing functions for inserting, searching, deleting users,
    and validating user login.
    """

    def __init__(self, db_name):
        """
        Initializes the UserLoginDB object with the specified database name.
        :param db_name: str, the name of the SQLite database.
        """
        self.db_name = db_name
        self.create_table()

    def create_table(self):
        """Creates the users table if it does not exist."""
        with closing(self._get_connection()) as connection:
            cursor = connection.cursor()
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS users (
                    username TEXT PRIMARY KEY,
                    password TEXT
                )
            """)
            connection.commit()

    def insert_user(self, username, password):
        """
        Inserts a new user into the "users" table.
        :param username: str, the username of the user.
        :param password: str, the password of the user.
        """
        with closing(self._get_connection()) as connection:
            cursor = connection.cursor()
            cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, password))
            connection.commit()

    def search_user_by_username(self, username):
        """
        Searches for users in the "users" table by username.
        :param username: str, the username of the user to search for.
        :return: list of tuples, the rows from the "users" table that match the search criteria.
        """
        with closing(self._get_connection()) as connection:
            cursor = connection.cursor()
            cursor.execute("SELECT username, password FROM users WHERE username = ?", (username,))
            return cursor.fetchall()

    def delete_user_by_username(self, username):
        """
        Deletes a user from the "users" table by username.
        :param username: str, the username of the user to delete.
        """
        with closing(self._get_connection()) as connection:
            cursor = connection.cursor()
            cursor.execute("DELETE FROM users WHERE username = ?", (username,))
            connection.commit()

    def validate_user_login(self, username, password):
        """
        Validates the user's login credentials.
        :param username: str, the username of the user to validate.
        :param password: str, the password of the user to validate.
        :return: bool, whether the user can log in correctly.
        """
        with closing(self._get_connection()) as connection:
            cursor = connection.cursor()
            cursor.execute("SELECT password FROM users WHERE username = ?", (username,))
            result = cursor.fetchone()
            return result is not None and result[0] == password

    def _get_connection(self):
        """Establishes a new database connection."""
        return sqlite3.connect(self.db_name)

    def close(self):
        """Closes the database connection."""
        # No need for explicit close here as we use context manager.
        pass