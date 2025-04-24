class Hotel:
    """
    A class to manage hotel bookings, check-ins, check-outs, and room availability.
    """

    def __init__(self, name, rooms):
        """
        Initialize the hotel management system.
        
        :param name: str, the hotel name.
        :param rooms: dict, available rooms in the hotel.
        """
        self.name = name
        self.available_rooms = rooms
        self.booked_rooms = {}

    def book_room(self, room_type, room_number, guest_name):
        """
        Book a specified number of rooms for a guest.

        :param room_type: str, type of room to book.
        :param room_number: int, number of rooms to book.
        :param guest_name: str, guest name.
        :return: str or int or bool, booking status.
        """
        if room_type not in self.available_rooms:
            return False

        available_count = self.available_rooms[room_type]

        if room_number <= available_count:
            self.available_rooms[room_type] -= room_number
            self.booked_rooms.setdefault(room_type, {}).setdefault(guest_name, 0)
            self.booked_rooms[room_type][guest_name] += room_number
            return 'Success!'
        else:
            return available_count if available_count > 0 else False

    def check_in(self, room_type, room_number, guest_name):
        """
        Check in a guest for a specified number of rooms.

        :param room_type: str, type of room to check in.
        :param room_number: int, number of rooms to check in.
        :param guest_name: str, guest name.
        :return: bool, check-in status.
        """
        if room_type not in self.booked_rooms or guest_name not in self.booked_rooms[room_type]:
            return False

        booked_count = self.booked_rooms[room_type][guest_name]

        if room_number > booked_count:
            return False

        if room_number == booked_count:
            del self.booked_rooms[room_type][guest_name]
        else:
            self.booked_rooms[room_type][guest_name] -= room_number

        return True

    def check_out(self, room_type, room_number):
        """
        Check out a specified number of rooms.

        :param room_type: str, type of room to check out.
        :param room_number: int, number of rooms to check out.
        """
        self.available_rooms[room_type] = self.available_rooms.get(room_type, 0) + room_number

    def get_available_rooms(self, room_type):
        """
        Get the number of available rooms of a specified type.

        :param room_type: str, type of room to check.
        :return: int, number of available rooms.
        """
        return self.available_rooms.get(room_type, 0)