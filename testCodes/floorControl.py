#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 21 19:27:03 2020

@author: pi
"""

import re
import time
import RPi.GPIO as GPIO
GPIO.setwarnings(False)
# Using BCM pinout for RaspberryPi. Other option is BOARD pinout.
GPIO.setmode(GPIO.BCM)
# Setting the GPIO pin 21 as output pin (Green LED)
GPIO.setup(21,GPIO.OUT)
# Setting the GPIO pin 19 as output pin (White LED)
GPIO.setup(19,GPIO.OUT)


#Function to generate control signal for floor 1
def firstFloor():
    print("Taking elevator to first floor")
    GPIO.output(19,GPIO.HIGH)
    time.sleep(5)
    GPIO.output(19,GPIO.LOW)
    
#Function to generate control signal for floor 2
def secondFloor():
    print("Taking elevator to second floor")
    GPIO.output(21,GPIO.HIGH)
    time.sleep(5)
    GPIO.output(21,GPIO.LOW)


#Testing different inputs from a text file
m1=r"one|first|1"
m2=r"second|two|2"
f = open('testIP.txt', 'r')
for lines in f:
#    print(lines.lower())
    if re.search(m1,lines,re.IGNORECASE):
        firstFloor()
    elif re.search(m2,lines,re.IGNORECASE):
        secondFloor()
    else:
        print("Wrong Input")        
f.close()


GPIO.cleanup()