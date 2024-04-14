palavraOculta = 'bicicleta'
#pode cometer no máximo 6 erros 

def forca(palavra):
    print('Vamos jogar forca!')
    tamanho = len(palavra)
    print(f'A palavra oculta possui {tamanho} letras')
    palavraForca = '_ ' * tamanho
    print(palavraForca)
    qtdErros = 0
    while qtdErros<6: 
        letra = input('Chute uma letra: ') 
        for i in range(0,tamanho): 
            if palavra[i]==letra: 
                posicao = i*2
                palavraForca = palavraForca[:posicao] + letra + palavraForca[posicao + 1:]
            else: 
                qtdErros+=1
                print(f'Você errou, pode errar apenas mais {6-qtdErros} vezes')  
            print(palavraForca)   
           
forca(palavraOculta)