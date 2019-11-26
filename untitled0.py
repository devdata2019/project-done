#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 21 16:58:48 2019

@author: utilisateur
"""

from sqlalchemy import create_engine
import pymysql 
import pandas as pd
import matplotlib.pyplot as plt

engine = create_engine('mysql://root@localhost/simplon')
df = pd.read_sql_query('SELECT * FROM jeux_video', engine)

x = df["prix"].head()
y = df ["nom"].head()


plt.figure(figsize=(9, 6))

plt.ylabel('nom')
plt.xlabel('prix')
line = plt.bar(x,y)
plt.suptitle('Test 1')
plt.setp(line, color='g', linewidth=20)


print(df)
