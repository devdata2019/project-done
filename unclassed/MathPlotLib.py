#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 21 09:55:21 2019

@author: utilisateur
"""

import pandas as pd
import matplotlib.pyplot as plt



"""titles = ['mpg','cylindres', 'deplacement', 'puissance', 'poids', 'accélération', 'année de modèle', 'origine', 'nom de la voiture' ]
print(titles)"""

auto_mpg = pd.read_excel("/home/utilisateur/Téléchargements/autompg.xlsx", sep='\t')

for col in auto_mpg.columns: 
    print(col) 

print(auto_mpg.describe())

data_70= auto_mpg.loc[auto_mpg['année de modèle'].isin(['70'])]
plt.figure(figsize=(6,6))
plt.bar(data_70['origine'],data_70['accélération'], color='black',width=0.2)
plt.xlabel('accélération')
plt.ylabel('origine')
plt.title('70s cars')

plt.figure(figsize=(6,6))
plt.bar(data_70['mpg'],data_70['déplacement'], color='black',width=0.2)
plt.xlabel('mpg')
plt.ylabel('déplacement')
plt.title('70s cars')

print(data_70.describe())

"""
poids = auto_mpg['poids']
depl = auto_mpg['d']

auto_mpg.plot(kind='scatter',x='poids',y='déplacement',color='red');
auto_mpg.plot(kind='scatter',x='puissance',y='accélération',color='black');
auto_mpg.plot(kind='bar',x='année de modèle',y='puissance',color='blue');
"""


x=auto_mpg['année de modèle']
y=auto_mpg['puissance']
plt.figure(figsize=(6,6))
plt.bar(x,y,width=.1)
plt.xlabel('année de modèle')
plt.ylabel('puissance')


poids = auto_mpg['poids']
depl = auto_mpg['déplacement']
plt.figure(figsize=(6,6))
plt.plot(poids, depl, 'o',color='red')
plt.xlabel('poids')
plt.ylabel('déplacement')


puis = auto_mpg['puissance']
acc = auto_mpg['accélération']
plt.figure(figsize=(6,6))
plt.plot(puis, acc, 'x',color='blue')
plt.xlabel('puissance')
plt.ylabel('accélération')



"""
plt.title('Déplacement de voiture en fonction du poids')
plt.xlabel('Poids')
plt.ylabel('Déplacement')
"""
