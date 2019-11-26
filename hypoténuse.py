#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 19 15:44:28 2019

@author: utilisateur
"""

#Ecrire un programme qui vérifie si un trinagle est rectangle

#Si ABC est un triangle rectangle en A, alors BC² =AB² + AC² .

import pandas as pd

import os

a = float(input("Entrer BC")) #BC
b = float(input("Entrer AB")) #AB                                                                                                                                                                       
c = float(input("Entrer AC")) #AC


v = [a,b,c]
h = max(v)

if h == (a**2 == b**2 + c**2) :
    print("Votre triangle est rectangle en BC")
elif h == (b**2 == a**2 + c**2) :
    print("Votre triangle est rectangle en AB")
elif h == (c**2 == a**2 + b**2) :
    print("Votre triangle est rectangle en AC")
else : 
    print("Votre triangle n'est pas rectangle")

os.system ("pause")
    
        

