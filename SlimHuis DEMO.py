#!/usr/bin/env python
__author__ = "Thomas De Witte"
__version__ = "1.0"

# IMPORTS
from gpiozero import DigitalOutputDevice
from gpiozero import Button
from gpiozero.pins.pigpio import PiGPIOFactory
import time

# VARIABLES
IP = PiGPIOFactory('192.168.0.112')  # CHANGE GREEN TEXT FOR IPADRESS

# SETUP RELAIS
RELAIS_PIN = [17, 22, 27, 10, 26, 19, 6, 11]
AMOUNT_CHANNELS = 4

# SETUP BUTTONS
BTN_PIN = [14, 15, 23, 12]
AMOUNT_BUTTONS = 4

# LISTS
relais = []
buttons = []


# FUNCTIONS
def set_up_relais():
    for i in range(AMOUNT_CHANNELS):
        relais.append(DigitalOutputDevice(pin=RELAIS_PIN[i], active_high=True, initial_value=False, pin_factory=IP))


def set_up_button():
    for i in range(AMOUNT_BUTTONS):
        buttons.append(Button(pin=BTN_PIN[i], pull_up=False, bounce_time=0.25, pin_factory=IP))
        

def toggle_button(button_nr):
    if buttons[button_nr].value == 1 and relais[button_nr].value == 0:
        turn_led_on()
        time.sleep(0.25)

    if buttons[button_nr].value == 1 and relais[button_nr].value == 1:
        relais[button_nr].off()
        time.sleep(0.25)


def check_button():
    while True:
        for i in range(AMOUNT_BUTTONS):
            toggle_button(i)


def turn_led_on():
    print("THE LED IS ON")
    # relais[button_nr].on()


def main():
    set_up_relais()
    set_up_button()
    check_button()


# MAIN START PROGRAM
if __name__ == "__main__":
    main()





