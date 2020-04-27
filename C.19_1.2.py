# NAME: Thomas De Witte
# VERSION: 1.2

# Library Import
from gpiozero import DigitalOutputDevice  # DIGITALOUTPUTDEVICE is for RELAIS
from gpiozero import Button
from gpiozero.pins.pigpio import PiGPIOFactory
import time
import timeit

# IPADRES CHANGE THE GREEN TEXT TO CHANGE IP ADRES
IP_ADRESS = PiGPIOFactory('192.168.0.112')


# Setup Outputs
# Relais
AMOUNT_CHANNELS = 4  # AMOUNT OF CHANNELS YOU WANT TO USE -- MAX 8!!
CH_PIN = [17, 22, 27, 10, 26, 19, 6, 11]  # THESE ARE THE PINS YOU CAN USE FOR RELAIS -- MAX 8 RELAIS!!!

# Buttons
AMOUNT_BUTTONS = 4  # AMOUNT OF BUTTONS YOU WANT TO USE -- MAX 4!!
BTN_PIN = [14, 15, 23, 12]  # THESE ARE THE PINS YOU CAN USE FOR BUTTONS -- MAX 4 BUTTONS!!!

# Variables
ch = []
btn = []

# Functions


def ch_setup():
    for j in range(AMOUNT_CHANNELS):
        ch.append(DigitalOutputDevice(CH_PIN[j], True, False, pin_factory=IP_ADRESS))


def btn_setup():
    for k in range(AMOUNT_BUTTONS):
        btn.append(Button(BTN_PIN[k], pull_up=False, bounce_time=0.25, pin_factory=IP_ADRESS))


def btn_toggle(nr_list):

    if btn[nr_list].value == 1 and ch[nr_list].value == 0:
        ch[nr_list].on()
        time.sleep(0.25)
    if btn[nr_list].value == 1 and ch[nr_list].value == 1:
        ch[nr_list].off()
        time.sleep(0.25)


# START PROGRAM
ch_setup()
btn_setup()
while True:
    for i in range(AMOUNT_BUTTONS):
        btn_toggle(i)
