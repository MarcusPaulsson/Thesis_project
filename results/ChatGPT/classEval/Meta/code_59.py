from datetime import datetime
import numpy as np

class MovieBookingSystem:
    def __init__(self):
        self.movies = []

    def add_movie(self, name, price, start_time, end_time, n):
        start_time_dt = datetime.strptime(start_time, '%H:%M')
        end_time_dt = datetime.strptime(end_time, '%H:%M')
        seats = np.zeros((n, n))
        movie_info = {
            'name': name,
            'price': price,
            'start_time': start_time_dt,
            'end_time': end_time_dt,
            'seats': seats
        }
        self.movies.append(movie_info)

    def book_ticket(self, name, seats_to_book):
        for movie in self.movies:
            if movie['name'].lower() == name.lower():
                for row, col in seats_to_book:
                    if movie['seats'][row][col] == 1:  # Seat is already booked
                        return 'Booking failed.'
                for row, col in seats_to_book:
                    movie['seats'][row][col] = 1  # Book the seats
                return 'Booking success.'
        return 'Movie not found.'

    def available_movies(self, start_time, end_time):
        start_time_dt = datetime.strptime(start_time, '%H:%M')
        end_time_dt = datetime.strptime(end_time, '%H:%M')
        available = []
        for movie in self.movies:
            if movie['start_time'] >= start_time_dt and movie['end_time'] <= end_time_dt:
                available.append(movie['name'])
        return available