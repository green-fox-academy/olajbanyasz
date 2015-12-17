import random
import json
import os

class Character():
    def __init__(self):
        self.name = ""
        self.health = 0
        self.dexterity = 0
        self.luck = 0
        self.potion = "Health Potion"
        self.position = 1
        self.inventory = {"Leather Armor", "Sword"}

    def returnHealthLuckDexterity(self):
        self.luck = random.randint(1,6) + 6
        self.health = random.randint(1,6) + random.randint(1,6) + 6
        self.dexterity = random.randint(1,6) + 6

    def playersnamesetter(self):
        os.system("clear")
        self.name = input("Please write your name: ")

    def addItemtoInventory(self, item):
        self.inventory.add(item)

    def removeItemfromInventory(self, item):
        self.inventory.remove(item)

    def addHealthPotiontoHero(self):
        self.potion = "Health Potion"

    def addDexterityPotiontoHero(self):
        self.potion = "Dexterity Potion"

    def addLuckPotiontoHero(self):
        self.potion = "Luck Potion"

    def displaycharacterfeatures(self):
        if self.name != "":
            print(      "You      : " + self.name +
                        " | H:" + str(self.health) +
                        " | D:" + str(self.dexterity) +
                        " | L:" + str(self.luck) +
                        " | Potion: " + self.potion + "\n"
                        "Inventory: " + str(self.inventory) + "\n")

    def makeJsonOutput(self):
        inventorylist = list(self.inventory)
        data = { "name" : self.name, "health" : self.health, "dexterity" : self.dexterity, "luck" : self.luck, "potion" : self.potion, "position" : self.position, "inventory" : inventorylist}
        json_str = json.dumps(data, indent=2)
        return json_str
