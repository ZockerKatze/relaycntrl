import tkinter as tk
import RPi.GPIO as GPIO
from time import sleep
import time
import random
import numpy as np
from colorama import Fore, Back, Style
GPIO.setwarnings(False)

print("( ___ )                                                                ( ___ )")
print(" |V7 |~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~| V7| ")
print(" |V7 |                                                               V7 | V7| ")
print(" |V7 |      ____  ________    _____  __  _______   ____________  __  V7 | V7| ")
print(" |V7 |     / __ \/ ____/ /   /   \ \/ / / ____/ | / /_  __/ __ \/ /  V7 | V7| ")
print(" |V7 |    / /_/ / __/ / /   / /| |\  / / /   /  |/ / / / / /_/ / /   V7 | V7| ")
print(" |V7 |   / _, _/ /___/ /___/ ___ |/ / / /___/ /|  / / / / _, _/ /___ V7 | V7| ")
print(" |V7 |  /_/ |_/_____/_____/_/  |_/_/  \____/_/ |_/ /_/ /_/ |_/_____/ V7 | V7| ")
print(" |V7 |                                                               V7 | V7| ")
print(" |V7_|~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|_V7| ")
print("(_____)                                                                (_____)")
print("Created by Rattatwingo 2024")
print("Initializing.")
print("Initializing..")
print("Initializing...")
print("Initialized!")
print("STARTING UI!")
print("UI started")
print(Style.BRIGHT + Fore.GREEN + "Everything fine! I guess?! Can't do a remote diagnostic")
print(Style.BRIGHT + Fore.WHITE + "")
print("SMOKE WEED")
print("  __      ")
print(" / /  _   ")
print("| |  (_)  ")
print("| |   _   ")
print("| |  (_)  ")
print(" \_\      ")

GPIO.setmode(GPIO.BCM)
pins = [2, 3, 26, 17, 27, 22, 10, 9]
for pin in pins:
    GPIO.setup(pin, GPIO.OUT)

def toggle_pin(pin):
    GPIO.output(pin, not GPIO.input(pin))

GPIO.output(pins, GPIO.HIGH) #set pins to snoop dawg

root = tk.Tk()
root.title("RelayCntrl V2")

def toggle_row(row_pins):
    for pin in row_pins:
        toggle_pin(pin)


buttons = []
for i, pin in enumerate(pins):
    row = i // 4  
    col = i % 4  
    button = tk.Button(root, text=f"Relay {i+1}", height=4, width=20, padx=10, pady=5, command=lambda p=pin: toggle_pin(p))
    button.grid(row=row, column=col)  
    buttons.append(button)

def update_buttons():
    for pin, button in zip(pins, buttons):
        state = "AUS" if GPIO.input(pin) else "EIN"
        button.config(text=f"RELAY {pins.index(pin)+1} ist gerade {state}")
        if state == "EIN":
            button.config(text=f"RELAY {pins.index(pin)+1} ist gerade {state}", bg="lightgreen", fg="black")
        else:
            button.config(text=f"RELAY {pins.index(pin)+1} ist gerade {state}", bg="brown1", fg="white")


def update_loop():
    update_buttons()
    root.after(100, update_loop) 

options_tab = tk.Frame(root)
options_tab.grid(row=0, column=0)

def testpinfunc(pins):
	GPIO.output(pins, GPIO.LOW)
	sleep(2)
	GPIO.output(pins, GPIO.HIGH)
	print(Style.BRIGHT + Fore.GREEN + "TRIGGERD EVERY PIN!")

##longass function now
def lol(pins):
    print(Style.BRIGHT + Fore.GREEN + "SEQUENCED!")
    
    try:
        while True:
            for pin in pins:
                GPIO.output(pin, GPIO.LOW)
                time.sleep(0.20)
                GPIO.output(pin, GPIO.HIGH)
    except KeyboardInterrupt:
        print(Style.BRIGHT + Fore.RED + "EXIT!")

## stupid ass function i hate python

def lolol(pins):
    try:
        while True:
            for pin in pins:
                np.random.shuffle(pins)
                print (pins) ##print nlist
                GPIO.output(pin, GPIO.LOW)
                time.sleep(0.2)
                GPIO.output(pin, GPIO.HIGH)
    except KeyboardInterrupt:
        pins[:] = [2, 3, 26, 17, 27, 22, 10, 9] ##[:] resets it idfk
        print(Fore.GREEN + Style.BRIGHT + "IDK SEQUENCED RANDOM")
        GPIO.output(pin, GPIO.HIGH)
        return pins


def printcode(print):
	print(Style.BRIGHT + Fore.RED + "ERROR")

test_pin_button = tk.Button(root, text="RELAYTEST", bg="firebrick3", fg="black", height=1, width=20, command=lambda pi=pins: testpinfunc(pins))
test_pin_button.grid(row=3)

rollbutton = tk.Button(root, text="SEQUENCETEST", bg="firebrick3", fg="black", height=1, width=20, command=lambda pi=pins: lol(pins))
rollbutton.grid(row=3, column=1)

spare= tk.Button(root, text="CLICKCLACK", bg="firebrick3", fg="black", height=1, width=20, command=lambda pi=pins: lolol(pins))
spare.grid(row=3, column=2)

spare2 = tk.Button(root, text="SPARE2", bg="firebrick3", fg="black", height=1, width=20, command=lambda ou=print: printcode(ou))
spare2.grid(row=3, column=3)


update_loop()
root.mainloop()

GPIO.cleanup()
