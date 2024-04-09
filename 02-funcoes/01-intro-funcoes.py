#Funções -> diminui a qtd de código se tem duplicação de código 
# mini programa -. uma entrada, processamento e saída 
# declaração e a chamada da função 
#Final da função pela endentação 
#Declaração 
# def nome_da_func (parametros): 
#     return -> retorno da função 

#Qual a dif entre parâmetro e argumento?
# Parâmetro -> referencia definida na assinatura da função 
# Argumento -> é valor ou referência passada ou enviada para um parâmetro -> pode passar o valor literal, uma variável ou a chamada de uma funcao  

print("Olá") #aqui está fazendo a chamada, o print já foi declarado 
#sum() ai somar uma sequencia de valores 

#Função sem retorno e sem parâmetro 
def imprimir_saudacao():
    print("Maria maria é um DOM")

#Função sem retorno e com parâmetro 
def imprimir_nome(nome):
    print(f'Nome: {nome}')

#Função com retorno e sem parâmetro 
def gerar_saudacao(): 
    return "Bom dia!"

#Função com retorno e com parâmetro 
#quando ñ chamou o argumento é nenhum 
# no python no tem sobrecarga, ou seja, funcoes com mesmo nome e assinaturas diferentes 
def gerar_saudacao_para(nome): 
    return f'Bom dia {nome}'
#chamada
imprimir_saudacao()
imprimir_nome("Millena")
print(gerar_saudacao())
print(gerar_saudacao_para('Millena'))
#"Millena" é argumento, enquanto (nome) é o parâmetro

# o melhor caso do uso dos funções -> utilizar funções com paramentros e retorno 
# Bom dia NOME (NOME é dinamico)


#Função pura -> não tem efeito colateral -> nao faz nada no sistema, tipo um IO -> e sem acesso a estado global 
#sem parametro com retorno não é bom 
def gerar_saudacao(nome): 
    return f"Bom dia, {nome}"

#pq as vzs ñ quer imprimir, ajuda a salvar, colocar num email 


#Calcule a média das notas de vários alunos 
#entrada = [[10,6],[7,9],[10,8]] -> duas notas de cada aluno
# calcular_media -> lista de notas -> media
# calcular_medias -> lista de lista de notas -> lista de médias

notasAlunos = [
    [10.0, 4.0], 
    [9.0, 6.0],
    [8.0, 7.0]
]

def calcular_media(notas): 
    return sum(notas)/len(notas)

def calcular_medias(notasAlunos):
    return [calcular_media(notas) for notas in notasAlunos]

#media = []
#for notas in notasAlunos: 
#   medias.append(calcular_media(notas))
#   return medias    

print(calcular_medias(notasAlunos)) #pq passou por um for -> para acessar as listas de cada aluno, por isso conseguiu mandar a lista para dentro de notas 


#Argumentos nomeados: 
# falar pra qual parametro vai sem seguir a ordem que foi colocada 

def nova_saudacao(nome, saudacao):
    return f'{saudacao}, {nome}'

print(nova_saudacao('Joao', 'Bom dia'))
print(nova_saudacao('Pedro', 'Boa noite'))
print(nova_saudacao(nome='Joao', saudacao='Bom dia'))
print(nova_saudacao(saudacao='Joao', nome='Bom dia'))
#se nomeou um tem que nomear todos 
#pode nomear aos ultimos, sem nomear os primeiros 


print("Olá", "Mundo", sep=", ", end=".\n")
#sep acessível via argumento nomeado


#Valores padrão para parâmetros: 
#Simular a sobrecarga
def obter_saudacao(nome, saudacao="Bom dia"):
    return f'{saudacao}, {nome}'

print(obter_saudacao("Pedro"))
print(obter_saudacao('Mih', 'Boa tarde'))


# *args(Non-Keyword Arguments)
def calcularMedia(notas):
    print(type(notas))
    return sum(notas)/len(notas)

calcularMedia([10.0, 7.0, 8.0])
calcularMedia((10.0, 8.0, 7.0))

def calcularMedia(*notas):
    return sum(notas)/len(notas)
# * pode passar qualquer numero de valores - qtd de argumentos que vc quiser e o python transforma em uma tupla
print(calcularMedia(10.0, 4.0, 8.0))#vai entender que são tres valores 


#def cpmtar_vogais_conso(): -> retorna um dicionário 