#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 22 19:13:52 2020

@author: pi
"""

import re
import time
import RPi.GPIO as GPIO

GPIO.setwarnings(False)
# Using BCM pinout for RaspberryPi. Other option is BOARD pinout.
GPIO.setmode(GPIO.BCM)
# Setting the GPIO pin 26 as output pin (Yellow LED)
GPIO.setup(26,GPIO.OUT)

#Function to generate control signal for floor 1
def triggerCommand():
    print("Trigger command received")
    GPIO.output(26,GPIO.HIGH)
    time.sleep(5)
    GPIO.output(26,GPIO.LOW)
    time.sleep(2)

#Testing different inputs from a text file
c1=r"[okay|ok|hey]\s*elevator"

f = open('commandTest.txt', 'r')
for lines in f:
#    print(lines.lower())
    if re.search(c1,lines,re.IGNORECASE):
        triggerCommand()
    else:
        print("Wrong Input")        
f.close()


GPIO.cleanup()