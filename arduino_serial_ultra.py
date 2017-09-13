import serial #Import Serial Library
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
int greenLed = 11
int yellowLed = 12
int redLed = 13
int buzzLed = 15
GPIO.setup(greenLed, GPIO.OUT)
GPIO.setup(yellowLed, GPIO.OUT)
GPIO.setup(redLed, GPIO.OUT)
GPIO.setup(buzzLed, GPIO.OUT)

arduinoSerialData = serial.Serial('com3',9600) #Create Serial port object called arduinoSerialData

while (1==1):
    if (arduinoSerialData.inWaiting()>0):
        myData = arduinoSerialData.readline()
        print(myData)
		distance = float(myData)
		
		if distance < 50:
		
		
		
