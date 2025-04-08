import sqlite3

class UserLoginDB:
    """
    This is a database management class for user login verification, providing functions for inserting user information, searching user information, deleting user information, and validating user login.
    """

    def __init__(self, db_name):
        """
        Initializes the UserLoginDB object with the specified database name.
        :param db_name: str, the name of the SQLite database.
        """
        self.db_name = db_name
        self.connection = sqlite3.connect(db_name)
        self.cursor = self.connection.cursor()
        self._create_table()

    def _create_table(self):
        """
        Creates the 'users' table if it doesn't exist.
        """
        try:
            query = """
            CREATE TABLE IF NOT EXISTS users (
                username TEXT PRIMARY KEY,
                password TEXT
            )
            """
            self.cursor.execute(query)
            self.connection.commit()
        except sqlite3.Error as e:
            print(f"Database error: {e}")
            raise

    def insert_user(self, username, password):
        """
        Inserts a new user into the "users" table.
        :param username: str, the username of the user.
        :param password: str, the password of the user.
        :return: None
        """
        try:
            query = "INSERT INTO users (username, password) VALUES (?, ?)"
            self.cursor.execute(query, (username, password))
            self.connection.commit()
        except sqlite3.Error as e:
            print(f"Database error: {e}")
            raise

    def search_user_by_username(self, username):
        """
        Searches for users in the "users" table by username.
        :param username: str, the username of the user to search for.
        :return: tuple or None: A tuple containing (username, password) if the user is found, otherwise None.
        """
        try:
            query = "SELECT username, password FROM users WHERE username = ?"
            self.cursor.execute(query, (username,))
            return self.cursor.fetchone()
        except sqlite3.Error as e:
            print(f"Database error: {e}")
            raise

    def delete_user_by_username(self, username):
        """
        Deletes a user from the "users" table by username.
        :param username: str, the username of the user to delete.
        :return: None
        """
        try:
            query = "DELETE FROM users WHERE username = ?"
            self.cursor.execute(query, (username,))
            self.connection.commit()
        except sqlite3.Error as e:
            print(f"Database error: {e}")
            raise

    def validate_user_login(self, username, password):
        """
        Validates user login by checking if the user exists and the password matches.
        :param username: str, the username of the user to validate.
        :param password: str, the password of the user to validate.
        :return: bool, True if the user can log in, False otherwise.
        """
        user = self.search_user_by_username(username)
        return user is not None and user[1] == password

    def close(self):
        """Closes the database connection."""
        self.connection.close()