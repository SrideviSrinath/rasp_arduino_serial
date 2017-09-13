import serial #Import Serial Library

arduinoSerialData = serial.Serial('com3',9600) #Create Serial port object called arduinoSerialData


while (1==1):
    if (arduinoSerialData.inWaiting()>0):
        myData = arduinoSerialData.readline() #string value
        print(myData)
		
		fahrValue = float(myData)
		fahrenheit = ((fahrValue*9)/5 + 32)
		print(fahrenheit)
		
		
		
