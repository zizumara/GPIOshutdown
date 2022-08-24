#! /usr/bin/python3
#
# GPIOshutdown.py:
#
# Monitor the state of a GPIO pin and initiate a shutdown if the pin is pulled low.
# Upon starting this script, delay for ARMING_DELAY seconds before beginning the
# monitoring action.  If the script is run via a service, this is a failsafe in case
# the GPIO malfunctions or is accidentally shorted, giving the user time to login
# and stop the service.

import RPi.GPIO as GPIO
import time
from os import _exit
import sys
import subprocess

SHUTDOWN_PIN = 26
ARMING_DELAY = 180

GPIO.setmode(GPIO.BOARD)
GPIO.setup(SHUTDOWN_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)
print(f'{time.ctime()}: GPIOshutdown arming on pin {SHUTDOWN_PIN} in {ARMING_DELAY} seconds...')
sys.stdout.flush()
time.sleep(ARMING_DELAY)
print(f'{time.ctime()}: GPIOshutdown armed on pin {SHUTDOWN_PIN}')
sys.stdout.flush()
while True:
    try:
        if not (GPIO.input(SHUTDOWN_PIN)):
            time.sleep(0.5)   # primitive debounce
            if not (GPIO.input(SHUTDOWN_PIN)):
                print(f'{time.ctime()}: GPIO pin {SHUTDOWN_PIN} is low -- initiating shutdown' )
                sys.stdout.flush()
                time.sleep(2)
                subprocess.call("sleep 5; shutdown -h now &", shell=True)
                time.sleep(60)
    except:
        print(f'Exception in GPIOshutdown.  Quitting...')
        sys.stdout.flush()
        break
