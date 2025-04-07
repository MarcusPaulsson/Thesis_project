from datetime import datetime
import numpy as np

class MovieBookingSystem:
    def __init__(self):
        self.movies = []

    def add_movie(self, name, price, start_time, end_time, n):
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
        movie = next((m for m in self.movies if m['name'].lower() == name.lower()), None)
        if not movie:
            return 'Movie not found.'

        for row, col in seats_to_book:
            if movie['seats'][row][col] == 1:
                return 'Booking failed.'

        for row, col in seats_to_book:
            movie['seats'][row][col] = 1

        return 'Booking success.'

    def available_movies(self, start_time, end_time):
        start_time_dt = datetime.strptime(start_time, '%H:%M')
        end_time_dt = datetime.strptime(end_time, '%H:%M')
        available = [
            movie['name'] for movie in self.movies 
            if movie['start_time'] >= start_time_dt and movie['end_time'] <= end_time_dt
        ]
        return available