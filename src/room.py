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
        output = f'Current room is {self.name}:\n\n{self.description}\n'
        if self.e_to:
            return f'{output} To the east is: {self.e_to.name} \n'
        elif self.w_to:
            return f'{output} To the west is: {self.w_to.name} \n'
        elif self.s_to:
            return f'{output} To the south is: {self.s_to.name} \n'
        elif self.n_to:
            return f'{output} To the north is: {self.n_to.name} \n'

    def print_items(self):
        print(self.items)

    def add_items_to_room(self, item):
        self.items.append(item)

    def remove_item_from_room(self, item):
        self.items.remove(item)
