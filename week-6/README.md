# Week 6 - Project

## Project
Text based RPG game

## Stories

### Main menu
Simple command line main menu
#### Print menu
- Given a User
- When the program is runned by typing `python game.py`
- Then the menu should be shown
Menu items: New game, Load Game, Exit

#### Select menu item
- When the menu is show
- Then it should list the possible menu items
- Then it should require an integer as selecting a menu items

#### Enter submenu
- When the menu item is selected (by pressing enter)
- Then it should enter the submenu (by printing the sub menu list)

#### Wrong input
- Given the menu waiting for an input
- When wrong input is entered
- Then it should print an error message and require the input again

#### Exit menu item
- Given the menu waiting for an input
- When the Exit item is selected
- Then it should exit

### New game

#### Name
- Given a user
- When the `New Game` menu item is selected
- Then it should ask for a name
- Then it should display it after enter it

#### Name Submenu
- Given an entered name
- When the name is displayed
- Then it should show a submenu
Menu items: Reenter name, Continue, Quit

#### Reenter Name
- Given an entered Name
- When the Reenter name submenu is selected
- Then it should ask for the name again

#### Quit
- Given an entered name
- When Quit is selected
- Then it should show the quit submenu:
Save and Quit, Quit without save, Resume
- Then Save and Quit should save the game and Quit
- Quit without save should not save the character

#### Roll stats
- Given an entered name
- When `Continue` is selected
- Then it should roll the basic stats and display them:
  - Dexterity: 1d6 + 6
  - Health: 2d6 + 12
  - Luck: 1d6 + 6
- Then it should show a submenu
Menu items: Reroll stats, Continue, Quit

#### Reroll stats
- Given the rolled stats
- When `Reroll stats` is selected
- Then it should refresh the stats with new values

#### Select Potion
- Given the rolled stats
- When `Continue` is selected
- Then it should show a submenu
Menu items: Potion of Health, Potion of Dexterity, Potion of Luck

#### Choosed Potion
- Given the potion menu
- When the potion is selected
- Then it should print the selected potion and show a submenu
Menu items: Reselect the Potion, 





