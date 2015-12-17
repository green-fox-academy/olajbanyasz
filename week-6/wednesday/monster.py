import random
import json
import os

class Monster():
    def __init__(self):
        self.name = "Monster"
        self.health = 0
        self.dexterity = 0
        self.luck = 0

    def returnHealthDexterity(self):
        self.health = random.randint(1,6) + random.randint(1,6) + 6
        self.dexterity = random.randint(1,6) + 6

    def returnLuck(self):
        self.luck = random.randint(1,6) + random.randint(1,6)

    def displaymonsterfeatures(self):
        if self.name != "":
            print(      "Enemy    : " + self.name +
                        " | H:" + str(self.health) +
                        " | D:" + str(self.dexterity) +
                        " | L:" + str(self.luck) + "\n")
