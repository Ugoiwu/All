from pynput.keyboard import Controller
from time import sleep

keyboard = Controller()

sleep(5)
for i in [chr(i) for i in range(ord('a'),ord('z')+1)]:
    #sleep(0.00000000000001)
    keyboard.press(f"{i}")
