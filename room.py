class Room():
    def __init__(self, room_name):
        self.name = room_name
        self.description = None
        self.number_of_rooms = None
        self.number_of_windows = None
        self.location = None
        self.floor_type = None
        self.is_air_conditioned = None
        self.linked_rooms = {}
        self.character = None

    def set_character(self, character):
        self.character = character

    def get_character(self):
        return self.character

    def set_description(self, room_description):
        self.description = room_description

    def get_name(self):
        return self.name

    def set_name(self, room_name):
        self.name = room_name

    def get_decription(self):
        return self.description

    def describe(self):
        print(self.description, self.name)

    def link_room(self, room_to_link, direction):
        self.linked_rooms[direction] = room_to_link
        #print(self.name + " linked rooms :" + repr(self.linked_rooms))

    def get_details(self):
        print(self.name)
        print('--------------------------------')
        print(self.description)
        for direction in self.linked_rooms:
            room = self.linked_rooms[direction]
            print("The " + room.get_name() + " is " + direction)

    def move(self, direction):
        if direction in self.linked_rooms:
            return self.linked_rooms[direction]
        else:
            print('You cannot move in that way')
            return self