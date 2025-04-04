class Hotel:
    """
    This is a class for hotel management system, managing the booking, check-in, check-out, and availability of rooms in a hotel with different room types.
    """

    def __init__(self, name, rooms):
        """
        Initialize the hotel name, available rooms, and booked rooms.
        :param name: str, the hotel name
        :param rooms: dict, available rooms by type
        """
        self.name = name
        self.available_rooms = rooms
        self.booked_rooms = {room_type: {} for room_type in rooms}

    def book_room(self, room_type, room_number, name):
        """
        Book a specified number of rooms for a guest.
        :param room_type: str, type of room to book
        :param room_number: int, number of rooms to book
        :param name: str, guest name
        :return: str or int or bool, booking status
        """
        if room_type not in self.available_rooms:
            return False

        available = self.available_rooms[room_type]
        if room_number <= available:
            self.available_rooms[room_type] -= room_number
            self.booked_rooms[room_type][name] = self.booked_rooms[room_type].get(name, 0) + room_number
            return 'Success!'
        elif available > 0:
            return available
        return False

    def check_in(self, room_type, room_number, name):
        """
        Check in a guest to their booked room.
        :param room_type: str, type of room to check in
        :param room_number: int, number of rooms to check in
        :param name: str, guest name
        :return: bool, check-in status
        """
        if room_type not in self.booked_rooms or name not in self.booked_rooms[room_type]:
            return False

        booked_rooms = self.booked_rooms[room_type][name]
        if room_number > booked_rooms:
            return False

        if room_number == booked_rooms:
            del self.booked_rooms[room_type][name]
        else:
            self.booked_rooms[room_type][name] -= room_number

        return True

    def check_out(self, room_type, room_number):
        """
        Check out a specified number of rooms and update available rooms.
        :param room_type: str, type of room to check out
        :param room_number: int, number of rooms to check out
        """
        if room_type in self.available_rooms:
            self.available_rooms[room_type] += room_number
        else:
            self.available_rooms[room_type] = room_number

    def get_available_rooms(self, room_type):
        """
        Get the number of specific type of available rooms.
        :param room_type: str, the room type to check
        :return: int, the remaining number of this type of rooms
        """
        return self.available_rooms.get(room_type, 0)