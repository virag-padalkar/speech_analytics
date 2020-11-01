#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov  1 20:27:23 2020

@author: virag
"""


import speech_recognition as sr

# obtain audio from the microphone
r = sr.Recognizer()
with sr.Microphone() as source:
    r.adjust_for_ambient_noise(source, duration=1)
    print("Say something!")
    audio = r.listen(source,phrase_time_limit=5)

response = r.recognize_google(audio)
if "switch on" in response:
    print ("Switching on LED")
else:
    print ("incorrect command")
