#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 29 18:55:42 2020

@author: pi
"""

# =============================================================================
# Python lib for capturing commands and generating control signals
# =============================================================================


import re
import time
import RPi.GPIO as GPIO
import logging
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

class commandParser:
    

#Instead of separate floors as variables we can use lookup dict of premade commands    
    def __init__(self):
        self.trigSignal = 21
        self.floor1Signal = 26
        self.floor2Signal = 19
        self.trigCommand = r"(okay|ok|hey|hi)\s*elevator"
        self.floor1Command = r"one|first|1"
        self.floor2Command = r"second|two|2"
        self.trigReceived = 0
        GPIO.setup(self.trigSignal,GPIO.OUT)
        GPIO.setup(self.floor1Signal,GPIO.OUT)
        GPIO.setup(self.floor2Signal,GPIO.OUT)
        
    def firstFloor(self):
        self.triggerIndicatorOFF()
        print("Floor 1 control signal generated")
        GPIO.output(self.floor1Signal,GPIO.HIGH)
        time.sleep(5)
        GPIO.output(self.floor1Signal,GPIO.LOW)
        time.sleep(2)
        
    def secondFloor(self):
        self.triggerIndicatorOFF()
        # print("Floor 2 control signal generated")
        logging.info('Florr 2 control signal generated')
        GPIO.output(self.floor2Signal,GPIO.HIGH)
        time.sleep(5)
        GPIO.output(self.floor2Signal,GPIO.LOW)
        time.sleep(2)
        
    def triggerIndicatorON(self):
        # print("Trigger received, waiting for input")
        logging.info('Trigger received, waiting ')
        GPIO.output(self.trigSignal,GPIO.HIGH)
        
    def triggerIndicatorOFF(self):
        # print("Thanks for input")
        logging.info('Thanks for the input')
        self.trigReceived=0
        GPIO.output(self.trigSignal,GPIO.LOW)

    def checkTrig(self,inp):
        if re.search(self.trigCommand,inp,re.IGNORECASE):
            self.trigReceived=1
            self.triggerIndicatorON()
        else:
            # print("Wrong Input")
            logging.error('Wrong info')
            self.triggerIndicatorOFF()
            
    def checkFloor(self,inp):
        if re.search(self.floor1Command,inp,re.IGNORECASE):
            self.firstFloor()
        elif re.search(self.floor2Command,inp,re.IGNORECASE):
            self.secondFloor()          
        else:
            # print("Wrong Floor Input")
            logging.error('Invalid floor input')
            self.triggerIndicatorOFF()
            
            