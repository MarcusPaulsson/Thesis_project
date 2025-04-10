from datetime import datetime
import numpy as np

class MovieBookingSystem:
    """
    A class representing a movie booking system that allows adding movies,
    booking tickets, and checking available movies within a given time range.
    """

    def __init__(self):
        """
        Initialize the movie booking system with an empty movie list.
        """
        self.movies = []

    def add_movie(self, name: str, price: float, start_time: str, end_time: str, n: int):
        """
        Add a new movie to the system.

        :param name: str, movie name
        :param price: float, price for one ticket
        :param start_time: str, start time in HH:MM format
        :param end_time: str, end time in HH:MM format
        :param n: int, size of the seats (n x n)
        """
        start_time_dt = datetime.strptime(start_time, '%H:%M')
        end_time_dt = datetime.strptime(end_time, '%H:%M')

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

    def book_ticket(self, name: str, seats_to_book: list) -> str:
        """
        Book tickets for a movie.

        :param name: str, movie name
        :param seats_to_book: list of tuples, representing seats to book [(row1, col1), (row2, col2), ...]
        :return: str, booking status message
        """
        movie = next((m for m in self.movies if m['name'].lower() == name.lower()), None)

        if not movie:
            return "Movie not found."

        if all(movie['seats'][row, col] == 0 for row, col in seats_to_book):
            for row, col in seats_to_book:
                movie['seats'][row, col] = 1  # Mark seat as booked
            return "Booking success."
        else:
            return "Booking failed."

    def available_movies(self, start_time: str, end_time: str) -> list:
        """
        Get a list of available movies within the specified time range.

        :param start_time: str, start time in HH:MM format
        :param end_time: str, end time in HH:MM format
        :return: list of str, names of available movies
        """
        start_time_dt = datetime.strptime(start_time, '%H:%M')
        end_time_dt = datetime.strptime(end_time, '%H:%M')

        available = [
            movie['name'] for movie in self.movies
            if movie['start_time'] >= start_time_dt and movie['end_time'] <= end_time_dt
        ]
        return available