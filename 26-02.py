import time     # import time library


def startmenu():     # Define startmenu function
    print("Welcome to Pharaoh's Legacy: Quest for the Lost Tomb!")
    print("--Start -- \n--Exit--")
    choice = input("What option would you like to select? ").title()
    while choice not in ('Start', 'Exit'):
        print("Sorry that is not a valid input. Please select either 'start' or 'exit'")
        choice = input("Do you want to start or exit? ").title()
    if choice == "Start":
        firstscene()
    elif choice == "Exit":
        exit()


def firstscene():
    pass


startmenu()
