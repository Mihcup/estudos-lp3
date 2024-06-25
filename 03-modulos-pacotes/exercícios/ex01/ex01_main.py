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
temperatura_ambiente = float(input("Qual é a temperatura ambiente? "))
temperatura_desejada = float(input("Qual é a temperatura desejada para o aquário? "))

volume = calcularVolume(comprimento,altura,largura) 
potencia = calcularPotencia(volume, temperatura_ambiente, temperatura_desejada)
filtragem = calcularFiltragem(volume)

print(f"O volume do aquário é {volume} L")
print(f"A potência do termostato deve ser de {potencia} watt")
print(f"A filtragem deve variar de {filtragem[0]} L/h a {filtragem[1]} L/h")