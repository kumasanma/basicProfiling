# -*- coding: utf-8 -*-
"""
Created on Thu Jun  4 21:42:20 2020

@author: keiji
"""
import pandas as pd
import pandas_profiling as pdp

df = pd.read_csv('train.csv')
pdp.ProfileReport(df)

