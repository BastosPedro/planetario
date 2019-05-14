#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 14 16:30:51 2019

@author: pedro
"""

import pandas as pd
import matplotlib.pyplot as plt

class Plotter:
   def __init__(self, filePath):
       xlsx = pd.ExcelFile(filePath, engine = "xlrd")
       sheetList = xlsx.sheet_names
       self.NumPlanets = len(sheetList)
       self.planetas = list()
       [self.planetas.append(pd.read_excel(xlsx, sheetList[x])) for x in range (self.NumPlanets)]

    
   def plot2d(self, colors):
       ax = plt.gca()
       
       for x in range (self.NumPlanets):
           self.planetas[x].plot(kind = "scatter", x = "x", y="y", color = colors[x], ax=ax)
       
       plt.show()