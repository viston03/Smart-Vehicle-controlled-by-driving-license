import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522

def write():

	reader = SimpleMFRC522()

	try:
		l1 = []
		text = input('Enter Driving Licence Number for new entry: ')
		l1.append(text)
		print('Now place your Licence to write......')
		reader.write(text)
		print('Data Successfully Written....')

	finally:
		GPIO.cleanup()
	return l1
