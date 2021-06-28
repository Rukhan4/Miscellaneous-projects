"""
Check if a word is equal to the reverse of itself
"""


def palindrome(s):
    """A palindrome is a word, phrase, or sequence that reads the same backwards as forwards.

    Args:
        s ([string]): [A variable that may or may not be a palindrome passed in by the user]
        s is reassigned to a version where there are no spaces and all lowercase, allowing phrases like
        'nurses RuN' to suffice as a palindrome!
    Returns:
        The string 's', reversed.
    """
    s = s.replace(" ", "").lower()
    return s == s[::-1]


playing = True
count = 0
while playing:
    attempt = str(input("Enter a word or phrase you think is a palindrome:"))
    if palindrome(attempt):
        print(f"The word/phrase {attempt} is a palindrome!")
        count += 1
    else:
        print(f"The word/phrase {attempt} is not a palindrome!")

    replay = input("Would you like to try another word/phrase? Enter Yes or No:")
    if replay[0].lower() == 'y':
        playing = True
        continue
    else:
        print(f"Thanks for playing! You guessed {count} palindrome/s!")
        playing = False
