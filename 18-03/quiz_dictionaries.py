import random

easy_quiz_questions = [
    {
        "question": "What is the correct way to print Hello World in the terminal?",
        "answers": ["print(Hello World)", "prnt('Hello World')", "print('Hello World')", "console.print('Hello World)"],
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
        "question": "How do you make a comment?",
        "answers": ["// text here", "# text here", "<!-- Text Here -->", "comment(text here)"],
        "correct": "# text here"
    },
    {
        "question": "How do you create a function called my_function()?",
        "answers": ["function my_function():", "create myFuntion():", "my_function() create:", "def my_function():"],
        "correct": "def my_function():"
    },
    {
        "question": "How do I load the Python library time?",
        "answers": ["load time", "import time", "open time", "include time"],
        "correct": "import time"
    },
    {
        "question": "How do I end a loop in Python?",
        "answers": ["break", "end", "stop", "exit"],
        "correct": "break"
    },
    {
        "question": "What is the correct file extension for Python files?",
        "answers": [".pt", ".pyt", ".py", ".pyth"],
        "correct": ".py"
    },
    {
        "question": "How do I make a string all uppper case?",
        "answers": ["upper()", "upper.string()", "upperCase()", "UPPER()"],
        "correct": "upper()"
    },
    {
        "question": "Which symbol is used to multiply numbers?",
        "answers": ["%", "x", "@", "*"]
    }
]

normal_quiz_questions = [
    {
        "question": "Which one of these is NOT an illegal variable name?",
        "answers": ["myvariable", "_myvariable", "MyVArIA_BlE", "my-variable"],
        "correct": "my-variable"
    },
    {
        "question": "How do you make a variable with the value of floating number 5.6?",
        "answers": ["x = float(5.6)", " x.float = 5.6", "x = 5.6", "x = 5.6(float)"],
        "correct": "x = float(5.6)"
    },
    {
        "question": "How do I add an item to the end of a list?",
        "answers": ["add()", "insert()", "append()", "insert.end()"],
        "correct": "append()"
    },
    {
        "question": "Is 'Hello' the same as \"Hello\"",
        "answers": ["Yes", "No", "Maybe", "Possibly?"],
        "correct": "Yes"
    },
    {
        "question": "How do you remove any whitespace from beginning and end of a string?",
        "answers": ["len()", "trim()", "str.trim()", "strip()"],
        "correct": "strip()"
    },
    {
        "question": "How do you start an if statement?",
        "answers": ["if x > y:", "if (x > y):", "if x > y then:", "x > y if true:"],
        "correct": "if x > y:"
    },
    {
        "question": "How do you start a while loop?",
        "answers": ["while x > y:", "while (x > y):", "x > y while:", "(x > y) while"],
        "correct": "while x > y"
    },
    {
        "question": "How do you start a for loop?",
        "answers": ["for x > y:", "for x in y:", "x > y for:", "for each x in y:"],
        "correct": "for x in y"
    },
    {
        "question": "What does pass do?",
        "answers": ["A placeholder, does nothing", "Passes a can of coke", "Restarts code", "Everything"],
        "correct": "A placeholder, does nothing"
    },
    {
        "question": "What data type is used to store a sequence of characters?",
        "answers": ["List", "Tuple", "String", "Set"],
        "correct": "String"
    }
]

hard_quiz_questions = [
    {
        "question": "What is the correct code to print the type of a variable?",
        "answers": ["print(typeof(x))", "print(type(x))", "typePrint(x)", "print.type(x)"],
        "correct": "print(type(x))"
    },
    {
        "question": "Which of these define a list?",
        "answers": ["\"{'green', 'blue', 'yellow', 'red}\"","\"['green', 'blue', 'yellow', 'red']\"", "\"('green', 'blue', 'yellow', 'red)\"", "\"{'green': 'blue', 'yellow': 'red'}\""],
        "correct": "\"['green', 'blue', 'yellow', 'red]\""
    },
    {
        "question": "Which of these define a dictionary?",
        "answers": ["\"{'green', 'blue', 'yellow', 'red}\"","\"['green', 'blue', 'yellow', 'red']\"", "\"('green', 'blue', 'yellow', 'red)\"", "\"{'green': 'blue', 'yellow': 'red'}\""],
        "correct": "\"{'green': 'blue', 'yellow': 'red'}\""
    },
    {
        "question": "Which collection is ordered, changeable and allows duplicate members?",
        "answers": ["List", "Dictionary", "List", "Tuple"],
        "correct": "List"
    },
    {
        "question": "Which collection doesn't allow duplicate members?",
        "answers": ["List", "Dictionary", "Set", "Tuple"],
        "correct": "Set"
    },
    {
        "question": "What does zip() function do?",
        "answers": ["Converts a list into a tuple", "Combines multiple iterables into an iterator of tuples", "Sorts a list", "Makes a .zip file from selected files"],
        "correct": "Combines multiple iterables into an iterator of tuples"
    }
]

correct_congrats = ["Ka Pai! You got that one correct!", 
                    "Great Job! You got that one right!", 
                    "Amazing! You got it right!", 
                    "Keep going! You're doing amazing!"]

def generate_incorrect_message(correct_answer):
    possible_answers = [
        f"So close! You got that one wrong, the answer was {correct_answer}",
        f"Better luck next time! You were wrong :( , the answer was {correct_answer}"
    ]
    return random.choice(possible_answers)