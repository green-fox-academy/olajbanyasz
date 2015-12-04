import os

def hello():
    os.system('clear')
    print('\n', "   *   *"*2,  'Hi, bro!', "*   *   "*2)
    print('\n', ' With this program, u can make a TODO list ' , '\n')
    listTodos()


def menuChooser():
    chooser = ""
    print('\n','  1: List TODOs','\n', '  2: Add new TODO','\n', '  3: Complete TODO','\n', '  4: List closed TODOs','\n', '  5: Clear  closed list','\n','  6: Quit','\n' )
    try:
        chooser = int(input("   Choose from the menu with numbers:  "))
        print("\n")
    except ValueError:
        os.system('clear')
        print("\n" , "  Wrong selection! Choose from 1-6!")
        menuChooser()

    if chooser == 1:
        listTodos()
    elif chooser == 2:
        addTodo()
    elif chooser == 3:
        closeTodo()
    elif chooser == 4:
        listClosedTodos()
    elif chooser == 5:
        clearClosedTodos()
    elif chooser == 6:
        os.system('clear')
        print("   Goodbye!")
        exit()
    else:
        print("\n" , "  Wrong selection! Choose from 1-6!")
        menuChooser()

def listTodos():
    os.system('clear')
    print("\n")
    fr = open('todos.txt', 'r')
    lines = fr.readlines()
    fr.close()
    print("\n" , "    Current TODOs:" , "\n")
    i = 1
    for line in lines:
        print("\t" + "\t" + str(i) + "  " + line.rstrip())
        i += 1
    menuChooser()

def listClosedTodos():
    os.system('clear')
    print("\n")
    fr = open('closedtodos.txt', 'r')
    lines = fr.readlines()
    fr.close()
    print("   Closed TODOs:" , "\n")
    i = 1
    for line in lines:
        print("\t" + "\t" + str(i) + "  " + line.rstrip())
        i += 1
    menuChooser()

def addTodo():
    os.system('clear')
    print("\n")
    fr = open('todos.txt', 'r')
    lines = fr.readlines()
    fr.close()
    print("\n" , "    Current TODOs:" , "\n")
    i = 1
    for line in lines:
        print("\t" + "\t" + str(i) + "  " + line.rstrip())
        i += 1
    print("\n")
    newTodo = input("  Write a new TODO: ").upper()
    if newTodo == "":
        os.system('clear')
        print("   This TODO was empty!!!")
    else:
        fr = open('todos.txt', 'r+')
        text = fr.read()
        newTodo += "\n"
        fr.write(newTodo)
        fr.close()
        listTodos()
    menuChooser()

def closeTodo():
    os.system('clear')
    choosedLineText = []
    fr = open('todos.txt', 'r')
    lines = fr.readlines()
    fr.close()
    print("  Current TODOs:" , "\n")
    i = 1
    for line in lines:
        print("\t" + "\t" + str(i) + "  " + line.rstrip())
        i += 1

    print("\n")

    try:
        choosedTodo = int(input("  Choose from the list with numbers to close:  "))
        if choosedTodo > (len(lines)) or choosedTodo < 1:
            os.system('clear')
            print("\n" , "  Nothing closed!")
            menuChooser()

    except ValueError:
        os.system('clear')
        print("  Nothing closed!")
        menuChooser()

    print("  You choosed this item to close: " + "\n" + "\t\t" + lines[choosedTodo-1])
    choosedLine = input("  Really want to close this?  Y/N: ").upper()


    if choosedLine == "Y":
        cfrtext = ""
        cfr = open('closedtodos.txt', 'r+')
        cfrtext = cfr.read()
        cfrtext = lines[choosedTodo-1]
        cfr.write(cfrtext)
        cfr.close()

        fr = open('todos.txt', 'r')
        lines = fr.readlines()
        fr.close()
        fr = open('todos.txt', 'w')
        lines.remove(lines[choosedTodo-1])
        fr.writelines(lines)
        fr.close()
    else:
        print("  Nothing closed!")
    listTodos()

def clearClosedTodos():
    os.system('clear')
    cfrtext = ""
    cfr = open('closedtodos.txt', 'w')
    cfr.write(cfrtext)
    cfr.close()
    listTodos()

hello()
