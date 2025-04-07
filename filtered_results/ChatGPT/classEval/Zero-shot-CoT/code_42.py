class Hotel:
    def __init__(self, name, rooms):
        self.name = name
        self.available_rooms = rooms
        self.booked_rooms = {}

    def book_room(self, room_type, room_number, name):
        if room_type not in self.available_rooms:
            return False
        if self.available_rooms[room_type] >= room_number:
            if room_type not in self.booked_rooms:
                self.booked_rooms[room_type] = {}
            if name in self.booked_rooms[room_type]:
                self.booked_rooms[room_type][name] += room_number
            else:
                self.booked_rooms[room_type][name] = room_number
            
            self.available_rooms[room_type] -= room_number
            return 'Success!'
        else:
            remaining = self.available_rooms[room_type]
            return remaining if remaining > 0 else False

    def check_in(self, room_type, room_number, name):
        if room_type not in self.booked_rooms or name not in self.booked_rooms[room_type]:
            return False
        booked_number = self.booked_rooms[room_type][name]
        if room_number > booked_number:
            return False
        if room_number == booked_number:
            del self.booked_rooms[room_type][name]
        else:
            self.booked_rooms[room_type][name] -= room_number
        return True

    def check_out(self, room_type, room_number):
        if room_type in self.available_rooms:
            self.available_rooms[room_type] += room_number
        else:
            self.available_rooms[room_type] = room_number

    def get_available_rooms(self, room_type):
        return self.available_rooms.get(room_type, 0)