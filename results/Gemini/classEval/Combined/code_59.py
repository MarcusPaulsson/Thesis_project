from datetime import datetime
import numpy as np

class MovieBookingSystem:
    """
    A class representing a movie booking system.
    """

    def __init__(self):
        """
        Initializes the MovieBookingSystem with an empty list of movies.
        """
        self.movies = []

    def add_movie(self, name, price, start_time, end_time, num_seats):
        """
        Adds a movie to the system.

        Args:
            name (str): The name of the movie.
            price (float): The price of a ticket for the movie.
            start_time (str): The start time of the movie in HH:MM format.
            end_time (str): The end time of the movie in HH:MM format.
            num_seats (int): The number of rows and columns in the seating arrangement (num_seats x num_seats).
        """
        try:
            start_time_obj = datetime.strptime(start_time, '%H:%M').time()
            end_time_obj = datetime.strptime(end_time, '%H:%M').time()
        except ValueError:
            print("Invalid time format. Please use HH:MM format.")
            return

        if not isinstance(price, (int, float)) or price <= 0:
            print("Invalid price. Price must be a positive number.")
            return

        if not isinstance(num_seats, int) or num_seats <= 0:
            print("Invalid number of seats. Number of seats must be a positive integer.")
            return
        
        movie = {
            'name': name,
            'price': price,
            'start_time': start_time_obj,
            'end_time': end_time_obj,
            'seats': np.zeros((num_seats, num_seats), dtype=int)  # Use int dtype for seats
        }
        self.movies.append(movie)

    def book_ticket(self, movie_name, seats_to_book):
        """
        Books tickets for a given movie.

        Args:
            movie_name (str): The name of the movie to book tickets for.
            seats_to_book (list of tuples): A list of (row, column) tuples representing the seats to book.

        Returns:
            str: A message indicating the booking status ("Booking success.", "Booking failed.", or "Movie not found.").
        """
        for movie in self.movies:
            if movie['name'] == movie_name:
                seats = movie['seats']
                rows, cols = seats.shape
                for row, col in seats_to_book:
                    if not (0 <= row < rows and 0 <= col < cols):
                        return "Booking failed."  # Seat out of range

                    if seats[row][col] == 1:
                        return "Booking failed."  # Seat already booked

                # Book the seats
                for row, col in seats_to_book:
                    seats[row][col] = 1
                return "Booking success."

        return "Movie not found."

    def available_movies(self, start_time, end_time):
        """
        Returns a list of movies that are available within the specified time range.

        Args:
            start_time (str): The start time of the range in HH:MM format.
            end_time (str): The end time of the range in HH:MM format.

        Returns:
            list of str: A list of movie names that are available within the specified time range.
        """
        available_movie_names = []
        try:
            start_time_obj = datetime.strptime(start_time, '%H:%M').time()
            end_time_obj = datetime.strptime(end_time, '%H:%M').time()
        except ValueError:
            print("Invalid time format. Please use HH:MM format.")
            return available_movie_names

        for movie in self.movies:
            if movie['start_time'] <= end_time_obj and movie['end_time'] >= start_time_obj:
                available_movie_names.append(movie['name'])
        return available_movie_names