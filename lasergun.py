from time import sleep
from time import time
import RPi.GPIO as GPIO

#Setting stuff up
leds = [24, 23, 22, 21, 18, 17]
buttons = [25, 4]

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

for pin in leds:
    GPIO.setup(pin, GPIO.OUT)

for pin in buttons:
    GPIO.setup(pin, GPIO.IN)
########################################
    
def allLeds(onOrOff):
    for pin in leds:
        GPIO.output(pin, onOrOff)

def check():
    for i in range(2):
        allLeds(True)
        sleep(0.1)
        allLeds(False)
        sleep(0.1)

def setDelay():
    start = time()
    print "Setting delay"
    while GPIO.input(buttons[1]) == 1:
        sleep(0.05)
        if time() - start > 2:
            check()
            print "Bye!"
            exit(0)
    newDelay = time() - start
    print "New delay:", newDelay
    return newDelay


#This one works awesomely
def push(array, time):
    cycleTime = time / 12.0
    for pin in array:
        GPIO.output(pin, True)
        sleep(cycleTime)
    for pin in array:
        GPIO.output(pin, False)
        sleep(cycleTime)

def go():
    duration = 1

    while True:
        sleep(0.05)
        #sleep(1)
        #print "Button says", GPIO.input(button)
        if GPIO.input(buttons[0]) == 1:
            push(leds, duration)
        elif GPIO.input(buttons[1]) == 1:
            duration = setDelay()

print "Hello!"
check()
go()