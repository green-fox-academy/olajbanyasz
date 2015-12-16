import random
import json

class Character():
    def __init__(self):
        self.name = ""
        self.health = 0
        self.dexterity = 0
        self.luck = 0
        self.potion = ""
        self.position = 1
        self.inventory = {"Leather Armor", "Sword"}

    def returnStartingLuck(self):
        return random.randint(1,6) + 6

    def returnStartingHealth(self):
        return random.randint(1,6) + random.randint(1,6) + 6

    def returnStartingDexterity(self):
        return random.randint(1,6) + 6

    def addItemtoInventory(self, item):
        self.inventory.add(item)

    def removeItemfromInventory(self, item):
        self.inventory.remove(item)

    def makeJsonOutput(self):
        inventorylist = list(self.inventory)
        data = { "name" : self.name, "health" : self.health, "dexterity" : self.dexterity, "luck" : self.luck, "potion" : self.position, "position" : self.position, "inventory" : inventorylist}
        json_str = json.dumps(data, indent=2)
        return json_str
