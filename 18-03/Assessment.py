import platform # import platform library
import os   # import OS library
import sys
import webbrowser
import time
try:
    import pick # trys to import pick library, used for making selection menus
except ModuleNotFoundError:     # if not found run this code
    if platform.system() == "Darwin":   # Gives instructions on how to install pick library on macOS or Linux
        os.system('clear')
        print("Hello! The Python module 'pick' is not installed because of\nthis my code will not run to fix this, open 'Terminal' and type\nin 'pip install pick' enter 'y' if it asks to install, once done rerun this code!")
        choice = input("Would you like to watch a video tutorial on how to do it? 'Yes' or 'No' ").title()
        if choice == "Yes":
            webbrowser.open("https://youtu.be/pJoe9UAr3Ao")
            exit()
        else:
            exit()
    elif platform.system() == "Windows":    # Gives instructions on how to install pick library on windows
        os.system('cls')
        print("Hello! The Python module 'pick' is not installed because of this my code will not run\nto fix this, type powershell into the search bar and open the app, then type in 'py -m pip install pick'\nenter 'y' if it asks to install, once done rerun this code!")
        choice = input("Would you like to watch a video tutorial on how to do it? 'Yes' or 'No' ").title()
        if choice == "Yes":
            webbrowser.open("https://youtu.be/iTUT3r-7RFc")
            exit()
        else:
            exit()
import random
from quiz_dictionaries import *     # imports everything from quiz_dictionaries.py so quiz questions, congrats message, incorrect questions & generate_incorrect_message() loads
global player_name     # Makes all these variables global so they have the same value between functions
global score
global clear_chat
global high_score
clear_chat = "Off"  # sets value of clear_chat settings to "off"
score = 0       # sets score to 0

for question in easy_quiz_questions:    # Shuffles answers to prevent easy cheating
    random.shuffle(question["answers"])
for question in normal_quiz_questions:
    random.shuffle(question["answers"])
for question in hard_quiz_questions:
    random.shuffle(question["answers"])

def clear(force=False):    # Defines clear function for clearing terminal
    if not force and clear_chat != "On":    # if not forced and clearchat is not on, do nothing
        return
    
    system = platform.system()
    if platform.system() == "Linux" or system == "Darwin":   # If operating system is equal to Darwin (macOS) or linux run OS specific clear command
        os.system('clear')
    elif platform.system() == "Windows":    # If operating system is equal to windows run windows specific clear command
        os.system('cls')

def load_high_score():
    global high_score
    file_path = os.path.join(os.path.dirname(__file__), 'high_score.txt')   # sets file path to current file path and make sures high_school.txt is made in current directory
    if os.path.exists(file_path):
        with open(file_path, 'r') as file:  # opens high_score.txt in read only mode
            high_score_str = file.read().strip()    # reads .txt and clears all whitespace
            if high_score_str:
                high_score = int(high_score_str)    # if there is a high score in file, set high_score variable to its value
            else:
                high_score = 0
    else:
        high_score = 0
    return high_score   # returns value of high_score

    
def save_high_score(score):     # defines variable and loads score variable
    global high_score
    file_path = os.path.join(os.path.dirname(__file__), 'high_score.txt')   # sets file path to current file path and make sures high_school.txt is made in current directory
    with open (file_path, 'w') as file:     # opens high_score.txt in write only mode
        file.write(str(score))      # Writes value of high_score as a string

def start_menu():  # Define start_menu function
    global questions
    high_score = load_high_score()  # runs load_high_score() function and sets its return value to the value of high_score
    clear(force=True)
    options = ["Start", "Settings", "Exit"]     # Creates list of options
    option, index = pick.pick(options, f"Hello {player_name} and Welcome to the Python Mastery Challenge!\nThe current high score is {high_score}", indicator = '->', default_index= 0)     # Creates the pick menu, sets options to the list options, makes the title and sets what the indicator looks like
    if option == "Start":
        difficulties = ["Easy", "Normal", "Hard"]   # Creates list of difficulties
        pick_difficulty, index = pick.pick(difficulties, "Pick a difficulty!", indicator='->')  # Creates pick menu to choose the difficulty you want to be quizzed on
        if pick_difficulty == "Easy":
            quiz(easy_quiz_questions)  # This runs the quiz function with the easy questions
        elif pick_difficulty == "Normal":
            quiz(normal_quiz_questions) # This runs the quiz function with the normal questions
        elif pick_difficulty == "Hard":
            quiz(hard_quiz_questions)   # This runs the quiz function with the hard questions
    elif option == "Settings":
        settings()  # Opens settings menu
    elif option == "Exit":
        print(f"Bye bye, {player_name} until next time!")
        exit()  # Ends python script


def settings():
    clear(force=True)
    global clear_chat
    global player_name
    global high_score
    options = [f"Clear Chat after choice: {clear_chat}", f"Name: {player_name}", "Reset High Score", "Back"]    # Creates list of settings to choose from
    option, index = pick.pick(options, "Settings", indicator='->', default_index=0)     # Creates the pick menu so you can select setting to configure
    print(option)
    if option == f"Clear Chat after choice: {clear_chat}":
        clear_chat = "On" if clear_chat == "Off" else "Off" # Sets clear_chat to "On" if it is "Off" or turns it "Off" if it is "On"
        settings()  # Re runs setting menu with updated settings
    elif option == f"Name: {player_name}":
        player_name = input("What do you want your new name to be? ").title()   # Re asks player for player_name if they choose to rename it
        settings()
    elif option == "Reset High Score":
        high_score = 0  # Resets high_score to 0
        save_high_score(high_score) # Saves high_score value in .txt file to the new high_score value
        settings()
    elif option == "Back":
        start_menu()

