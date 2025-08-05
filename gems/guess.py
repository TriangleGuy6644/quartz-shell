import random
ALIASES = {
    'guessing': 'guess',
    'guessinggame': 'guess',
    'numberguesser':  'guess',
    'numguess': 'guess'
}


def main(args):
    try:
        if not args:
            print("Usage: guess <max number>")
        max = int(args[0])
        num = random.randint(1, max)
        guess = int(input(f"Guess a number from 1-{max}!\n> "))
        if guess == num:
            print("Correct!")
            return
        elif guess != num:
            print(f"Incorrect! The number was {num}")
    except ValueError:
        print("Please enter a valid value.\n")


