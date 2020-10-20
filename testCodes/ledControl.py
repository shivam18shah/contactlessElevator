# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
# necessary to control the GPIO pins
import RPi.GPIO as GPIO
import time
GPIO.setwarnings(False)
# Using BCM pinout for RaspberryPi. Other option is BOARD pinout.
GPIO.setmode(GPIO.BCM)
# Setting the GPIO pi 21 as output pin
GPIO.setup(21,GPIO.OUT)
#status= input("Press 1 to turn on . Press 0 to turn off")
#if (status == '1'):

#Set GPIO output to high for on and low for off
#if you connect the pin to anode of the led
#other wise reverse connection
#Always connect led in series with led to limit current to avoid boom.
print("Led on")
GPIO.output(21,GPIO.HIGH)
time.sleep(1)
print("Led off")
GPIO.output(21,GPIO.LOW)
time.sleep(1)
GPIO.cleanup()
