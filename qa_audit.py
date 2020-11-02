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
	with sample_audio as source:
		audio = r.record(source)
	output = r.recognize_google(audio)
	return output

# print transcript on screen for further processing
def generate_transcript():
	transcript = parse_audio()
	print ("Audio file contents: ")
	print (transcript)
	print ("----")

# analyze transciption
def qa_check():
    output = parse_audio()
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
	generate_transcript()
	qa_check()
	
if __name__ == "__main__":
	main()
