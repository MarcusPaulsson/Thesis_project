from datetime import datetime
import numpy as np

class MovieBookingSystem:
    """
    this is a class as movie booking system, which allows to add movies, book tickets and check the available movies within a given time range. 
    """

    def __init__(self):
        """
        Initialize movies contains the information about movies
        """
        self.movies = []

    def add_movie(self, name, price, start_time, end_time, n):
        """
        Add a new movie into self.movies
        :param name: str, movie name
        :param price: float, price for one ticket
        :param start_time: str
        :param end_time: str
        :param n: int, the size of seats(n*n)
        """
        try:
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
        except ValueError:
            print("Invalid time format. Please use HH:MM format.")

    def book_ticket(self, name, seats_to_book):
        """
        Book tickets for a movie. Change the seats value in self.movies if book successfully.
        :param name: str, movie name
        :param seats_to_book: list of tuples, representing seats to book [(row1, col1), (row2, col2), ...]
        :return: str, booking status message. "Movie not found." for no such movie.
                "Booking success." for successfully booking, or "Booking failed." otherwise
        """
        for movie in self.movies:
            if movie['name'] == name:
                seats = movie['seats']
                rows, cols = seats.shape
                
                # Check for invalid seat numbers
                for row, col in seats_to_book:
                    if not (0 <= row < rows and 0 <= col < cols):
                        return "Invalid seat number."

                booking_success = True
                for row, col in seats_to_book:
                    if seats[row, col] == 1:
                        booking_success = False
                        break
                
                if booking_success:
                    for row, col in seats_to_book:
                        seats[row, col] = 1
                    return 'Booking success.'
                else:
                    return 'Booking failed.'
        return 'Movie not found.'

    def available_movies(self, start_time, end_time):
        """
        Get a list of available movies within the specified time range
        :param start_time: str, start time in HH:MM format
        :param end_time: str, end time in HH:MM format
        :return: list of str, names of available movies
        """
        available_movies_list = []
        try:
            start_time_dt = datetime.strptime(start_time, '%H:%M').time()
            end_time_dt = datetime.strptime(end_time, '%H:%M').time()

            for movie in self.movies:
                movie_start_time = movie['start_time'].time()
                movie_end_time = movie['end_time'].time()

                if movie_start_time <= end_time_dt and movie_end_time >= start_time_dt:
                    available_movies_list.append(movie['name'])
        except ValueError:
            print("Invalid time format. Please use HH:MM format.")
        return available_movies_list