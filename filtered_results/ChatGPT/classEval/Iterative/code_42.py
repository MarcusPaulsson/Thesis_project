class Hotel:
    """
    A class representing a hotel management system for managing bookings, check-ins, check-outs, and room availability.
    """

    def __init__(self, name, rooms):
        """
        Initialize the hotel with a name and the available room types.
        :param name: str, the name of the hotel
        :param rooms: dict, available rooms with room types as keys and counts as values
        """
        self.name = name
        self.available_rooms = rooms
        self.booked_rooms = {}

    def book_room(self, room_type, room_number, name):
        """
        Attempt to book a specified number of rooms of a certain type for a guest.
        :param room_type: str, the type of room to book
        :param room_number: int, the number of rooms to book
        :param name: str, the name of the guest
        :return: str or int or bool, result of the booking attempt
        """
        if room_type not in self.available_rooms:
            return False
        
        available_count = self.available_rooms[room_type]
        
        if room_number <= available_count:
            self.available_rooms[room_type] -= room_number
            if room_type not in self.booked_rooms:
                self.booked_rooms[room_type] = {}
            if name not in self.booked_rooms[room_type]:
                self.booked_rooms[room_type][name] = 0
            self.booked_rooms[room_type][name] += room_number
            return 'Success!'
        elif available_count > 0:
            return available_count
        else:
            return False

    def check_in(self, room_type, room_number, name):
        """
        Check in a guest for a booked room.
        :param room_type: str, the type of room
        :param room_number: int, the number of rooms to check in
        :param name: str, the name of the guest
        :return: bool, True if check-in is successful, False otherwise
        """
        if room_type not in self.booked_rooms or name not in self.booked_rooms[room_type]:
            return False
        
        booked_count = self.booked_rooms[room_type][name]
        
        if room_number > booked_count:
            return False
        
        self.booked_rooms[room_type][name] -= room_number
        if self.booked_rooms[room_type][name] == 0:
            del self.booked_rooms[room_type][name]
        
        return True

    def check_out(self, room_type, room_number):
        """
        Check out a number of rooms, updating availability.
        :param room_type: str, the type of room
        :param room_number: int, the number of rooms to check out
        """
        if room_type not in self.available_rooms:
            self.available_rooms[room_type] = 0
        self.available_rooms[room_type] += room_number

    def get_available_rooms(self, room_type):
        """
        Get the count of available rooms of a specific type.
        :param room_type: str, the type of room to check
        :return: int, the count of available rooms
        """
        return self.available_rooms.get(room_type, 0)