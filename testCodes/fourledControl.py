#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 12 15:40:08 2020

@author: pi
"""
# =============================================================================
# Controlling 4 leds on 4 different GPIOs
# =============================================================================

import RPi.GPIO as GPIO
import time
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
# Controlling the leds one after the other
# =============================================================================

#Green On
GPIO.output(21,GPIO.HIGH)
time.sleep(2)

#Red on
GPIO.output(20,GPIO.HIGH)
time.sleep(2)

#Yelow on
GPIO.output(26,GPIO.HIGH)
time.sleep(2)

#White on
GPIO.output(19,GPIO.HIGH)
time.sleep(2)

#Green Off
GPIO.output(21,GPIO.LOW)
time.sleep(2)

#Red Off
GPIO.output(20,GPIO.LOW)
time.sleep(2)

#Yellow Off
GPIO.output(26,GPIO.LOW)
time.sleep(2)
#White off
GPIO.output(19,GPIO.LOW)
time.sleep(2)

GPIO.cleanup()