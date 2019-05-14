#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May  7 22:46:12 2019

@author: pedro
"""

from reader import Data
from calculator import EulerModule

dadosTeste = Data("4planetasXY.txt")

eulerTeste = EulerModule(dadosTeste)

eulerHistorico = eulerTeste.spreadSheet("mdsmeajude.xlsx")