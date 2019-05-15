#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May  7 22:46:12 2019

@author: pedro
"""

from reader import Data
from plotter import Plotter
from calculator import EulerModule

dadosTeste = Data("2planetasXY.txt")

eulerTeste = EulerModule(dadosTeste)

eulerTeste.spreadSheet("mdsmeajude.xlsx")

plotagem = Plotter("mdsmeajude.xlsx")

plotagem.plot2d(["blue", "orange"], "teste.pdf")