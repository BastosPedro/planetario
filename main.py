#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May  7 22:46:12 2019

@author: pedro
"""

from reader import Data
from calculator import EulerModule

#dados = Data("exemplo1.txt")
dados2 = Data("exemplo2.txt")

#teste2 = EulerModule(dados2.planetas, dados2.contato_dem, dados2.contato_iteracao, dados2.parametros_tempo)
teste2 = EulerModule(dados2.planetas, dados2.contato_dem, dados2.contato_iteracao, dados2.parametros_tempo)

#asdadas = teste2.setupHistory()
#historico2 = teste2.compute()
historico2 = teste2.compute()

teste2.spreadSheet(historico2, "mdsmeajude.xlsx")