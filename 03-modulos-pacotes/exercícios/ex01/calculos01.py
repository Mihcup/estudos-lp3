"""
Módulo que com funções que realizam os cálculos para informações solicitadas no exercício 1 
"""

def calcularVolume(comprimento, altura, largura):
    return comprimento*altura*largura

def calcularPotencia(volume, temp_ambiente, temp_desejada):
    return round(volume*0.05*(temp_desejada-temp_ambiente),2)

def calcularFiltragem(volume): 
    return [volume*2,volume*3]