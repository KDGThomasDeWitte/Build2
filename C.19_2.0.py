# NAME: Thomas De Witte
# VERSION: 2.0

# LIBRARIES
from gpiozero import DigitalOutputDevice  # DIGITALOUTPUTDEVICE is for RELAIS
from gpiozero import Button
from gpiozero.pins.pigpio import PiGPIOFactory
import time
import timeit

# CONFIG
IP_ADRESS = PiGPIOFactory('192.168.0.112')  # IPADRES CHANGE THE GREEN TEXT TO CHANGE IP ADRES
BOUNCE_TIME = 0.01  # CONFIG THE BOUNCE TIME HERE
TRESHOLD_LONG_PUSH = 1  # CONFIG HERE THE TIME TO HAVE A LONG PUSH
TRESHOLD_TIME_TO_PRESS = 1.5

# SETUP
# Relais
AMOUNT_CHANNELS = 4  # AMOUNT OF CHANNELS YOU WANT TO USE -- MAX 8!!
CH_PIN = [17, 22, 27, 10, 26, 19, 6, 11]  # THESE ARE THE PINS YOU CAN USE FOR RELAIS -- MAX 8 RELAIS!!

# Buttons
AMOUNT_BUTTONS = 4  # AMOUNT OF BUTTONS YOU WANT TO USE -- MAX 4!!
BTN_PIN = [14, 15, 23, 12]  # THESE ARE THE PINS YOU CAN USE FOR BUTTONS -- MAX 4 BUTTONS!!

# VARIABLEs
ch = []
btn = []


# FUNCTIONS
def main():  # MAIN FUNCTION
    ch_setup()
    btn_setup()
    btn_check()


def ch_setup():  # SETS UP THE PINS TROUGH A LOOP
    for channel in ch:
        ch.append(DigitalOutputDevice(CH_PIN[channel], True, False, pin_factory=IP_ADRESS))
        print(ch[channel])


def btn_setup():  # SETS UP THE PINS TROUGH A LOOP
    for k in range(AMOUNT_BUTTONS):
        btn.append(Button(BTN_PIN[k], pull_up=False, bounce_time=BOUNCE_TIME, pin_factory=IP_ADRESS))


def btn_toggle(nr_list, times_pressed):  # CHECKS IF THE BUTTON IS PUSHED AND GOES TROUGH A SET FUNCTIONALITY
    if times_pressed == 1:
        if ch[nr_list].value == 0:  # IF BUTTON IS PUSHED AND CHANNEL OFF
            ch[nr_list].on()
            btn_check()
        if ch[nr_list].value == 1:  # IF BUTTON IS PUSHED AND CHANNEL ON
            ch[nr_list].off()
            btn_check()
    if times_pressed == 2:
        if ch[nr_list].value == 0:
            all_leds_on()
            btn_check()
        if ch[nr_list].value == 1:
            all_leds_off()
            btn_check()
    if times_pressed >= 3:
        if ch[nr_list].value == 0:
            all_leds_on()
            time.sleep(5)
            for i in range(3):
                all_leds_off()
                time.sleep(0.5)
                all_leds_on()
                time.sleep(0.5)
            btn_check()
        if ch[nr_list].value == 1:
            time.sleep(5)
            all_leds_off()
            btn_check()


def all_leds_on():
    for h in range(AMOUNT_CHANNELS):
        ch[h].on()


def all_leds_off():
    for h in range(AMOUNT_CHANNELS):
        ch[h].off()


def btn_long_push(nr_list):
    start = time.time()
    while btn[nr_list].value == 1:
        end = time.time()
        time_elapsed = end - start
        if time_elapsed > TRESHOLD_LONG_PUSH:
            if ch[nr_list].value == 0:
                ch[nr_list].on()
                time.sleep(5)
                for i in range(3):
                    ch[nr_list].off()
                    time.sleep(0.5)
                    ch[nr_list].on()
                    time.sleep(0.5)
                ch[nr_list].off()
                btn_check()
            if ch[nr_list].value == 1:
                time.sleep(5)
                ch[nr_list].off()
                btn_check()
            time.sleep(1)
            btn_check()


def btn_pressed(nr_list):
    if btn[nr_list].value == 1:
        start = time.time()
        times_pushed = 1
        btn_long_push(nr_list)
        while True:
            time.sleep(0.1)
            end = time.time()
            time_elapsed = end - start
            print(time_elapsed)
            if btn[nr_list].value == 1 and time_elapsed < TRESHOLD_TIME_TO_PRESS:
                times_pushed += 1
                start = end
            if time_elapsed > TRESHOLD_TIME_TO_PRESS:
                print(times_pushed)
                btn_toggle(nr_list, times_pushed)


def btn_check():
    while True:
        for i in range(AMOUNT_BUTTONS):
            btn_pressed(i)


# START PROGRAM
if __name__ == "__main__":
    main()
