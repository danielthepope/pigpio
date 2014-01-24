from time import sleep
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.OUT)

for i in range(5):
	GPIO.output(17, True)
	sleep(0.5)
	GPIO.output(17, False)
	sleep(0.5)

