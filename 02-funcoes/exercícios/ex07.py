#pode cometer no máximo 6 erros 
#Função que verifica se a letra está na palavra e a insere 
def verificarLetra(palavra, palavraForca,qtdErro):
    letra = input('Chute uma letra: ') 
    tamanho = len(palavra)
    encontrouLetra = False
    ganhou = False
    for i in range(0,tamanho): 
        if palavra[i]==letra: 
            posicao = i*2
            palavraForca = palavraForca[:posicao] + letra + palavraForca[posicao + 1:]
            encontrouLetra=True
    if not encontrouLetra:
        print(f'Essa letra não está na palavra. Você já cometeu {qtdErro+1} erro(s)')
        qtdErro += 1
    forcaPalavra = palavraForca.replace(' ','')
    if forcaPalavra==palavra:
        print('Parabéns você ganhou')
        ganhou=True
    return palavraForca, letra, ganhou, qtdErro

#Função que verifica o chute do usuário 
def verificarPalavra(palavra,qtdErro): 
    palavraInserida = input('Insira a seu chute: ')
    palavraInserida = palavraInserida.lower()
    if palavraInserida==palavra: 
        print('Você acertou :)')
        return True, qtdErro
    else: 
        print(f'Palavra errada! Você já cometeu {qtdErro+1} erro(s)')
        qtdErro+=1
        return False,qtdErro
#Função que realiza as principais manipulações da forca 
def forca(palavra):
    print('Vamos jogar forca!')
    print('Você pode cometer apenas 5 erros, tome cuidado!')
    tamanho = len(palavra)
    print(f'A palavra oculta possui {tamanho} letras')
    palavraForca = '_ ' * tamanho
    print(palavraForca,'\n')
    qtdErros = 0
    cont = 0
    letrasInseridas=''
    ganhou = False
    while qtdErros<=5 and not ganhou: 
        print('--------------------------------------------------------------')
        print(f'{cont+1}ª rodada (s)')
        if cont>0:
            print(f'Você ja chutou a(s) seguinte(s) letra(s): {letrasInseridas}')
        
        if cont>3: 
            escolha = int(input('A partir dessa rodada você pode tentar chutar uma palavra - \nDigite 1 para chutar uma palavra e 2 para chutar uma letra\n'))
            if escolha==1: 
                ganhou,erro = verificarPalavra(palavra,qtdErros)
                qtdErros+=erro
                if ganhou:
                    palavraForca='b i c i c l e t a'
            elif escolha==2: 
                letra = ''
                palavraForca,letra,ganhou,qtdErros = verificarLetra(palavra,palavraForca,qtdErros)
                letrasInseridas+=letra+' '
        else: 
            letra = ''
            palavraForca,letra,ganhou,qtdErros = verificarLetra(palavra,palavraForca,qtdErros)
            letrasInseridas+=letra+' '
        
        print(palavraForca)   
        cont+=1

print('FIM DE JOGO')

palavraOculta = 'bicicleta'
forca(palavraOculta)