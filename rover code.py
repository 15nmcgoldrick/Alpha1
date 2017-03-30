# coding: utf-8
 import  RPi.GPIO as GPIO
 from time import sleep 

 GPIO.setmode (GPIO.BOARD)

 GPIO.setmode(17, GPIO.OUT)
 GPIO.setup(19, GPIO.OUT)
 GPIO.setup(22,GPIO.OUT)
 GPIO.setup(26,GPIO.OUT)
 while True:
 	 
 	      key=input("this will move wheels foward,frlrs we will use ")
 	      
 	       if key == "f":                       #this moves it foward
 	            GPIO.output(17, GPIO.HIGH)
 	            sleep(2)
 	            GPIO.output(17,GPIO.LOW)
 	                           
 	         elif  key =="r":                   #this will make it reverse 
 	             GPIO.output(19, GPIO.HIGH)
 	             sleep(1)
 	             GPIO.output(19, GPIO.LOW)
 	             
 	         elif key =="l":                  #this will make it go left
 	         	GPIO.output(22, GPIO.HIGH)
 	         	sleep(1)
 	         	GPIO.output(22, GPIO.LOW)
 	         	
 	         elif  key == "r":            #this makes it go right
 	          GPIO.output(26, GPIO.HIGH)  
 	          sleep(1)
 	          GPIO.output(26,GPIO.LOW)
 	          
 	         else key == "s":
 	         	GPIO.cleanup()
 	         	print"motors are turing off"
 	         	sleep(1)
 	         	
 	         	#sensor code
import RPi.GPIO as GPIO
import time
GPIO.setwarnings(false)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(22, GPIO.OUT)             # makes pin 22 as an output pin

        while True:
        	GPIO.output(22,1)               #outputs HIGH signal 5v on pin 22
          time.sleep(1)                 #time delay of one second 
          
          GPIO.output(22,0)              #outputs LOW 0v on pin 22
          time.sleep(1)                  #time delay of one second 
