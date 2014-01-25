from time import sleep
import RPi.GPIO as GPIO

red = 17
green = 18
blue = 21

GPIO.setmode(GPIO.BCM)
GPIO.setup(red, GPIO.OUT)
GPIO.setup(green, GPIO.OUT)
GPIO.setup(blue, GPIO.OUT)

def white(duration):
        GPIO.output(red, True)
        GPIO.output(green, True)
        GPIO.output(blue, True)
        sleep(duration)
        GPIO.output(red, False)
        GPIO.output(green, False)
        GPIO.output(blue, False)

        
def multicolours(duration, r, g, b):
	cycles = int(duration * 100)
	ron = r / 100.0
	gon = g / 100.0
	bon = b / 100.0
	roff = 0.01 - ron
	goff = 0.01 - gon
	boff = 0.01 - bon
	for i in range(cycles):
		GPIO.output(red, True)
		GPIO.output(green, True)
		GPIO.output(blue, True)
		sleep(ron)
		GPIO.output(red, False)
		GPIO.output(green, False)
		GPIO.output(blue, False)
		sleep(roff)

# duration in seconds, brightness from 0 to 1
def lighton(led, duration, brightness):
	cycles = int(duration * 100)
	ontime = (brightness ** 2) / 100.0
	offtime = 0.01 - ontime
	for i in range(cycles):
		GPIO.output(led, True)
		sleep(ontime)
		GPIO.output(led, False)
		sleep(offtime)

def on(duration, ontime, offtime):
	for i in range(duration):
		GPIO.output(17, True)
		sleep(ontime)
		GPIO.output(17, False)
		sleep(offtime)

print "Hello Kieran"

for i in range(100):
	lighton(red, 0.02, i / 100.0)

for i in range(100):
	lighton(blue, 0.02, 1.0 - (i / 100.0))

#multicolours(0.5,1,1,1)

print "Goodbye Kieran"
