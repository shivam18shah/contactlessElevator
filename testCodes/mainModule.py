#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Jan  4 16:41:26 2021

@author: pi
"""

import micStreaming
import controlLib
import threading
import time


class mainModule(micStreaming.micAudio,controlLib.controlCommands):
    
    def __init__(self):
        super().__init__(self)
        self.audioData = ""
        
    def micStrmFunc (self):
        self.runModel()
        
    def tempFunc(self):
        while True:
            print("string in audio is",self.strmdata)
            time.sleep(1)


if __name__ == '__main__':
    try:
        x = mainModule()
        p1=threading.Thread(target=x.micStrmFunc)
#        p2=threading.Thread(target=x.tempFunc)
        p1.start()
#        p2.start()
        p1.join()
#        p2.join()
    except KeyboardInterrupt:
        print("Stopping code execution")
        print("Restart the script")        