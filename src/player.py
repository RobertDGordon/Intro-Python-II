# Write a class to hold player information, e.g. what room they are in
# currently.

class Player:
    def __init__(self, name, current_room):
        self.name = name
        self.current_room = current_room
    
    def move(self, direction):
        next_room = getattr(self.current_room, f"{direction}_to")
        if next_room == None:
            print(" ")
            print("The path is blocked.")
        else:
            self.current_room = next_room
            print('Current room from move:', self.current_room.name)
            print('Description: ', self.current_room.description)

