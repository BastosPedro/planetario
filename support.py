#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 11 15:33:12 2019

@author: pedro
"""
from numpy.linalg import norm
import scipy.constants as con

def gravForce(coordA, coordB, mA, mB):
    r = (coordA-coordB)
    escalar = (con.G * mA * mB)/(norm(r)**3)
    return -1*(escalar * r)
    
def springForce(coordA, coordB, radA, radB, k):
    r = (coordA - coordB)
    if norm(r) < (radA + radB):
        deltaX = (radA+radB) - norm(r)
        return (k * deltaX) * r
    else:
        return 0

def calculateForce(coordA, coordB, radA, radB, mA, mB, k):
    return gravForce(coordA, coordB, mA, mB) - springForce(coordA, coordB, radA, radB, k)