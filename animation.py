from time import sleep
from time import time
import RPi.GPIO as GPIO

#Setting stuff up
leds = [24, 23, 22, 21, 18, 17]
buttons = [25, 4]

sample = []
sample.append([[leds[0],0.6],[leds[1],0],[leds[2],0],[leds[3],0],[leds[4],0],[leds[5],0.200000000000001]])
sample.append([[leds[0],0.55],[leds[1],1],[leds[2],0],[leds[3],0],[leds[4],0],[leds[5],0.150000000000001]])
sample.append([[leds[0],0.5],[leds[1],0.5],[leds[2],1],[leds[3],0],[leds[4],0],[leds[5],0.100000000000001]])
sample.append([[leds[0],0.45],[leds[1],0.2],[leds[2],0.5],[leds[3],1],[leds[4],0],[leds[5],0.0500000000000009]])
sample.append([[leds[0],0.4],[leds[1],0],[leds[2],0.2],[leds[3],0.5],[leds[4],1],[leds[5],0]])
sample.append([[leds[0],0.35],[leds[1],0],[leds[2],0],[leds[3],0.2],[leds[4],0.5],[leds[5],0]])
sample.append([[leds[0],0.3],[leds[1],0],[leds[2],0],[leds[3],0],[leds[4],0.2],[leds[5],0]])
sample.append([[leds[0],0.25],[leds[1],0],[leds[2],0],[leds[3],0],[leds[4],0],[leds[5],0]])
sample.append([[leds[0],0.200000000000001],[leds[1],0],[leds[2],0],[leds[3],0],[leds[4],0],[leds[5],0.6]])
sample.append([[leds[0],0.150000000000001],[leds[1],0],[leds[2],0],[leds[3],0],[leds[4],1],[leds[5],0.55]])
sample.append([[leds[0],0.100000000000001],[leds[1],0],[leds[2],0],[leds[3],1],[leds[4],0.5],[leds[5],0.5]])
sample.append([[leds[0],0.0500000000000009],[leds[1],0],[leds[2],1],[leds[3],0.5],[leds[4],0.25],[leds[5],0.45]])
sample.append([[leds[0],0],[leds[1],1],[leds[2],0.5],[leds[3],0.25],[leds[4],0],[leds[5],0.4]])
sample.append([[leds[0],0],[leds[1],0.5],[leds[2],0.25],[leds[3],0],[leds[4],0],[leds[5],0.35]])
sample.append([[leds[0],0],[leds[1],0.25],[leds[2],0],[leds[3],0],[leds[4],0],[leds[5],0.3]])
sample.append([[leds[0],0],[leds[1],0],[leds[2],0],[leds[3],0],[leds[4],0],[leds[5],0.25]])


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
    for i in range(cycles):
        allLeds(True)
        for l in range(5):
            GPIO.output(artup[l][0], False)
            sleep(delays[l])
        GPIO.output(artup[5][0], False)
        sleep((1-artup[-1][1]) / 100.0)
                        
def animate(duration):
    frameTime = duration / float(len(sample))
    print 1.0 / frameTime, "fps"
    while True:
        for step in sample:
            varyBrightness(step, frameTime)

animate(1)