import sqlite3

class BookManagementDB:
    """
    This is a database class as a book management system, used to handle the operations of adding, removing, updating, and searching books.
    """

    def __init__(self, db_name):
        """
        Initializes the class by creating a database connection and cursor,
        and creates the book table if it does not already exist.
        :param db_name: str, the name of db file
        """
        self.db_name = db_name  # Store db_name for potential future use
        self.connection = sqlite3.connect(db_name)
        self.cursor = self.connection.cursor()
        self.create_table()

    def create_table(self):
        """
        Creates the book table in the database if it does not already exist.
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
            # Consider raising the exception or handling it appropriately
            raise

    def add_book(self, title, author):
        """
        Adds a book to the database with the specified title and author,
        setting its availability to 1 as free to borrow.
        :param title: str, book title
        :param author: str, author name
        """
        try:
            self.cursor.execute("INSERT INTO books (title, author, available) VALUES (?, ?, ?)", (title, author, 1))
            self.connection.commit()
        except sqlite3.Error as e:
            print(f"Database error: {e}")
            self.connection.rollback()  # Rollback in case of error
            raise

    def remove_book(self, book_id):
        """
        Removes a book from the database based on the given book ID.
        :param book_id: int
        """
        try:
            self.cursor.execute("DELETE FROM books WHERE id = ?", (book_id,))
            self.connection.commit()
        except sqlite3.Error as e:
            print(f"Database error: {e}")
            self.connection.rollback()
            raise

    def borrow_book(self, book_id):
        """
        Marks a book as borrowed in the database based on the given book ID.
        :param book_id: int
        """
        try:
            self.cursor.execute("UPDATE books SET available = 0 WHERE id = ?", (book_id,))
            self.connection.commit()
        except sqlite3.Error as e:
            print(f"Database error: {e}")
            self.connection.rollback()
            raise

    def return_book(self, book_id):
        """
        Marks a book as returned in the database based on the given book ID.
        :param book_id: int
        """
        try:
            self.cursor.execute("UPDATE books SET available = 1 WHERE id = ?", (book_id,))
            self.connection.commit()
        except sqlite3.Error as e:
            print(f"Database error: {e}")
            self.connection.rollback()
            raise

    def search_books(self):
        """
        Retrieves all books from the database and returns their information.
        :return books: list[tuple], the information of all books in database
        """
        try:
            self.cursor.execute("SELECT * FROM books")
            books = self.cursor.fetchall()
            return books
        except sqlite3.Error as e:
            print(f"Database error: {e}")
            return []  # Or raise, depending on desired behavior

    def close_connection(self):
        """Closes the database connection."""
        if self.connection:
            self.connection.close()