class MenuItem:
    def __init__(self, num, name, action):
        self.num = num
        self.name = name
        self.action = action

    def is_selected(self, number):
        return str(self.num) == number

    def call_action(self):
        return self.action()

    def print_myself(self):
        print("{} {}".format(self.num, self.name))
