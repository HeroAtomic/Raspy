import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

GPIO.setup(18, GPIO.OUT)
GPIO.setup(19, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(20, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(21, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)


def move_servo(gp_input, pw):
    print('GPIO {} HIGH'.format(gp_input))
    # PWM faking
    print('ON {} s'.format(pw))
    GPIO.output(18, GPIO.HIGH)
    time.sleep(pw)

    print('OFF {} s'.format(0.02 - pw))
    GPIO.output(18, GPIO.LOW)
    time.sleep(0.02 - pw)


while True:
  if GPIO.input(19):
    print('GPIO 19 HIGH')
    move_servo(19, 0.0007)
  elif GPIO.input(20):
    print('GPIO 20 HIGH')
    move_servo(20, 0.0015)
  elif GPIO.input(21):
    print('GPIO 21 HIGH')
    move_servo(21, 0.0022)