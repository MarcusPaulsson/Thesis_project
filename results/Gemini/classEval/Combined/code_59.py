from datetime import datetime
import numpy as np

class MovieBookingSystem:
    """
    A movie booking system that allows adding movies, booking tickets, and checking available movies within a given time range.
    """

    def __init__(self):
        """
        Initializes the movie booking system with an empty list of movies.
        """
        self.movies = []

    def add_movie(self, name, price, start_time, end_time, num_seats):
        """
        Adds a new movie to the system.

        Args:
            name (str): The name of the movie.
            price (float): The price of a ticket for the movie.
            start_time (str): The start time of the movie in HH:MM format (e.g., "17:05").
            end_time (str): The end time of the movie in HH:MM format (e.g., "19:25").
            num_seats (int): The number of rows and columns in the seating arrangement (e.g., 3 for a 3x3 grid).
        """
        try:
            start_time_dt = datetime.strptime(start_time, '%H:%M')
            end_time_dt = datetime.strptime(end_time, '%H:%M')
        except ValueError:
            raise ValueError("Invalid time format. Please use HH:MM format.")

        if not isinstance(num_seats, int) or num_seats <= 0:
            raise ValueError("Number of seats must be a positive integer.")

        self.movies.append({
            'name': name,
            'price': price,
            'start_time': start_time_dt,
            'end_time': end_time_dt,
            'seats': np.zeros((num_seats, num_seats))
        })

    def book_ticket(self, name, seats_to_book):
        """
        Books tickets for a movie, marking the selected seats as occupied.

        Args:
            name (str): The name of the movie to book tickets for.
            seats_to_book (list of tuples): A list of (row, column) tuples representing the seats to book.
                                             Rows and columns are 0-indexed.

        Returns:
            str: A message indicating the booking status:
                 - "Movie not found." if the movie is not in the system.
                 - "Booking failed." if any of the requested seats are already booked or invalid.
                 - "Booking success." if the booking is successful.
        """
        for movie in self.movies:
            if movie['name'] == name:
                seats = movie['seats']
                rows, cols = seats.shape
                for row, col in seats_to_book:
                    if not (0 <= row < rows and 0 <= col < cols):
                        return "Booking failed."  # Invalid seat
                    if seats[row][col] == 1:
                        return "Booking failed."  # Seat already booked

                # All seats are available, so book them
                for row, col in seats_to_book:
                    seats[row][col] = 1
                return "Booking success."

        return "Movie not found."

    def available_movies(self, start_time, end_time):
        """
        Retrieves a list of movies that are playing within the specified time range.

        Args:
            start_time (str): The start time of the desired time range in HH:MM format (e.g., "12:00").
            end_time (str): The end time of the desired time range in HH:MM format (e.g., "22:00").

        Returns:
            list of str: A list of the names of the movies that are playing within the specified time range.
        """
        try:
            start_time_dt = datetime.strptime(start_time, '%H:%M')
            end_time_dt = datetime.strptime(end_time, '%H:%M')
        except ValueError:
            raise ValueError("Invalid time format. Please use HH:MM format.")

        available_movies_list = []
        for movie in self.movies:
            if movie['start_time'] <= end_time_dt and movie['end_time'] >= start_time_dt:
                available_movies_list.append(movie['name'])

        return available_movies_list