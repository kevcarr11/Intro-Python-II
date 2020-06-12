class Item:
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def __str__(self):
        return f'{self.name} - {self.description}'

    def on_take(self):
        print(f'You have picked up a {self.name}')

items = {
    "flashlight": Item('Flashlight',
                       'The item is used to see in the dark'),
    "coin": Item('Coin', 
                        'They are the main currency of my adventure game'),
    "rusty sword": Item('Rusty Sword',
                        'Rusty swords are plentiful but do little damage'),
    "shiny star": Item('Shiny Star',
                        'If the player gets a Star, they will become invincible.'),
    "health": Item('Health',
                   'Used to restore health to 100%')
}