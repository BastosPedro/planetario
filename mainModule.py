#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 14 21:25:40 2019

@author: pedro
"""
from readingModule import Data
from plottingModule import Plotter
from analysisModule import EulerModule

class MainModule():
    """Esta classe condensa os modulos, de forma a tornar os testes mais convenientes."""
    def __init__(self):
        pass

    def complicado(self):
        """Roda o teste demonstrativo de três corpos celestes movendo-se no espaço. O método
        retorna instâncias do módulo de leitura, de análise e de visualização já carregados com os dados."""
        dadosTeste = Data("entradas/complicado.txt")
        print("dados lidos")

        eulerTeste = EulerModule(dadosTeste)
        print("calculos feitos")

        eulerTeste.spreadSheet("saidas/complicado.xlsx")
        print("planilha salva")

        plotagem = Plotter("saidas/complicado.xlsx")
        print("planilha lida")

        plotagem.plot3dToFile(["red", "green", "blue"], "saidas/complicado.pdf")
        plotagem.plot3d(["red", "blue", "green"])
        print("plotagem feita")
        
        return dadosTeste, eulerTeste, plotagem
    
    def simples(self):
        """Roda o teste demonstrativo de dois corpos celestes movendo-se no plano. O método
        retorna instâncias do módulo de leitura, de análise e de visualização já carregados com os dados."""
        dadosTeste = Data("entradas/simples.txt")
        print("dados lidos")
        
        eulerTeste = EulerModule(dadosTeste)
        print("calculos feitos")

        eulerTeste.spreadSheet("saidas/simples.xlsx")
        print("planilha salva")

        plotagem = Plotter("saidas/simples.xlsx")
        print("planilha lida")

        plotagem.plot2dToFile(["red", "blue"], "saidas/simples.pdf")
        plotagem.plot2d(["red", "blue"])
        print("plotagem feita")
        
        return dadosTeste, eulerTeste, plotagem
    
    def batida(self):
        """Roda o teste demonstrativo de dois corpos celestes chocando-se no plano. O método
        retorna instâncias do módulo de leitura, de análise e de visualização já carregados com os dados."""
        dadosTeste = Data("entradas/batida.txt")
        print("dados lidos")

        eulerTeste = EulerModule(dadosTeste)
        print("calculos feitos")

        eulerTeste.spreadSheet("saidas/batida.xlsx")
        print("planilha salva")

        plotagem = Plotter("saidas/batida.xlsx")
        print("planilha lida")

        plotagem.plot2dToFile(["red", "blue"], "saidas/batida.pdf")
        plotagem.plot2d(["red", "blue"])
        print("plotagem feita")
        
        return dadosTeste, eulerTeste, plotagem
    
    def custom2dplot(self, txtPath, xlsxPath, colors, imagePath):
        """Teste customizado, recebe o nome do arquivo .txt a ser lido, o nome da planilha .xlsx a ser testada, uma lista com as cores desejadas pelo usuário
        e o nome do imagem a ser salva em memória secundária. Ele faz a checagem nas entradas do .txt e do .xlsx, levantando exceções caso não funcionem. O método
        retorna instâncias do módulo de leitura, de análise e de visualização já carregados com os dados. Faz a plotagem dos dados em 2d (plano x0y)."""
        
        if ".txt" not in txtPath:
            raise Exception("Formato errado, tem que ser .txt!")
        elif ".xlsx" not in xlsxPath:
            raise Exception("Formato errado, tem que ser .txt!")
        else:   
            dadosTeste = Data(txtPath)
            print("dados lidos")

            eulerTeste = EulerModule(dadosTeste)
            print("calculos feitos")

            eulerTeste.spreadSheet(xlsxPath)
            print("planilha salva")

            plotagem = Plotter(xlsxPath)
            print("planilha lida")

            plotagem.plot2dToFile(colors, imagePath)
            plotagem.plot2d(colors)
            print("plotagem feita")
        
            return dadosTeste, eulerTeste, plotagem
    
    def custom3dplot(self, txtPath, xlsxPath, colors, imagePath):
        """Teste customizado, recebe o nome do arquivo .txt a ser lido, o nome da planilha .xlsx a ser testada, uma lista com as cores desejadas pelo usuário
        e o nome do imagem a ser salva em memória secundária. Ele faz a checagem nas entradas do .txt e do .xlsx, levantando exceções caso não funcionem. O método
        retorna instâncias do módulo de leitura, de análise e de visualização já carregados com os dados. Faz a plotagem dos dados em 3d."""
        
        if ".txt" not in txtPath:
            raise Exception("Formato errado, tem que ser .txt!")
        elif ".xlsx" not in xlsxPath:
            raise Exception("Formato errado, tem que ser .txt!")
        else:   
            dadosTeste = Data(txtPath)
            print("dados lidos")

            eulerTeste = EulerModule(dadosTeste)
            print("calculos feitos")

            eulerTeste.spreadSheet(xlsxPath)
            print("planilha salva")

            plotagem = Plotter(xlsxPath)
            print("planilha lida")

            plotagem.plot3dToFile(colors, imagePath)
            plotagem.plot3d(colors)
            print("plotagem feita")
        
            return dadosTeste, eulerTeste, plotagem
    
    
main = MainModule()