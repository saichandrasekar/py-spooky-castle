from room import Room
from item import Item
from character import Enemy, Friend
from rpginfo import RPGInfo

kitchen = Room('Kitchen')
kitchen.set_description('A well equipped facility for cooking')

#kitchen.describe()

ball_room = Room('Ballroom')
ball_room.set_description('A swanky place for a get together')
ball_room.link_room(kitchen, "WEST")
kitchen.link_room(ball_room, 'EAST')
#ball_room.describe()

dining_hall = Room('Dining Hall')
dining_hall.set_description('A quiet area for a peaceful food')
dining_hall.link_room(kitchen, 'SOUTH')
kitchen.link_room(dining_hall, 'NORTH')
#dining_hall.describe()

#kitchen.get_details()

table = Item()
table.set_name('Table')
table.set_description('Italian Wooden Table')

#table.describe()

current_room = kitchen

dave = Enemy('Dave', 'A smelly zombie')
dave.set_weakness('cheese')
dining_hall.set_character(dave)

sam = Friend('Sam', 'A smart & brave girl')
ball_room.set_character(sam)

spooky_castle = RPGInfo('THe Spooky Castle')
spooky_castle.welcome()
spooky_castle.info()

RPGInfo.author = "Tm, Sai Chandrasekar with Raspberry Pi Foundation"
RPGInfo.credits()

while True:
    print('\n')
    current_room.get_details()

    inhabitant = current_room.get_character()
    if inhabitant is not None:
        inhabitant.describe()
    print('What do you want to do: direction to move, talk, fight, steal, sleep, bribe or gift')
    command = input('> ')
    #current_room = current_room.move(command)

    if command in ["NORTH", "SOUTH", "EAST", "WEST"]:
        current_room = current_room.move(command)
    elif command == "talk":
        if inhabitant is not None:
            inhabitant.set_conversation('Hi Hello')
            inhabitant.talk()
        else:
            print('There is not one to talk')
    elif command == 'fight':
        if inhabitant is not None:
            print('What will you fight with')
            fight_with = input()
            if not inhabitant.fight(fight_with):
                exit(-1)
        else:
            print('There is no one to fight with')
    elif command == 'sleep':
        if inhabitant is not None:
            inhabitant.do_sleep()
        else:
            print('There is no one in the room...')
    elif command == 'steal':
        if inhabitant is not None:
            inhabitant.steal_stash()
        else:
            print('There is no one in the room...')
    elif command == 'bribe':
        if inhabitant is not None:
            inhabitant.add_bribe(10)
        else:
            print('There is no one in the room...')
    elif command == 'gift':
        print('What do you want to gift')
        gift_item_name = input()
        gift_item = Item()
        gift_item.set_name(gift_item_name)
        if inhabitant is not None and isinstance(inhabitant, Friend):
            inhabitant.give_gift(gift_item)
        else:
            print('There is no one or it is an enemy')