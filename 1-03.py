import platform
import time  # import time library
import os   # import OS library
import pick
global playername     # Makes playername a global variable to be used anywhere
global xp
global clearchat
clearchat = "Off"

def clear():
    if platform.system() == "Darwin":
        os.system('clear')
    elif platform.system() == "Windows":
        os.system('cls')


def startmenu():  # Define startmenu function
    clear()
    print(f"Hello {playername} and Welcome to The Forest of Secrets!")
    time.sleep(1)
    print("--Start --\n--Settings--\n--Exit--")
    choice = input("What option would you like to select? ").title()    # Asks player to select an option from main menu
    while choice not in ('Start', 'Settings', 'Exit'):  # If answer isn't valid, reask
        print("Sorry that is not a valid input. Please select either 'start', 'settings', or 'exit'")
        choice = input("What option would you like to select?")
    if choice == "Start":
        introduction()
    elif choice == "Settings":
        settings()
    elif choice == "Exit":
        print(f"Bye bye {playername}, until next time!")
        exit()


def settings():
    clear()
    global clearchat
    options = [f"Clear Chat after choice: {clearchat}"]
    option, index = pick.pick(options, "--Settings--", indicator='->', default_index=0)
    print(option)
    if option:
        clearchat = "On" if clearchat == "Off" else "Off"
    settings()
    

def death():    # defines the death function that is called upon player death
    print("You died!")
    restart = input("Would you like to try again? Yes or no: ").title()
    xp = 0

    if restart == "Yes":
        introduction()
    elif restart == "No":
        startmenu()
    else:
        print("That is a not a valid option please select either 'Yes' or 'No'")
        death()


def introduction():   # defines first scene
    print(f"One day in 2177 you {playername}, the world renowned famous explorer, was exploring the ruins of the once popular New York City")
    time.sleep(1)
    print("You stumble across a split in the road, to the left is a destroyed shopping district and to the right is apartments? Where do you go?")
    choice = input("Shopping or Apartments?").title()
    if choice == "Shopping":
        shopping()
    elif choice == "Right":
        apartments()


def shopping():
    print("You walk towards the shopping district, it starts raining so you put on your raincoat but, the rain burns through your clothes!")
    time.sleep(0.5)
    print("It's acid rain!! Your skin is burning, you run towards the closet shelter a destroyed pizza restaurant.")
    time.sleep(0.5)
    print("You run inside, slam the door and desperately try to find first aid tools but then you hear banging at the door, the infected found you, what do you do?")
    time.sleep(0.5)
    choice = input("Hide or Fight? ")


def apartments():
    print("You walk towards the apartments, the wind picks up it becomes hard to see as dust is flying everywhere, you seek shelter inside until the wind stops")
    time.sleep(0.5)
    print("You take the time to explore the apartment room to see remnants of the lost world")

clear()     # Clears terminal of random not needed
playername = input("Hello Adventurer what is your name? ").title()  # Asks player for name and assigns it to variable "playername"
startmenu()
