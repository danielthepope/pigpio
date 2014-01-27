from time import sleep
from time import time
import RPi.GPIO as GPIO
import sys
import pickle

#Setting stuff up
leds = [24, 23, 22, 21, 18, 17]
buttons = [25, 4]

argc = len(sys.argv)
argv = sys.argv

animation = []

sample = []
sample.append([[leds[0],1],[leds[1],0],[leds[2],0],[leds[3],0],[leds[4],0],[leds[5],0]])
sample.append([[leds[0],0.5],[leds[1],1],[leds[2],0],[leds[3],0],[leds[4],0],[leds[5],0]])
sample.append([[leds[0],0.2],[leds[1],0.5],[leds[2],1],[leds[3],0],[leds[4],0],[leds[5],0]])
sample.append([[leds[0],0],[leds[1],0.2],[leds[2],0.5],[leds[3],1],[leds[4],0],[leds[5],0]])
sample.append([[leds[0],0],[leds[1],0],[leds[2],0.2],[leds[3],0.5],[leds[4],1],[leds[5],0]])
sample.append([[leds[0],0],[leds[1],0],[leds[2],0],[leds[3],0.2],[leds[4],0.5],[leds[5],1]])
sample.append([[leds[0],0],[leds[1],0],[leds[2],0],[leds[3],0],[leds[4],0.2],[leds[5],0.5]])
sample.append([[leds[0],0],[leds[1],0],[leds[2],0],[leds[3],0],[leds[4],0],[leds[5],0.2]])
sample.append([[leds[0],0],[leds[1],0],[leds[2],0],[leds[3],0],[leds[4],0],[leds[5],0]])
sample.append([[leds[0],0],[leds[1],0],[leds[2],0],[leds[3],0],[leds[4],0],[leds[5],1]])
sample.append([[leds[0],0],[leds[1],0],[leds[2],0],[leds[3],0],[leds[4],1],[leds[5],0.5]])
sample.append([[leds[0],0],[leds[1],0],[leds[2],0],[leds[3],1],[leds[4],0.5],[leds[5],0.2]])
sample.append([[leds[0],0],[leds[1],0],[leds[2],1],[leds[3],0.5],[leds[4],0.2],[leds[5],0]])
sample.append([[leds[0],0],[leds[1],1],[leds[2],0.5],[leds[3],0.2],[leds[4],0],[leds[5],0]])
sample.append([[leds[0],1],[leds[1],0.5],[leds[2],0.2],[leds[3],0],[leds[4],0],[leds[5],0]])
sample.append([[leds[0],0.5],[leds[1],0.2],[leds[2],0],[leds[3],0],[leds[4],0],[leds[5],0]])
sample.append([[leds[0],0.2],[leds[1],0],[leds[2],0],[leds[3],0],[leds[4],0],[leds[5],0]])
sample.append([[leds[0],0],[leds[1],0],[leds[2],0],[leds[3],0],[leds[4],0],[leds[5],0]])

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
    #sortedList = sorted(artup, key=lambda tup: tup[1])
    artup.sort(key=lambda tup: tup[1])
    delays = [0,0,0,0,0]
    for i in range(5):
        delays[i] = (artup[i+1][1]**2 - artup[i][1]**2) / 100.0
    cycles = int(duration * 100)
    onLeds = []
    for i in range(cycles):
        for l in range(6):
            if artup[l][1] > 0:
                GPIO.output(artup[l][0], True)
        for l in range(5):
            GPIO.output(artup[l][0], False)
            sleep(delays[l])
        GPIO.output(artup[5][0], False)
        sleep((1-artup[-1][1]) / 100.0)
                        
def animate(sequence, duration):
    frameTime = duration / float(len(sequence))
    print 1.0 / frameTime, "fps"
    while True:
        for step in sequence:
            varyBrightness(step, frameTime)

if argc == 1:
    print 'Sample animation'
    print "To load a different animation, type 'sudo python animation.py *.seq"
    animate(sample, 1)
else:
    if argv[1].endswith('.seq'):
        animation = pickle.load(open(argv[1], "rb"))
        animate(animation, 1)
    else:
        print "Please type a valid *.seq filename"
