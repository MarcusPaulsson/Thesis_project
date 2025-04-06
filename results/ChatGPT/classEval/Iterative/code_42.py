class Hotel:
    """
    This class represents a hotel management system, managing the booking, check-in, check-out, and availability of rooms in a hotel with different room types.
    """

    def __init__(self, name, rooms):
        """
        Initialize the hotel management system.
        :param name: str, the hotel name.
        :param rooms: dict, available rooms by type.
        """
        self.name = name
        self.available_rooms = rooms
        self.booked_rooms = {}

    def book_room(self, room_type, room_number, name):
        """
        Book rooms of a specified type if available.
        :param room_type: str, type of room to book.
        :param room_number: int, number of rooms to book.
        :param name: str, guest name.
        :return: str or int or bool, result of the booking attempt.
        """
        if room_type not in self.available_rooms:
            return False

        if self.available_rooms[room_type] >= room_number:
            self.available_rooms[room_type] -= room_number
            if room_type not in self.booked_rooms:
                self.booked_rooms[room_type] = {}
            self.booked_rooms[room_type][name] = self.booked_rooms[room_type].get(name, 0) + room_number
            return 'Success!'
        else:
            return self.available_rooms[room_type] if self.available_rooms[room_type] > 0 else False

    def check_in(self, room_type, room_number, name):
        """
        Check in a guest if they have a booking.
        :param room_type: str, type of room to check in.
        :param room_number: int, number of rooms to check in.
        :param name: str, guest name.
        :return: bool, whether check-in was successful.
        """
        if room_type not in self.booked_rooms or name not in self.booked_rooms[room_type] or self.booked_rooms[room_type][name] < room_number:
            return False

        if self.booked_rooms[room_type][name] == room_number:
            del self.booked_rooms[room_type][name]
        else:
            self.booked_rooms[room_type][name] -= room_number

        return True

    def check_out(self, room_type, room_number):
        """
        Check out rooms, updating availability.
        :param room_type: str, type of room to check out.
        :param room_number: int, number of rooms to check out.
        """
        if room_type in self.available_rooms:
            self.available_rooms[room_type] += room_number
        else:
            self.available_rooms[room_type] = room_number

    def get_available_rooms(self, room_type):
        """
        Get the number of available rooms of a specific type.
        :param room_type: str, type of room to check.
        :return: int, number of available rooms.
        """
        return self.available_rooms.get(room_type, 0)