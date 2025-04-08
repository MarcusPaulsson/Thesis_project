class Hotel:
    """
    A class to manage the booking, check-in, check-out, and availability of rooms in a hotel.
    """

    def __init__(self, name, rooms):
        """
        Initialize the hotel management system.
        :param name: str - the hotel name
        :param rooms: dict - available rooms with their types and counts
        """
        self.name = name
        self.available_rooms = rooms
        self.booked_rooms = {}

    def book_room(self, room_type, room_number, guest_name):
        """
        Book rooms of a specified type.
        :param room_type: str - type of room to book
        :param room_number: int - number of rooms to book
        :param guest_name: str - name of the guest
        :return: str or int or bool - booking status
        """
        if room_type not in self.available_rooms:
            return False
        
        available_count = self.available_rooms[room_type]
        
        if available_count >= room_number:
            self.available_rooms[room_type] -= room_number
            self.booked_rooms.setdefault(room_type, {}).setdefault(guest_name, 0)
            self.booked_rooms[room_type][guest_name] += room_number
            return 'Success!'
        elif available_count > 0:
            return available_count
        else:
            return False

    def check_in(self, room_type, room_number, guest_name):
        """
        Check in a guest for the booked room.
        :param room_type: str - type of room to check in
        :param room_number: int - number of rooms to check in
        :param guest_name: str - name of the guest
        :return: bool - check-in status
        """
        if room_type not in self.booked_rooms or guest_name not in self.booked_rooms[room_type]:
            return False
        
        booked_count = self.booked_rooms[room_type][guest_name]
        
        if room_number > booked_count:
            return False
        
        self.booked_rooms[room_type][guest_name] -= room_number
        if self.booked_rooms[room_type][guest_name] == 0:
            del self.booked_rooms[room_type][guest_name]
        return True

    def check_out(self, room_type, room_number):
        """
        Check out a guest and make rooms available again.
        :param room_type: str - type of room to check out
        :param room_number: int - number of rooms to check out
        """
        self.available_rooms.setdefault(room_type, 0)
        self.available_rooms[room_type] += room_number

    def get_available_rooms(self, room_type):
        """
        Get the number of available rooms of a specific type.
        :param room_type: str - the room type to inquire about
        :return: int - the count of available rooms
        """
        return self.available_rooms.get(room_type, 0)