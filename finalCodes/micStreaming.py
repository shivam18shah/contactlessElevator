#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Jan  4 13:07:17 2021

@author: pi
"""

# =============================================================================
# Python code for main lib and running the code
# =============================================================================

#Import libraries for all the dependencies
from vosk import Model, KaldiRecognizer
import pyaudio
import controlLib
import RPi.GPIO as GPIO
import os
import logging

#Class declaration for OOPM inheritance and usage in main code
class micAudio(controlLib.controlCommands):
# Can be changed during class object declaration   
    def __init__(self,modelRate=16000,sampleRate=16000,bufferSize=24000,readRate=4000):
        super().__init__(self)
        self.mrate = modelRate
        self.srate = sampleRate
        self.buffsize = bufferSize
        self.rrate = readRate
        self.strmdata = ""
        
# Function to initialize the speech to text stream device and ML Model
    def initModel(self):
        model = Model("model")
        rec = KaldiRecognizer(model, 16000)
        p = pyaudio.PyAudio()
        stream = p.open(format=pyaudio.paInt16, channels=1, rate=16000, input=True, frames_per_buffer=24000)
        return rec,stream
    
# Function to start speech to text model to get text output     
    def runModel(self):
        rec,stream = self.initModel()
        stream.start_stream()
        while True:
            try:
                data = stream.read(4000,exception_on_overflow = False)
                if rec.AcceptWaveform(data):
                    self.strmdata = rec.Result()
                    logging.info(self.strmdata)
                    # print(self.strmdata)
                    self.checkTrig(self.strmdata)
                    self.checkFloor(self.strmdata)
                else:
                    pass
            except:
                stream.stop_stream()
                # print("Stream Stopped")
                logging.exception('Stream stopped')


    def getPID(self):
        f = open ("pidNo.txt",'w')
        pidNo = str(os.getpid())
        print(pidNo)
        f.write(pidNo)
        f.close


if __name__ == '__main__':
    try:
        logging.info('Process pid is: ', os.getpid())
        # print("Process pid is",os.getpid())
        x = micAudio(16000,16000,24000,4000)
        x.getPID()
        x.runModel()
    except KeyboardInterrupt:
        logging.exception('Stopping code execution')
        # print("Stopping code execution")
        logging.info('Restart the script')
        # print("Restart the script")   
        GPIO.cleanup()
