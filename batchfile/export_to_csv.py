#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov  4 22:32:18 2020

@author: virag
"""


import os
import pandas as pd

filelist = os.listdir("/home/virag/Documents/speech/batchfile")
df = pd.DataFrame(columns=["fileid", "qc_check1","qc_check2","qc_check3"])
for i in range(len(filelist)):
    if "py" not in filelist[i]:
        df.loc[i] = [filelist[i], "pass", "pass","pass"]
    else:
        continue

