import platform # import platform library
import os   # import OS library
import pick # import pick library, used for making selection menus
import random
global playername     # Makes playername a global variable to be used anywhere
global score
global clearchat
clearchat = "Off"
score = 0
quizQuestions = [
    {
        "question": "What is the correct way to print Hello World in the python terminal?",
        "answers": ["print(Hello World)", "prnt('Hello World')", "print('Hello World')", "print = 'Hello World'"],
        "correct": "print('Hello World')"
    },
    {
        "question": "What is the correct way to give x the value of 2?",
        "answers": ["x = 1", "x: 1", "x == 1", "x equal 1"],
        "correct": "x = 1"
    }
]


def clear(force=False):    # Defines clear function for clearing terminal
    if not force and clearchat != "On":
        return
    
    system = platform.system()
    if platform.system() == "Linux" or system == "Darwin":   # If operating system is equal to Darwin (macOS) run macOS specific clear command
        os.system('clear')
    elif platform.system() == "Windows":    # If operating system is equal to windows run windows specific clear command
        os.system('cls')

def startmenu():  # Define startmenu function
    global questions
    clear()
    options = ["--Start--", "--Settings--", "--Exit--"]
    option, index = pick.pick(options, f"Hello {playername} and Welcome to the Python Mastery Challenge!", indicator = '->', default_index= 0)
    if option == "--Start--":
        quiz(quizQuestions)
    elif option == "--Settings--":
        settings()
    elif option == "--Exit--":
        print(f"Bye bye, {playername} until next time!")
        exit()


def settings():
    clear(force=True)
    global clearchat
    global playername
    options = [f"Clear Chat after choice: {clearchat}", f"Name: {playername}", "Exit"]
    option, index = pick.pick(options, "--Settings--", indicator='->', default_index=0)
    print(option)
    if option == f"Clear Chat after choice: {clearchat}":
        clearchat = "On" if clearchat == "Off" else "Off"
        settings()
    elif option == f"Name: {playername}":
        playername = input("What do you want your new name to be? ").title()
        settings()
    elif option == "Exit":
        startmenu()

def formatQuestions(questionInfo):      # Formats questions and gets the user's answer
    question = questionInfo["question"]
    options = questionInfo["answers"]
    picker = pick.Picker(options, title =question)
    pickedItem = picker.start()
    return pickedItem[0]


def quiz(questions):
    global score
    score = 0
    totalQuestions = len(questions)
    random.shuffle(questions)
    questionProgress = 0

    for questionInfo in questions:
        userAnswer = formatQuestions(questionInfo)
        correctAnswer = questionInfo["correct"]

        if userAnswer == correctAnswer:
            print("Ka Pai! You got that one correct!")
            score += 1
        else:
            print(f"You got it wrong, better luck next time! The correct answer was {correctAnswer}")

        if questionProgress < totalQuestions - 1:
            input("Press Enter to continue!")  # Make user trigger next question, giving time to read what code spits out.
            clear()

    print(f"You've finished the quiz! Your score is: {score}/{totalQuestions}")



    



clear(force=True)     # Clears terminal of random not needed
playername = input("Hello Quizzer! What is your name? ").title()  # Asks player for name and assigns it to variable "playername"
options = ["--On--", "--Off--"]
option, index = pick.pick(options, "Would like to turn on Clear Chat? Clear chat clears the terminal after every dialogue input!", indicator = '->', default_index= 0)
if option == "--On--":
    clearchat = "On"
elif option == "--Exit--":
    clearchat = "Off"

startmenu()
