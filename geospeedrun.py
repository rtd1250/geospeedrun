#!/usr/bin/env python3

import random
import threading
from time import sleep
from pynput.keyboard import Controller

keyboard = Controller()

def pressRandom():
    for i in range (0,500):
        number = str(random.randint(1,4))
        delayP = 0.08 #for some randomness and more human pace, use random.uniform(0.05,0.1)
        delayR = 0.00 #same here: random.uniform(0.05,0.1)
        sleep(delayP)
        keyboard.press(number)
        sleep(delayR)
        keyboard.release(number)

#give time to switch windows and start smashing the keys
sleep(1)


# Multithreading!
for i in range(4):
    threading.Thread(target=pressRandom).start()
