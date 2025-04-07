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
        if room_type not in self.booked_rooms or name not in self.booked_rooms[room_type] or self.booked_rooms[room_type][name] < room_number:
            return False
        
        self.booked_rooms[room_type][name] -= room_number
        if self.booked_rooms[room_type][name] == 0:
            del self.booked_rooms[room_type][name]

        return True

    def check_out(self, room_type, room_number):
        if room_type not in self.available_rooms:
            self.available_rooms[room_type] = 0
        self.available_rooms[room_type] += room_number

    def get_available_rooms(self, room_type):
        return self.available_rooms.get(room_type, 0)