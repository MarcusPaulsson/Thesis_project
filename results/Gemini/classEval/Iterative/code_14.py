import sqlite3

class BookManagementDB:
    """
    Manages a database of books, allowing for adding, removing, borrowing, returning, and searching.
    """

    def __init__(self, db_name):
        """
        Initializes the database connection and creates the books table if it doesn't exist.

        Args:
            db_name (str): The name of the database file.
        """
        try:
            self.connection = sqlite3.connect(db_name)
            self.cursor = self.connection.cursor()
            self.create_table()
        except sqlite3.Error as e:
            print(f"Database connection error: {e}")
            self.connection = None  # or raise the exception

    def create_table(self):
        """
        Creates the 'books' table with columns: id, title, author, and availability.
        id is the primary key and autoincrements. availability defaults to 1 (available).
        """
        try:
            self.cursor.execute('''
                CREATE TABLE IF NOT EXISTS books (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    title TEXT NOT NULL,
                    author TEXT NOT NULL,
                    availability INTEGER NOT NULL DEFAULT 1
                )
            ''')
            self.connection.commit()
        except sqlite3.Error as e:
            print(f"Error creating table: {e}")

    def add_book(self, title, author):
        """
        Adds a new book to the database.

        Args:
            title (str): The title of the book.
            author (str): The author of the book.
        """
        if not self.connection:
            print("No database connection.")
            return

        try:
            self.cursor.execute('''
                INSERT INTO books (title, author, availability)
                VALUES (?, ?, ?)
            ''', (title, author, 1))
            self.connection.commit()
        except sqlite3.Error as e:
            print(f"Error adding book: {e}")
            self.connection.rollback()  # Rollback in case of error

    def remove_book(self, book_id):
        """
        Removes a book from the database based on its ID.

        Args:
            book_id (int): The ID of the book to remove.
        """
        if not self.connection:
            print("No database connection.")
            return

        try:
            self.cursor.execute('''
                DELETE FROM books
                WHERE id = ?
            ''', (book_id,))
            self.connection.commit()
        except sqlite3.Error as e:
            print(f"Error removing book: {e}")
            self.connection.rollback()

    def borrow_book(self, book_id):
        """
        Marks a book as borrowed (availability = 0).

        Args:
            book_id (int): The ID of the book to borrow.
        """
        if not self.connection:
            print("No database connection.")
            return

        try:
            self.cursor.execute('''
                UPDATE books
                SET availability = 0
                WHERE id = ?
            ''', (book_id,))
            self.connection.commit()
        except sqlite3.Error as e:
            print(f"Error borrowing book: {e}")
            self.connection.rollback()

    def return_book(self, book_id):
        """
        Marks a book as returned (availability = 1).

        Args:
            book_id (int): The ID of the book to return.
        """
        if not self.connection:
            print("No database connection.")
            return


        try:
            self.cursor.execute('''
                UPDATE books
                SET availability = 1
                WHERE id = ?
            ''', (book_id,))
            self.connection.commit()
        except sqlite3.Error as e:
            print(f"Error returning book: {e}")
            self.connection.rollback()

    def search_books(self, title=None, author=None):
        """
        Searches for books in the database based on title and/or author. If no search terms are provided,
        it returns all books.

        Args:
            title (str, optional): The title to search for. Defaults to None.
            author (str, optional): The author to search for. Defaults to None.

        Returns:
            list[tuple]: A list of tuples, where each tuple represents a book's information (id, title, author, availability).
        """
        if not self.connection:
            print("No database connection.")
            return []

        query = '''SELECT * FROM books'''
        params = []
        where_clauses = []

        if title:
            where_clauses.append("title LIKE ?")
            params.append(f"%{title}%")  # Use LIKE for partial matches
        if author:
            where_clauses.append("author LIKE ?")
            params.append(f"%{author}%")

        if where_clauses:
            query += " WHERE " + " AND ".join(where_clauses)

        try:
            self.cursor.execute(query, params)
            books = self.cursor.fetchall()
            return books
        except sqlite3.Error as e:
            print(f"Error searching books: {e}")
            return []

    def close_connection(self):
        """Closes the database connection."""
        if self.connection:
            self.connection.close()
            self.connection = None #Avoid using closed connection