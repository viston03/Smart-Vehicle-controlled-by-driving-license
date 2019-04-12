import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522

def read():

	reader = SimpleMFRC522()

	try:
		print('Please Scan your Licence.....')

		id, text = reader.read()
		print(id,"Welcome")

	finally:

		GPIO.cleanup()
	return text
