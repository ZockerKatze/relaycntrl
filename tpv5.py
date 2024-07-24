import tkinter as tk
import RPi.GPIO as GPIO
from time import sleep
from colorama import init, Fore, Back, Style
GPIO.setwarnings(False)


print("( ___ )                                                                ( ___ )")
print(" |   |~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|   | ")
print(" |   |                                                               V2 |   | ")
print(" |   |      ____  ________    _____  __  _______   ____________  __  V2 |   | ")
print(" |   |     / __ \/ ____/ /   /   \ \/ / / ____/ | / /_  __/ __ \/ /  V2 |   | ")
print(" |   |    / /_/ / __/ / /   / /| |\  / / /   /  |/ / / / / /_/ / /   V2 |   | ")
print(" |   |   / _, _/ /___/ /___/ ___ |/ / / /___/ /|  / / / / _, _/ /___ V2 |   | ")
print(" |   |  /_/ |_/_____/_____/_/  |_/_/  \____/_/ |_/ /_/ /_/ |_/_____/ V2 |   | ")
print(" |   |                                                               V2 |   | ")
print(" |___|~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|___| ")
print("(_____)                                                                (_____)")
sleep(2)
print("Created by Rattatwingo 2024")
sleep(0.5)
print("Initialitzing.")
sleep(0.5)
print("Initialitzing..")
sleep(0.5)
print("Initialitzing...")
sleep(0.5)
print("Initialized!")
print("STARTING UI!")
sleep(1)
print("ui started")
sleep(0.1)
print(Style.BRIGHT + Fore.GREEN + "everything fine! i guess?! Cant do a remote diagnostic")
print(Style.BRIGHT + Fore.WHITE + "")
print("SMOKE WEED")
print("  __      ")
print(" / /  _   ")
print("| |  (_)  ")
print("| |   _   ")
print("| |  (_)  ")
print(" \_\      ")

#WEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEED
#WEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEED
#WEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEED
#

GPIO.setmode(GPIO.BCM)
pins = [2, 3, 4, 17, 27, 22, 10, 9]
for pin in pins:
    GPIO.setup(pin, GPIO.OUT)


def toggle_pin(pin):
    GPIO.output(pin, not GPIO.input(pin))

root = tk.Tk()
root.title("RELAYCNTRL V2")

def toggle_row(row_pins):
    for pin in row_pins:
        toggle_pin(pin)

buttons = []
for i, pin in enumerate(pins):
    row = i // 4  
    col = i % 4  
    button = tk.Button(root, text=f"Relay", height=4, width=15, padx=10, pady=5, command=lambda p=pin: toggle_pin(p))
    button.grid(row=row, column=col)
    buttons.append(button)

# smokeweedeverydayupdate
def update_buttons():
    for pin, button in zip(pins, buttons):
        state = "OFF" if GPIO.input(pin) else "ON"
        button.config(text=f"RELAY ---> {state}")


# updateweedeveryday
def update_loop():
    update_buttons()
    root.after(100, update_loop) 

update_loop()
root.mainloop()

GPIO.cleanup()

#this programm is sveryshitty 