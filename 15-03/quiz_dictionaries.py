import random

easy_quiz_questions = [
    {
        "question": "What is the correct way to print Hello World in the python terminal?",
        "answers": ["print(Hello World)", "prnt('Hello World')", "print('Hello World')", "print = 'Hello World'"],
        "correct": "print('Hello World')"
    },
    {
        "question": "What is the correct way to give x the value of 1?",
        "answers": ["x = 1", "x: 1", "x == 1", "x equal 1"],
        "correct": "x = 1"
    },
    {
        "question": "How do you print the variable 'x'?",
        "answers": ["prnt(x)", "print('x')", "print(x)", "print[x]"],
        "correct": "print(x)"
    },
    {
        "question": "How do you make a comment in Python code?",
        "answers": ["// text here", "# text here", "<!-- Text Here -->", "comment(text here)"],
        "correct": "# text here"
    },
    {
        "question": "How do you create a function called my_function() in Python?",
        "answers": ["function my_function():", "create myFuntion():", "my_function() create:", "def my_function():"],
        "correct": "def my_function():"
    }
]

normal_quiz_questions = [
    {
        "question": "This is a normal question test",
        "answers": ["Wrong", "Wrong 2", "Correct", "Wrong 3"],
        "correct": "Correct"
    }
]

hard_quiz_questions = [
    {
        "question": "This is a hard question test",
        "answers": ["Wrong", "Wrong 2", "Correct", "Wrong 3"],
        "correct": "Correct"
    }
]

correct_congrats = ["Ka Pai! You got that one correct!", "Great Job! You got that one right!", "Amazing! You got it right!", "Keep going! You're doing amazing!"]

def generate_incorrect_message(correct_answer):
    possible_answers = [
        f"So close! You got that one wrong, the answer was {correct_answer}",
        f"Better luck next time! You were wrong :( , the answer was {correct_answer}"
    ]
    return random.choice(possible_answers)