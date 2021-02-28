#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 12 16:52:56 2020

@author: pi
"""
# =============================================================================
# Contolling the led using commandline inputs
# =============================================================================

import RPi.GPIO as GPIO
import time
import logging
GPIO.setwarnings(False)
# Using BCM pinout for RaspberryPi. Other option is BOARD pinout.
GPIO.setmode(GPIO.BCM)
# Setting the GPIO pin 21 as output pin (Green LED)
GPIO.setup(21,GPIO.OUT)
# Setting the GPIO pin 20 as output pin (Red LED)
GPIO.setup(20,GPIO.OUT)
# Setting the GPIO pin 26 as output pin (Yellow LED)
GPIO.setup(26,GPIO.OUT)
# Setting the GPIO pin 19 as output pin (White LED)
GPIO.setup(19,GPIO.OUT)


# =============================================================================
# Control part of the commandline input
# =============================================================================

while True:
    cS = raw_input("Enter a character to control the leds \n G -> green on g -> green off \n R -> red on  r -> red off \n Y -> yellow on  y-> yellow off \n W -> white on  w -> white off\n")
    if(cS == 'G'):
        GPIO.output(21,GPIO.HIGH)
    elif(cS == 'g'):
        GPIO.output(21,GPIO.LOW)
    elif(cS == 'R'):
        GPIO.output(20,GPIO.HIGH)
    elif(cS == 'r'):
        GPIO.output(20,GPIO.LOW)
    elif(cS == 'Y'):
        GPIO.output(26,GPIO.HIGH)
    elif(cS == 'y'):
        GPIO.output(26,GPIO.LOW)
    elif(cS == 'W'):
        GPIO.output(19,GPIO.HIGH)
    elif(cS == 'w'):
        GPIO.output(19,GPIO.LOW)
    else:
        logging.error('Incorrect input please select again')
        # print("Incorrect input please select again")
#        