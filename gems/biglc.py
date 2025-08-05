from pyfiglet import Figlet
from datetime import datetime as dt
import os
import time
import keyboard

ALIASES = {
    'lcbig': 'biglc',
    'blc': 'biglc',
    'bigliveclock': 'biglc'
}
def main(args):
    f = Figlet(font='big')
    try:
        while True:
            now = dt.now()
            f = Figlet(font='big')
            ct = now.strftime("%I:%M:%S %p")
            os.system('cls')
            print (f.renderText(ct)) 
            time.sleep(1)
    except KeyboardInterrupt:
        print("\nClock Stopped!")
