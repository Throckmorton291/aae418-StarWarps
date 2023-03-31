import RPi.GPIO as GPIO
import time

#Defines pinout as actual pin numbers and not Broadcom SOC pin numbers
GPIO.setmode(GPIO.BOARD)

#Pin definitions
led = 37
actuator = 31
PWMpin = 32

#Set up pins as outputs
GPIO.setup(led,GPIO.OUT)
GPIO.setup(actuator,GPIO.OUT)
GPIO.setup(PWMpin,GPIO.OUT)
pi_pwm = GPIO.PWM(PWMpin,1000)

#Start PWM duty cycle
pi_pwm.start(0)

#Turn on the LED
GPIO.output(led,True)
while True:
    for duty in range(0,101,1):
        pi_pwm.ChangeDutyCycle(duty) #provide duty cycle in the range 0-100
        sleep(0.01)
    sleep(0.5)
    
    for duty in range(100,-1,-1):
        pi_pwm.ChangeDutyCycle(duty)
        sleep(0.01)
    sleep(0.5)

#Run the linear actuator
#GPIO.output(actuator,True)
#time.sleep(1)
#GPIO.output(actuator,False)
