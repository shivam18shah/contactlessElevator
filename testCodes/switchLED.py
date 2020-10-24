#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 12 12:25:07 2020

@author: pi
"""
# =============================================================================
# Code for controlling the LED using button switch
# =============================================================================

# necessary to control the GPIO pins
import RPi.GPIO as GPIO
import time
GPIO.setwarnings(False)
# Using BCM pinout for RaspberryPi. Other option is BOARD pinout.
GPIO.setmode(GPIO.BCM)
# Setting the GPIO pin 21 as output pin
GPIO.setup(21,GPIO.OUT)
# Setting the GPIO pin 20 as input pin
GPIO.setup(20,GPIO.IN)

#Set GPIO output to high for on and low for off
#if you connect the pin to anode of the led
#other wise reverse connection
#Always connect led in series with led to limit current to avoid boom.

#Infinite loop to keep code running forever. Press Ctrl+C to stop
while True:
#    if (GPIO.input(20)):
#        print("Led on")
#        GPIO.output(21,GPIO.input(20))
#        time.sleep(0.05)
#    else:
#        print("Led off")
#        GPIO.output(21,GPIO.input(20))
#        time.sleep(0.05)

# =============================================================================
# One line code to control led usig switch (Cannot print status on terminal)
# =============================================================================
        GPIO.output(21,GPIO.input(20))
        
# =============================================================================
# Code for printing status of switch without led control        
# =============================================================================
#    if(GPIO.input(20)):
#        print("pressed")
#        time.sleep(1)
#    else:
#        print("not pressed")
#        time.sleep(1)

        