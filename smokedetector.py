from gpiozero import LED
import RPi.GPIO as GPIO
import time

#GPIO Setup
channel = 21
GPIO.setmode(GPIO.BCM)
GPIO.setup(channel, GPIO.IN)

#LED Setup
led = LED(18)

def callback(channel):
    if GPIO.input(channel):
        print("GAS has been detected")
        led.on()
        time.sleep(5)
        led.off()
        
GPIO.add_event_detect(channel, GPIO.RISING, bouncetime=3) #Detects a change in value on Pin 21
GPIO.add_event_callback(channel, callback) #assigns function to pin 21 and runs function

#forever loop
while True:
    time.sleep(0.5)
