from gpiozero import LED
import multiprocessing
import time


def blink_led1():
    while True:
        print("Turn LED 1 on")
        time.sleep(5)
        print("Turn LED 1 off")
        time.sleep(2)


def blink_led2():
    while True:
        print("Turn LED 2 on")
        time.sleep(2)
        print("Turn LED 2 off")
        time.sleep(5)


if __name__ == '__main__':
    process_1 = multiprocessing.Process(target=blink_led1)
    process_2 = multiprocessing.Process(target=blink_led2)
    process_1.start()
    process_2.start()
