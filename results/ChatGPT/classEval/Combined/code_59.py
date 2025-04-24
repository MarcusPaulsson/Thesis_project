from datetime import datetime
import numpy as np

class MovieBookingSystem:
    """
    A class representing a movie booking system, which allows adding movies, booking tickets,
    and checking available movies within a given time range.
    """

    def __init__(self):
        """Initialize the movie booking system with an empty movie list."""
        self.movies = []

    def add_movie(self, name: str, price: float, start_time: str, end_time: str, n: int):
        """
        Add a new movie to the system.
        
        :param name: str, movie name
        :param price: float, price for one ticket
        :param start_time: str, start time in HH:MM format
        :param end_time: str, end time in HH:MM format
        :param n: int, the size of seats (n x n)
        """
        start_time_dt = self._parse_time(start_time)
        end_time_dt = self._parse_time(end_time)

        if start_time_dt >= end_time_dt:
            raise ValueError("End time must be after start time.")

        seats = np.zeros((n, n), dtype=int)

        movie = {
            'name': name,
            'price': price,
            'start_time': start_time_dt,
            'end_time': end_time_dt,
            'seats': seats
        }
        self.movies.append(movie)

    def book_ticket(self, name: str, seats_to_book: list):
        """
        Book tickets for a movie. Update the seats if booking is successful.
        
        :param name: str, movie name
        :param seats_to_book: list of tuples, representing seats to book [(row1, col1), (row2, col2), ...]
        :return: str, booking status message
        """
        movie = self._find_movie(name)
        if not movie:
            return 'Movie not found.'

        if not self._are_seats_available(movie['seats'], seats_to_book):
            return 'Booking failed.'

        self._book_seats(movie['seats'], seats_to_book)
        return 'Booking success.'

    def available_movies(self, start_time: str, end_time: str):
        """
        Get a list of available movies within the specified time range.
        
        :param start_time: str, start time in HH:MM format
        :param end_time: str, end time in HH:MM format
        :return: list of str, names of available movies
        """
        start_time_dt = self._parse_time(start_time)
        end_time_dt = self._parse_time(end_time)
        return [
            movie['name'] for movie in self.movies
            if movie['start_time'] >= start_time_dt and movie['end_time'] <= end_time_dt
        ]

    def _find_movie(self, name: str):
        """Helper method to find a movie by name."""
        return next((movie for movie in self.movies if movie['name'].lower() == name.lower()), None)

    def _parse_time(self, time_str: str) -> datetime:
        """Convert a time string in HH:MM format to a datetime object."""
        return datetime.strptime(time_str, '%H:%M')

    def _are_seats_available(self, seats: np.ndarray, seats_to_book: list) -> bool:
        """Check if the requested seats are available."""
        return all(seats[row, col] == 0 for row, col in seats_to_book)

    def _book_seats(self, seats: np.ndarray, seats_to_book: list):
        """Mark the requested seats as booked."""
        for row, col in seats_to_book:
            seats[row, col] = 1