import platform # import platform library
import os   # import OS library
import pick # import pick library, used for making selection menus
import random
from quiz_dictionaries import *
global player_name     # Makes player_name a global variable to be used anywhere
global score
global clear_chat
clear_chat = "Off"
score = 0

for question in easy_quiz_questions:
    random.shuffle(question["answers"])

def clear(force=False):    # Defines clear function for clearing terminal
    if not force and clear_chat != "On":
        return
    
    system = platform.system()
    if platform.system() == "Linux" or system == "Darwin":   # If operating system is equal to Darwin (macOS) run macOS specific clear command
        os.system('clear')
    elif platform.system() == "Windows":    # If operating system is equal to windows run windows specific clear command
        os.system('cls')

def start_menu():  # Define start_menu function
    global questions
    clear(force=True)
    options = ["Start", "Settings", "Exit"]
    option, index = pick.pick(options, f"Hello {player_name} and Welcome to the Python Mastery Challenge!", indicator = '->', default_index= 0)
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
    options = [f"Clear Chat after choice: {clear_chat}", f"Name: {player_name}", "Back"]
    option, index = pick.pick(options, "Settings", indicator='->', default_index=0)
    print(option)
    if option == f"Clear Chat after choice: {clear_chat}":
        clear_chat = "On" if clear_chat == "Off" else "Off"
        settings()
    elif option == f"Name: {player_name}":
        player_name = input("What do you want your new name to be? ").title()
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
    while True:
        global score
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
