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
    
        self.count = (self.parametros_tempo.tempo_final_simulacao[0]/self.parametros_tempo.dt[0])
        self.history = self.compute()
                      
    def setupHistory(self):
        """Monta a lista de DataFrames (cada DataFrame representa um corpo celeste), a ser preenchida pelo método Compute"""
        history = list()
        size = len(self.planetas)
        
        #aqui é preaprado o índice o dataframe
        index = list()
        aux = len(str(self.parametros_tempo.dt[0]))-2
        for x in range(0, int(self.count)+1):
            index.append(round(x*self.parametros_tempo.dt[0], aux))
       
        
        
        #aqui a lista de dataframes é montada preparado o dataframe é montado
        for x in range(size):
            history.append(pd.DataFrame(index = range(0, len(index)), columns = ["x", "y", "z", "v0x", "v0y", "v0z"])) #dataframe vazio
            history[x].iloc[0] = self.planetas.iloc[x][['x','y','z', 'v0x', 'v0y', 'v0z']] #recebe os valores iniciais
            history[x] = history[x].reindex(index) #dataframe recebe o novo index, ficando então um dataframe cheio de NaNs, a serem preenchidos pelo compute
            
        return history
    
    def compute(self):
        """Faz os calculos de força, aceleração em cada instante para cada planeta, e usando o método de euler, calcula a velocidade e posição para cada ponto no intervalo,
        prencheendo os DataFrames de cada planeta"""
        numPlanets = len(self.planetas)
        
        history = self.setupHistory()
        
        #"iteracoes"
        for x in range (1, int(self.count)+1):
            print(x)
            #calculos para cada planeta numa dada instancia   
            for m in range (numPlanets):
                #calcula da força sofrida por cada planeta
                force = np.zeros(3)
                for n in range(numPlanets):
                    if n != m:
                        thisPlanet = np.array(history[m].iloc[x-1][["x","y","z"]])
                        otherPlanet = np.array(history[n].iloc[x-1][["x","y","z"]])
                        
                        force = force + calculateForce(thisPlanet, otherPlanet, 
                             self.planetas.raio[m], self.planetas.raio[n], 
                             self.planetas.massa[m], self.planetas.massa[n], self.contato_dem.loc[self.contato_iteracao[m][n]][0])
                        
                        
            
                #calculo da aceleracao, velocidade, e posicao em cada planeta no instante analisado  
                accel = force/self.planetas.massa[m]
                print(force)
                history[m].iloc[x][["v0x", "v0y", "v0z"]] = history[m].iloc[x-1][["v0x", "v0y", "v0z"]].values + (self.parametros_tempo.dt[0] * accel)
                history[m].iloc[x][["x", "y", "z"]] = history[m].iloc[x-1][["x", "y", "z"]].values + (self.parametros_tempo.dt[0] * history[m].iloc[x][["v0x", "v0y", "v0z"]].values)
            
            
        return history
    
    def spreadSheet(self, filePath):
        """Adiciona massa e raio de cada planeta para seu respectivo DataFrame, e então joga todo em uma planilha .xlsx com o nome do e diretório desejado pelo usuário"""
        size = len(self.history)
        
        writer = pd.ExcelWriter(filePath, engine = "openpyxl")
        
        pacing = int((self.parametros_tempo.tempo_final_simulacao[0]/self.parametros_tempo.numero_de_passos_impressao[0])/self.parametros_tempo.dt[0])
                  
        printHistory = list()     
        for x in range(size):
            printHistory.append(pd.DataFrame(columns = ["x", "y", "z", "v0x", "v0y", "v0z"]))
            
            for y in range(0, int(self.count)+1, pacing):
                printHistory[x] = printHistory[x].append(self.history[x].iloc[y])            
                
            printHistory[x]["raio"] = self.planetas.iloc[x].raio
            printHistory[x]["massa"] = self.planetas.iloc[x].massa
            printHistory[x].index.name = "instante"
            name = "Corpo Celeste {}".format(int(self.planetas.iloc[x].id))
            printHistory[x].to_excel(writer, sheet_name = name)
        
        writer.save()
        
        return printHistory
        
            
            
