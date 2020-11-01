#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Created on Sat Oct 31 03:52:14 2020

@author: virag
"""

# import libraries
import speech_recognition as sr

# set up speech regonition object and parse audio file
r = sr.Recognizer()
sample_audio = sr.AudioFile("disclaimer_no.wav")
with sample_audio as source:
	audio = r.record(source)
output = r.recognize_google(audio)
print ("Audio file contents: ")
print (output)

# analyze transciption 
if "recorded" in output and "monitoring" in output:
    print ("QA check pass")
else:
    print ("QA check fail")
