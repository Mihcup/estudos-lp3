"""
Módulo que com funções que realizam os cálculos para informações solicitadas no exercício 1 
"""

def calcularVolume(comprimento, altura, largura):
    return comprimento*altura*largura

def calcularPotencia(volume):
    return volume*0.05*25

def calcularFiltragem(volume): 
    return [volume*2,volume*3]