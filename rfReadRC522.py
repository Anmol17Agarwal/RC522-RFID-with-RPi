import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522

reader = SimpleMFRC522()

try:
        id, text = reader.read() #reading id and text
        print(id)
        print(text)
finally:
        GPIO.cleanup() #clear data
