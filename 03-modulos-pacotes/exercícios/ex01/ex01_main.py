"""
Ex01. Crie um programa que recebe como entrada o comprimento, altura e a largura de um aquário e 
calcule as seguintes informações.

1. O volume do aquário em litros;
2. A potência do termostato necessária para manter a temperatura adequada dentro do aquário;
3. A quantidade em litros de filtragem por hora necessária para manter a qualidade da água.
Volume é dado por (comprimento * altura * largura) / 1000
A potência do termostato depende do tamanho do aquário e da temperatura ambiente. 
Para o cálculo utilizar a fórmula: potencia = volume * 0,05 * (temperatura desejada - temperatura ambiente)
A quantidade de filtragem por hora deve ser no mínimo 2 a 3 vezes o volume do aquário.
"""
from calculos01 import *

comprimento = float(input("Comprimento do Aquário: "))
altura = float(input("Altura do Aquário: "))
largura = float(input("Comprimento do Aquário: "))

volume = calcularVolume(comprimento,altura,largura) 
potencia = calcularPotencia(volume)
filtragem = calcularFiltragem(volume)

print(volume,potencia,filtragem)