#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 11 14:16:51 2019

@author: pedro
"""
import pandas as pd
import numpy as np
from support import calculateForce

class EulerModule:
    
    def __init__(self, planetas, contato_dem, contato_iteracao, parametros_tempo):
        self.planetas = planetas
        self.contato_dem = contato_dem
        self.contato_iteracao = contato_iteracao
        self.parametros_tempo = parametros_tempo
    
        self.pacing = int(self.parametros_tempo.tempo_final_simulacao[0]/self.parametros_tempo.numero_de_passos_impressao[0])
    
                      
    def setupHistory(self):
        history = list()
        size = len(self.planetas)
        
        index = list()
        for x in range(0, self.parametros_tempo.tempo_final_simulacao[0]+1, self.pacing):
            index.append(x)
           
        [history.append(pd.DataFrame(index = range(0, len(index)), columns = ["x", "y", "z", "v0x", "v0y", "v0z"])) for x in range(size)]
        
        for x in range(size):
            history[x].iloc[0] = self.planetas.iloc[x][['x','y','z', 'v0x', 'v0y', 'v0z']]
            history[x] = history[x].reindex(index)
            
        return history
    
    def compute(self):
        tf = self.parametros_tempo.tempo_final_simulacao[0]
        numPlanets = len(self.planetas)
        print(numPlanets)
        
        history = self.setupHistory()
        
        for x in range (self.pacing, tf+1, self.pacing):
            
            #calculo da força em cada planeta no instante analisado   
            force = [0]*numPlanets
            for m in range (numPlanets):
                for n in range(numPlanets):
                    if n != m:
                        thisPlanet = np.array(history[m].loc[x-self.pacing][["x","y","z"]])
                        otherPlanet = np.array(history[n].loc[x-self.pacing][["x","y","z"]])
                        
                        force[m] = force[m] + calculateForce(thisPlanet, otherPlanet, 
                             self.planetas.raio[m], self.planetas.raio[n], 
                             self.planetas.massa[m], self.planetas.massa[n], self.contato_iteracao[m][n])
            
            #calculo da aceleracao, velocidade, e posicao em cada planeta no instante analisado  
            for m in range(numPlanets):
                accel = force[m]/self.planetas.massa[m]
                history[m].loc[x][["v0x", "v0y", "v0z"]] = history[m].loc[x-self.pacing][["v0x", "v0y", "v0z"]].values + (self.parametros_tempo.dt[0] * accel)
                history[m].loc[x][["x", "y", "z"]] = history[m].loc[x-self.pacing][["x", "y", "z"]].values + (self.parametros_tempo.dt[0] * history[m].loc[x][["v0x", "v0y", "v0z"]].values)
            
            
        return history
    
    def spreadSheet(self, history, filePath):
        size = len(history)
        
        writer = pd.ExcelWriter(filePath)
        
        for x in range(size):
            history[x]["raio"] = self.planetas.iloc[x].raio
            history[x]["massa"] = self.planetas.iloc[x].massa
            name = "Corpo Celeste {}".format(int(self.planetas.iloc[x].id))
            history[x].to_excel(writer, sheet_name = name)
        
        writer.save()
        
        return history
        
            
            
