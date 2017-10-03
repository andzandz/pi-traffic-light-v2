# Import the RPi GPIO module so we can control GPIO devices
import RPi.GPIO as GPIO

# These are BOARD pin numberings
red_pin = 12
yellow_pin = 10
green_pin = 8

# Set the pin numbering mode to BOARD (you can also use BCM)
GPIO.setmode(GPIO.BOARD)

# Set up the GPIO pins as OUTPUT so we can control LEDs on them
GPIO.setup(red_pin,GPIO.OUT)
GPIO.setup(yellow_pin,GPIO.OUT)
GPIO.setup(green_pin,GPIO.OUT)

# Some simple traffic light functions, for convenience

def red():
    GPIO.output(red_pin,    True)   # turn red ON
    GPIO.output(yellow_pin, False)  # turn yellow OFF
    GPIO.output(green_pin,  False)  # turn green OFF

def red_yellow():
    GPIO.output(red_pin,    True)
    GPIO.output(yellow_pin, True)
    GPIO.output(green_pin,  False)

def yellow():
    GPIO.output(red_pin,    False)
    GPIO.output(yellow_pin, True)
    GPIO.output(green_pin,  False)
    
def green():
    GPIO.output(red_pin,    False)
    GPIO.output(yellow_pin, False)
    GPIO.output(green_pin,  True)

def cleanup():
    GPIO.cleanup()
