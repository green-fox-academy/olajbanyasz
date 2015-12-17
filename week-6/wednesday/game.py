from menu import *
from menuitem import *
from character import *
from monster import *
import time

class Game():

    def __init__(self):
        self.menu = None
        self.mainmenu()
        self.player = Character()
        self.enemy = Monster()

    def mainmenu(self):
        self.menu = Menu([
                        MenuItem(1, "New Game", self.newgamemenu),
                        MenuItem(2, "Load Game", self.loadGame),
                        MenuItem(0, "Exit Game", exit),
                        ])

    def rerollmenu(self):
        self.player.returnHealthLuckDexterity()
        self.player.displaycharacterfeatures()
        self.menu = Menu([
                        MenuItem(1, "Reroll Stats", self.rerollmenu),
                        MenuItem(2, "Continue", self.selectpotionmenu),
                        MenuItem(3, "Save Game", self.saveGame),
                        MenuItem(0, "Quit", exit)
                        ])

    def newgamemenu(self):
        self.player.playersnamesetter()
        self.player.displaycharacterfeatures()
        self.menu = Menu([
                        MenuItem(1, "Reenter Name", self.newgamemenu),
                        MenuItem(2, "Continue", self.rerollmenu),
                        MenuItem(3, "Save Game", self.saveGame),
                        MenuItem(0, "Quit", exit)
                        ])

    def quitmenu(self):
        self.player.displaycharacterfeatures()
        self.menu = Menu([
                        MenuItem(1, "Quit without save", exit),
                        MenuItem(2, "Quit with save", self.saveGame),
                        MenuItem(0, "Resume", self.beginmenu)
                        ])

    def savemenu(self):
        self.player.displaycharacterfeatures()
        self.menu = Menu([
                        MenuItem(1, "Add New Item", self.saveGame),
                        MenuItem(2, "Resume", self.mainmenu),
                        MenuItem(3, "Quit", exit)
                        ])

    def selectpotionmenu(self):
        self.player.displaycharacterfeatures()
        self.menu = Menu([
                        MenuItem(1, "Select - Potion of Health", self.player.addHealthPotiontoHero),
                        MenuItem(2, "Select - Potion of Dexterity", self.player.addDexterityPotiontoHero),
                        MenuItem(3, "Select - Potion of Luck", self.player.addLuckPotiontoHero),
                        MenuItem(4, "Continue", self.reselectpotionmenu),
                        ])

    def reselectpotionmenu(self):
        self.player.displaycharacterfeatures()
        self.menu = Menu([
                        MenuItem(1, "Reselect Potion", self.selectpotionmenu),
                        MenuItem(2, "Continue", self.beginmenu),
                        MenuItem(3, "Quit", self.savemenu)
                        ])

    def beginmenu(self):
        self.player.displaycharacterfeatures()
        self.menu = Menu([
                        MenuItem(1, "Begin Game", self.rollenemyfeatures),
                        MenuItem(2, "Save Game", self.saveGame),
                        MenuItem(3, "Quit", self.reselectpotionmenu)
                        ])

    def rollenemyfeatures(self):
        self.enemy.returnHealthDexterity()
        self.fightmenu()

    def fightmenu(self):
        os.system("clear")
        self.player.displaycharacterfeatures()
        self.enemy.displaymonsterfeatures()
        self.menu = Menu([
                        MenuItem(1, "Strike", self.strike),
                        MenuItem(2, "Retreat", self.saveGame),
                        MenuItem(3, "Quit", self.saveGame)
                        ])

    def strike(self):
        os.system("clear")
        self.enemy.luck = 0
        self.player.displaycharacterfeatures()
        self.enemy.displaymonsterfeatures()
        if int(self.player.dexterity) >= int(self.enemy.dexterity):
            print("You hit the monster\n")
        else:
            print("The monster hits you\n")
        self.menu = Menu([
                        MenuItem(1, "Continue", self.storethechanges),
                        MenuItem(2, "Try your luck", self.tryluck),
                        MenuItem(3, "Retreat", self.saveGame),
                        MenuItem(4, "Quit", self.saveGame)
                        ])

    def storethechanges(self):
        os.system("clear")
        if int(self.player.dexterity) >= int(self.enemy.dexterity):
            self.enemy.health -= 2
        else:
            self.player.health -= 2
        self.fightmenu()

    def tryluck(self):
        self.enemy.returnLuck()
        a = int(self.player.luck) < int(self.enemy.luck)
        b = int(self.player.dexterity) < int(self.enemy.dexterity)
        if a and b:
            self.player.health = int(self.player.health) - 3
            print("You have no luck!")
        elif not(a) and b:
            self.player.health = int(self.player.health) - 1
            self.player.luck = int(self.player.luck) - 1
            print("You have luck!")
        elif a and not(b):
            self.enemy.health = int(self.enemy.health) - 1
            print("You have no luck!")
        else:
            self.enemy.health = int(self.enemy.health) - 4
            self.player.luck = int(self.player.luck) - 1
            print("You have luck!")
        time.sleep(3)
        self.fightmenu()

    def listingJsonFilesinThisDirectory(self):
        filesinthisdirectory = os.listdir()
        jsonfilesinthisdirectory = list(filter(lambda x: x.endswith(".json"), filesinthisdirectory))
        return jsonfilesinthisdirectory

    def loadGame(self):
        os.system("clear")
        jsonfilesinthisdirectory = self.listingJsonFilesinThisDirectory()
        if len(jsonfilesinthisdirectory) == 0:
            print("No Early Saves!")
        else:
            print("Early Saves:\n")
            for i in range(len(jsonfilesinthisdirectory)):
                print(str(i) + " : "  + jsonfilesinthisdirectory[i])
            try:
                print("\n")
                choice = int(input("Choose a file from saves: "))
                os.system("clear")
                if not 0 <= choice <= len(jsonfilesinthisdirectory)-1:
                    os.system("clear")
                    print("Wrong choice!")
                    loadGame()
                else:
                    self.loadcharacterfromjson(jsonfilesinthisdirectory[choice])

            except ValueError:
                os.system("clear")
                print("Wrong choice!")
                loadGame()

    def loadcharacterfromjson(self, choosedfile):
        with open(choosedfile) as f:
            myjson = f.read()
        attrs = json.loads(myjson)
        for attr in attrs:
            setattr(self.player, attr, str(attrs[attr]))
        self.beginmenu()

    def saveGame(self):
        os.system("clear")
        jsonfilesinthisdirectory = self.listingJsonFilesinThisDirectory()
        if len(jsonfilesinthisdirectory) == 0:
            print("No Early Saves!")
        else:
            print("Early Saves:\n")
            for i in range(len(jsonfilesinthisdirectory)):
                print(str(i) + " : "  + jsonfilesinthisdirectory[i])
            print("\n")
        file = input("Write the filename into save: ")
        filename = file + ".json"
        with open(filename, "w") as f:
            f.write(self.player.makeJsonOutput())

def main():
    game = Game()
    while True:
        menu = game.menu
        os.system("clear")
        menu.display_menu()
        choice = input("Choose an item: ")
        menu.choose(choice)

main()
