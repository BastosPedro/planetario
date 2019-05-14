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
    """Classe recebe os dados lidos pela classe Data, e faz todos os cálculos de posição e velocidade, a partir do método de Euler, podendo salvar os resultados numa planilha"""
    
    def __init__(self, data):
        """Recebe uma instância da classe Data, com as informações retiradas do arquivo txt, e retorna um objeto da classe EulerModule, já feito os cálculos de velocidade e posicão
        para um sistema, na forma de uma lista de DataFrames do Pandas, cada DataFrame representando um corpo celeste"""
        self.planetas = data.planetas
        self.contato_dem = data.contato_dem
        self.contato_iteracao = data.contato_iteracao
        self.parametros_tempo = data.parametros_tempo
    
        self.pacing = int(self.parametros_tempo.tempo_final_simulacao[0]/self.parametros_tempo.numero_de_passos_impressao[0])
        self.history = self.compute()
                      
    def setupHistory(self):
        """Monta a lista de DataFrames (cada DataFrame representa um corpo celeste), a ser preenchida pelo método Compute"""
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
        """Faz os calculos de força, aceleração em cada instante para cada planeta, e usando o método de euler, calcula a velocidade e posição para cada ponto no intervalo,
        prencheendo os DataFrames de cada planeta"""
        tf = self.parametros_tempo.tempo_final_simulacao[0]
        numPlanets = len(self.planetas)
        
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
    
    def spreadSheet(self, filePath):
        """Adiciona massa e raio de cada planeta para seu respectivo DataFrame, e então joga todo em uma planilha .xlsx com o nome do e diretório desejado pelo usuário"""
        size = len(self.history)
        
        writer = pd.ExcelWriter(filePath, engine = "openpyxl")
        
        for x in range(size):
            self.history[x]["raio"] = self.planetas.iloc[x].raio
            self.history[x]["massa"] = self.planetas.iloc[x].massa
            self.history[x].index.name = "instante"
            name = "Corpo Celeste {}".format(int(self.planetas.iloc[x].id))
            self.history[x].to_excel(writer, sheet_name = name)
        
        writer.save()
        
            
            
