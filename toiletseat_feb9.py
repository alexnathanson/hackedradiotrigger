#! Beagle Bone Black
#!/usr/bin/python

import Adafruit_BBIO.GPIO as GPIO
import time
import pygame


pygame.init()

GPIO.setup("P8_11", GPIO.IN)

flag = 0
alertTime = 0
downTime = 0
ss = 0
pygame.mixer.music.load('alarmsound.wav')


def recordEvent (ss):
	#!record seat state data
        seat = open("seatstate.txt","a+")
        seat.write(time.strftime("%d/%m/%Y"))
        seat.write(" ")
        seat.write (time.strftime("%H:%M:%S"))
        seat.write(" ")

	if ss == 1:
                seat.write("The seat is up \n")
		print "It's up"
                time.sleep(.01)
	elif ss == 0:
                seat.write("The seat is down \n")
                print "It's down"
                seat.close()
                time.sleep(.01)
	return;

def makeNoise():
	#! do stuff to make noise
	pygame.mixer.music.play(0)
	return;

while True:
	
	#! if button is pressed (radio message send every 7 seconds from Trinket)
	if GPIO.input("P8_11"):
		#!test it
		print "yes"
		if flag == 0:
			makeNoise()
			flag = 1
			 #!record seat state data
                        recordEvent(1)
			alertTime = time.time() + 7
			downTime = time.time() + 9
		else:
			if time.time() >= alertTime:
				makeNoise()
				#!record seat state data
            			recordEvent(1)				
				alertTime = time.time() + 7
				downTime = time.time() + 9
	elif flag == 1:
		if time.time() > downTime:
			flag = 0
			pygame.mixer.music.stop()
			recordEvent(0)
