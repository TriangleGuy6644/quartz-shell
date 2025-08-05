import curses
import random
import sys
import time
from string import printable
from argparse import ArgumentParser, ArgumentDefaultsHelpFormatter

# Colors map
COLORS = {
    "BLACK" : curses.COLOR_BLACK,
    "BLUE" : curses.COLOR_BLUE,
    "CYAN" : curses.COLOR_CYAN,
    "GREEN" : curses.COLOR_GREEN,
    "MAGENTA" : curses.COLOR_MAGENTA,
    "RED" : curses.COLOR_RED,
    "WHITE" : curses.COLOR_WHITE,
    "YELLOW" : curses.COLOR_YELLOW,
}

def rand_string(character_set, length):
    return "".join(random.choice(character_set) for _ in range(length))

def matrix_main(stdscr):
    curses.curs_set(0)
    curses.start_color()
    curses.init_pair(9, FG, BG)
    stdscr.bkgd(curses.color_pair(9))
    size = stdscr.getmaxyx()

    background = rand_string(printable.strip(), size[0] * size[1])
    foreground = []
    dispense = []

    delta = 0
    bg_refresh_counter = random.randint(3, 7)
    lt = time.time()

    while True:
        if CLEAR:
            stdscr.clear()
        else:
            stdscr.erase()

        now = time.time()
        delta += (now - lt) * UPDATES_PER_SECOND
        lt = now

        while delta >= 1:
            if stdscr.getmaxyx() != size:
                return  # restart on resize

            for _ in range(LETTERS_PER_UPDATE):
                dispense.append(random.randint(0, size[1] - 1))

            # Iterate backwards to safely pop from dispense
            for i in reversed(range(len(dispense))):
                c = dispense[i]
                foreground.append([0, c])
                if not random.randint(0, PROBABILITY):
                    dispense.pop(i)

            # Iterate backwards to safely pop from foreground
            for i in reversed(range(len(foreground))):
                b = foreground[i]
                if b[0] < size[0] - 1:
                    stdscr.addstr(b[0], b[1], background[b[0] * size[1] + b[1]], curses.color_pair(9))
                    b[0] += 1
                else:
                    foreground.pop(i)

            bg_refresh_counter -= 1
            if bg_refresh_counter <= 0:
                background = rand_string(printable.strip(), size[0] * size[1])
                bg_refresh_counter = random.randint(3, 7)

            delta -= 1
            stdscr.refresh()

def main(args):
    parser = ArgumentParser(description="Create the matrix falling text.", formatter_class=ArgumentDefaultsHelpFormatter)

    parser.add_argument("-b", "--background", default="black",
            help="The colour of the falling text.")
    parser.add_argument("-c", "--clear", action="store_true",
            help="Use stdscr.clear() instead of stdscr.erase().")
    parser.add_argument("-f", "--foreground", default="green",
            help="The colour of the falling text.")
    parser.add_argument("-l", "--letters", type=int, default=2,
            help="The number of letters produced per update.")
    parser.add_argument("-p", "--probability", type=int, default=5,
            help="1/p probability of a dispense point deactivating each tick.")
    parser.add_argument("-u", "--ups", type=int, default=15,
            help="The number of updates to perform per second.")

    parsed_args = parser.parse_args(args)

    global BG, CLEAR, FG, LETTERS_PER_UPDATE, PROBABILITY, UPDATES_PER_SECOND
    CLEAR = parsed_args.clear
    FG = COLORS.get(parsed_args.foreground.upper(), curses.COLOR_GREEN)
    BG = COLORS.get(parsed_args.background.upper(), curses.COLOR_BLACK)
    LETTERS_PER_UPDATE = abs(parsed_args.letters)
    PROBABILITY = parsed_args.probability - 1
    UPDATES_PER_SECOND = abs(parsed_args.ups)

    try:
        while True:
            curses.wrapper(matrix_main)
    except (EOFError, KeyboardInterrupt):
        print("\nExiting matrix...")
        sys.exit(0)
