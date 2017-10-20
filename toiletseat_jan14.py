#!/usr/bin/python

import Adafruit_BBIO.GPIO as GPIO
import time


GPIO.setup("P8_11", GPIO.IN)

while True:
	if GPIO.input("P8_11"):
		seat = open("seatstate.txt","a+")
		seat.write(time.strftime("%d/%m/%Y"))
		seat.write(" ")
		seat.write (time.strftime("%H:%M:%S"))
		seat.write(" ")
		seat.write("The seat is up \n")
		while GPIO.input("P8_11"):
			time.sleep(.01)
		seat.write(time.strftime("%d/%m/%Y"))
		seat.write(" ")
		seat.write (time.strftime("%H:%M:%S"))
		seat.write(" ")
		seat.write("The seat is down \n")
		seat.close()
	time.sleep(.01)