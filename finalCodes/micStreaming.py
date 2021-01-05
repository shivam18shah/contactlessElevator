#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Jan  4 13:07:17 2021

@author: pi
"""

from vosk import Model, KaldiRecognizer
#import os
import pyaudio
import controlLib
import RPi.GPIO as GPIO
import time

class micAudio(controlLib.controlCommands):
    
    def __init__(self,modelRate=16000,sampleRate=16000,bufferSize=24000,readRate=4000):
        super().__init__(self)
        self.mrate = modelRate
        self.srate = sampleRate
        self.buffsize = bufferSize
        self.rrate = readRate
        self.strmdata = ""
        
    def initModel(self):
        model = Model("model")
        rec = KaldiRecognizer(model, 16000)
        p = pyaudio.PyAudio()
        stream = p.open(format=pyaudio.paInt16, channels=1, rate=16000, input=True, frames_per_buffer=24000)
        return rec,stream
    
    def runModel(self):
        rec,stream = self.initModel()
        stream.start_stream()
        while True:
            try:
                data = stream.read(16000,exception_on_overflow = False)
#                if len(data) == 0:
#                    break
                if rec.AcceptWaveform(data):
                    self.strmdata = rec.Result()
#                    print(self.strmdata)
                    self.checkTrig(self.strmdata)
#                    print(self.trigReceived)
#                    time.sleep(1)
                    self.checkFloor(self.strmdata)
            #        a = rec.Result()
            #        if re.search(substring1, a, re.IGNORECASE) or re.search(substring2,a, re.IGNORECASE) or re.search(substring3,a, re.IGNORECASE):
            #            print(a)
                else:
                    pass
#                    print(rec.PartialResult())
            except:
                stream.stop_stream()
#                self.runModel()
                print("Stream Stopped")
#
if __name__ == '__main__':
    try:
        x = micAudio(16000,16000,24000,4000)
        x.runModel()
    except KeyboardInterrupt:
        print("Stopping code execution")
        print("Restart the script")   
        GPIO.cleanup()
