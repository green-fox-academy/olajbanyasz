import os
import random
import json
from character import *

hero = Character()


def menumaker(menulist, hero):
    os.system("clear")
    while True:
        if hero.name != "":
            print(      "Username: " + hero.name +
                        " | H:" + str(hero.health) +
                        " | D:" + str(hero.dexterity) +
                        " | L:" + str(hero.luck) +
                        " | Potion: " + hero.potion + "\n"
                        "Invetory: " + str(hero.inventory) + "\n")

        for i in menulist:
            print('{} {}'.format(i[0], i[1]))
        try:
            choice = int(input("Choose an option: "))
            os.system("clear")
            if not 0 <= choice <= len(menulist)-1:
                os.system("clear")
                print("Wrong choice!")
            else:
                menulist[choice][2]()
        except ValueError:
            os.system("clear")
            print("Wrong choice!")

dir listingJsonFilesinThisDirectory():
    print(listdir(path='.'))

def loadGame():
    listingJsonFilesinThisDirectory()

def nameinput():
    name = input("Please write your name: ")
    return name

def newGame():
    global user
    hero.name = nameinput()
    menumaker(namesubmenulist, hero)

def quitResume():
    menumaker(namesubmenulist, hero)

def saveGame():
    file = input("Write the filename into save: ")
    filename = file + ".json"
    with open(filename, "w") as f:
        f.write(hero.makeJsonOutput())

def exitGame():
    os.system("clear")
    exit()

def continueGame():
    return True

def beginGame():
    menumaker(begingamemenulist, hero)

def quitMenu():
    menumaker(quitmenulist, hero)

def saveGameMenu():
    menumaker(savegamemenulist, hero)

def continueMakeUser():
    hero.dexterity = hero.returnStartingDexterity()
    hero.health = hero.returnStartingHealth()
    hero.luck = hero.returnStartingLuck()
    menumaker(rerollmenulist, hero)

def selectPotion():
    menumaker(selectpotionmenulist, hero)

def addHealthPotiontoHero():
    hero.potion = "Health Potion"
    menumaker(reselectpotionmenulist, hero)

def addDexterityPotiontoHero():
    hero.potion = "Dexterity Potion"
    menumaker(reselectpotionmenulist, hero)

def addLuckPotiontoHero():
    hero.potion = "Luck Potion"
    menumaker(reselectpotionmenulist, hero)
mainmenulist =  [
                [0,"Exit",exitGame],
                [1,"New Game",newGame],
                [2,"Load Game",loadGame]
                ]

namesubmenulist =   [
                    [0,"Reenter Name",newGame],
                    [1,"Continue",continueMakeUser],
                    [2,"Save",saveGame],
                    [3,"Quit",quitMenu]
                    ]

quitmenulist =  [
                [0,"Quit without save",exitGame],
                [1,"Quit with save",saveGame],
                [2,"Resume",quitResume]
                ]

rerollmenulist =    [
                    [0,"Reroll stats",continueMakeUser],
                    [1,"Continue",selectPotion],
                    [2,"Save",saveGame],
                    [3,"Quit",quitMenu]
                    ]

selectpotionmenulist =      [
                            [0,"Select - Potion of Health",addHealthPotiontoHero],
                            [1,"Select - Potion of Dexterity",addDexterityPotiontoHero],
                            [2,"Select - Potion of Luck",addLuckPotiontoHero]
                            ]

reselectpotionmenulist =    [
                            [0,"Reselect Potion",selectPotion],
                            [1,"Continue",beginGame],
                            [2,"Quit",quitMenu]
                            ]

begingamemenulist =         [
                            [0,"Begin",saveGame],
                            [1,"Save",saveGameMenu],
                            [2,"Quit",quitMenu]
                            ]

savegamemenulist =          [
                            [0,"Add New Item",saveGame],
                            [1,"Resume",beginGame],
                            [2,"Quit",quitMenu]
                            ]


menumaker(mainmenulist, hero)
