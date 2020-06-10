class Item:
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def __str__(self):
        return f'{self.name} - {self.description}'

items = {
    "Flashlight": Item('Anchor',
                       'The item is used to see in the dark'),
    "Coin": Item('Coin', 
                        'They are the main currency of my adventure game'),
    "Rusty Sword": Item('Rusty Sword',
                        'Rusty swords are plentiful but do little damage'),
    "Shiny Sword": Item('Shiny Sword',
                        'If the player gets a Star, they will become invincible.'),
    "Health Kit": Item('Health Kit',
                        'Used to restore health to 100%')
}