#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 29 18:55:42 2020

@author: pi
"""

# =============================================================================
# Python lib for capturing commands and generating control signals
# =============================================================================

#Import libraries for all the dependencies
import re
import time
import RPi.GPIO as GPIO
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

#Class declaration for OOPM inheritance and usage in main code
class controlCommands(object):
    

#Instead of separate floors as variables we can use lookup dict of premade commands    
    def __init__(self,indicator=19,floor1=21,floor2=20):
        self.trigSignal = 20
        self.floor1Signal = 21
        self.floor2Signal = 19
        self.trigCommand = r"(okay|ok|hey)\s*(elevator|later)"
        self.floor1Command = r"(one|first|1)\s*floor"
        self.floor2Command = r"(second|two|2)\s*floor"
        self.trigReceived = 0
        GPIO.setup(self.trigSignal,GPIO.OUT)
        GPIO.setup(self.floor1Signal,GPIO.OUT)
        GPIO.setup(self.floor2Signal,GPIO.OUT)

# Generate control signal for first floor (change time.sleep value to change the duration of signal)
    def firstFloor(self):
        GPIO.output(self.floor1Signal,GPIO.HIGH)
        time.sleep(2)
        GPIO.output(self.floor1Signal,GPIO.LOW)
        

#Generate control signal for second floor (change time.sleep value to change the duration of signal)
    def secondFloor(self):
        GPIO.output(self.floor2Signal,GPIO.HIGH)
        time.sleep(2)
        GPIO.output(self.floor2Signal,GPIO.LOW)

#Generate control signal for trigger indicator LED on       
    def triggerIndicatorON(self):
        GPIO.output(self.trigSignal,GPIO.HIGH)

#Generate control signal for trigger indicator LED off      
    def triggerIndicatorOFF(self):
        self.trigReceived=0
        GPIO.output(self.trigSignal,GPIO.LOW)

#Check if the trigger command has been read or not
    def checkTrig(self,inp):
        if re.search(self.trigCommand,inp,re.IGNORECASE):
            self.trigReceived=1
            self.triggerIndicatorON()
        else:
            self.triggerIndicatorOFF()

#Check if any floor command has been received or not           
    def checkFloor(self,inp):
        if re.search(self.floor1Command,inp,re.IGNORECASE):
            self.firstFloor()
        if re.search(self.floor2Command,inp,re.IGNORECASE):
            self.secondFloor()          
            
            