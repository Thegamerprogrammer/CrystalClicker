import time
import threading
from pynput.mouse import Button, Controller
from pynput.keyboard import Listener, KeyCode
from tqdm import tqdm
import winsound

for i in tqdm (range (100), 
               desc="Loading...", 
               ascii=False, ncols=75):
    time.sleep(0.02)
  
print("Complete.")

winsound.Beep(1000,1000)


delay = 0.001
button = Button.left
start_stop_key = KeyCode(char='[')
exit_key = KeyCode(char=']')

print('Welcome To CrystalClicker By Thegamerprogram!')
print('Version 1.0')

winsound.Beep(1000,1000)

answer = input('Want Help? yes/no?: ')

if answer.lower().strip() == "yes":
    print('Here Delay Means How Fast The Clicker Needs To Click')
    print('For Example: If The Number Is Below 1 set it as 0.0<yournumber>')
    print('If The Number Is Below That Number set it as 0.00<yournumber>')
    print('I Hope This Helped You!')
    print('Restart To Run The Program')
    winsound.Beep(1000,1000)
    while True:

        input("Press Enter to continue...")
else:
    winsound.Beep(1000,1000)
    cps = float(input('Enter The Delay: '))
    print('Selected:')
    print(cps)

print('Press "[" To Start The Autoclicker Press "[" Again To Pause The Autoclicker')
print('Press "]" to Exit the Autoclicker')

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
        print('Exiting...')
        winsound.Beep(1000,1000)
        time.sleep(2)
        click_thread.exit()
        listener.stop()


with Listener(on_press=on_press) as listener:
    listener.join()
