import time  # import time library
global playername     # Makes playername a global variable to be used anywhere


def startmenu():  # Define startmenu function
    playername = input("Hello Adventurer what is your playername? ").title()    # Asks player for name and assigns it to variable "playername"
    print(f"Hello {playername} and Welcome to The Forest of Secrets!")
    time.sleep(1)
    print("--Start -- \n--Exit--")
    choice = input("What option would you like to select? ").title()    # Asks player to select an option from main menu
    while choice not in ('Start', 'Exit'):  # If answer isn't valid, reask
        print("Sorry that is not a valid input. Please select either 'start' or 'exit'")
        choice = input("Do you want to start or exit? ").title()
    if choice == "Start":
        firstscene()
    elif choice == "Exit":
        print(f"Bye bye {playername}, until next time!")
        exit()


def death():    # defines the death function that is called upon player death
    print("You died!")
    restart = input("Would you like to try again? Yes or no: ").title()

    if restart == "Yes":
        firstscene()
    elif restart == "No":
        startmenu()
    else:
        print("That is a not a valid option please select either 'Yes' or 'No'")
        death()


def firstscene():   # defines first scene
    print(f"One day in 2077 you, {playername}, the world renowned famous explorer was exploring the ruins of the once popular New York City")
    time.sleep(1)
    print("You stumble across a split in the road, to the left is a destroyed shopping district and to the right is apartments? Which was do you go?")
    choice = input("Left or Right?").title()
    if choice == "Left":
        print("You walk towards the shopping district, it starts raining so you put on your raincoat but, the rain burns through your clothes!")
        time.sleep(0.5)
        print("It's acid rain!! Your skin is burning, you run towards the closet shelter a destroyed pizza restaurant.")
        time.sleep(0.5)
        print("You run inside, slam the door and desperately try to find first aid tools but then you hear banging at the door, the infected found you, what do you do?")
        time.sleep(0.5)
        choice = input("Hide or Fight? ")
        if choice:
            pass
    elif choice == "Right":
        pass


startmenu()
