"""
The Magic 8 ball takes in a yes or no answer and responds based on an index of possible responses
"""

import random

# The answers that the magic 8 ball may choose from
answers = [
    # positive answers
    "It is certain", "Without a doubt", "You may rely on it", "It is decidedly so", "As I see it, yes",

    # neutral answers
    "Better not tell you now", "Ask again later", "Cannot predict now", "Concentrate and ask again",

    # negative answers
    "Don’t count on it", "Outlook unlikely", "My sources say no", "Very doubtful", "My reply is no"
]

# Introduction statement
print("Hello, I am the magic 8 ball, here to answer your questions. They may be yes or no questions only. ")
name = str(input("What is your name?: "))
print("Hello " + name)

# The actual Magic8Ball function


def Magicball():
    print("What is your question?: ")
    input()
    print(answers[random.randint(0, len(answers)-1)])
    Replay()

# Decide if the user would like to ask another question.
# Note this function will terminate if anything besides something starting with Y is entered


def Replay():
    replay = str(input("Do you have another question?[Y/N]: "))
    if replay[0].upper() == "Y":
        Magicball()
    elif replay[0].upper() == "N":
        exit()


Magicball()
