from datetime import datetime
import numpy as np

class MovieBookingSystem:
    """
    A movie booking system that allows adding movies, booking tickets, 
    and checking available movies within a specified time range.
    """

    def __init__(self):
        """Initialize the movie list."""
        self.movies = []

    def add_movie(self, name: str, price: float, start_time: str, end_time: str, n: int):
        """
        Add a new movie to the system.
        :param name: Movie name.
        :param price: Ticket price.
        :param start_time: Start time in HH:MM format.
        :param end_time: End time in HH:MM format.
        :param n: Size of the seating grid (n x n).
        """
        start_time_dt = datetime.strptime(start_time, '%H:%M')
        end_time_dt = datetime.strptime(end_time, '%H:%M')
        seats = np.zeros((n, n), dtype=int)
        
        self.movies.append({
            'name': name,
            'price': price,
            'start_time': start_time_dt,
            'end_time': end_time_dt,
            'seats': seats
        })

    def book_ticket(self, name: str, seats_to_book: list) -> str:
        """
        Book tickets for a specified movie.
        :param name: Movie name.
        :param seats_to_book: List of tuples representing seats to book.
        :return: Status message indicating the result of the booking attempt.
        """
        movie = next((m for m in self.movies if m['name'].lower() == name.lower()), None)
        
        if not movie:
            return "Movie not found."
        
        if any(movie['seats'][row, col] == 1 for row, col in seats_to_book):
            return "Booking failed."

        for row, col in seats_to_book:
            movie['seats'][row, col] = 1
            
        return "Booking success."

    def available_movies(self, start_time: str, end_time: str) -> list:
        """
        Get a list of movies that are available within the specified time range.
        :param start_time: Start time in HH:MM format.
        :param end_time: End time in HH:MM format.
        :return: List of available movie names.
        """
        start_time_dt = datetime.strptime(start_time, '%H:%M')
        end_time_dt = datetime.strptime(end_time, '%H:%M')
        
        return [
            movie['name'] for movie in self.movies
            if not (movie['end_time'] <= start_time_dt or movie['start_time'] >= end_time_dt)
        ]