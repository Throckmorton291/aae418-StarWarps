import RPi.GPIO as GPIO
import time

#Defines pinout as actual pin numbers and not Broadcom SOC pin numbers
GPIO.setmode(GPIO.BOARD)

#Pin definitions
led = 37
actuator = 33

#Set up pins as outputs
GPIO.setup(led,GPIO.OUT)
GPIO.setup(actuator,GPIO.OUT)

#Turn on the LED
GPIO.output(led,True)

#Run the linear actuator
GPIO.output(actuator,True)
time.sleep(1)
GPIO.output(actuator,False)
