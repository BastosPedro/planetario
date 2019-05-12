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
        
        self.history = list()
        size = len(planetas)
        [self.history.append(pd.DataFrame(columns = ["x", "y", "z", "v0x", "v0y", "v0z"])) for x in range(size)]
        for x in range(size):
            self.history[x] = self.history[x].append(self.planetas.iloc[x][['x','y','z', 'v0x', 'v0y', 'v0z']])
            self.history[x] = self.history[x].reset_index(drop=True)
        
     
    def compute(self):
        tf = self.parametros_tempo.tempo_final_simulacao[0]
        pacing = int(tf/self.parametros_tempo.numero_de_passos_impressao[0])
        numPlanets = len(self.planetas) 
        
        for x in range (0, tf, pacing):
            
            #calculo da força em cada planeta no instante analisado   
            force = [0]*numPlanets
            for m in range (numPlanets):
                for n in range(numPlanets):
                    if n != m:
                       force[m] = force[m] + calculateForce(np.array([self.planetas.x[m], self.planetas.y[m], self.planetas.z[m]]), 
                            np.array([self.planetas.x[n], self.planetas.y[n], self.planetas.z[n]]), 
                            self.planetas.raio[m], self.planetas.raio[n], self.planetas.massa[m], self.planetas.massa[n], self.contato_iteracao[m][n])
            
            
             #calculo da aceleracao em cada planeta no instante analisado  
            accel = [0]*numPlanets
            for m in range(numPlanets):
                accel[m] = force[m]/self.planetas.massa[m]
            
        print(force)
        print(accel)
                      

