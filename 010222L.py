class Character:
    def __init__(self, stats, items, abilities):
        # Expected: Dictionary (Stat -> Value)
        self.statBlock = stats
        # Expected: Dictionary (Location -> Item)
        self.itemBlock = items
        # Expected: List
        self.abilityBlock = abilities

    def levelUp(self, quant = 1):
        self.statBlock["level"] += quant

    def statChange(self, stat, quant):
        self.statBlock[stat] += quant

    def setItem(self, pos, item):
        #TODO check if this works right with pointers
        temp = self.itemBlock[pos]
        self.itemBlock[pos] = item
        return temp

    def gainAbility(self, ability):
        self.abilityBlock.append(ability)
