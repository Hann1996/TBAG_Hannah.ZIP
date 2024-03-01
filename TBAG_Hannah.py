from room import room  
from character import Hero 
print()

# Creating instances of Room and setting descriptions
kitchen = room("kitchen")
ballroom = room("ballroom")
dining_hall = room("Dining room")

kitchen.set_descritption("A dark dirty room buzzing with flies")
ballroom.set_descritption("A beautiful place to forget all troubles")
dining_hall.set_descritption("A large room with golden decorations")

# Linking the rooms together
kitchen.link_room(dining_hall, "south")
dining_hall.link_room(kitchen, "north")
dining_hall.link_room(ballroom, "west")
ballroom.link_room(dining_hall, "east")

Richard = Hero("Richard", "A brave knight on a conquest to defeat ogers")
Richard.set_conversation("Onward to victory")
Richard.set_weakness("Ogers")

dining_hall.set_character(Richard)

current_room = kitchen
while True:
    print("\n")
    current_room.get_details()
    inhabitant = current_room.get_character()
    
    if inhabitant is not None:
     inhabitant.describe()

    command = input("what is you command > ")
    if command == "exit":
       
        current_room = kitchen.move(command)

        command=input(">")

    
    elif command in ["north", "south", "east", "west"]:
        current_room = current_room.move(command)
    elif command == "talk":
        if current_room.inhabitant:
            current_room.inhabitant.talk()
        else:
            print("There's no one to talk to in this room.")
    elif command == "fight":
        if current_room.inhabitant:
            weapon_choice = input("Choose a weapon to fight with: ")
            result = current_room.inhabitant.fight(weapon_choice)
            if not result:
                print("You lost the fight. Game over.")
                break
        else:
            print("There's no one to fight in this room.")
    elif command == "steal":
        if current_room.inhabitant:
            current_room.inhabitant.steal()
    else:
        print("there`s no one to steal from in this room.")
command == "bribe"
if current_room.inhabitant:
           current_room.inhabitant.bribe()
else:
            print("there`s no one to bribe in this room.")
command == "sleep"
if current_room.inhabitant:
        current_room.inhabitant.sleep()
else:
    print("there`s no one to make sleep in this room.")

else:
print("Invalid command. Try again.")


class New_Friend(Character):
    def __init__(self, name, description):
        super().__init__(name, description)
        self.gift_received = False


def hug (self):
     print(f"{self.name}: A warm greeing from a friend is always delightful!")

def offer_gift(self):
        print(f"{self.name}: How thoughful! I accept your gift with gratitude.")
        self.gift_recieved = True

new_friend = ("Buddy" , "A new friend made along the journey.")
new_friend.hug ("Greet new friend and embark on journey to defeat ogers together.")
new_friend.offer_gift("offer Buddy a healing potion.")

command == "hug"
if current_room.inhabitant and isinstance(current_room.inhabitant):
     current_room.inhabitant.hug ()
else:
     print ("There is one new friend Buddy to hug in this room.")
command == "offer_gift"
if current_room.inhabitant and isinstance(current_room.inhabitant):
    current_room.inhabitant.offer_gift()
else: 
    print("There is on new friend Buddy to offer gift to in this room.")


class Task:
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def perform_action(self):
        print(f"You perform the task: {self.name}")

# Example usage:
sword = Task("Sword", "A sharp and shiny sword")

# Accessing attributes
print(f"Task: {sword.name}")
print(f"Description: {sword.description}")

# Performing the action associated with the task
sword.perform_action()
