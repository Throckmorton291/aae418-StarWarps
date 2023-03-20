import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)

led =  8
GPIO.setup(led,GPIO.OUT)

