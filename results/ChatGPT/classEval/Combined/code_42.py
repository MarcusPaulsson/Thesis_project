class Hotel:
    """
    A hotel management system that manages room booking, check-in, check-out, and room availability for various room types.
    """

    def __init__(self, name, rooms):
        """
        Initialize the hotel with a name and a dictionary of available rooms.
        
        :param name: str, the hotel name.
        :param rooms: dict, available rooms by type and quantity.
        """
        self.name = name
        self.available_rooms = rooms
        self.booked_rooms = {}

    def book_room(self, room_type, room_number, name):
        """
        Book a specified number of rooms of a certain type for a guest.
        
        :param room_type: str, the type of room to be booked.
        :param room_number: int, the number of rooms to book.
        :param name: str, the name of the guest booking the room.
        :return: str or int or bool, booking status.
        """
        if room_type not in self.available_rooms:
            return False

        available_count = self.available_rooms[room_type]
        if room_number <= available_count:
            self.available_rooms[room_type] -= room_number
            self.booked_rooms.setdefault(room_type, {})
            self.booked_rooms[room_type][name] = self.booked_rooms[room_type].get(name, 0) + room_number
            return 'Success!'
        elif available_count > 0:
            return available_count
        return False

    def check_in(self, room_type, room_number, name):
        """
        Check in a guest if their room is booked.
        
        :param room_type: str, the type of room.
        :param room_number: int, the number of rooms to check in.
        :param name: str, the name of the guest checking in.
        :return: bool, check-in success status.
        """
        if room_type not in self.booked_rooms or name not in self.booked_rooms[room_type]:
            return False

        booked_count = self.booked_rooms[room_type][name]
        if room_number > booked_count:
            return False

        if room_number == booked_count:
            del self.booked_rooms[room_type][name]
        else:
            self.booked_rooms[room_type][name] -= room_number
        
        return True

    def check_out(self, room_type, room_number):
        """
        Check out a specified number of rooms and update availability.
        
        :param room_type: str, the type of room to check out.
        :param room_number: int, the number of rooms to check out.
        """
        if room_type not in self.available_rooms:
            self.available_rooms[room_type] = 0
        
        self.available_rooms[room_type] += room_number

    def get_available_rooms(self, room_type):
        """
        Get the count of available rooms of a specific type.
        
        :param room_type: str, the type of room.
        :return: int, the number of available rooms.
        """
        return self.available_rooms.get(room_type, 0)