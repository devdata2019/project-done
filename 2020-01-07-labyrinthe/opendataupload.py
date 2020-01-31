#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan  7 09:55:41 2020

@author: utilisateur
"""

from sqlalchemy import create_engine
import pandas as pd
import pymysql
import time
engine = create_engine("mysql+pymysql://root:@localhost/opendata")

def importcsv(link, table, date):
    print("Lecture des données")
    start_time = time.time()
    csize = 300000
    df = pd.read_csv(link, compression = 'zip', chunksize = csize, parse_dates = date)
    print("Données lu")
    i = csize
    for chunk in df:
        chunk.to_sql(table, con = engine, if_exists='append', index = False)
        i += csize
        print(i)
    return print("Temps d execution : %s secondes ---" % (time.time() - start_time))


importcsv('https://www.data.gouv.fr/fr/datasets/r/09af65ff-c1c6-40bb-bfcb-b80f7ac93b72', 'hist_etab', ['dateFin', 'dateDebut'])