#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 29 21:42:09 2020

@author: pi
"""

#import controlLib
import time
from threading import Timer
#f = controlLib.commandParser()

#def input_with_timeout(x):
    
def time_up():
    print("Time up,try again")
    
    
#    t = Timer(x,time_up)
#    try:
#        t.start()
#        b = raw_input("Which floor?")
#    except Exception:
#        print("really")
#        b = None

        
#    if b != True:
#        t.cancel()
        
#input_with_timeout(3)

t1 = Timer(5,raw_input("type something"))
try:
    t1.start()
except:
    time_up()
    t1.cancel()
#while True:
#    a = raw_input("\nWhat is the command phrase?\n")
#    f.checkTrig(a)
#    recInp = 0
#    if f.trigReceived:
#        timeout = time.time() + 10.0
#        while ((time.time() < timeout) or recInp == 0):
#            b = raw_input("\nWhich floor?\n")
#            recInp = 1
#        if recInp:
#            f.checkFloor(b)
#        else:
#            print("Say the floor within 10 sec")
#            f.triggerIndicatorOFF()
#    else:
#        print("Incorrect Command try again\n")