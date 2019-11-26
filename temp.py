# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

# -*-coding:utf-8 -*

import os
import math

a = 3 
b= -7
c= -23

delta = b**2 - 4  * a * c

x1 = (-b - math.sqrt(delta)) / (2*a) 
x2 = (-b + math.sqrt(delta)) / (2*a) 

print(x1)
print(x2)