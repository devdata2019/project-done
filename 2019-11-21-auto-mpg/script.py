#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 21 11:43:06 2019

@author: utilisateur
"""
import matplotlib.pyplot as plt
import pandas 

df = pandas.read_excel("/home/utilisateur/Documents/project/auto-mpg/autompg.xlsx" , sep='/t' , header = 0)
df.columns = ["mpg","cylindres", "déplacement","puissance","poids","accélération","année de modèle","origine","Nom de la voiture"]


x = df["Nom de la voiture"].head()
y = df ["poids"].head()

df.loc[df['poids'].isin(some_values)]

plt.figure(figsize=(15, 8))

plt.ylabel("Nom de la voiture")
plt.xlabel("poids")
line = plt.bar(x,y)
plt.suptitle('Test 1')
plt.setp(line, color='r', linewidth=20)



print(df)