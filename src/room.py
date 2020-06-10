# Implement a class to hold room information. This should have name and
# description attributes.
class Room:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.n_to = None
        self.s_to = None
        self.e_to = None
        self.w_to = None
        self.items = []

    def __repr__(self):
        return f'{self.name} - {self.description}' 
    
    def __str__(self):
        print('\n')
        return f'Current room is {self.name}:\n\n{self.description}'

    def print_items(self):
        print(self.items)

    def add_items_to_room(self, item):
        self.items.append(item)

