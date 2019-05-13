import RPi.GPIO as GPIO
import time
import sys

ledRed = 10
ledGreen = 17
ledOrange = 22

GPIO.setmode(GPIO.BCM)
GPIO.setwarning(False)

GPIO.setup(ledRed, GPIO.OUT)
GPIO.output(ledRed, GPIO.LOW)
GPIO.setup(ledGreen, GPIO.OUT)
GPIO.output(ledGreen, GPIO.LOW)
GPIO.setup(ledOrange, GPIO.OUT)
GPIO.output(ledOrange, GPIO.LOW)

try:
    while true:
        print("TrafficLight: Green")
        GPIO.output(ledGreen, GPIO.HIGH)

        time.sleep(10)

        print("TrafficLight: Orange")
        GPIO.output(ledGreen, GPIO.LOW)
        GPIO.output(ledOrange, GPIO.HIGH)

        time.sleep(2)

        print("TrafficLight: Red")
        GPIO.output(ledOrange, GPIO.LOW)
        GPIO.output(ledRed, GPIO.HIGH)

        time.sleep(10)

        GPIO.output(ledRed, GPIO.LOW)

except KeyboardInterrupt:
    GPIO.cleanup()
    sys.exit(0)
