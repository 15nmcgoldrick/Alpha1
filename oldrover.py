import RPi.GPIO as GPIO #GPIO Libraries
from time import sleep #Sleep Functions
import readchar

GPIO.setmode(GPIO.BCM) #Setting Up

GPIO.setup(23, GPIO.OUT)#Right Motor Forwards
GPIO.setup(24, GPIO.OUT)# Backwards
GPIO.setup(17, GPIO.OUT)#Left Motor Backwards
GPIO.setup(27, GPIO.OUT)
GPIO.setup(26, GPIO.OUT)
GPIO.setup(16, GPIO.OUT)


print("Welcome to the Awesome Robot!!!")
sleep(2)

while True:

    key=readchar.readkey()

    if key=="1": 
        GPIO.output(17, GPIO.HIGH)
        GPIO.output(24, GPIO.HIGH)
	GPIO.output(16, GPIO.HIGH)
        sleep(0.4)
        GPIO.output(17, GPIO.LOW)
        GPIO.output(24, GPIO.LOW)
	GPIO.output(16, GPIO.LOW)

        
    elif key=="2":
        GPIO.output(17, GPIO.HIGH)
        sleep(0.4)
        GPIO.output(17, GPIO.LOW)

    elif key=="3":
        GPIO.output(24, GPIO.HIGH)
        sleep(0.4)
        GPIO.output(24, GPIO.LOW)
	
    elif key=="4":
        GPIO.output(27, GPIO.HIGH)
        sleep(0.4)
        GPIO.output(27, GPIO.LOW)
	
    elif key=="5":
        GPIO.output(23, GPIO.HIGH)
        sleep(0.4)
        GPIO.output(23, GPIO.LOW)
	        
    elif key=="6":
        GPIO.output(27, GPIO.HIGH)
        GPIO.output(23, GPIO.HIGH)
	GPIO.output(26, GPIO.HIGH)
        sleep(0.4)
        GPIO.output(27, GPIO.LOW)
        GPIO.output(23, GPIO.LOW)
	GPIO.output(26, GPIO.LOW)
	
    elif key=="k": #kamakazie
        GPIO.output(17, GPIO.HIGH)
        GPIO.output(24, GPIO.HIGH)
        sleep(999999999999999999999999999999999999)
        GPIO.output(17, GPIO.LOW)
        GPIO.output(24, GPIO.LOW)

    elif key=="z":
        GPIO.cleanup()
        sleep(1)
        break
