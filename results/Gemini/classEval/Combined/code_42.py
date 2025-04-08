class Hotel:
    """
    Manages hotel bookings, check-ins, check-outs, and room availability.
    """

    def __init__(self, name, rooms):
        """
        Initializes the Hotel object.

        Args:
            name (str): The name of the hotel.
            rooms (dict): A dictionary representing the available rooms, where keys are room types (e.g., 'single', 'double')
                         and values are the number of available rooms of that type.
        """
        self.name = name
        self.available_rooms = rooms
        self.booked_rooms = {}

    def book_room(self, room_type, room_number, guest_name):
        """
        Books a room of the specified type for the given guest.

        Args:
            room_type (str): The type of room to book (e.g., 'single', 'double').
            room_number (int): The number of rooms to book.
            guest_name (str): The name of the guest making the booking.

        Returns:
            str: 'Success!' if the booking was successful.
            int: The number of available rooms of the requested type if the requested number exceeds availability, but some rooms are available.
            bool: False if the room type doesn't exist or if there are no rooms of that type available.
        """
        if room_type not in self.available_rooms:
            return False

        available_rooms = self.available_rooms[room_type]

        if room_number <= available_rooms:
            if room_type not in self.booked_rooms:
                self.booked_rooms[room_type] = {}

            if guest_name not in self.booked_rooms[room_type]:
                self.booked_rooms[room_type][guest_name] = 0

            self.booked_rooms[room_type][guest_name] += room_number
            self.available_rooms[room_type] -= room_number
            return 'Success!'
        elif available_rooms > 0:
            return available_rooms
        else:
            return False

    def check_in(self, room_type, room_number, guest_name):
        """
        Checks in a guest to a booked room.

        Args:
            room_type (str): The type of room being checked into.
            room_number (int): The number of rooms being checked into.
            guest_name (str): The name of the guest checking in.

        Returns:
            bool: False if the room_type is not in the booked_rooms, guest name is not in the booked rooms for that type or room_number exceeds the booked quantity. None otherwise.
        """
        if room_type not in self.booked_rooms or guest_name not in self.booked_rooms[room_type] or room_number > self.booked_rooms[room_type][
            guest_name]:
            return False

        self.booked_rooms[room_type][guest_name] -= room_number

        if self.booked_rooms[room_type][guest_name] == 0:
            del self.booked_rooms[room_type][guest_name]
            if not self.booked_rooms[room_type]:
                del self.booked_rooms[room_type]

        return

    def check_out(self, room_type, room_number):
        """
        Checks out a guest from a room, making it available again.

        Args:
            room_type (str): The type of room being checked out.
            room_number (int): The number of rooms being checked out.
        """
        self.available_rooms[room_type] = self.available_rooms.get(room_type, 0) + room_number

    def get_available_rooms(self, room_type):
        """
        Gets the number of available rooms of a specific type.

        Args:
            room_type (str): The type of room to check availability for.

        Returns:
            int: The number of available rooms of the specified type.
        """
        return self.available_rooms.get(room_type, 0)