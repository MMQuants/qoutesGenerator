# -*- coding: utf-8 -*-
"""
Created on Sun Jan 13 10:09:25 2019

@author: marin
"""
import pandas as pd

df = pd.read_csv(
        'D:/Downloads/tickDataGBPJPY2007-2017.csv',
        names = ["Date","Time","open","high","low","close","volume"]
        )

print("We have {} rows".format(len(df.index)))

df['15min_high'] = df['high'].rolling(window=15).max()
df['15min_low'] = df['low'].rolling(window=15).min()
df = df.iloc[::15, :]
df = df[["Date","Time","open","15min_high","15min_low","close","volume"]]
df = df.iloc[1:,:]

print("Redused to {} rows".format(len(df.index)))

df.to_csv("D:/15minuteCSV.csv", header=0, index=0)