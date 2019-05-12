#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May  7 22:46:12 2019

@author: pedro
"""

from reader import Data
from calculator import EulerModule

dados = Data("exemplo2.txt")
teste = EulerModule(dados.planetas, dados.contato_dem, dados.contato_iteracao, dados.parametros_tempo)

teste.compute()