import sqlite3

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
        self.connection = sqlite3.connect(db_name)
        self.cursor = self.connection.cursor()
        self.create_table()

    def create_table(self):
        """
        Creates the users table if it doesn't already exist.
        """
        create_table_query = """
            CREATE TABLE IF NOT EXISTS users (
                username TEXT PRIMARY KEY,
                password TEXT
            )
        """
        self.cursor.execute(create_table_query)
        self.connection.commit()

    def insert_user(self, username, password):
        """
        Inserts a new user into the "users" table.
        :param username: str, the username of the user.
        :param password: str, the password of the user.
        :return: None
        """
        try:
            self.cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, password))
            self.connection.commit()
        except sqlite3.IntegrityError:
            pass  # Handle duplicate username error if necessary

    def search_user_by_username(self, username):
        """
        Searches for users in the "users" table by username.
        :param username: str, the username of the user to search for.
        :return: list of tuples, the rows from the "users" table that match the search criteria.
        """
        self.cursor.execute("SELECT username, password FROM users WHERE username = ?", (username,))
        return self.cursor.fetchone()

    def delete_user_by_username(self, username):
        """
        Deletes a user from the "users" table by username.
        :param username: str, the username of the user to delete.
        :return: None
        """
        self.cursor.execute("DELETE FROM users WHERE username = ?", (username,))
        self.connection.commit()

    def validate_user_login(self, username, password):
        """
        Determine whether the user can log in, that is, the user is in the database and the password is correct.
        :param username: str, the username of the user to validate.
        :param password: str, the password of the user to validate.
        :return: bool, representing whether the user can log in correctly.
        """
        user = self.search_user_by_username(username)
        if user and user[1] == password:
            return True
        return False

    def close(self):
        """
        Closes the database connection.
        """
        self.connection.close()