from datetime import datetime
import numpy as np

class MovieBookingSystem:
    """
    A class representing a movie booking system.
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
            price (float): The price of a movie ticket.
            start_time (str): The start time of the movie in HH:MM format (e.g., "17:05").
            end_time (str): The end time of the movie in HH:MM format (e.g., "19:25").
            n (int): The size of the square seating arrangement (n x n).
        """
        try:
            start_time_dt = datetime.strptime(start_time, '%H:%M').time()
            end_time_dt = datetime.strptime(end_time, '%H:%M').time()
        except ValueError:
            raise ValueError("Invalid time format. Please use HH:MM.")

        # Create datetime objects with a default date (1900-01-01) for time comparisons
        start_datetime = datetime.combine(datetime(1900, 1, 1), start_time_dt)
        end_datetime = datetime.combine(datetime(1900, 1, 1), end_time_dt)

        if end_datetime <= start_datetime:
            raise ValueError("End time must be later than start time.")

        self.movies.append({
            'name': name,
            'price': price,
            'start_time': start_datetime,
            'end_time': end_datetime,
            'seats': np.zeros((n, n), dtype=int)  # Use integers for seat representation (0: available, 1: booked)
        })

    def book_ticket(self, movie_name, seats_to_book):
        """
        Books tickets for a specified movie.

        Args:
            movie_name (str): The name of the movie to book tickets for.
            seats_to_book (list of tuples): A list of (row, col) tuples representing the seats to book.

        Returns:
            str: A message indicating the booking status ("Booking success.", "Booking failed.", or "Movie not found.").
        """
        for movie in self.movies:
            if movie['name'] == movie_name:
                seats = movie['seats']
                rows, cols = seats.shape
                for row, col in seats_to_book:
                    if not (0 <= row < rows and 0 <= col < cols):
                        return "Booking failed. Invalid seat coordinates."

                # Check if any of the seats are already booked
                if any(seats[row, col] == 1 for row, col in seats_to_book):
                    return "Booking failed. Some seats are already booked."

                # Book the seats
                for row, col in seats_to_book:
                    seats[row, col] = 1
                return "Booking success."

        return "Movie not found."

    def available_movies(self, start_time, end_time):
        """
        Retrieves a list of movies that are playing within a given time range.

        Args:
            start_time (str): The start time of the time range in HH:MM format (e.g., "12:00").
            end_time (str): The end time of the time range in HH:MM format (e.g., "22:00").

        Returns:
            list of str: A list of movie names that are playing within the specified time range.
        """
        try:
            start_time_dt = datetime.strptime(start_time, '%H:%M').time()
            end_time_dt = datetime.strptime(end_time, '%H:%M').time()
        except ValueError:
            raise ValueError("Invalid time format. Please use HH:MM.")

        start_datetime = datetime.combine(datetime(1900, 1, 1), start_time_dt)
        end_datetime = datetime.combine(datetime(1900, 1, 1), end_time_dt)

        available_movies_list = []
        for movie in self.movies:
            if movie['start_time'] <= end_datetime and movie['end_time'] >= start_datetime:
                available_movies_list.append(movie['name'])
        return available_movies_list

if __name__ == '__main__':
    system = MovieBookingSystem()
    system.add_movie('Batman', 49.9, '17:05', '19:25', 3)
    print(system.movies)
    print(system.book_ticket('Batman', [(0, 0), (0, 1)]))
    print(system.book_ticket('Batman', [(0, 0)]))
    print(system.book_ticket('batman', [(0, 0)]))
    print(system.available_movies('12:00', '22:00'))