'''
Identificadores 
nome que dá para variáveis, funções - pode usar letra, numero e _ 
são case sensitive 
diversas palavras reservadas - main ñ é palavra reservada 
'''

#variáveis:
idade = 20 
velocidade = 20.2
velocidade = velocidade+10.0

#função: def somar(n1,n2)

#constante: 
PI = 3.14 #convenção: uso das letras maiusculas

# docstring - wxplica na documentação
# documentar código de funções e classes 

def somar(n1,n2): 
    '''
    Função que soma dois números
    :param n1: primeiro número 
    :param n2: segundo número
    :return: soma dos números
    '''
    #pode validar se é do tipo desejado 
    return n1+n2 

soma = somar(10.0,2.0)
#como ñ definiu o tipo - pode colocar string, boolean - "qualquer tipo"
print('A soma é:',soma)

'''
python tem tipo dinâmico, assim como js que não tem tipagem estática
ts consegue colocar tipo na variável usando o js  
'''
