# NAME: Thomas De Witte
# Version: 1.1

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
CH2 = DigitalOutputDevice(22, True, False, pin_factory=factory)
CH3 = DigitalOutputDevice(27, True, False, pin_factory=factory)
CH4 = DigitalOutputDevice(10, True, False, pin_factory=factory)
CH = [CH1, CH2, CH3, CH4]
# LED's
LED1 = DigitalOutputDevice(26, pin_factory=factory)
LED2 = DigitalOutputDevice(19, pin_factory=factory)
LED3 = DigitalOutputDevice(6, pin_factory=factory)
LED4 = DigitalOutputDevice(11, pin_factory=factory)
LED = [LED1, LED2, LED3, LED4]
# Setup Inputs
# Buttons
BTN1 = Button(pin=14, pull_up=False, bounce_time=0.25, pin_factory=factory)
BTN2 = Button(pin=15, pull_up=False, bounce_time=0.25, pin_factory=factory)
BTN3 = Button(pin=23, pull_up=False, bounce_time=0.25, pin_factory=factory)
BTN4 = Button(pin=12, pull_up=False, bounce_time=0.25, pin_factory=factory)
BTN = [BTN1, BTN2, BTN3, BTN4]

def btn1_toggle():
    if BTN1.value == 1 and CH1.value == 0:
        CH1.on()
        LED1.on()
        time.sleep(0.25)
    if BTN1.value == 1 and CH1.value == 1:
        CH1.off()
        LED1.off()
        time.sleep(0.25)


def btn2_toggle():
    if BTN2.value == 1 and CH2.value == 0:
        CH2.on()
        LED2.on()
        time.sleep(0.25)
    if BTN2.value == 1 and CH2.value == 1:
        CH2.off()
        LED2.off()
        time.sleep(0.25)


def btn3_toggle():
    if BTN3.value == 1 and CH3.value == 0:
        CH3.on()
        LED3.on()
        time.sleep(0.25)
    if BTN3.value == 1 and CH3.value == 1:
        CH3.off()
        LED3.off()
        time.sleep(0.25)


def btn4_toggle():
    if BTN4.value == 1 and CH4.value == 0:
        CH4.on()
        LED4.on()
        time.sleep(0.25)
    if BTN4.value == 1 and CH4.value == 1:
        CH4.off()
        LED4.off()
        time.sleep(0.25)


while True:
    btn1_toggle()
    btn2_toggle()
    btn3_toggle()
    btn4_toggle()
t
