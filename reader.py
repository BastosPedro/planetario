# -*- coding: utf-8 -*-
"""
Spyder Editor

Este é um arquivo de script temporário.
"""

import pandas as pd

class Data:
    """o módulo de leitura dos dados, recebe as informações num arquivo txt e as organiza em dataframes dos pandas 
        para serem acessados e manipulados facilmente pelos outros módulos"""
    
    def __init__(self, filePath):
        """aqui é onde ocorre a leitura dos dados a partir do arquivo fornecido pelo usuario"""
        file = list(open(filePath).read().split("\n"))
        filesize = len(file)
        hashlist = list()
        
        for x in range(filesize):
            if "#" in file[x]:
                hashlist.append(x)

        
        #esse aqui lê o #PLANETAS
        self.planetas = pd.read_csv(filePath, skiprows = 2, nrows = hashlist[1]-3, sep = " ", header = None,
                               names = ["id" ,"x", "y", "z", "v0x", "v0y", "v0z", "raio", "massa"])

        #esse aqui lê o #CONTATO DEM
        self.contato_dem = pd.read_csv(filePath, skiprows = hashlist[1]+2, nrows = hashlist[2]-hashlist[1]-3, sep = " ", header = None,
                                       names = ["idModelo", "Kn"])

        #esse aqui lê o #CONTATO_ITERACAO
        self.contato_iteracao = pd.read_csv(filePath, skiprows = hashlist[2]+1, nrows = hashlist[3]-hashlist[2]-2, sep = " ", header = None)

        #aqui lê o #INTEGRADOR
        self.integrador = file[hashlist[3]+1]

        #aqui lê o PARAMETROS_TEMPO
        self.parametros_tempo = pd.read_csv(filePath, skiprows = hashlist[4]+1, nrows = hashlist[5]-hashlist[4]-2, sep = " ", header = None,
                                            names = ["dt", "tempo_final_simulacao", "numero_de_passos_impressao"])    
