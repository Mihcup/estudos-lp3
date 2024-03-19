# for, while, break, continue
# operador in - serve para fazer o foreach
for letra in 'Python': 
    print(letra)
    #vai pegar cada letra e passar para a variável "letra"

itens = ['banana', 'arroz', 'limão']
alunos = ['Maria', 'Pedro']

for item in itens: 
    print(item)


for i in range(5):
    print(i)

for i in range(0,11,2):
    print(i)

lista = list(range(101)) # criar uma lista de zero a cem
print(type(lista))

#while
contador = 0
while contador <=5:
    print(contador)
    contador +=1 

#ñ tem do while 

#break 
# encontre o primeiro numero par
numeros = [1,3,4,5,8,11]

for numero in numeros: 
    if numero % 2 == 0:
        print(numero)
        break

#continue
numeros = [3,-1,3,0,-2]
for numero in numeros: 
    if numero<=0: 
        continue
    print(numero)
#mudar a lógica
for numero in numeros: 
    if numero>0:
        print(numero)

#compreensão de lista
#forma consisa de criar listas em python 

numeros = [2,3,4,5,6]
quadrados = []
#criar a lista de quadrados
for numero in numeros: 
    quadrados.append(numero**2)

quadrados = [numero ** 2 for numero in numeros] # é a forma consisa e coloca dentro de uma lista
print(quadrados)

palavra = 'Olá mundo'
letras = [letra for letra in palavra]
letras = [letra.upper() for letra in palavra]
print(letras)
#compreensão de listas - uma lista na outra

numeros = [1,2,3,4,5,6,7,8,9,10]
pares = [numero for numero in numeros if numero % 2 == 0]
#não dá para colocar else, pq o if é só um filtro 
print(pares)