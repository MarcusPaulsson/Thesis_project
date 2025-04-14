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
                          where keys are room types (str) and values are
                          the number of available rooms of that type (int).
        """
        self.name = name
        self.available_rooms = rooms.copy()  # Create a copy to avoid modifying the original
        self.booked_rooms = {}

    def book_room(self, room_type, room_number, name):
        """
        Books rooms of a specified type for a guest.

        Args:
            room_type (str): The type of room to book.
            room_number (int): The number of rooms to book.
            name (str): The name of the guest making the booking.

        Returns:
            str: 'Success!' if the booking was successful.
            int: The number of available rooms of the specified type if the
                 requested number exceeds availability but some rooms are still available.
            bool: False if the room type is not available or if there are no
                  rooms of the specified type available.
        """
        if room_type not in self.available_rooms:
            return False

        available = self.available_rooms[room_type]

        if room_number <= available:
            self.available_rooms[room_type] -= room_number

            if room_type not in self.booked_rooms:
                self.booked_rooms[room_type] = {}

            if name not in self.booked_rooms[room_type]:
                self.booked_rooms[room_type][name] = 0

            self.booked_rooms[room_type][name] += room_number
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
            bool: True if check-in was successful, False otherwise.
        """
        if room_type not in self.booked_rooms or name not in self.booked_rooms[room_type] or self.booked_rooms[room_type].get(name, 0) < room_number:
            return False

        if room_number == self.booked_rooms[room_type][name]:
            del self.booked_rooms[room_type][name]
            if not self.booked_rooms[room_type]:
                del self.booked_rooms[room_type]
        else:
            self.booked_rooms[room_type][name] -= room_number
        return True

    def check_out(self, room_type, room_number):
        """
        Checks a guest out of a room, making it available again.

        Args:
            room_type (str): The type of room being checked out.
            room_number (int): The number of rooms being checked out.
        """
        self.available_rooms[room_type] = self.available_rooms.get(room_type, 0) + room_number

    def get_available_rooms(self, room_type):
        """
        Gets the number of available rooms of a specified type.

        Args:
            room_type (str): The type of room to check availability for.

        Returns:
            int: The number of available rooms of the specified type.
        """
        return self.available_rooms.get(room_type, 0)