import sqlite3

class BookManagementDB:
    """
    A database class for a book management system, handling operations for adding, removing, updating, and searching books.
    """

    def __init__(self, db_name):
        """
        Initializes the class by creating a database connection and cursor, 
        and creates the book table if it does not already exist.
        :param db_name: str, the name of the database file
        """
        self.connection = sqlite3.connect(db_name)
        self.cursor = self.connection.cursor()
        self.create_table()

    def create_table(self):
        """
        Creates the book table in the database if it does not already exist.
        """
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS books (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT NOT NULL,
                author TEXT NOT NULL,
                available INTEGER NOT NULL DEFAULT 1
            )
        ''')
        self.connection.commit()

    def add_book(self, title: str, author: str) -> None:
        """
        Adds a book to the database with the specified title and author, 
        setting its availability to 1 (available).
        :param title: str, book title
        :param author: str, author name
        """
        self.cursor.execute('''
            INSERT INTO books (title, author) VALUES (?, ?)
        ''', (title, author))
        self.connection.commit()

    def remove_book(self, book_id: int) -> None:
        """
        Removes a book from the database based on the given book ID.
        :param book_id: int, the ID of the book to remove
        """
        self.cursor.execute('''
            DELETE FROM books WHERE id = ?
        ''', (book_id,))
        self.connection.commit()

    def borrow_book(self, book_id: int) -> None:
        """
        Marks a book as borrowed in the database based on the given book ID.
        :param book_id: int, the ID of the book to borrow
        """
        self.cursor.execute('''
            UPDATE books SET available = 0 WHERE id = ?
        ''', (book_id,))
        self.connection.commit()

    def return_book(self, book_id: int) -> None:
        """
        Marks a book as returned in the database based on the given book ID.
        :param book_id: int, the ID of the book to return
        """
        self.cursor.execute('''
            UPDATE books SET available = 1 WHERE id = ?
        ''', (book_id,))
        self.connection.commit()

    def search_books(self) -> list:
        """
        Retrieves all books from the database and returns their information.
        :return: list[tuple], the information of all books in the database
        """
        self.cursor.execute('''
            SELECT * FROM books
        ''')
        return self.cursor.fetchall()

    def close(self) -> None:
        """
        Closes the database connection.
        """
        self.connection.close()