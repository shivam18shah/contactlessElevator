#!/usr/bin/env python3

from vosk import Model, KaldiRecognizer
import logging
import os
#import re

if not os.path.exists("model"):
    print ("Please download the model from https://alphacephei.com/vosk/models and unpack as 'model' in the current folder.")
    logging.basicConfig('Model does not exist')
    exit (1)

import pyaudio

#substring1 = "Hey"
#substring2 = "Okay"
#substring3 = "Elevator"

model = Model("model")
rec = KaldiRecognizer(model, 16000)
  
p = pyaudio.PyAudio()
stream = p.open(format=pyaudio.paInt16, channels=1, rate=16000, input=True, frames_per_buffer=24000)
stream.start_stream()

while True:
    data = stream.read(4000)
    if len(data) == 0:
        break
    if rec.AcceptWaveform(data):
        print(rec.Result())
#        a = rec.Result()
#        if re.search(substring1, a, re.IGNORECASE) or re.search(substring2,a, re.IGNORECASE) or re.search(substring3,a, re.IGNORECASE):
#            print(a)
    else:
        print(rec.PartialResult())

print(rec.FinalResult())
