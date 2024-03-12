# 1.Numérico: 
# int, float, complex

# int
idade = 17
# float
altura = 1.60 

#2. Bool
verdade = True 
mentira = False 

# 3. Strings 
#sequência de caracteres - pode acessar cada caracter individualmente 

nome = 'Millena'
Nome = "Mih"

#multilinha - manter a formatação da string
frase = """Olá mundo, 
Como você está?
Teste
"""
print(frase)

#interpolação de string - "Concatenar"
# f-string - tudo que for variável coloca entre chaves 
nome1 = 'João Campos'
idade1= 20 
frase1 = f'Olá {nome1}. Você tem {idade1} anos'
print(frase1)

#char é uma string de um caracter só


nome2 = 'SILVIO santos'
primeiraLetra = nome2[0]
print(nome2[-1])
print(nome2[-3])

#String são objetos 
# instanciar uma String - variável do tipo String que aponta para um objeto da String 
print(nome2.capitalize())
nome2.upper() #retorna uma nova String em maiúsculo 

# 4.list
#lista de valores
#indexada
#pode ser alterada 
habilidades = [] #uma lista vazia
habilidades = ['ingles','ler','linguagem c, java']
habilidades[1] # pode ser uma lista, uma tupla, uma string
#dá para usar os índices negativos também 

habilidades.append('JavaScript')
#append adicionar no final da lista 
habilidades.insert(2,'csss')
# uma lista ñ é só e um tipo - ñ precisa usar 
habilidades.insert(True,'html')
#converte o True para 1 
print(habilidades)
#algorismo do insert sempre empurra 
#habilidades.clear() #deixa a lista vazia 

#para cada habilidade
for habilidade in habilidades: 
    print(habilidade)

#função
def somar(n1,n2=2):
    return n1+n2
somar(10.0,2.0)
somar(n2=10.0,n1=2.0)

# 5. Tuple - "meio que lista de valores" que não pode ser alterada, ñ pode inserir, nem retirar 
opcoes = ('sim','não','talvez')
print(opcoes[0])
#no muda durante a execução do cóigo 
for opcao in opcoes: 
    print(opcao)

#set - conjunto de valores 
# não permite elementos duplicados e não é indexado 
habilidades = {'python','java','c','java'} #ñ adiciona o java novamente 
print(habilidades)
#habilidades[0] - ñ funciona 

# 6. dict(dicionário)
# palavra -> definição 
#conjunto de chave e valor
# chave -> valor
# key -> value 

nome = 'Pedro Alves'
idade = 17 
habilidades = ['Java','C#','CSS']
empregado = True 
#caracteríticas do canditado 

#conjunto de chave valor 
candidato = {
    'nome': 'Pedro Alves',
    'idade': 17,
    'habilidades':['Java','C#','CSS'],
    'empregado':True
}
print(candidato.keys())
print(candidato.values())
print(candidato['nome'])

# 7.None - nulo 
nome = None 
#None é o tipo e o literal 
#serve para quando precisar inicializar 