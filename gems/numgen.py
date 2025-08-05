import random
ALIASES = {
    'numbergenerator': 'numgen',
}

def main(args):
    if not args:
        print("Usage: numgen <min> <max>")
        return
    
    try:
        min = int(args[0])
        max = int(args[1])
        
    except ValueError:
        print("both min and max should be integers.")
    
    if min > max:
        print("The minimum cant be larger than the maximum, idiot.")
    if min == max:
        print("min and max cannot be the same, fuckface.")


    result = random.randint(min, max)
    print(f"Generated Number: {result}")
