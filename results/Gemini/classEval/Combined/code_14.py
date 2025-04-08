import sqlite3

class BookManagementDB:
    """
    Manages book operations in a SQLite database.
    """

    def __init__(self, db_name):
        """
        Initializes the database connection and creates the books table if it doesn't exist.

        Args:
            db_name (str): The name of the SQLite database file.
        """
        self.db_name = db_name
        self.connection = sqlite3.connect(db_name)
        self.cursor = self.connection.cursor()
        self._create_table()  # Use underscore to indicate it's a 'private' method

    def _create_table(self):
        """
        Creates the 'books' table if it doesn't already exist.
        """
        try:
            self.cursor.execute("""
                CREATE TABLE IF NOT EXISTS books (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    title TEXT NOT NULL,
                    author TEXT NOT NULL,
                    available INTEGER NOT NULL DEFAULT 1
                )
            """)
            self.connection.commit()
        except sqlite3.Error as e:
            print(f"Database error: {e}")
            raise

    def add_book(self, title, author):
        """
        Adds a new book to the database.

        Args:
            title (str): The title of the book.
            author (str): The author of the book.
        """
        try:
            self.cursor.execute("""
                INSERT INTO books (title, author, available) VALUES (?, ?, ?)
            """, (title, author, 1))
            self.connection.commit()
        except sqlite3.Error as e:
            print(f"Database error: {e}")
            raise

    def remove_book(self, book_id):
        """
        Removes a book from the database based on its ID.

        Args:
            book_id (int): The ID of the book to remove.
        """
        try:
            self.cursor.execute("""
                DELETE FROM books WHERE id = ?
            """, (book_id,))
            self.connection.commit()
        except sqlite3.Error as e:
            print(f"Database error: {e}")
            raise

    def borrow_book(self, book_id):
        """
        Marks a book as borrowed (unavailable).

        Args:
            book_id (int): The ID of the book to borrow.
        """
        try:
            self.cursor.execute("""
                UPDATE books SET available = 0 WHERE id = ?
            """, (book_id,))
            self.connection.commit()
        except sqlite3.Error as e:
            print(f"Database error: {e}")
            raise

    def return_book(self, book_id):
        """
        Marks a book as returned (available).

        Args:
            book_id (int): The ID of the book to return.
        """
        try:
            self.cursor.execute("""
                UPDATE books SET available = 1 WHERE id = ?
            """, (book_id,))
            self.connection.commit()
        except sqlite3.Error as e:
            print(f"Database error: {e}")
            raise

    def search_books(self):
        """
        Retrieves all books from the database.

        Returns:
            list: A list of tuples, where each tuple represents a book
                  (id, title, author, available).
        """
        try:
            self.cursor.execute("""
                SELECT * FROM books
            """)
            books = self.cursor.fetchall()
            return books
        except sqlite3.Error as e:
            print(f"Database error: {e}")
            raise

    def close_connection(self):
        """
        Closes the database connection.  It's good practice to close the connection
        when you're done with the database.
        """
        if self.connection:
            self.connection.close()