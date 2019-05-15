#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May  7 22:46:12 2019

@author: pedro
"""

from reader import Data
from plotter import Plotter
from calculator import EulerModule


def main():
    """Instancia as classes e executa os métodos em ordem adequadada, recebendo os dados do usuário apropriadamente"""
    print("Bem vindo!")

    dadosTeste = Data(input("Escreva o nome do arquivo (com seu diretório, se necessário) a ser lido: "))

    print("Fazendo cálculos, espere...\n")
    eulerTeste = EulerModule(dadosTeste)
    print("Cálculos concluídos!\n")


    sheetName = input("Escreva o nome da planilha (formato .xlsx, com seu diretório se necessário) a ser gravado: ")
    if ".xlsx" not in sheetName:
        raise Exception("Formato errado, tem que ser .xlsx!")
    else:
        eulerTeste.spreadSheet(sheetName)
        print("Os dados foram gravados numa planilha!\n")

    cores = input("Escreva as cores dos corpos celestes no gráfico (em inglês), separadas por vírgula (sem espaço): ").split(sep = ",")
    if len(cores) != len(eulerTeste.planetas):
        raise Exception ("Número de cores diferente do número de corpos celestes!")
    else:
        plotagem = Plotter(sheetName)
        plotagem.plot2d(cores, input("Escreva o nome da imagem (com seu diretório, se necessário) a ser gravada: "))
        print("Plotagem concluída com sucesso!\n")
    
    return

main()