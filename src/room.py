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

    def addItem(self, *newItems):
        for item in newItems:
            self.items.append(item)

    def removeItem(self, item):
        for roomItem in self.items:
            if item == roomItem.name:
                self.items.remove(roomItem)
        # if item in self.items.name:
        #     self.items.remove(item)
        # else:
        #     print(f"Cannot find {item}")

    def room_items(self):
        if len(self.items) == 0:
            print(" ")
            print("The room is empty.")
        else:
            print("In the room is:")
            for item in self.items:
                print(item.name)