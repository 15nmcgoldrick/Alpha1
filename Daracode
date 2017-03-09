import RPi.GPIO as GPIO #imports gpio
from time import sleep #imports sleep
import readchar #imports characters

GPIO.setmode(GPIO.BOARD)

GPIO.setup(11, GPIO.OUT)
GPIO.setup(11, GPIO.IN)    #sensor input
GPIO.setup(13, GPIO.OUT) 
GPIO.setup(16, GPIO.OUT) 
GPIO.setup(18, GPIO.OUT)

i=GPIO.input(11)

if i ==0:
  print "all clear"
  
elif i ==1:
  print "WATCH OUT"


while True:

        key=input("Type to control. Use the letters W, S, A and D") #says what letters are being used to control

        if key == "w":                  #forward
            GPIO.output(11, GPIO.HIGH)
            sleep(1)
            GPIO.output(11, GPIO.LOW)

        elif key == "s":                #reverse
            GPIO.output(13, GPIO.HIGH)
            sleep(1)
            GPIO.output(13, GPIO.LOW)

        elif key == "a":                #steers left
            GPIO.output(16, GPIO.HIGH)
            sleep(1)
            GPIO.output(16, GPIO.LOW)
            

        elif key == "d":                #steers right
            GPIO.output(18, GPIO.HIGH)
            sleep(1)
            GPIO.output(18, GPIO.LOW)
        
        elif key == "z":                #quits the program
            GPIO.cleanup()
            print("Motors on safe, exiting.")
            sleep(1)
            break
