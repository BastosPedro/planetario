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

    
   def plot2dToFile(self, colors, filePath):
       
       ax = plt.gca()
       
       
       for x in range (self.NumPlanets):
           firstPos = self.planetas[x].head(1)
           lastPos = self.planetas[x].tail(1)
           
           trajectory = self.planetas[x].drop(self.planetas[x].head(1).index)
           trajectory = trajectory.drop(trajectory.tail(1).index)
           
           
           firstPos.plot(kind = "scatter", x = "x", y="y", color = colors[x], alpha = 0.5, ax=ax, zorder = 2)
           trajectory.plot(kind = "line", x = "x", y="y", color = "black", alpha = 0.25, ax=ax, legend = False, zorder = 1)
           lastPos.plot(kind = "scatter", x = "x", y="y", color = colors[x], ax=ax, zorder = 3)
       
       plt.savefig(filePath)
       
   def plot2d(self, colors):
       
       ax = plt.gca()
       
       
       for x in range (self.NumPlanets):
           firstPos = self.planetas[x].head(1)
           lastPos = self.planetas[x].tail(1)
           
           trajectory = self.planetas[x].drop(self.planetas[x].head(1).index)
           trajectory = trajectory.drop(trajectory.tail(1).index)
           
           
           firstPos.plot(kind = "scatter", x = "x", y="y", color = colors[x], alpha = 0.5, ax=ax, zorder = 2)
           trajectory.plot(kind = "line", x = "x", y="y", color = "black", alpha = 0.25, ax=ax, legend = False, zorder = 1)
           lastPos.plot(kind = "scatter", x = "x", y="y", color = colors[x], ax=ax, zorder = 3)
       
       plt.show()
 