# Write a class to hold player information, e.g. what room they are in
# currently.

class Player:
    def __init__(self, name, current_room):
        self.name = name
        self.current_room = current_room
        self.items = []
    
    def move(self, direction):
        next_room = getattr(self.current_room, f"{direction}_to")
        if next_room == None:
            print(" ")
            print("You can't go that way.")
        else:
            self.current_room = next_room
            print(" ")
            print('Current room from move:', self.current_room.name)
            print('Description: ', self.current_room.description)

    def look(self):
        self.current_room.room_items()

    def inventory(self):
        print(" ")
        print("Inventory:")
        for item in self.items:
            print(item.name)

    def addItem(self, action):
        print(f"Adding {action}")
        for item in self.current_room.items:
            if item.name == action:
                self.items.append(item)
                self.current_room.removeItem(item)
            else:
                print(f'Error, cannot find {action}')
        
    def dropItem(self, action):
        print(f"Dropping {action}")
        for item in self.items:
            if item.name == action:
                self.items.remove(item)
                self.current_room.addItem(item)
            else:
                print(f'Error, cannot drop {action}')
