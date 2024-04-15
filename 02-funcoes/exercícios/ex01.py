import random 
valorAleatorio = random.randrange(1,101)
entradaInicial = int(input('Qual é o seu palpite? '))

def jogoDeAdivinhacao (entrada,aleatorio): 
    while entrada!=aleatorio: 
        if entrada> aleatorio: 
            print('Seu palpite está alto')
        else: 
            print("Seu palpite está baixo")
        entrada = int(input('Tente novamente!'))
    return 'Você acertou!'

print(jogoDeAdivinhacao(entradaInicial, valorAleatorio))
