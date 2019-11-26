#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 19 14:03:49 2019

@author: utilisateur
"""

# Ecrire un programme qui à partir de la saisie d'un rayon et d'une hauteur, 
#calcule le volume d'un cône droit. (Utiliser l'instruction input pour saisis 
#les valeurs et print pour afficher le resultat.

#Soit un cône dont la hauteur est de 6 cm et dont 
#la base a un rayon de 3 cm. Le volume V de ce cône est égal à :

#V = pi x 3² x 6 / 3 ≈ 56,55 cm³

import math
import os 

continue_equation = True 

while continue_equation:
    
    a = float(input("Entrer votre rayon"))

    print("Vous venez de saisir:",a)

    b = float(input("Entrer votre hauteur"))
    print("Vous venez de saisir:",b)


V = math.pi * a**2 * b / 3 

print(V)