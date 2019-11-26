#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 21 16:03:07 2019

@author: utilisateur
"""


import pandas.io.sql
import pyodbc
import pandas as pd

# Parameters
server = 'localhost '
db = 'simplon'
UID = 'ejhb-t430'

conn = pyodbc.connect('DRIVER={SQL Server};SERVER=' + server + ';DATABASE=' + db + '; UID = ' + UID + '; PWD = ' + UID + 'Trusted_Connection=yes')