def format_questions(question_info):
    question = question_info["question"]    # Sets value of question to the question key in the quiz_dictionaries dictionary.
    options = question_info["answers"]  # Sets options of question to the answers key in the quiz_dictionaries dictionary.
    picker = pick.Picker(options, title=question, indicator='->')   # Creates picker to choose answer in
    pickedItem = picker.start()
    return pickedItem[0]



def quiz(questions):
    global high_score
    high_score = load_high_score()  # Loads high_score by running the load_high_score() function
    while True:
        score = 0
        total_questions = len(questions)    # Sets total_questions value based on how many questions there are
        random.shuffle(questions)   # Shuffles questions
        question_progress = 0

        for question_info in questions: # Run until it runs out of questions
            user_answer = format_questions(question_info)   # Sets user answer to selected answer in picker menu
            correct_answer = question_info["correct"]   # Sets value of correct_answer to the correct key in the quiz_dictionaries dictionary

            if user_answer == correct_answer:
                congrats_message = random.choice(correct_congrats)  # Sets congrats_message to a random items from the correct_congrats list
                print(congrats_message) # Prints valeu of congrats_message
                score += 1  # Adds 1 to score.
            else:
                print(generate_incorrect_message(correct_answer)) # Print returned value of generate_incorrect_message function and passes in value of correct_answer so it spits out incorrect message with the value of the correct answer
            
            question_progress += 1  # Adds 1 to question progress
            if question_progress == total_questions:
                if score > high_score: # if score is greater than high_score run this code
                    save_high_score(score)  # saves score as new high_score
                    high_score = score 
                    options = ["Start Menu", "Exit"]    # Creates list of options
                    option, index = pick.pick(options, f"You've finished the quiz & got the new high score! The high score is now {high_score}! Your score is: {score}/{total_questions} \nReturn to start menu or exit?", indicator='->')  # Creates picker menu for player to choose option from
                    if option == "Start Menu":
                        start_menu()
                    elif option == "Exit":
                        clear() # Clears chat
                        print(f"Thanks for playing {player_name}, until next time!")
                        exit()  # Quits game
                else:
                    options = ["Start Menu", "Exit"]    # CReates list of options
                    option, index = pick.pick(options, f"You've finished the quiz! Your score is: {score}/{total_questions} \nReturn to start menu or exit?", indicator='->')   # Create picker so player can choose option to select
                    if option == "Start Menu":
                        start_menu()
                    elif option == "Exit":
                        clear()
                        print(f"Thanks for playing {player_name}, until next time!")
                        exit()
            
            remaining_questions = total_questions - question_progress   # makes remaining_questions variable equal to total_questions subtracted by question_progress
            input(f"Press enter to continue! Your score so far is {score}/{question_progress} only {remaining_questions} left!")    # Makes user press enter to continue so they can see score and how many left
            clear()

# Start of script
clear(force=True)     # Clears terminal of random not needed
if sys.version_info[:3] > (3,12):   # Checks to see if python version is greater than 3.12
    if platform.system() == "Windows":  # Gives instructions on how to install python 3.11.6 for windows
        print("You are using Python 3.12, currently this version is not supported because the UI library does not support 3.12.\nIf you go to https://www.python.org/ftp/python/3.11.6/python-3.11.6-amd64.exe you can download and install Python 3.11.6.\nThis version is supported recommended when running this program")
        choice = input("Would you like to watch a video tutorial on how to install it and open the download link? 'Yes' or 'No' ").title()
        if choice == "Yes":
            webbrowser.open('https://www.python.org/ftp/python/3.11.6/python-3.11.6-amd64.exe')
            webbrowser.open('https://youtu.be/aQyk-adGeFQ')
            exit()
        else:
            exit()
    elif platform.system() == "Darwin":     # Gives instructions on how to install python 3.11.6 for macOS
        print("You are using Python 3.12, currently this version is not supported because the UI library does not support 3.12.\nIf you go to https://www.python.org/ftp/python/3.11.6/python-3.11.6-macos11.pkg you can download and install Python 3.11.6.\nThis version is supported recommended when running this program")
        choice = input("Would you like to watch a video tutorial on how to install it and open the download link? 'Yes' or 'No' ").title()
        if choice == "Yes":
            webbrowser.open_new("https://www.python.org/ftp/python/3.11.6/python-3.11.6-macos11.pkg")
            webbrowser.open_new("https://youtu.be/2Oy5HgLvhOs")
            exit()
        else:
            exit()
player_name = input("Hello Quizzer! What is your name? ").title()  # Asks player for name and assigns it to variable "playername"
while not player_name:  # If nothing is inputed to player_name reask for player_name
    clear(force=True)
    print("You didn't input anything. Please enter your name")
    player_name = input("Hello Quizzer! What is your name? ")
options = ["On", "Off"] # Creates list of options
option, index = pick.pick(options, "Would like to turn on Clear Chat? Clear chat clears the terminal after every dialogue input!", indicator = '->', default_index= 0)  # Creates picker menu so player can choose option
if option == "On":
    clear_chat = "On"
elif option == "Exit":
    clear_chat = "Off"

start_menu()    # Runs the start menu
