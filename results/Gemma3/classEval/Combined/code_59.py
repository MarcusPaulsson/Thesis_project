from datetime import datetime
import numpy as np

class MovieBookingSystem:
    """
    This is a class for a movie booking system, which allows adding movies,
    booking tickets, and checking available movies within a given time range.
    """

    def __init__(self):
        """
        Initializes the movie list.
        """
        self.movies = []

    def add_movie(self, name, price, start_time, end_time, n):
        """
        Adds a new movie to the movie list.

        Args:
            name (str): The name of the movie.
            price (float): The price of a ticket for the movie.
            start_time (str): The start time of the movie in HH:MM format.
            end_time (str): The end time of the movie in HH:MM format.
            n (int): The size of the seating arrangement (n x n).
        """
        try:
            start_time = datetime.strptime(start_time, '%H:%M')
            end_time = datetime.strptime(end_time, '%H:%M')
            seats = np.zeros((n, n))
            movie = {
                'name': name,
                'price': price,
                'start_time': start_time,
                'end_time': end_time,
                'seats': seats
            }
            self.movies.append(movie)
        except ValueError:
            print("Invalid time format. Please use HH:MM.")

    def book_ticket(self, name, seats_to_book):
        """
        Books tickets for a movie.

        Args:
            name (str): The name of the movie.
            seats_to_book (list of tuples): A list of seats to book,
                                             represented as (row, col) tuples.

        Returns:
            str: A message indicating the booking status.
                 "Movie not found." if the movie is not found.
                 "Booking success." if the booking is successful.
                 "Booking failed." if the booking fails (e.g., seat already taken).
        """
        for movie in self.movies:
            if movie['name'] == name:
                seats = movie['seats']
                all_available = True
                for row, col in seats_to_book:
                    if not (0 <= row < seats.shape[0] and 0 <= col < seats.shape[1]):
                        return "Booking failed."  # Invalid seat
                    if seats[row][col] == 1:
                        all_available = False
                        break

                if all_available:
                    for row, col in seats_to_book:
                        seats[row][col] = 1
                    return 'Booking success.'
                else:
                    return 'Booking failed.'
        return 'Movie not found.'

    def available_movies(self, start_time, end_time):
        """
        Gets a list of available movies within the specified time range.

        Args:
            start_time (str): The start time in HH:MM format.
            end_time (str): The end time in HH:MM format.

        Returns:
            list of str: A list of movie names that are available within the
                         specified time range.
        """
        try:
            start_time = datetime.strptime(start_time, '%H:%M')
            end_time = datetime.strptime(end_time, '%H:%M')
            available_movies = []
            for movie in self.movies:
                if movie['start_time'] >= start_time and movie['end_time'] <= end_time:
                    available_movies.append(movie['name'])
            return available_movies
        except ValueError:
            print("Invalid time format. Please use HH:MM.")
            return []