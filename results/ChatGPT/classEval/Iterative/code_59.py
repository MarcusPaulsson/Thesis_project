from datetime import datetime
import numpy as np

class MovieBookingSystem:
    """
    A class representing a movie booking system, allowing the addition of movies,
    booking of tickets, and checking available movies within a specified time range.
    """

    def __init__(self):
        """
        Initialize an empty list to hold movie information.
        """
        self.movies = []

    def add_movie(self, name, price, start_time, end_time, n):
        """
        Add a new movie to the system.
        :param name: str, movie name
        :param price: float, price for one ticket
        :param start_time: str, start time in HH:MM format
        :param end_time: str, end time in HH:MM format
        :param n: int, the size of seats (n*n)
        """
        start_time = datetime.strptime(start_time, '%H:%M')
        end_time = datetime.strptime(end_time, '%H:%M')

        if start_time >= end_time:
            raise ValueError("End time must be after start time.")

        if any(movie['name'].lower() == name.lower() for movie in self.movies):
            raise ValueError("Movie already exists.")

        seats = np.zeros((n, n), dtype=int)  # Using int for seat status (0: available, 1: booked)
        self.movies.append({
            'name': name,
            'price': price,
            'start_time': start_time,
            'end_time': end_time,
            'seats': seats
        })

    def book_ticket(self, name, seats_to_book):
        """
        Book tickets for a movie.
        :param name: str, movie name
        :param seats_to_book: list of tuples, representing seats to book [(row1, col1), (row2, col2), ...]
        :return: str, booking status message
        """
        movie = next((m for m in self.movies if m['name'].lower() == name.lower()), None)
        if not movie:
            return "Movie not found."
        
        seats = movie['seats']
        for row, col in seats_to_book:
            if row < 0 or row >= seats.shape[0] or col < 0 or col >= seats.shape[1]:
                return "Booking failed: Invalid seat selection."
            if seats[row, col] == 1:
                return "Booking failed: Seat already booked."
        
        for row, col in seats_to_book:
            seats[row, col] = 1
        
        return "Booking success."

    def available_movies(self, start_time, end_time):
        """
        Get a list of available movies within the specified time range.
        :param start_time: str, start time in HH:MM format
        :param end_time: str, end time in HH:MM format
        :return: list of str, names of available movies
        """
        start_time = datetime.strptime(start_time, '%H:%M')
        end_time = datetime.strptime(end_time, '%H:%M')

        return [
            movie['name'] for movie in self.movies
            if movie['start_time'] >= start_time and movie['end_time'] <= end_time
        ]