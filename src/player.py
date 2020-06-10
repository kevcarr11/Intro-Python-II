# Write a class to hold player information, e.g. what room they are in
# currently.
class Player:
    def __init__(self, name, current_room):
        self.name = name
        self.current_room = current_room
        self.items = []

    def add_items_to_player(self, item):
        self.items.append(item)

    def move_player(self, direction):
        if direction == 'n':
            return self.current_room.n_to
        elif (direction == 's'):
            return self.current_room.s_to
        elif (direction == 'e'):
            return self.current_room.e_to
        elif (direction == 'w'):
            return self.current_room.w_to 
            
    def __str__(self):
        output = f'{self.name} - {self.current_room} \n'
        for idx, item in enumerate(self.items):
            output += ' ' + str(idx+1) + '. ' + item + '\n'

        return output