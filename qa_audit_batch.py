#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Created on Sat Oct 31 03:52:14 2020

@author: virag
"""

# import libraries
import speech_recognition as sr
import pandas as pd
import os

def parse_audio(filename):
    r = sr.Recognizer()
    sample_audio = sr.AudioFile(filename)
    print ("Capturing audio for processing . . \n")
    with sample_audio as source:
        audio = r.record(source)
    output = r.recognize_google(audio)
    return output

# print transcript on screen for further processing
def generate_transcript():
	print ("Audio file contents: ")
	print (output)
	print ("----")

# analyze transcipt
def qa_check_recording(output):
    if "recorded" and "monitoring" in output:
        print ("Recording disclaimer pass")
        print ("----")
        return "pass"
    else:
        print ("Recording disclaimer fail")
        print ("----")
        return "fail"
    
def qa_check_pricing(output):
    if "prices" and "subject" and "change" in output:
        print ("Pricing disclaimer pass")
        print ("----")
        return "pass"
    else:
        print ("Pricing disclaimer fail")
        print ("----")
        return "fail"

# scan folder for all audio files


# set up speech regonition object and parse audio file

def main():
    filelist = os.listdir("/home/virag/Documents/speech/batchfile")
    df = pd.DataFrame(columns=["fileid", "qa_check1","qa_check2"])
    for i in range(len(filelist)):
        if "wav" in filelist[i]:
            output = parse_audio(filelist[i])
            generate_transcript(output)
            qa_check1 = qa_check_recording(output)
            qa_check2 = qa_check_pricing(output)
            df.loc[i] = [filelist[i], qa_check1, qa_check2]
        else:
            continue
    df.to_excel("qa_check_report.xlsx")

if __name__ == "__main__":
	main()