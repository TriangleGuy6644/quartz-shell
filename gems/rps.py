import random
# ALIASES
ALIASES = {
    'rockpaperscissors': 'rps',
}

def main(args):
    choices = ['rock', 'paper', 'scissors']
    
    if args and args[0].lower() in choices:
        user_choice = args[0].lower()
    else:
        user_choice = input("Choose rock, paper, or scissors: ").strip().lower()
        if user_choice not in choices:
            print("\033[91mInvalid choice. Pick rock, paper, or scissors.\033[0m")
            return

    bot_choice = random.choice(choices)
    print(f"\033[94mYou chose:\033[0m {user_choice}")
    print(f"\033[95mQuartz chose:\033[0m {bot_choice}")

    if user_choice == bot_choice:
        result = "It's a tie!"
    elif (
        (user_choice == 'rock' and bot_choice == 'scissors') or
        (user_choice == 'paper' and bot_choice == 'rock') or
        (user_choice == 'scissors' and bot_choice == 'paper')
    ):
        result = "\033[92mYou win!\033[0m"
    else:
        result = "\033[91mYou lose!\033[0m"

    print(result)
