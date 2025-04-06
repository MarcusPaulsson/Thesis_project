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

    def add_movie(self, name, price, start_time_str, end_time_str, n):
        """
        Adds a new movie to the system.

        Args:
            name (str): The name of the movie.
            price (float): The price of a ticket for the movie.
            start_time_str (str): The start time of the movie in HH:MM format.
            end_time_str (str): The end time of the movie in HH:MM format.
            n (int): The size of the square seating arrangement (n x n).
        """
        try:
            start_time = datetime.strptime(start_time_str, '%H:%M').time()
            end_time = datetime.strptime(end_time_str, '%H:%M').time()

            # Convert time objects to datetime objects for comparison
            now = datetime.now()
            start_datetime = datetime.combine(now.date(), start_time)
            end_datetime = datetime.combine(now.date(), end_time)

            seats = np.zeros((n, n))
            self.movies.append({
                'name': name,
                'price': price,
                'start_time': start_datetime,
                'end_time': end_datetime,
                'seats': seats
            })
        except ValueError:
            print("Invalid time format.  Please use HH:MM format.")
            return

    def book_ticket(self, name, seats_to_book):
        """
        Books tickets for a movie, marking the seats as occupied.

        Args:
            name (str): The name of the movie to book tickets for.
            seats_to_book (list of tuples): A list of tuples, where each tuple
                represents a seat to book in the format (row, column).

        Returns:
            str: A message indicating the booking status.
                "Movie not found." if the movie is not found.
                "Booking success." if the booking is successful.
                "Booking failed." if the booking fails (e.g., seats are already taken).
        """
        for movie in self.movies:
            if movie['name'] == name:
                seats = movie['seats']
                for row, col in seats_to_book:
                    if not (0 <= row < seats.shape[0] and 0 <= col < seats.shape[1]):
                        return "Booking failed. Invalid seat selection."

                for row, col in seats_to_book:
                    if seats[row, col] == 1:
                        return "Booking failed. Seat already taken."

                for row, col in seats_to_book:
                    seats[row, col] = 1
                return "Booking success."
        return "Movie not found."

    def available_movies(self, start_time_str, end_time_str):
        """
        Returns a list of movies that are playing within the specified time range.

        Args:
            start_time_str (str): The start time of the range in HH:MM format.
            end_time_str (str): The end time of the range in HH:MM format.

        Returns:
            list of str: A list of movie names that are playing within the specified time range.
        """
        try:
            start_time = datetime.strptime(start_time_str, '%H:%M').time()
            end_time = datetime.strptime(end_time_str, '%H:%M').time()

             # Convert time objects to datetime objects for comparison
            now = datetime.now()
            start_datetime = datetime.combine(now.date(), start_time)
            end_datetime = datetime.combine(now.date(), end_time)


            available_movie_names = []
            for movie in self.movies:
                if movie['start_time'] <= end_datetime and movie['end_time'] >= start_datetime:
                    available_movie_names.append(movie['name'])
            return available_movie_names

        except ValueError:
            print("Invalid time format. Please use HH:MM format.")
            return []