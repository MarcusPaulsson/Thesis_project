import sqlite3
import hashlib

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
        """Connects to the database."""
        try:
            self.connection = sqlite3.connect(self.db_name)
            self.cursor = self.connection.cursor()
        except sqlite3.Error as e:
            print(f"Database connection error: {e}")
            raise

    def create_table(self):
        """
        Creates the "users" table if it does not already exist.
        """
        try:
            self.cursor.execute("""
                CREATE TABLE IF NOT EXISTS users (
                    username TEXT PRIMARY KEY,
                    password TEXT
                )
            """)
            self.connection.commit()
        except sqlite3.Error as e:
            print(f"Database table creation error: {e}")
            raise

    def _hash_password(self, password):
        """Hashes the password using SHA-256."""
        hashed_password = hashlib.sha256(password.encode('utf-8')).hexdigest()
        return hashed_password

    def insert_user(self, username, password):
        """
        Inserts a new user into the "users" table.
        :param username: str, the username of the user.
        :param password: str, the password of the user.
        :return: None
        """
        try:
            hashed_password = self._hash_password(password)
            self.cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, hashed_password))
            self.connection.commit()
        except sqlite3.IntegrityError:
            print(f"Username '{username}' already exists.")
            raise
        except sqlite3.Error as e:
            print(f"Database insertion error: {e}")
            raise

    def search_user_by_username(self, username):
        """
        Searches for users in the "users" table by username.
        :param username: str, the username of the user to search for.
        :return:list of tuples, the rows from the "users" table that match the search criteria.
        """
        try:
            self.cursor.execute("SELECT * FROM users WHERE username = ?", (username,))
            return self.cursor.fetchall()
        except sqlite3.Error as e:
            print(f"Database search error: {e}")
            raise

    def delete_user_by_username(self, username):
        """
        Deletes a user from the "users" table by username.
        :param username: str, the username of the user to delete.
        :return: None
        """
        try:
            self.cursor.execute("DELETE FROM users WHERE username = ?", (username,))
            self.connection.commit()
        except sqlite3.Error as e:
            print(f"Database deletion error: {e}")
            raise

    def validate_user_login(self, username, password):
        """
        Determine whether the user can log in, that is, the user is in the database and the password is correct
        :param username:str, the username of the user to validate.
        :param password:str, the password of the user to validate.
        :return:bool, representing whether the user can log in correctly
        """
        try:
            self.cursor.execute("SELECT password FROM users WHERE username = ?", (username,))
            result = self.cursor.fetchone()

            if result:
                hashed_password = result[0]
                return self._hash_password(password) == hashed_password
            else:
                return False
        except sqlite3.Error as e:
            print(f"Database validation error: {e}")
            raise


    def close(self):
        """
        Closes the database connection.
        """
        if self.connection:
            self.connection.close()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close()


if __name__ == '__main__':
    # Example Usage (without doctests for brevity)
    try:
        with UserLoginDB("user_database.db") as user_db:
            # Insert a user
            try:
                user_db.insert_user('testuser', 'securepassword')
            except sqlite3.IntegrityError:
                print("User already exists.")


            # Validate login
            if user_db.validate_user_login('testuser', 'securepassword'):
                print("Login successful!")
            else:
                print("Login failed.")

            # Search for the user
            user = user_db.search_user_by_username('testuser')
            print(f"User found: {user}")

            # Delete the user
            user_db.delete_user_by_username('testuser')
            print("User deleted.")

    except Exception as e:
        print(f"An error occurred: {e}")