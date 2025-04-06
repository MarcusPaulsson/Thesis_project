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
        """Connects to the SQLite database."""
        try:
            self.connection = sqlite3.connect(self.db_name)
            self.cursor = self.connection.cursor()
        except sqlite3.Error as e:
            print(f"Database connection error: {e}")
            raise

    def close(self):
        """Closes the database connection."""
        if self.connection:
            self.connection.close()

    def create_table(self):
        """Creates the 'users' table if it doesn't exist."""
        try:
            self.cursor.execute("""
                CREATE TABLE IF NOT EXISTS users (
                    username TEXT PRIMARY KEY,
                    password TEXT NOT NULL
                )
            """)
            self.connection.commit()
        except sqlite3.Error as e:
            print(f"Table creation error: {e}")
            raise

    def insert_user(self, username, password):
        """
        Inserts a new user into the "users" table.
        :param username: str, the username of the user.
        :param password: str, the password of the user.
        :return: None
        >>> user_db = UserLoginDB("user_database.db")
        >>> user_db.create_table()
        >>> user_db.insert_user('user1', 'pass1')
        """
        try:
            self.cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, password))
            self.connection.commit()
        except sqlite3.Error as e:
            print(f"Insert error: {e}")
            raise

    def search_user_by_username(self, username):
        """
        Searches for users in the "users" table by username.
        :param username: str, the username of the user to search for.
        :return:list of tuples, the rows from the "users" table that match the search criteria.
        >>> user_db = UserLoginDB("user_database.db")
        >>> user_db.create_table()
        >>> user_db.insert_user('user1', 'pass1')
        >>> result = user_db.search_user_by_username('user1')
        len(result) = 1
        """
        try:
            self.cursor.execute("SELECT * FROM users WHERE username = ?", (username,))
            result = self.cursor.fetchall()
            return result
        except sqlite3.Error as e:
            print(f"Search error: {e}")
            raise

    def delete_user_by_username(self, username):
        """
        Deletes a user from the "users" table by username.
        :param username: str, the username of the user to delete.
        :return: None
        >>> user_db = UserLoginDB("user_database.db")
        >>> user_db.create_table()
        >>> user_db.insert_user('user1', 'pass1')
        >>> user_db.delete_user_by_username('user1')
        """
        try:
            self.cursor.execute("DELETE FROM users WHERE username = ?", (username,))
            self.connection.commit()
        except sqlite3.Error as e:
            print(f"Delete error: {e}")
            raise

    def validate_user_login(self, username, password):
        """
        Determine whether the user can log in, that is, the user is in the database and the password is correct
        :param username:str, the username of the user to validate.
        :param password:str, the password of the user to validate.
        :return:bool, representing whether the user can log in correctly
        >>> user_db = UserLoginDB("user_database.db")
        >>> user_db.create_table()
        >>> user_db.insert_user('user1', 'pass1')
        >>> user_db.validate_user_login('user1', 'pass1')
        True
        """
        try:
            self.cursor.execute("SELECT * FROM users WHERE username = ? AND password = ?", (username, password))
            result = self.cursor.fetchone()
            return result is not None
        except sqlite3.Error as e:
            print(f"Validation error: {e}")
            raise

if __name__ == '__main__':
    import doctest
    doctest.testmod()