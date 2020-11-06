#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov  6 01:39:36 2020

@author: virag
"""


import re

# regex patterns
generic_pattern = r"\b(?:\d[ -]*?){13,16}\b"
visa_pattern = r"4[0-9 -]{15,18}"
mastercard_pattern = r"5[1-5][0-9 -]{2}[0-9 -]{12,14}"

a = "your card number is 5511 1111 1111 1111 and the cvv number is 573"
result = re.search(generic_pattern,a)
print (result)
if result:
    print ("Might contain cc")
else:
    print ("Does not contain cc")