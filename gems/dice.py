import random

def main(args):
    if not args:
        print("Usage: dice <sides>")
        return
    
    

    try:
        sides = int(args[0])
    except ValueError:
        print("<sides> must be a number :3")
    
    diceroll = random.randint(1, sides)
    print(f"You rolled {diceroll}!")

