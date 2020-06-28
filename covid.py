import RPi.GPIO as GPIO
import time
from datetime import datetime as dt
from colorama import Fore

walk_in_GPIO = 19
walk_out_GPIO = 20
warning_GPIO = 18

people = 0
capacity = 10


def count_people(count):
    if GPIO.event_detected(walk_in_GPIO):
        count += 1
        print(Fore.BLUE + 'Walk in detected: {}'.format(dt.now()))
    if GPIO.event_detected(walk_out_GPIO):
        count -= 1
        print(Fore.BLUE + 'Walk out detected: {}'.format(dt.now()))
    return count


if __name__ == '__main__':
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)

    GPIO.setup(walk_in_GPIO, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    GPIO.setup(walk_out_GPIO, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    GPIO.setup(warning_GPIO, GPIO.OUT)

    GPIO.add_event_detect(walk_in_GPIO, GPIO.RISING, bouncetime=200)
    GPIO.add_event_detect(walk_out_GPIO, GPIO.RISING, bouncetime=200)

    while True:
        people = count_people(people)

        if people > capacity:
            GPIO.output(warning_GPIO, 1)
            print(Fore.RED + '{} - WARNING: {}/{} people in room'.format(dt.now(), people, capacity))
            time.sleep(1)
        elif people == capacity:
            GPIO.output(warning_GPIO, 1)
            print(Fore.YELLOW + '{} - {} people in room'.format(dt.now(), people))
            time.sleep(1)
        elif people < capacity:
            GPIO.output(warning_GPIO, 0)
            print(Fore.GREEN + '{} - {} people in room'.format(dt.now(), people))
            time.sleep(1)