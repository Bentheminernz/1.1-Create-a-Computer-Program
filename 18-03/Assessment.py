import platform # import platform library
import os   # import OS library
import pick # import pick library, used for making selection menus
import random
from quiz_dictionaries import *
global player_name     # Makes player_name a global variable to be used anywhere
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
    if not force and clear_chat != "On":
        return
    
    system = platform.system()
    if platform.system() == "Linux" or system == "Darwin":   # If operating system is equal to Darwin (macOS) run macOS specific clear command
        os.system('clear')
    elif platform.system() == "Windows":    # If operating system is equal to windows run windows specific clear command
        os.system('cls')

def load_high_score():
    global high_score
    file_path = os.path.join(os.path.dirname(__file__), 'high_score.txt')
    if os.path.exists(file_path):
        with open(file_path, 'r') as file:
            high_score_str = file.read().strip()
            if high_score_str:
                high_score = int(high_score_str)
            else:
                high_score = 0
    else:
        high_score = 0
    return high_score

    
def save_high_score(score):
    global high_score
    file_path = os.path.join(os.path.dirname(__file__), 'high_score.txt')
    with open (file_path, 'w') as file:
        file.write(str(score))

def start_menu():  # Define start_menu function
    global questions
    high_score = load_high_score()
    clear(force=True)
    options = ["Start", "Settings", "Exit"]
    option, index = pick.pick(options, f"Hello {player_name} and Welcome to the Python Mastery Challenge!\nThe current high score is {high_score}", indicator = '->', default_index= 0)
    if option == "Start":
        difficulties = ["Easy", "Normal", "Hard"]
        pick_difficulty, index = pick.pick(difficulties, "Pick a difficulty!", indicator='->')
        if pick_difficulty == "Easy":
            quiz(easy_quiz_questions)  # This should call the quiz function with the easy questions
        elif pick_difficulty == "Normal":
            quiz(normal_quiz_questions)
        elif pick_difficulty == "Hard":
            quiz(hard_quiz_questions)
    elif option == "Settings":
        settings()
    elif option == "Exit":
        print(f"Bye bye, {player_name} until next time!")
        exit()


def settings():
    clear(force=True)
    global clear_chat
    global player_name
    global high_score
    options = [f"Clear Chat after choice: {clear_chat}", f"Name: {player_name}", "Reset High Score", "Back"]
    option, index = pick.pick(options, "Settings", indicator='->', default_index=0)
    print(option)
    if option == f"Clear Chat after choice: {clear_chat}":
        clear_chat = "On" if clear_chat == "Off" else "Off"
        settings()
    elif option == f"Name: {player_name}":
        player_name = input("What do you want your new name to be? ").title()
        settings()
    elif option == "Reset High Score":
        high_score = 0
        save_high_score(high_score)
        settings()
    elif option == "Back":
        start_menu()

def format_questions(question_info):      # Formats questions and gets users answer
    question = question_info["question"]
    options = question_info["answers"]
    picker = pick.Picker(options, title=question, indicator='->')
    pickedItem = picker.start()
    return pickedItem[0]



def quiz(questions):
    global high_score
    high_score = load_high_score()
    while True:
        score = 0
        total_questions = len(questions)
        random.shuffle(questions)
        question_progress = 0

        for question_info in questions:
            user_answer = format_questions(question_info)
            correct_answer = question_info["correct"]

            if user_answer == correct_answer:
                congrats_message = random.choice(correct_congrats)
                print(congrats_message)
                score += 1
            else:
                print(generate_incorrect_message(correct_answer))
            
            question_progress += 1
            if question_progress == total_questions:
                if score > high_score:
                    save_high_score(score)
                    high_score = score 
                    options = ["Start Menu", "Exit"]
                    option, index = pick.pick(options, f"You've finished the quiz & got the new high score! The high score is now {high_score}! Your score is: {score}/{total_questions} \nReturn to start menu or exit?", indicator='->')
                    if option == "Start Menu":
                        start_menu()
                    elif option == "Exit":
                        clear()
                        print(f"Thanks for playing {player_name}, until next time!")
                        exit()
                else:
                    options = ["Start Menu", "Exit"]
                    option, index = pick.pick(options, f"You've finished the quiz! Your score is: {score}/{total_questions} \nReturn to start menu or exit?", indicator='->')
                    if option == "Start Menu":
                        start_menu()
                    elif option == "Exit":
                        clear()
                        print(f"Thanks for playing {player_name}, until next time!")
                        exit()
            
            remaining_questions = total_questions - question_progress
            input(f"Press enter to continue! Your score so far is {score}/{question_progress} only {remaining_questions} left!")
            clear()
        print(f"You've finished the quiz! Your score is: {score}/{question_progress}")


clear(force=True)     # Clears terminal of random not needed
player_name = input("Hello Quizzer! What is your name? ").title()  # Asks player for name and assigns it to variable "playername"
options = ["On", "Off"]
option, index = pick.pick(options, "Would like to turn on Clear Chat? Clear chat clears the terminal after every dialogue input!", indicator = '->', default_index= 0)
if option == "On":
    clear_chat = "On"
elif option == "Exit":
    clear_chat = "Off"

start_menu()
