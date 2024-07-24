import RPi.GPIO as GPIO
import tkinter as tk
from time import sleep
from colorama import init, Fore, Back, Style
GPIO.setwarnings(False)

print("( ___ )                                                              ( ___ )")
print(" |   |~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|   | ")
print(" |   |                                                                |   | ")
print(" |   |      ____  ________    _____  __  _______   ____________  __   |   | ")
print(" |   |     / __ \/ ____/ /   /   \ \/ / / ____/ | / /_  __/ __ \/ /   |   | ")
print(" |   |    / /_/ / __/ / /   / /| |\  / / /   /  |/ / / / / /_/ / /    |   | ")
print(" |   |   / _, _/ /___/ /___/ ___ |/ / / /___/ /|  / / / / _, _/ /___  |   | ")
print(" |   |  /_/ |_/_____/_____/_/  |_/_/  \____/_/ |_/ /_/ /_/ |_/_____/  |   | ")
print(" |   |                                                                |   | ")
print(" |___|~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|___| ")
print("(_____)                                                              (_____)")
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
print(Style.BRIGHT + Fore.GREEN + "everything fine!")

print("  __     ")
print(" / /  _  ")
print("| |  (_) ")
print("| |   _  ")
print("| |  (_) ")
print(" \_\     ")



GPIO.setmode(GPIO.BCM)
pins = [2, 3, 4, 17, 27, 22, 10, 9]
for pin in pins:
    GPIO.setup(pin, GPIO.OUT)
    GPIO.output(pin, GPIO.HIGH)

# Create GUI for snoop dawg 1337
root = tk.Tk()
root.title("RELAYCNTRL")

def toggle_pin(pin):
    if GPIO.input(pin):  # HIGH snoop dawg weed mode 1337 420 69
        GPIO.output(pin, GPIO.LOW)  # snoop dawg HIGH LOW
    else:
        GPIO.output(pin, GPIO.HIGH)  # nix snoop dawg LOW HIGH

def toggle_row(row_pins):
    for pin in row_pins:
        toggle_pin(pin)

# snoop dawg high mode 1337
for pin in pins:
    GPIO.output(pin, GPIO.HIGH)

#
# ab hier ist ein wilder brainfuck, wer gehirnzellen behalten will soll nicht weiter gehen
# letzte warnung sonst kommt der marabu und snoop dawg und raucht dich zu


buttons = [] #oaschloch funktionsglumpat
for i, pin in enumerate(pins):
    button = tk.Button(root, text=f"RELAY {i+1}", command=lambda p=pin: toggle_pin(p), height=4, width=15, font=("Helvetica", 12), bg="lightgrey", fg="black", padx=10, pady=5)
    row = i // 4  
    col = i % 4 
    button.grid(row=row, column=col)  
    buttons.append(button)

    if (i + 1) % 4 == 0: 
        row_pins = pins[i - 3:i + 1]  
        fifth_button = tk.Button(root, text="<-- ON/OFF", command=lambda r=row_pins: toggle_row(r), height=4, width=15, font=("Helvetica", 12), bg="lightgrey", fg="black", padx=10, pady=5)
        fifth_button.grid(row=row, column=col + 1) 
        buttons.append(fifth_button)

root.mainloop()

GPIO.cleanup()
