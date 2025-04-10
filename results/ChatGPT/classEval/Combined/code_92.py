import sqlite3

class UserLoginDB:
    """
    A class for managing user login verification using an SQLite database.
    Provides methods for user registration, lookup, deletion, and validation.
    """

    def __init__(self, db_name):
        """
        Initializes the UserLoginDB with the specified database name.
        :param db_name: str, the name of the SQLite database.
        """
        self.connection = sqlite3.connect(db_name)
        self.cursor = self.connection.cursor()
        self.create_table()

    def create_table(self):
        """Creates the users table if it does not exist."""
        create_table_query = """
        CREATE TABLE IF NOT EXISTS users (
            username TEXT PRIMARY KEY,
            password TEXT NOT NULL
        )
        """
        self.cursor.execute(create_table_query)
        self.connection.commit()

    def insert_user(self, username, password):
        """
        Inserts a new user into the "users" table.
        :param username: str, the username of the user.
        :param password: str, the password of the user.
        """
        insert_query = "INSERT INTO users (username, password) VALUES (?, ?)"
        self.cursor.execute(insert_query, (username, password))
        self.connection.commit()

    def search_user_by_username(self, username):
        """
        Searches for a user in the "users" table by username.
        :param username: str, the username of the user to search for.
        :return: tuple or None, the user record if found, otherwise None.
        """
        search_query = "SELECT username, password FROM users WHERE username = ?"
        self.cursor.execute(search_query, (username,))
        return self.cursor.fetchone()

    def delete_user_by_username(self, username):
        """
        Deletes a user from the "users" table by username.
        :param username: str, the username of the user to delete.
        """
        delete_query = "DELETE FROM users WHERE username = ?"
        self.cursor.execute(delete_query, (username,))
        self.connection.commit()

    def validate_user_login(self, username, password):
        """
        Validates if the provided credentials are correct.
        :param username: str, the username of the user to validate.
        :param password: str, the password of the user to validate.
        :return: bool, True if the user can log in, False otherwise.
        """
        user = self.search_user_by_username(username)
        return user is not None and user[1] == password

    def close(self):
        """Closes the database connection."""
        self.connection.close()