import sqlite3
from contextlib import closing

class UserLoginDB:
    """
    This is a database management class for user login verification, providing functions for inserting user information, 
    searching user information, deleting user information, and validating user login.
    """

    def __init__(self, db_name):
        """
        Initializes the UserLoginDB object with the specified database name.
        :param db_name: str, the name of the SQLite database.
        """
        self.db_name = db_name
        self.create_table()

    def create_table(self):
        """
        Creates the "users" table if it does not exist.
        """
        with closing(self.connect()) as conn:
            cursor = conn.cursor()
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS users (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    username TEXT UNIQUE NOT NULL,
                    password TEXT NOT NULL
                )
            ''')
            conn.commit()

    def connect(self):
        """
        Establish a new database connection.
        :return: sqlite3.Connection
        """
        return sqlite3.connect(self.db_name)

    def insert_user(self, username, password):
        """
        Inserts a new user into the "users" table.
        :param username: str, the username of the user.
        :param password: str, the password of the user.
        :return: None
        """
        with closing(self.connect()) as conn:
            cursor = conn.cursor()
            try:
                cursor.execute('''
                    INSERT INTO users (username, password)
                    VALUES (?, ?)
                ''', (username, password))
                conn.commit()
            except sqlite3.IntegrityError:
                print(f"User '{username}' already exists.")

    def search_user_by_username(self, username):
        """
        Searches for users in the "users" table by username.
        :param username: str, the username of the user to search for.
        :return: list of tuples, the rows from the "users" table that match the search criteria.
        """
        with closing(self.connect()) as conn:
            cursor = conn.cursor()
            cursor.execute('''
                SELECT * FROM users WHERE username = ?
            ''', (username,))
            return cursor.fetchall()

    def delete_user_by_username(self, username):
        """
        Deletes a user from the "users" table by username.
        :param username: str, the username of the user to delete.
        :return: None
        """
        with closing(self.connect()) as conn:
            cursor = conn.cursor()
            cursor.execute('''
                DELETE FROM users WHERE username = ?
            ''', (username,))
            conn.commit()

    def validate_user_login(self, username, password):
        """
        Determine whether the user can log in, that is, the user is in the database and the password is correct.
        :param username: str, the username of the user to validate.
        :param password: str, the password of the user to validate.
        :return: bool, representing whether the user can log in correctly.
        """
        with closing(self.connect()) as conn:
            cursor = conn.cursor()
            cursor.execute('''
                SELECT * FROM users WHERE username = ? AND password = ?
            ''', (username, password))
            return cursor.fetchone() is not None

    def close(self):
        """
        Closes the database connection. (Not needed with context management)
        """
        pass