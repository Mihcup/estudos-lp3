'''
Convenção: 
A: 90-100
B: 80-89
C: 70-79
D: 60-69
E: 50-59
F: 0-49
'''

pontuacao = float(input('Qual foi a sua pontuação? (0-100)'))

#definindo a função
def pontuacaoDiferente(pontuacao):
    p = ''
    if pontuacao>=90:
        p='A'
    elif pontuacao>=80:
        p='B'
    elif pontuacao>=70:
        p='C'
    elif pontuacao>=60: 
        p='D'
    elif pontuacao>=50:
        p='E'
    else: 
        p='F'
    return p 

#chamando a função
print(pontuacaoDiferente(pontuacao))