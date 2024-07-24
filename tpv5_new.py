import tkinter as tk
import RPi.GPIO as GPIO
from time import sleep
from colorama import init, Fore, Back, Style
GPIO.setwarnings(False)

print("( ___ )                                                                ( ___ )")
print(" |V2 |~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~| V2| ")
print(" |V2 |                                                               V2 | V2| ")
print(" |V2 |      ____  ________    _____  __  _______   ____________  __  V2 | V2| ")
print(" |V2 |     / __ \/ ____/ /   /   \ \/ / / ____/ | / /_  __/ __ \/ /  V2 | V2| ")
print(" |V2 |    / /_/ / __/ / /   / /| |\  / / /   /  |/ / / / / /_/ / /   V2 | V2| ")
print(" |V2 |   / _, _/ /___/ /___/ ___ |/ / / /___/ /|  / / / / _, _/ /___ V2 | V2| ")
print(" |V2 |  /_/ |_/_____/_____/_/  |_/_/  \____/_/ |_/ /_/ /_/ |_/_____/ V2 | V2| ")
print(" |V2 |                                                               V2 | V2| ")
print(" |V2_|~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|_V2| ")
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
pins = [2, 3, 4, 17, 27, 22, 10, 9]
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
## very shitty color thing


def update_loop():
    update_buttons()
    root.after(100, update_loop) 

update_loop()
root.mainloop()

GPIO.cleanup()

#i hate python every day every night
