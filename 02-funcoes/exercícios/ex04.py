candidato1 = 0 
candidato2 = 0
candidato3 = 0
continuar = 1

def simuladorEleicoes(candidatos): 
    #usar a função max(..)
    print('Seja bem-vindo ao Simulador de Eleições')
    continuar = 1 
    while continuar==1:
        opcao = int(input('Qual candidato deseja votar? \n1.Candidato 1\n2.Candidato 2\n3.Candidato 3\n'))
        match opcao:
            case 1: 
                candidatos[0]+=1
            case 2: 
                candidatos[1]+=1
            case 3: 
                candidatos[2]+=1
        continuar = int(input('Deseja continuar? Digite 1 para continuar e outro número qualquer para sair\n'))
    #chegando no candidato vencedor
    maior = candidatos[0] 
    vencedor='O vencedor é candidato 1'
    if candidatos[1]>maior:
        vencedor = 'O vencedor é o candidato 2'
        maior=candidatos[1]
    elif candidatos[1]==maior: 
        vencedor='Houve empate entre os candidatos'
    elif candidatos[2]>maior: 
        vencedor='O vencedor é candidato 3'
        maior=candidatos[2]
    elif candidatos[2]==maior: 
        vencedor='Houve empate entre os candidatos'
    return f'{vencedor} \nQuantidade de votos de cada candidato: \nCandidato 1: {candidatos[0]}\nCandidato 2: {candidatos[1]}\nCandidato 3: {candidatos[2]}'

#chamando a função
print(simuladorEleicoes([candidato1,candidato2,candidato3]))
