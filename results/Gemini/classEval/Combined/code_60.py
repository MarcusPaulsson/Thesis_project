import sqlite3

class MovieTicketDB:
    """
    This is a class for movie database operations, which allows for inserting movie information, searching for movie information by name, and deleting movie information by ID.
    """

    def __init__(self, db_name):
        """
        Initializes the MovieTicketDB object with the specified database name.
        :param db_name: str, the name of the SQLite database.
        """
        self.db_name = db_name
        self.connection = sqlite3.connect(db_name)
        self.cursor = self.connection.cursor()
        self._create_table()


    def _create_table(self):
        """
        Creates a "tickets" table in the database if it does not exist already.
        Fields include ID (INTEGER PRIMARY KEY AUTOINCREMENT), movie_name (TEXT NOT NULL),
        theater_name (TEXT NOT NULL), seat_number (TEXT NOT NULL), and customer_name (TEXT NOT NULL).
        :return: None
        """
        try:
            self.cursor.execute("""
                CREATE TABLE IF NOT EXISTS tickets (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    movie_name TEXT NOT NULL,
                    theater_name TEXT NOT NULL,
                    seat_number TEXT NOT NULL,
                    customer_name TEXT NOT NULL
                )
            """)
            self.connection.commit()
        except sqlite3.Error as e:
            print(f"Database error: {e}")


    def insert_ticket(self, movie_name, theater_name, seat_number, customer_name):
        """
        Inserts a new ticket into the "tickets" table.
        :param movie_name: str, the name of the movie.
        :param theater_name: str, the name of the theater.
        :param seat_number: str, the seat number.
        :param customer_name: str, the name of the customer.
        :return: None
        """
        try:
            self.cursor.execute("""
                INSERT INTO tickets (movie_name, theater_name, seat_number, customer_name)
                VALUES (?, ?, ?, ?)
            """, (movie_name, theater_name, seat_number, customer_name))
            self.connection.commit()
        except sqlite3.Error as e:
            print(f"Database error: {e}")

    def search_tickets_by_customer(self, customer_name):
        """
        Searches for tickets in the "tickets" table by customer name.
        :param customer_name: str, the name of the customer to search for.
        :return: list of tuples, the rows from the "tickets" table that match the search criteria.
        """
        try:
            self.cursor.execute("""
                SELECT * FROM tickets WHERE customer_name = ?
            """, (customer_name,))
            return self.cursor.fetchall()
        except sqlite3.Error as e:
            print(f"Database error: {e}")
            return []

    def delete_ticket(self, ticket_id):
        """
        Deletes a ticket from the "tickets" table by ticket ID.
        :param ticket_id: int, the ID of the ticket to delete.
        :return: None
        """
        try:
            self.cursor.execute("""
                DELETE FROM tickets WHERE id = ?
            """, (ticket_id,))
            self.connection.commit()
        except sqlite3.Error as e:
            print(f"Database error: {e}")

    def close(self):
        """
        Closes the database connection.
        :return: None
        """
        try:
            self.connection.close()
        except sqlite3.Error as e:
            print(f"Database error: {e}")