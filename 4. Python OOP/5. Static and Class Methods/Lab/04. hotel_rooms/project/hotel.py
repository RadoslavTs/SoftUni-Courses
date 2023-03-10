from project.room import Room


class Hotel:
    def __init__(self, name: str):
        self.name = name
        self.rooms = []
        self.guests = 0

    @classmethod
    def from_stars(cls, stars_count: int):
        return cls(f"{stars_count} stars Hotel")

    def add_room(self, room: Room):
        self.rooms.append(room)

    def take_room(self, room_number, people):
        try:
            room = next(filter(lambda x: x.number == room_number, self.rooms))
            result = room.take_room(people)

            if result:
                return result

            self.guests += people

        except StopIteration:
            pass

    def free_room(self, room_number):
        try:
            room = next(filter(lambda x: x.number == room_number, self.rooms))
            guests = room.guests
            result = room.free_room()
            if result:
                return result

            self.guests -= guests

        except StopIteration:
            pass

    def status(self):
        return f"Hotel {self.name} has {self.guests} total guests\n" \
               f"Free rooms: {', '.join(str(x.number) for x in self.rooms if not x.is_taken)}\n" \
               f"Taken rooms: {', '.join(str(x.number) for x in self.rooms if x.is_taken)}"