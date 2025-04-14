from datetime import datetime
import numpy as np

class MovieBookingSystem:
    """
    A movie booking system that allows adding movies, booking tickets,
    and checking available movies within a given time range.
    """

    def __init__(self):
        """
        Initializes the movie booking system with an empty list of movies.
        """
        self.movies = []

    def add_movie(self, name, price, start_time, end_time, n):
        """
        Adds a new movie to the system.

        Args:
            name (str): The name of the movie.
            price (float): The price of a ticket for the movie.
            start_time (str): The start time of the movie in HH:MM format (e.g., "17:05").
            end_time (str): The end time of the movie in HH:MM format (e.g., "19:25").
            n (int): The size of the square seating arrangement (n x n).
        """
        try:
            start_time_dt = datetime.strptime(start_time, '%H:%M')
            end_time_dt = datetime.strptime(end_time, '%H:%M')
        except ValueError:
            raise ValueError("Invalid time format. Please use HH:MM format.")

        if not isinstance(price, (int, float)):
            raise TypeError("Price must be a number.")
        if price <= 0:
            raise ValueError("Price must be positive.")

        if not isinstance(n, int):
            raise TypeError("Seat size must be an integer.")
        if n <= 0:
            raise ValueError("Seat size must be positive.")

        seats = np.zeros((n, n))
        movie = {
            'name': name,
            'price': price,
            'start_time': start_time_dt,
            'end_time': end_time_dt,
            'seats': seats
        }
        self.movies.append(movie)

    def book_ticket(self, name, seats_to_book):
        """
        Books tickets for a movie, marking the selected seats as occupied.

        Args:
            name (str): The name of the movie to book tickets for.
            seats_to_book (list of tuples): A list of (row, col) tuples representing the seats to book.

        Returns:
            str: A message indicating the booking status:
                - "Movie not found." if the movie is not found.
                - "Booking success." if the booking is successful.
                - "Booking failed." if one or more seats are already booked.
        """
        for movie in self.movies:
            if movie['name'] == name:
                seats = movie['seats']
                for row, col in seats_to_book:
                    if not (0 <= row < seats.shape[0] and 0 <= col < seats.shape[1]):
                        return 'Booking failed. Invalid seat selection.'

                all_available = all(seats[row][col] == 0 for row, col in seats_to_book)

                if all_available:
                    for row, col in seats_to_book:
                        seats[row][col] = 1
                    return 'Booking success.'
                else:
                    return 'Booking failed.'
        return 'Movie not found.'

    def available_movies(self, start_time, end_time):
        """
        Retrieves a list of movies that are playing within the specified time range.

        Args:
            start_time (str): The start time of the desired time range in HH:MM format (e.g., "12:00").
            end_time (str): The end time of the desired time range in HH:MM format (e.g., "22:00").

        Returns:
            list of str: A list of movie names that are playing within the specified time range.
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