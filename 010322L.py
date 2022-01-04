class Item:
    def __init__(self, value, details):
        self.id = value
        #In an ideal world, this should probably be gotten from a lookup table
        self.pos = details[pos]
        self.effect = details[pos]

    def equip(self, character):
        character.setItem(pos, self)

    def use(self):
        return self.effect