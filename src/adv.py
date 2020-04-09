from room import Room
from player import Player
from item import Item, Treasure

# Declare all items
book = Treasure("book", "a dusty old book", 100)
flashlight = Treasure("flashlight", "it lights up the dark, batteries included?", 200)
laptop = Treasure("laptop", "a relic from decades ago, but it still powers on...", 500)
disk = Treasure("disk", "a disk that is floppy", 400)

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

room['outside'].addItem(book)
room['foyer'].addItem(disk, flashlight)
room['treasure'].addItem(laptop)


#
# Main
#

# Make a new player object that is currently in the 'outside' room.

player = Player('Bob', room['outside'])

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
    current_room = player.current_room
    print(f" ")
    # print(f"Current room: {current_room.name}")
    # print(f"Description: {current_room.description}")
    # print(f" ")
    move = input("What is your move? ")
    if move == "q":
        print(f" ")
        print(f'Exiting...')
        exit()
    elif move == "n":
        player.move(move)
    elif move == "s":
        player.move(move)
    elif move == "e":
        player.move(move)
    elif move == "w":
        player.move(move)
    else:
        print(f" ")
        print(f'Not so fast...')
