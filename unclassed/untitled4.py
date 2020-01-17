#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 21 16:35:07 2019

@author: utilisateur
"""

from sqlalchemy import create_engine
import pymysql 
import pandas as pd

db_connection_str = create_engine('mysql://ejhb-T430@localhost/simplon')
db_connection = create_engine(db_connection_str)

df = pd.read_sql('SELECT * FROM simplon', con=db_connection)



print(df)


