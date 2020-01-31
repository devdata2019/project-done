#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 20 09:38:19 2019

@author: utilisateur
"""

#créer un prog qui donne le prix ttc après avoir saisie le prix Hors Taxe.
#ce prog doit se repeat pour pouvoir entrer plusieurs prix à la suite et ne 
#s'arrête que si l'user entre 0 
#la taxe est de 20 %
x = -1

while x != 0 :
    x = float(input("entrer un prix hors taxe"))
    p_final = x * 1.2
    print("TTC :",p_final)
    