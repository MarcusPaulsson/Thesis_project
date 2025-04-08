import sqlite3
from contextlib import closing

class MovieTicketDB:
    """
    A class for managing a movie ticket database, allowing for operations like inserting, 
    searching, and deleting movie ticket records.
    """

    def __init__(self, db_name):
        """
        Initializes the MovieTicketDB object with the specified database name.
        
        :param db_name: str, the name of the SQLite database.
        """
        self.db_name = db_name
        self._initialize_db()

    def _initialize_db(self):
        """Creates the database table if it does not exist."""
        with closing(sqlite3.connect(self.db_name)) as connection:
            with closing(connection.cursor()) as cursor:
                cursor.execute('''
                    CREATE TABLE IF NOT EXISTS tickets (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        movie_name TEXT NOT NULL,
                        theater_name TEXT NOT NULL,
                        seat_number TEXT NOT NULL,
                        customer_name TEXT NOT NULL
                    )
                ''')
                connection.commit()

    def insert_ticket(self, movie_name, theater_name, seat_number, customer_name):
        """
        Inserts a new ticket into the "tickets" table.
        
        :param movie_name: str, the name of the movie.
        :param theater_name: str, the name of the theater.
        :param seat_number: str, the seat number.
        :param customer_name: str, the name of the customer.
        """
        with closing(sqlite3.connect(self.db_name)) as connection:
            with closing(connection.cursor()) as cursor:
                cursor.execute('''
                    INSERT INTO tickets (movie_name, theater_name, seat_number, customer_name)
                    VALUES (?, ?, ?, ?)
                ''', (movie_name, theater_name, seat_number, customer_name))
                connection.commit()

    def search_tickets_by_customer(self, customer_name):
        """
        Searches for tickets in the "tickets" table by customer name.
        
        :param customer_name: str, the name of the customer to search for.
        :return: list of tuples, the rows from the "tickets" table that match the search criteria.
        """
        with closing(sqlite3.connect(self.db_name)) as connection:
            with closing(connection.cursor()) as cursor:
                cursor.execute('''
                    SELECT * FROM tickets WHERE customer_name = ?
                ''', (customer_name,))
                return cursor.fetchall()

    def delete_ticket(self, ticket_id):
        """
        Deletes a ticket from the "tickets" table by ticket ID.
        
        :param ticket_id: int, the ID of the ticket to delete.
        """
        with closing(sqlite3.connect(self.db_name)) as connection:
            with closing(connection.cursor()) as cursor:
                cursor.execute('''
                    DELETE FROM tickets WHERE id = ?
                ''', (ticket_id,))
                connection.commit()