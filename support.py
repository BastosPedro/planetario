#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 11 15:33:12 2019

@author: pedro
"""
from numpy.linalg import norm
import scipy.constants as con

def gravForce(coordA, coordB, mA, mB):
    """Calcula, vetorialmente, a força gravitacional que um corpo B exerce em um corpo A (ou o contrário, dependendo da interpretação).
    a função recebe as coordenadas e massas dos corpos desejados, e retorna uma força em sua forma vetorial (um array, obivamente)"""
    r = (coordA-coordB)
    escalar = (con.G * mA * mB)/(norm(r)**3)
    return (escalar * (r/norm(r)))
    
def springForce(coordA, coordB, radA, radB, k):
    """Essa função recebe as coordenadas dos corpos, seus raios, e uma constante elástica. Ela checa primeiro se existe um choque entre os corpos,
    e em seugida calcula, vetorialmente, a força de reação, como se o corpo estivesse sendo impulsionado por uma mola, que foi comprimida uma distancia
    deltaX igual ao quanto um dos corpos entrou no outro. Caso não exista choque, essa força é zero"""
    r = (coordA - coordB)
    if norm(r) < (radA + radB):
        deltaX = norm(r) - (radA+radB)
        return (k * deltaX) * (r/norm(r))
    else:
        return 0

def calculateForce(coordA, coordB, radA, radB, mA, mB, k):
    """Soma as forças gravitacional e de reação ao choque entre um corppo A e B"""
    return gravForce(coordA, coordB, mA, mB) #- springForce(coordA, coordB, radA, radB, k)