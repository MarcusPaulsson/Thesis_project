import sqlite3
from contextlib import closing

class BookManagementDB:
    """
    This is a database class for a book management system, used to handle the operations of adding, removing, updating, and searching books.
    """

    def __init__(self, db_name):
        """
        Initializes the class by creating a database connection,
        and creates the book table if it does not already exist.
        :param db_name: str, the name of the database file
        """
        self.db_name = db_name
        with closing(self.connect()) as conn:
            self.create_table(conn)

    def connect(self):
        """
        Establishes and returns a new database connection.
        :return: sqlite3.Connection
        """
        return sqlite3.connect(self.db_name)

    def create_table(self, conn):
        """
        Creates the book table in the database if it does not already exist.
        :param conn: sqlite3.Connection, the database connection
        """
        with conn:
            conn.execute('''
                CREATE TABLE IF NOT EXISTS books (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    title TEXT NOT NULL,
                    author TEXT NOT NULL,
                    available INTEGER NOT NULL DEFAULT 1
                )
            ''')

    def add_book(self, title, author):
        """
        Adds a book to the database with the specified title and author,
        setting its availability to 1 as free to borrow.
        :param title: str, book title
        :param author: str, author name
        """
        with closing(self.connect()) as conn:
            with conn:
                conn.execute('''
                    INSERT INTO books (title, author) 
                    VALUES (?, ?)
                ''', (title, author))

    def remove_book(self, book_id):
        """
        Removes a book from the database based on the given book ID.
        :param book_id: int
        """
        with closing(self.connect()) as conn:
            with conn:
                conn.execute('''
                    DELETE FROM books WHERE id = ?
                ''', (book_id,))

    def borrow_book(self, book_id):
        """
        Marks a book as borrowed in the database based on the given book ID.
        :param book_id: int
        """
        with closing(self.connect()) as conn:
            with conn:
                conn.execute('''
                    UPDATE books SET available = 0 WHERE id = ?
                ''', (book_id,))

    def return_book(self, book_id):
        """
        Marks a book as returned in the database based on the given book ID.
        :param book_id: int
        """
        with closing(self.connect()) as conn:
            with conn:
                conn.execute('''
                    UPDATE books SET available = 1 WHERE id = ?
                ''', (book_id,))

    def search_books(self):
        """
        Retrieves all books from the database and returns their information.
        :return: list[tuple], the information of all books in the database
        """
        with closing(self.connect()) as conn:
            cursor = conn.execute('SELECT * FROM books')
            return cursor.fetchall()

    def close(self):
        """
        Closes the database connection. This method is not strictly necessary
        since we are using context managers, but it can be used if needed.
        """
        pass