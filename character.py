class Character():

    # Create a character
    def __init__(self, char_name, char_description):
        self.name = char_name
        self.description = char_description
        self.conversation = None

    # Describe this character
    def describe(self):
        print(self.name + " is here!")
        print(self.description)

    # Set what this character will say when talked to
    def set_conversation(self, conversation):
        self.conversation = conversation

    # Talk to this character
    def talk(self):
        if self.conversation is not None:
            print("[" + self.name + " says]: " + self.conversation)
        else:
            print(self.name + " doesn't want to talk to you")

    # Fight with this character
    def fight(self, combat_item):
        print(self.name + " doesn't want to fight with you")
        return True


class Enemy(Character):

    def __init__(self, char_name, char_description):
        super().__init__(char_name, char_description)
        self.weakness = None
        self.stash = 0
        self.is_wake = True

    def do_sleep(self):
        self.is_wake = False
        self.set_conversation('shhh.......')
        self.talk()

    def add_bribe(self, coins):
        if coins > 0:
            self.set_conversation('Hmmm....I see')
            self.stash += coins
        else:
            self.set_conversation('You puny sticky stick')
        self.talk()

    def steal_stash(self):
        if not self.is_wake:
            coins = self.stash
            self.stash = 0
            return coins
        else:
            self.set_conversation('You puny stick')
            self.talk()

    def set_weakness(self, item):
        self.weakness = item

    def get_weakness(self):
        return self.weakness

    def fight(self, combat_item):
        if combat_item == self.weakness:
            print("You fend " + self.name + " off with the " + combat_item)
            return True
        else:
            print(self.name + " crushes you, puny adventurer")
            return False


class Friend(Character):

    def __init__(self, char_name, char_description):
        super().__init__(char_name, char_description)
        self.gifts = []

    def give_hug(self):
        self.set_conversation('Wow..')
        self.talk()

    def give_gift(self, item):
        self.gifts.append(item)
        self.set_conversation('Thank you pal..')
        self.talk()
        self.show_gifts()

    def show_gifts(self):
        for item in self.gifts:
            print(item.get_name())
