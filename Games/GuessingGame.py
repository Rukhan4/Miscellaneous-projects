import random

num = random.randint(1, 100)
num

print("Welcome to the guessing game!")
print("The rules of this game are:\n")
print("I(the subconscious of your mind) will choose a random number between 1, and 100")
print("You then attempt to guess this number. There is no limit to how many guesses you have, however,")
print("each incorrect guess is counted!")
print("If you are within 10 of the number, I will say warm, and if further than 10, I will say cold")
print('Subsequently, if you become closer to my number, I will say warmer, and for the latter, I will')
print("say colder\n")
print("Good luck, happy guessing!")

guesses = [0]

while True:
    guess = int(input('What is your guess?(1-100) \t'))

    if guess < 1 or guess > 100:
        print('Must be between 1-100!')
        continue

    if guess == num:
        print(f'Congratulations, you guessed my number in {len(guesses)} guesses!')
        break
    guesses.append(guess)

    if guesses[-2]:
        if abs(num-guess) < abs(num-guesses[-2]):
            print('Warmer')
        else:
            print('Colder')

    else:
        if abs(num-guess) <= 10:
            print('Warm')
        else:
            print('Cold')
