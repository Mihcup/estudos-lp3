# Utilizando as diretrizes de Índice de Massa Corporal (IMC) da Organização Mundial de Saúde (OMS), 
# crie uma calculadora que solicita ao usuário seu peso (Kg) e sua altura (m) 
# e apresenta em qual classificação o indivíduo se encaixa. Além disso, o programa deve apresentar quanto o indivíduo precisa perder ou ganhar de peso para chegar no peso normal (imc = 24,9).
#IMC = peso / altura * altura
from calculo_imc import calcular_imc

print("Bem-vindo a calculadora de IMC")
peso = float(input("Qual a seu peso? "))
altura= float(input("Qual a sua altura? "))

imc, classificacao,frase = calcular_imc(peso,altura)

print(f'O valor do IMC é {imc}, assim sua classificação é {classificacao}')
print(frase)