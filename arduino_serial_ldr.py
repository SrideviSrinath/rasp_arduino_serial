import serial #Import Serial Library
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)
ldrPin = 11
GPIO.setup(ldrPin, GPIO.OUT)
arduinoSerialData = serial.Serial('/dev/ttyACM0',9600) #Create Serial port object called arduinoSerialData

while (1==1):
    if (arduinoSerialData.inWaiting()>0):
        myData = arduinoSerialData.readline()
        data = float(myData)
        if data < 800:
            print("the output is less than 800: {}".format(data))
            GPIO.output(11, GPIO.HIGH)
        else:
            print("the output is greater than 800: {}".format(data))
            GPIO.output(11, GPIO.LOW)
