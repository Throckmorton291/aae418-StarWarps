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

#Set frequency on PWM pin
actuatorPWM = GPIO.PWM(actuator,1000)

#Start PWM duty cycle at 0
actuatorPWM.start(0)

#Turn on the LED
GPIO.output(led,True)

#Run the linear actuator

#Change the PWM duty cycle to control motor
pi_pwm.ChangeDutyCycle(10)
time.sleep(0.5)
pi_pwm.ChangeDutyCycle(50)
time.sleep(1)
