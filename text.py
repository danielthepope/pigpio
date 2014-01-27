from time import sleep
from time import time
import RPi.GPIO as GPIO
import sys
import pickle

#Setting stuff up
leds = [24, 23, 22, 21, 18, 17]
buttons = [25, 4]
symbol = {}
execfile("letters.py")

argc = len(sys.argv)
argv = sys.argv


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

#Takes an array of tuples and sets each LED's brightness for a duration
# [(17,0.5),(18,1),...]
def varyBrightness(artup, duration):
    for pin in artup:
        if pin[1] == 1:
            GPIO.output(pin[0], True)
        else:
            GPIO.output(pin[0], False)
    sleep(duration)

def changeSpeed(animation, duration, speed):
    duration /= speed
    frameTime = duration / float(len(animation))
    print 1.0 / frameTime, "fps"
    print duration, "seconds"
    while GPIO.input(buttons[0]) == 1:
        sleep(0.02)
    return frameTime
                        
def animate(sequence, duration):
    animation = []
    for char in sequence:
        animation.extend(symbol[char])
    speed = 1
    frameTime = changeSpeed(animation, duration, speed)
    while True:
        for step in animation:
            if GPIO.input(buttons[0]) == 1:
                if speed == 1:
                    speed = 0.1
                else:
                    speed = 1
                frameTime = changeSpeed(animation, duration, speed)
            varyBrightness(step, frameTime)
        #sleep(1)

if argc == 1:
    sequence = 'HELLO'
else:
    sequence = ' '.join(argv[1:])

sequence += "                                                     "
animate(sequence, len(sequence) * 0.01)
