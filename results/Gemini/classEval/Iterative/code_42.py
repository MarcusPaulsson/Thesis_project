class Hotel:
    """
    Manages hotel bookings, check-ins, check-outs, and room availability.
    """

    def __init__(self, name, rooms):
        """
        Initializes the Hotel object.

        Args:
            name (str): The name of the hotel.
            rooms (dict): A dictionary representing the available rooms,
                          where keys are room types (e.g., 'single', 'double')
                          and values are the number of available rooms of that type.
        """
        if not isinstance(name, str):
            raise TypeError("Hotel name must be a string.")
        if not isinstance(rooms, dict):
            raise TypeError("Rooms must be a dictionary.")
        for room_type, count in rooms.items():
            if not isinstance(room_type, str):
                raise TypeError("Room type must be a string.")
            if not isinstance(count, int) or count < 0:
                raise ValueError("Room count must be a non-negative integer.")

        self.name = name
        self.available_rooms = rooms.copy()  # Create a copy to avoid external modification
        self.booked_rooms = {}  # {room_type: {guest_name: num_rooms}}

    def book_room(self, room_type, room_number, name):
        """
        Books rooms of a specified type for a guest.

        Args:
            room_type (str): The type of room to book (e.g., 'single', 'double').
            room_number (int): The number of rooms to book.
            name (str): The name of the guest making the booking.

        Returns:
            str: 'Success!' if the booking was successful.
            int: The remaining number of available rooms of that type if the
                 requested number exceeds availability but some rooms are still available.
            bool: False if the room type is not available or the requested number
                  exceeds the total number of rooms of that type.
        Raises:
            TypeError: if room_type or name is not a string, or room_number is not an integer
            ValueError: if room_number is not positive.
        """
        if not isinstance(room_type, str):
            raise TypeError("Room type must be a string.")
        if not isinstance(room_number, int):
            raise TypeError("Room number must be an integer.")
        if not isinstance(name, str):
            raise TypeError("Guest name must be a string.")
        if room_number <= 0:
            raise ValueError("Room number must be positive.")

        if room_type not in self.available_rooms:
            return False

        available = self.available_rooms[room_type]

        if available >= room_number:
            # Update booked_rooms
            if room_type not in self.booked_rooms:
                self.booked_rooms[room_type] = {}
            if name not in self.booked_rooms[room_type]:
                self.booked_rooms[room_type][name] = 0
            self.booked_rooms[room_type][name] += room_number

            # Update available_rooms
            self.available_rooms[room_type] -= room_number
            return 'Success!'
        elif available > 0:
            return available
        else:
            return False

    def check_in(self, room_type, room_number, name):
        """
        Checks a guest into a booked room.

        Args:
            room_type (str): The type of room being checked into.
            room_number (int): The number of rooms being checked into.
            name (str): The name of the guest checking in.

        Returns:
            None

        Raises:
            TypeError: if room_type or name is not a string, or room_number is not an integer
            ValueError: if room_number is not positive.
            ValueError: If the check-in fails due to incorrect information.
        """
        if not isinstance(room_type, str):
            raise TypeError("Room type must be a string.")
        if not isinstance(room_number, int):
            raise TypeError("Room number must be an integer.")
        if not isinstance(name, str):
            raise TypeError("Guest name must be a string.")
        if room_number <= 0:
            raise ValueError("Room number must be positive.")

        if room_type not in self.booked_rooms or name not in self.booked_rooms[room_type]:
            raise ValueError("Check-in failed: No booking found for this room type and guest.")

        booked_number = self.booked_rooms[room_type].get(name, 0)
        if booked_number < room_number:
            raise ValueError("Check-in failed: Number of rooms exceeds booked rooms.")

        self.booked_rooms[room_type][name] -= room_number
        if self.booked_rooms[room_type][name] == 0:
            del self.booked_rooms[room_type][name]
            if not self.booked_rooms[room_type]:
                del self.booked_rooms[room_type]

    def check_out(self, room_type, room_number):
        """
        Checks a guest out of a room, making it available again.

        Args:
            room_type (str): The type of room being checked out.
            room_number (int): The number of rooms being checked out.

        Raises:
            TypeError: if room_type is not a string, or room_number is not an integer
            ValueError: if room_number is not positive.
        """
        if not isinstance(room_type, str):
            raise TypeError("Room type must be a string.")
        if not isinstance(room_number, int):
            raise TypeError("Room number must be an integer.")
        if room_number <= 0:
            raise ValueError("Room number must be positive.")

        if room_type in self.available_rooms:
            self.available_rooms[room_type] += room_number
        else:
            self.available_rooms[room_type] = room_number

    def get_available_rooms(self, room_type):
        """
        Gets the number of available rooms of a specific type.

        Args:
            room_type (str): The type of room to query.

        Returns:
            int: The number of available rooms of the specified type.
        Raises:
            TypeError: if room_type is not a string
        """
        if not isinstance(room_type, str):
            raise TypeError("Room type must be a string.")
        return self.available_rooms.get(room_type, 0)