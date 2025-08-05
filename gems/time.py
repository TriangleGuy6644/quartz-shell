from datetime import datetime as dt
ALIASES = {
    'date': 'time',
}
def main(args):
    current_time = dt.now()
    ct = current_time
    print(f"It is currently {current_time.hour}:{current_time.minute}:{current_time.second} on {ct.year}-{ct.month}-{ct.day}.")