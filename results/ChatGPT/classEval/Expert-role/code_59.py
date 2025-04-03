from datetime import datetime
import numpy as np

class MovieBookingSystem:
    """
    A class for a movie booking system that allows adding movies, booking tickets,
    and checking available movies within a given time range.
    """

    def __init__(self):
        """
        Initialize movies contains the information about movies.
        """
        self.movies = []

    def add_movie(self, name, price, start_time, end_time, n):
        """
        Add a new movie into self.movies.
        :param name: str, movie name
        :param price: float, price for one ticket
        :param start_time: str
        :param end_time: str
        :param n: int, the size of seats (n*n)
        """
        start_time_dt = datetime.strptime(start_time, '%H:%M')
        end_time_dt = datetime.strptime(end_time, '%H:%M')
        seats = np.zeros((n, n))
        self.movies.append({
            'name': name,
            'price': price,
            'start_time': start_time_dt,
            'end_time': end_time_dt,
            'seats': seats
        })

    def book_ticket(self, name, seats_to_book):
        """
        Book tickets for a movie. Change the seats value in self.movies if booked successfully.
        :param name: str, movie name
        :param seats_to_book: list of tuples, representing seats to book [(row1, col1), (row2, col2), ...]
        :return: str, booking status message.
        """
        for movie in self.movies:
            if movie['name'].lower() == name.lower():
                for seat in seats_to_book:
                    row, col = seat
                    if movie['seats'][row, col] == 0:
                        movie['seats'][row, col] = 1  # Mark seat as booked
                    else:
                        return 'Booking failed.'
                return 'Booking success.'
        return 'Movie not found.'

    def available_movies(self, start_time, end_time):
        """
        Get a list of available movies within the specified time range.
        :param start_time: str, start time in HH:MM format
        :param end_time: str, end time in HH:MM format
        :return: list of str, names of available movies
        """
        start_time_dt = datetime.strptime(start_time, '%H:%M')
        end_time_dt = datetime.strptime(end_time, '%H:%M')
        available = []
        for movie in self.movies:
            if movie['start_time'] >= start_time_dt and movie['end_time'] <= end_time_dt:
                available.append(movie['name'])
        return available