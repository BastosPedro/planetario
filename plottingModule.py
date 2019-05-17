#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 14 16:30:51 2019

@author: pedro
"""

import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D #vem com o matplotlib

class Plotter:
   """Módulo de visualização do projeto, ao ser instanciado, faz a leitura de um arquivo gerado pelo módolo de análise para então realizar a plotagem"""
   def __init__(self, filePath):
       """Faz a leitura dos fornecidos pela planilha criada pelo módulo de análise"""
       xlsx = pd.ExcelFile(filePath, engine = "xlrd")
       sheetList = xlsx.sheet_names
       self.NumPlanets = len(sheetList)
       self.planetas = list()
       [self.planetas.append(pd.read_excel(xlsx, sheetList[x])) for x in range (self.NumPlanets)]

    
   def plot2dToFile(self, colors, filePath):
       """Faz a plotagem 2d e retorna no um arquivo com diretório, nome, e formato(consulte documentação do matplotlib para saber os formatos suportados) 
       especificados pelo usuário. Além dessas informações, o método também recebe uma lista com as cores que o usuário deseja ver no gráfico."""
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
       """Faz a plotagem 2d e mostra o gráfico numa janela (caso seja rodado direto no iPython). Recebe uma 
       lista com as cores desejadas pelo usuário para cada corpo celeste."""
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
 
    
   def plot3dToFile(self, colors, filePath):
      """Faz a plotagem 3d e mostra o gráfico numa janela (caso seja rodado direto no iPython). Recebe uma 
      lista com as cores desejadas pelo usuário para cada corpo celeste."""
      fig = plt.figure()
      ax3d = fig.add_subplot(111, projection = "3d")
       
       
      for x in range (self.NumPlanets):
          firstPos = self.planetas[x].head(1)
          lastPos = self.planetas[x].tail(1)
           
          trajectory = self.planetas[x].drop(self.planetas[x].head(1).index)
          trajectory = trajectory.drop(trajectory.tail(1).index)
           
          ax3d.scatter(firstPos["x"], firstPos["y"], firstPos["z"], color = colors[x], alpha = 0.5)
          ax3d.plot(trajectory["x"], trajectory["y"], trajectory["z"], color = "black", alpha = 0.25)
          ax3d.scatter(lastPos["x"], lastPos["y"], lastPos["z"], color = colors[x])
       
      plt.savefig(filePath)
      
    
   def plot3d(self, colors):
       """Faz a plotagem 3d e mostra o gráfico numa janela (caso seja rodado direto no iPython). Recebe uma 
       lista com as cores desejadas pelo usuário para cada corpo celeste."""
       fig = plt.figure()
       ax3d = fig.add_subplot(111, projection = "3d")
       
       
       for x in range (self.NumPlanets):
           firstPos = self.planetas[x].head(1)
           lastPos = self.planetas[x].tail(1)
           
           trajectory = self.planetas[x].drop(self.planetas[x].head(1).index)
           trajectory = trajectory.drop(trajectory.tail(1).index)
           
           ax3d.scatter(firstPos["x"], firstPos["y"], firstPos["z"], color = colors[x], alpha = 0.5)
           ax3d.plot(trajectory["x"], trajectory["y"], trajectory["z"], color = "black", alpha = 0.25)
           ax3d.scatter(lastPos["x"], lastPos["y"], lastPos["z"], color = colors[x])
       
       plt.show()
      
           
           
                    
        