import os

class Menu:
    def __init__(self, items):
        self.items = items

    def choose(self, number):
        for item in self.items:
            if item.is_selected(number):
                return item.call_action()
        print("Wrong Input")

    def display_menu(self):
        for item in self.items:
            item.print_myself()

    def clear_display(self):
        os.system("clear")
