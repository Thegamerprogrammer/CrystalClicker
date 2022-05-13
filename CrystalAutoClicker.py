import time
import threading
from pynput.mouse import Button, Controller
from pynput.keyboard import Listener, KeyCode
from tqdm import tqdm
import winsound
import sys

for i in tqdm (range (100), 
               desc="Loading...", 
               ascii=False, ncols=75):
    time.sleep(0.02)
  
print("Complete.")

winsound.Beep(1000,1000)

message = 'Welcome To CrystalAutoClicker By Thegamerprogram!. \n\
Version 1.0. \n\
It Is Recommended To Learn How To Use The App If You Are Running It For The First Time. \n\
'
print('Running On Python: '+sys.version)
def typewriter(message):
        for char in message:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(0.1)
typewriter(message)

winsound.Beep(1000,1000)

answer = input('\n\
Want Help? yes/no?: ')

if answer.lower().strip() == "yes":
    message = "Here Delay Means How Fast The Clicker Needs To Click. \n\
For Example: If The Number Is Below 1 Set It As 0.0<yournumber>. \n\
If The Number Is Below The Number Shown Above Set It As 0.00<yournumber>. \n\
After That You Will Be Prompted With An Input Inside It You Should Put It Like This Ex: Button.left or Button.Right If You Put It Wrong It Won't work. \n\
I Hope This Helped You!. \n\
Restart To Run The Program. \n\
Press The Enter Key To Quit."
    def typewriter(message):
        for char in message:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(0.1)
    typewriter(message)
    winsound.Beep(1000,1000)
    input("")
    quit()
else:
    winsound.Beep(1000,1000)
    message = 'Please Enter The Delay:'
    def typewriter(message):
        for char in message:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(0.1)
    typewriter(message)
    cps = float(input('\n\
Enter Here: '))
    print(cps)
    winsound.Beep(1000, 1000)
    delay = 0.001
    winsound.Beep(1000, 1000)
    message = '\n\
Which Button Of The Mouse To AutoClick'
    def typewriter(message):
        for char in message:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(0.1)
    typewriter(message)
    ans = eval(input('\n\
Enter Here: '))
    button = ans
    print('Selected:')
    print(button)
    winsound.Beep(1000, 1000)
    start_stop_key = KeyCode(char='[')
    exit_key = KeyCode(char=']')

message = 'Press "[" To Start The Autoclicker Press "[" Again To Pause The Autoclicker. \n\
Press "]" to Exit the Autoclicker'

def typewriter(message):
        for char in message:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(0.1)
typewriter(message)

winsound.Beep(1000,1000)


class ClickMouse(threading.Thread):
    def __init__(self, delay, button):
        super(ClickMouse, self).__init__()
        self.delay = delay
        self.button = button
        self.running = False
        self.program_running = True

    def start_clicking(self):
        self.running = True

    def stop_clicking(self):
        self.running = False

    def exit(self):
        self.stop_clicking()
        self.program_running = False

    def run(self):
        while self.program_running:
            while self.running:
                mouse.click(self.button)
                time.sleep(cps)
            time.sleep(0.1)


mouse = Controller()
click_thread = ClickMouse(delay, button)
click_thread.start()


def on_press(key):
    if key == start_stop_key:
        if click_thread.running:
            click_thread.stop_clicking()
            winsound.Beep(1000,1000)
        else:
            click_thread.start_clicking()
            winsound.Beep(1000,1000)
    elif key == exit_key:
        message = '\n\
Exiting....'
        def typewriter(message):
            for char in message:
                sys.stdout.write(char)
                sys.stdout.flush()
                time.sleep(0.1)
        typewriter(message)
        winsound.Beep(1000,1000)
        time.sleep(2)
        click_thread.exit()
        listener.stop()


with Listener(on_press=on_press) as listener:
    listener.join()
