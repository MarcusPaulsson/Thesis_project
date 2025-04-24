class Hotel:
    """
    This is a class as hotel management system, managing the booking, check-in, check-out, and availability of rooms in a hotel with different room types.
    """

    def __init__(self, name, rooms):
        """
        Initialize the three fields in Hotel System.
        name is the hotel name.
        available_rooms stores the remaining rooms in the hotel
        booked_rooms stores the rooms that have been booked and the person's name who booked rooms.
        """
        self.name = name
        self.available_rooms = rooms
        self.booked_rooms = {}

    def book_room(self, room_type, room_number, name):
        """
        Books a room of the specified type for a guest.

        :param room_type: The type of room to book (e.g., "single", "double").
        :param room_number: The number of rooms of the specified type to book.
        :param name: The name of the guest making the booking.
        :return: "Success!" if the booking was successful.
                 The number of available rooms of the specified type if the requested number exceeds availability.
                 False if the room type is not available or if there are no rooms of that type available.
        """
        if room_type not in self.available_rooms:
            return False

        if self.available_rooms[room_type] == 0:
            return False

        if room_number <= self.available_rooms[room_type]:
            if room_type not in self.booked_rooms:
                self.booked_rooms[room_type] = {}

            if name not in self.booked_rooms[room_type]:
                self.booked_rooms[room_type][name] = 0

            self.booked_rooms[room_type][name] += room_number
            self.available_rooms[room_type] -= room_number
            return 'Success!'
        else:
            return self.available_rooms[room_type]

    def check_in(self, room_type, room_number, name):
        """
        Checks a guest into a booked room.

        :param room_type: The type of room to check into.
        :param room_number: The number of rooms to check into.
        :param name: The name of the guest checking in.
        :return: True if the check-in was successful, False otherwise.
        """
        if room_type not in self.booked_rooms:
            return False

        if name not in self.booked_rooms[room_type]:
            return False

        if self.booked_rooms[room_type][name] < room_number:
            return False

        self.booked_rooms[room_type][name] -= room_number

        if self.booked_rooms[room_type][name] == 0:
            del self.booked_rooms[room_type][name]
            if not self.booked_rooms[room_type]:
                del self.booked_rooms[room_type]

        return True

    def check_out(self, room_type, room_number):
        """
        Checks a guest out of a room, making it available again.

        :param room_type: The type of room to check out.
        :param room_number: The number of rooms to check out.
        """
        if room_type in self.available_rooms:
            self.available_rooms[room_type] += room_number
        else:
            self.available_rooms[room_type] = room_number

    def get_available_rooms(self, room_type):
        """
        Gets the number of available rooms of a specific type.

        :param room_type: The type of room to check availability for.
        :return: The number of available rooms of the specified type.
        """
        if room_type in self.available_rooms:
            return self.available_rooms[room_type]
        else:
            return 0