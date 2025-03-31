import sqlite3

class BookManagementDB:
    """
    This is a database class as a book management system, used to handle the operations of adding, removing, and searching books.
    """

    def __init__(self, db_name):
        """
        Initializes the class by creating a database connection and cursor,
        and creates the book table if it does not already exist
        :param db_name: str, the name of db file
        """
        self.connection = sqlite3.connect(db_name)
        self.cursor = self.connection.cursor()
        # Check if the table exists or not
        self.create_table()

    def create_table(self):
        """
        Creates the book table in the database if it does not already exist.
        """
        try:
            self.cursor.execute('''CREATE TABLE books (id INTEGER PRIMARY KEY AUTOINCREMENT, title TEXT NOT NULL,
                               author TEXT NOT NULL, availability INT DEFAULT 1)''')
        except sqlite3.OperationalError as e:
            pass # If table already exists, it will give an error, so we can ignore it.

    def add_book(self, title, author):
        """
        Adds a book to the database with the specified title and author,
        setting its availability to 1 as free to borrow.
        :param title: str, book title
        :param author: str, author name
        >>> book_db = BookManagementDB("test.db")
        >>> book_db.create_table()
        >>> book_db.add_book('book1', 'author')
        """
        self.cursor.execute('''INSERT INTO books (title, author) VALUES(?,?)''', (title, author))
        self.connection.commit() # commit the changes to the database

    def remove_book(self, book_id):
        """
        Removes a book from the database based on the given book ID.
        :param book_id: int
        >>> book_db = BookManagementDB("test.db")
        >>> book_db.remove_book(1)
        """
        self.cursor.execute('''DELETE FROM books WHERE id=?''', (book_id,))
        self.connection.commit() # commit the changes to the database

    def borrow_book(self, book_id):
        """
        Marks a book as borrowed in the database based on the given book ID.
        :param book_id: int
        >>> book_db = BookManagementDB("test.db")
        >>> book_db.borrow_book(1)
        """
        self.cursor.execute('''UPDATE books SET availability=0 WHERE id=?''', (book_id,))
        self.connection.commit() # commit the changes to the database

    def return_book(self, book_id):
        """
        Marks a book as returned in the database based on the given book ID.
        :param book_id: int
        >>> book_db = BookManagementDB("test.db")
        >>> book_db.return_book(1)
        """
        self.cursor.execute('''UPDATE books SET availability=1 WHERE id=?''', (book_id,))
        self.connection.commit() # commit the changes to the database

    def search_books(self):
        """
        Retrieves all books from the database and returns their information.
        :return books: list[tuple], the information of all books in database
        >>> book_db.search_books()
        [(1, 'book1', 'author', 1)]
        """
        self.cursor.execute('''SELECT * FROM books''')
        return self.cursor.fetchall() # Return a list of tuples with the data.