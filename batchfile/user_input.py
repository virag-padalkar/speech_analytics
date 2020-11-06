#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov  7 02:51:33 2020

@author: virag
"""


import os

audio_path = input("Enter path where audio files are stored (Enter ~ for current folder): ")

if audio_path == "~":
    filelist = os.listdir(os.getcwd())
else:
    filelist = os.listdir(user_input)

print (filelist)