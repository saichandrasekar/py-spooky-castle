from character import Character
from character import Enemy
from item import Item

dave = Enemy('Dave', 'A smelly zombie')
#dave.describe()

dave.set_conversation('Hi hello. How are you')
dave.talk()
dave.set_weakness('cheese')

print('What will you fight with')
fight_with = input()
dave.fight(fight_with)
