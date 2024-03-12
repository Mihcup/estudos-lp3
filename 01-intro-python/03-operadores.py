# Operadores aritméticos 
# + - / * % **
nota1 = 10.0 
nota2 = 7.0
nota3 = 8.5 

media = (nota1+nota2+nota3)/3 
print('%.2f'%media)

#potenciação
numero = 10 
elevadoAoQuadrado = 10**2 
print(elevadoAoQuadrado)

#Operadores lógicos 
# and, or, not 
print(True and True)
print(True or False)
#operadores lógicos devolvem outro boolean 
#verdade = True and True -> vai retornar um boolean, podendo ser armazenado em outro lugar 
# or meio que o contrário do and 

#permitir a entrada no sistema
#REGRAS: usuario não bloqueado e usuario é um funcionário e hora atual entre 8h e 18h
#caso for admin pode acessar de qualque forma - não cai em nenhuma regra 
usuarioBloqueado = False 
usuarioFuncionario = True 
horaAtual = 17 
usuarioAdmin = False 

funcionarioAtivo = usuarioFuncionario and not usuarioBloqueado
horarioComercial = (horaAtual>=8) and (horaAtual<=18)

if (funcionarioAtivo and horarioComercial) or usuarioAdmin: 
    print('Bem-vindo :)')
else: 
    print('Acesso não liberado :(')

'''
-> como colocar em outro arquivo 
def dentroHorarioComercial(hora): 
    return hora>=8 and hora<=18
'''

# Operadores de comparação
# == != > < >= <= -> retorna um boolean 
nota1 = 10.0
nota2 = 10.0
if nota1>nota2: 
    print('Aluno foi melhor na nota 1')
elif (nota1==nota2): 
    print('O aluno tirou a mesma nota nas duas provas')
else: 
    print('Aluno foi  melhor na nota 2')

#Operador is, is not -> avaliar se ocupa o mesmo espaço de memoria
#Operador de identidade 
#Comparar se os objetos são o mesmo -> mesmo espaço de memória

a = [1,2,3]
b = [1,2,3]
print(a==b)
print(a is b) #False -> coisas diferentes 
c = b # apontamento para o mesmo espaço de memória -> ñ tem como manipular o ponteiro em python
print(c is b)
#== avalia o conteudo - mesmos valores

#Operador in e not in 
#se comporta diferente dependendo do contexto
#usado para verificar se um elemento existe em uma sequencia -. str, tupla, lista 
opcoes = ('sim','não','talvez')
opcao = input('Digite uma opção: ')
opcao = opcao.lower().strip()
#strip tira os espaços do início e do fim 
# passa pro lower e dps tira os espaços - chamar de forma encadeada
if opcao in opcoes: 
    print('ok')
else: 
    print('inválido')

#dict
opcoes = {
    'sim': ['sim', 's', 'y'],
    'nao': ['não', 'n', 'nao'],
}
