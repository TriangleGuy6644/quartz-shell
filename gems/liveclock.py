ALIASES = {
    "lc": "liveclock",
    "clock": "liveclock"
}

from datetime import datetime as dt
import os; import time

def main(args):
    try:
        while True:
            now = dt.now()
            ct = now.strftime("%I:%M:%S %p")
            os.system('cls')
            print(ct)
            time.sleep(1)
    except KeyboardInterrupt:
        print("\nClock Stopped!")