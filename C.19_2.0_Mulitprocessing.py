# Library Import
from gpiozero import DigitalOutputDevice  # DIGITALOUTPUTDEVICE is for RELAIS
from gpiozero import Button
from gpiozero.pins.pigpio import PiGPIOFactory
import time
import multiprocessing

# IPADRES CHANGE THE GREEN TEXT TO CHANGE IP ADRES
factory = PiGPIOFactory('192.168.0.112')

# Setup Outputs
# Relais
CH1 = DigitalOutputDevice(17, True, False, pin_factory=factory)
CH2 = DigitalOutputDevice(22, True, False, pin_factory=factory)

# Setup Inputs
# Buttons
BTN1 = Button(pin=14, pull_up=False, bounce_time=0.25, pin_factory=factory)
BTN2 = Button(pin=15, pull_up=False, bounce_time=0.25, pin_factory=factory)


def toggle_led_one():
    while True:
        if BTN1.value == 1:
            CH1.on()
            print("CH1 ON")
            wait_led()
            print("CH1 OFF")
            CH1.off()


def toggle_led_two():
    while True:
        if BTN2.value == 1:
            CH2.on()
            print("CH2 ON")
            wait_led()
            print("CH2 OFF")
            CH2.off()


def wait_led():
    print("2SEC wait")
    time.sleep(2)
    print("WAIT OVER")


if __name__ == '__main__':
    x1 = multiprocessing.Process(target=toggle_led_one)
    x2 = multiprocessing.Process(target=toggle_led_two)
    x1.start()
    x2.start()
