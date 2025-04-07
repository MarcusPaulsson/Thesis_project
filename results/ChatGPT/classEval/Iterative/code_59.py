from datetime import datetime
import numpy as np

class MovieBookingSystem:
    """
    This class represents a movie booking system, which allows adding movies, booking tickets,
    and checking the available movies within a given time range.
    """

    def __init__(self):
        """
        Initialize the movie booking system with an empty list of movies.
        """
        self.movies = []

    def add_movie(self, name, price, start_time, end_time, n):
        """
        Add a new movie to the system.
        :param name: str, movie name
        :param price: float, price for one ticket
        :param start_time: str, movie start time in 'HH:MM' format
        :param end_time: str, movie end time in 'HH:MM' format
        :param n: int, the size of seats (n*n)
        """
        start_time_dt = datetime.strptime(start_time, '%H:%M')
        end_time_dt = datetime.strptime(end_time, '%H:%M')

        if end_time_dt <= start_time_dt:
            raise ValueError("End time must be after start time.")

        seats = np.zeros((n, n), dtype=int)
        self.movies.append({
            'name': name,
            'price': price,
            'start_time': start_time_dt,
            'end_time': end_time_dt,
            'seats': seats
        })

    def book_ticket(self, name, seats_to_book):
        """
        Book tickets for a movie. Update the seats status if booking is successful.
        :param name: str, movie name
        :param seats_to_book: list of tuples, representing seats to book [(row1, col1), (row2, col2), ...]
        :return: str, booking status message.
        """
        for movie in self.movies:
            if movie['name'].lower() == name.lower():
                for row, col in seats_to_book:
                    if 0 <= row < movie['seats'].shape[0] and 0 <= col < movie['seats'].shape[1]:
                        if movie['seats'][row][col] == 0:
                            movie['seats'][row][col] = 1
                        else:
                            return 'Booking failed.'
                    else:
                        return 'Invalid seat position.'
                return 'Booking success.'
        return 'Movie not found.'

    def available_movies(self, start_time, end_time):
        """
        Get a list of available movies within the specified time range.
        :param start_time: str, start time in 'HH:MM' format
        :param end_time: str, end time in 'HH:MM' format
        :return: list of str, names of available movies
        """
        start_time_dt = datetime.strptime(start_time, '%H:%M')
        end_time_dt = datetime.strptime(end_time, '%H:%M')

        available = []
        for movie in self.movies:
            if movie['start_time'] >= start_time_dt and movie['end_time'] <= end_time_dt:
                available.append(movie['name'])
        return available