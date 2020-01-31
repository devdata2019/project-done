#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 20 09:54:41 2019

@author: utilisateur
"""

#ecrire un pro qui verifie si la [1,2,3,4,3,2,1] est palindrome.

ls = [1,2,3,4,3,2,1]

re_ls = []

for i in ls :
    re_ls.insert(0,i)
if ls == re_ls :
    print("La liste est un palindrome")
else : 
    print("La liste n'est pas un palindrome")
    
    
    
    

