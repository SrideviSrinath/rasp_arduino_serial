import serial #Import Serial Library
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
#int greenLed = 11
#int yellowLed = 12
#int redLed = 13
#int buzzLed = 15
GPIO.setup(11, GPIO.OUT)
GPIO.setup(12, GPIO.OUT)
GPIO.setup(13, GPIO.OUT)
GPIO.setup(15, GPIO.OUT)

arduinoSerialData = serial.Serial('/dev/ttyACM0',9600) #Create Serial port object called arduinoSerialData

while (1==1):
    if (arduinoSerialData.inWaiting()>0):
        myData = arduinoSerialData.readline()
        print(myData)
	distance = float(myData)
	if distance < 50:
            print("the distance is less than 50")
            GPIO.output(11, GPIO.HIGH)
        else:
            GPIO.output(11, GPIO.LOW)
        if distance < 20:
            print("the distance is less than 20")
            GPIO.output(12, GPIO.HIGH)
        else:
            GPIO.output(12, GPIO.LOW)
        if distance < 5:
            print("the distance is less than 5")
            GPIO.output(13, GPIO.HIGH)
        else:
            GPIO.output(13, GPIO.LOW)
        if (distance > 5 or distance <= 0):
            print("out of range")
            GPIO.output(15, GPIO.LOW)
        else:
            print("the distance is: {} cm".format(distance))
            GPIO.output(15, GPIO.HIGH)
        
		
		
		
