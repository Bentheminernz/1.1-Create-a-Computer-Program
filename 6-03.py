import platform # import platform library
import time  # import time library
import os   # import OS library
import pick
global playername     # Makes playername a global variable to be used anywhere
global xp
global clearchat
global timedelay
clearchat = "Off"
timedelay = 1


def clear(force=False):    # Defines clear function for clearing terminal
    if not force and clearchat != "On":
        return
    
    system = platform.system()
    if platform.system() == "Linux" or system == "Darwin":   # If operating system is equal to Darwin (macOS) run macOS specific clear command
        os.system('clear')
    elif platform.system() == "Windows":    # If operating system is equal to windows run windows specific clear command
        os.system('cls')


def startmenu():  # Define startmenu function
    clear()
    options = ["--Start--", "--Settings--", "--Exit--"]
    option, index = pick.pick(options, f"Hello {playername} and Welcome to the Forest of Secrets!", indicator = '->', default_index= 0)
    if option == "--Start--":
        introduction()
    elif option == "--Settings--":
        settings()
    elif option == "--Exit--":
        print(f"Bye bye, {playername} until next time!")
        time.sleep(timedelay)
        exit()


def settings():
    clear(force=True)
    global clearchat
    global playername
    global timedelay
    options = [f"Clear Chat after choice: {clearchat}", f"Name: {playername}", f"Time Delay: {timedelay}s", "Exit"]
    option, index = pick.pick(options, "--Settings--", indicator='->', default_index=0)
    print(option)
    if option == f"Clear Chat after choice: {clearchat}":
        clearchat = "On" if clearchat == "Off" else "Off"
        settings()
    elif option == f"Name: {playername}":
        playername = input("What do you want your new name to be? ").title()
        settings()
    elif option == f"Time Delay: {timedelay}s":
        new_timedelay = input("What do you want the new Time Delay to be? ")
        try:
            timedelay = int(new_timedelay)
        except ValueError:
            print("Please enter a valid number for the time delay.")
            time.sleep(2)
        settings()
    elif option == "Exit":
        startmenu()
    

def death():    # defines the death function that is called upon player death
    global xp
    xp = 0
    options = ["Respawn", "Main Menu", "Exit"]
    option, index = pick.pick(options, "You died!", indicator='->', default_index=0)
    if option == "Respawn":
        clear(force=True)
        introduction()
    elif option == "Main Menu":
        clear(force=True)
        startmenu()
    elif option == "Exit":
        print(f"Bye bye, {playername} until next time!")
        time.sleep(timedelay)
        exit()


def introduction():   # defines first scene
    clear(force=True)
    print(f"One day in 2177 you {playername}, the world renowned famous explorer, was exploring the ruins of the once popular New York City")
    time.sleep(timedelay)
    print("You stumble across a split in the road, to the left is a destroyed shopping district and to the right is apartments? Where do you go?")
    choice = input("Shopping or Apartments? ").title()
    while choice not in ('Shopping', 'Apartments'):
        print(f"{choice} is not a valid answer. Please select either 'Shopping' or 'Apartments'")
        choice = input("Shopping or Apartments? ").title()
    if choice == "Shopping":
        clear()
        shopping()
    elif choice == "Apartments":
        clear()
        apartments()


def shopping():
    print("You walk towards the shopping district, it starts raining so you put on your raincoat but, the rain burns through your clothes!")
    time.sleep(timedelay)
    print("It's acid rain!! Your skin is burning, you run towards the closet shelter a destroyed pizza restaurant.")
    time.sleep(timedelay)
    print("You run inside, slam the door and desperately try to find first aid tools but then you hear banging at the door, the infected found you, what do you do?")
    time.sleep(timedelay)
    choice = input("Hide or Fight? ")


def apartments():
    print("You walk towards the apartments, the wind picks up it becomes hard to see as dust is flying everywhere, you seek shelter inside until the wind stops")
    time.sleep(timedelay)
    print("You take the time to explore the apartment room to see remnants of the lost world")

clear(force=True)     # Clears terminal of random not needed
playername = input("Hello Adventurer what is your name? ").title()  # Asks player for name and assigns it to variable "playername"
startmenu()
