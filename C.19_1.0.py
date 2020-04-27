# NAME: Thomas De Witte
# Version: 1.0

# Library Import
from gpiozero import DigitalOutputDevice  # DIGITALOUTPUTDEVICE is for RELAIS
from gpiozero import Button
from gpiozero.pins.pigpio import PiGPIOFactory
import time

# IPADRES CHANGE THE GREEN TEXT TO CHANGE IP ADRES
factory = PiGPIOFactory('192.168.0.112')

# Setup Outputs
# Relais
CH1 = DigitalOutputDevice(17, True, False, pin_factory=factory)

# LED's
LED1 = DigitalOutputDevice(26, pin_factory=factory)

# Setup Inputs
# Buttons
BTN1 = Button(pin=14, pull_up=False, bounce_time=0.25, pin_factory=factory)


if BTN1.value == 1 and CH1.value == 0:
    CH1.on()
    LED1.on()
    time.sleep(0.25)
if BTN1.value == 1 and CH1.value == 1:
    CH1.off()
    LED1.off()
    time.sleep(0.25)

