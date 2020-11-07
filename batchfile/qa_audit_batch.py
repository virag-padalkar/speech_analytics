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
import re
from datetime import date

# parse audio file
def parse_audio(filename):
    r = sr.Recognizer()
    sample_audio = sr.AudioFile(filename)
    print ("Capturing audio for processing . . \n")
    with sample_audio as source:
        audio = r.record(source)
    output = r.recognize_google(audio)
    return output

# print transcript on screen for further processing
def generate_transcript(output):
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

def cc_check(output):
    cc_pattern = r"\b(?:\d[ -]*?){13,16}\b"
    cc_result = re.search(cc_pattern, output)
    if cc_result:
        return "fail"
    else:
        return "pass"

# set up speech regonition object and parse audio file
def main():
    audio_path = input("Enter path for audio files (Input ~ for current folder): ")
    if audio_path == "~":
        filelist = os.listdir(os.getcwd())
    else: 
        filelist = os.listdir(audio_path)
    df = pd.DataFrame(columns=["fileid", "qa_check1","qa_check2", "qa_check3"])
    for i in range(len(filelist)):
        if "wav" in filelist[i]:
            output = parse_audio(filelist[i])
            generate_transcript(output)
            qa_check1 = qa_check_recording(output)
            qa_check2 = qa_check_pricing(output)
            qa_check3 = cc_check(output)
            df.loc[i] = [filelist[i], qa_check1, qa_check2, qa_check3]
        else:
            continue
    df.to_excel("qa_check_report - " + str(date.today()) + ".xlsx")

if __name__ == "__main__":
	main()
