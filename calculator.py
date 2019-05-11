#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 11 14:16:51 2019

@author: pedro
"""
from reader import Data
#import pandas as pd
from support import calculateForce

import numpy as np

class BaseModule:
    
    def __init__(self, filePath):
        self.data = Data(filePath)
        
    def aprroximate(self):
        return 0


teste = BaseModule("exemplo2.txt")


seila = calculateForce(np.array([teste.data.planetas.x[0],teste.data.planetas.y[0]]), np.array([teste.data.planetas.x[1],teste.data.planetas.y[1]]), 
                  teste.data.planetas.raio[0], teste.data.planetas.raio[1], teste.data.planetas.massa[0], teste.data.planetas.massa[1], teste.data.contato_iteracao[0][1])
7