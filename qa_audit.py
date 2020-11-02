#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Created on Sat Oct 31 03:52:14 2020

@author: virag
"""

# import libraries
import speech_recognition as sr

# set up speech regonition object and parse audio file
def parse_audio():
    r = sr.Recognizer()
    sample_audio = sr.AudioFile("disclaimer_yes.wav")
    print ("Capturing audio for processing . . \n")
    with sample_audio as source:
        audio = r.record(source)
    global output
    output = r.recognize_google(audio)
    return output

# print transcript on screen for further processing
def generate_transcript():
	print ("Audio file contents: ")
	print (output)
	print ("----")

# analyze transcipt
def qa_check():
    if "recorded" and "monitoring" in output:
        print ("Recording disclaimer pass")
        print ("----")
    else:
        print ("Recording disclaimer fail")
        print ("----")
    
    if "prices" and "subject" and "change" in output:
        print ("Pricing disclaimer pass")
        print ("----")
    else:
        print ("Pricing disclaimer fail")
        print ("----")

def main():
	parse_audio()
	generate_transcript()
	qa_check()
	
if __name__ == "__main__":
	main()
