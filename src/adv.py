from room import Room
from player import Player
from item import items
# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
}


# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']


#
# Main

# items
rusty_sword = items['rusty sword']
coin = items['coin']
flashlight = items['flashlight']
shiny_sword = items['shiny star']
health_kit = items['health']

room['outside'].add_items_to_room(rusty_sword)
room['foyer'].add_items_to_room(flashlight)
room['overlook'].add_items_to_room(shiny_sword)
room['narrow'].add_items_to_room(health_kit)
room['treasure'].add_items_to_room(coin)


# Make a new player object that is currently in the 'outside' room.

new_user = input(
    '  Welcome to my adventure game maze. \n \nPlease enter your name to get started: ')
user = Player(new_user, room['outside'])
print(f'Hello {user.name}, do you think you can find the missing treasure?\n')
print(user.current_room)
print('\n')
print('Current items in this room:\n')
for idx, item in enumerate(user.current_room.items):
    print(f'{str(idx+1)}. {item}')
    print('\n')
    print('\n')


# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.

while True:
    choice = input('Please choose your next path or press q to quit: ')
    cmd = len(choice.split(' '))
    try:
        if cmd == 2:
            verb = choice.split(' ')[0].lower()
            action = choice.split(' ')[1]
            if verb == 'get' or verb == 'take':
                for i in user.current_room.items:
                    if i.name.lower() == action.lower():
                        user.items.append(action)
                        print(user.current_room.items)
                        items[str(action)].on_take()
                    else:
                        print('No such item in this room exist')
        elif cmd == 1:
            if (choice == 'q'):
                break
            elif choice == 'n' or choice == 's' or choice == 'e' or choice == 'w':
                if user.move_player(choice) is None:
                    print('You hit a wall, move not allowed')
                else:
                    user.current_room = user.move_player(choice)
                    print(user.current_room)
                    print('\n')
                    print('Items currently in this room:\n')
                    for idx, item in enumerate(user.current_room.items):
                        print(f'{str(idx+1)}. {str(item)}')
                        print('\n')
                        print('\n')
            else:
                print('Please enter a valid direction: n, s, e, w')
        else:
            print('Your input was unrecognized')
    except ValueError:
        print('Please enter a valid direction')
