ALIASES = {
    'sqrt': 'squareroot'
}
from math import sqrt as sr

def main (args):
    try:
        if not args:
            print("Usage: squareroot <number>")
            return
        num = float(args[0])
        result = sr(num)
        print(f"The square root of {num} is {result}.")
    except ValueError:
        print("Please type an actual number.")
        return