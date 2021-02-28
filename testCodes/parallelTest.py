#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Jan  2 15:54:29 2021

@author: pi
"""

import threading
import time
import logging

class sharing(object):

    def __init__(self):
        self.a = 0
        self.b = 0 
       
    def test_func1(self):
        while True:
            self.a = self.a + 1
            print ("value of a is",self.a)
            time.sleep(1)

    
    def test_func2(self):
        while True:

            if (self.a % 5 == 0):
                self.b+=1
                print ("value of b is",self.b)
            time.sleep(1)

if __name__ == '__main__':
    try:
        x = sharing()
        p1=threading.Thread(target=x.test_func1)
        p2=threading.Thread(target=x.test_func2)
        p1.start()
        p2.start()
        p1.join()
        p2.join()
    except KeyboardInterrupt:
        # print("Stopping code execution")
        logging.exception('Stopping code execution')

# =============================================================================
# https://stackoverflow.com/questions/11436502/closing-all-threads-with-a-keyboard-interrupt
#        For controlling infinite loop execution and closing threads
# =============================================================================
