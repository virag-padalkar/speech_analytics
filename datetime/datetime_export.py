#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov  7 19:43:54 2020

@author: virag
"""


from datetime import date
import numpy as np
import pandas as pd
df = pd.DataFrame(np.random.randint(0,100, size = (15, 3)),columns=["A","B","C"])
df.to_excel("test excel - " + str(date.today()) + ".xlsx")
