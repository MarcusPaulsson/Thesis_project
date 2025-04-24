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
        self.connection = None
        self.cursor = None
        self.connect()
        self.create_table()

    def connect(self):
        """
        Establishes a connection to the SQLite database.
        """
        try:
            self.connection = sqlite3.connect(self.db_name)
            self.cursor = self.connection.cursor()
        except sqlite3.Error as e:
            print(f"Database connection error: {e}")
            raise

    def close(self):
        """
        Closes the database connection.
        """
        if self.connection:
            self.connection.close()

    def create_table(self):
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
            print(f"Error creating table: {e}")
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
        except sqlite3.IntegrityError:
            print(f"Username '{username}' already exists.")
            return False
        except sqlite3.Error as e:
            print(f"Error inserting user: {e}")
            self.connection.rollback()
            return False
        return True

    def search_user_by_username(self, username):
        """
        Searches for users in the "users" table by username.
        :param username: str, the username of the user to search for.
        :return: tuple, the row from the "users" table that matches the search criteria, or None if not found.
        """
        try:
            query = "SELECT username, password FROM users WHERE username = ?"
            self.cursor.execute(query, (username,))
            result = self.cursor.fetchone()
            return result
        except sqlite3.Error as e:
            print(f"Error searching user: {e}")
            return None

    def delete_user_by_username(self, username):
        """
        Deletes a user from the "users" table by username.
        :param username: str, the username of the user to delete.
        :return: True if deleted, False otherwise
        """
        try:
            query = "DELETE FROM users WHERE username = ?"
            self.cursor.execute(query, (username,))
            self.connection.commit()
            return self.connection.total_changes > 0 # Check if any rows were actually deleted
        except sqlite3.Error as e:
            print(f"Error deleting user: {e}")
            self.connection.rollback()
            return False

    def validate_user_login(self, username, password):
        """
        Determine whether the user can log in, that is, the user is in the database and the password is correct
        :param username:str, the username of the user to validate.
        :param password:str, the password of the user to validate.
        :return:bool, representing whether the user can log in correctly
        """
        try:
            query = "SELECT password FROM users WHERE username = ?"
            self.cursor.execute(query, (username,))
            result = self.cursor.fetchone()

            if result:
                return result[0] == password
            else:
                return False
        except sqlite3.Error as e:
            print(f"Error validating user: {e}")
            return False