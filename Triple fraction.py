#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 19 11:55:03 2019

@author: utilisateur
"""

import math
import os 

d = 440*256*71

n = 217*256*71 +101*440*71 + 86*440*256

print(n,'/',d) 

gcd_1 = math.gcd(n,d) 

print(gcd_1)

n_fi = n/gcd_1
d_fi = d/gcd_1

print(n_fi,'/',d_fi)

