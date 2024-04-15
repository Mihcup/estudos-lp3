frase = input('Entre com uma frase :)')

def contagemPalavras(frase):
    fraseSemPontuacao = frase.replace('.', '').replace(',', '')
    fraseSemPontuacao = fraseSemPontuacao.lower()
    dicionario = {}
    palavras = fraseSemPontuacao.split()
    for palavra in palavras: 
        if palavra in dicionario.keys():
            dicionario[palavra]+=1
        else:
            dicionario[palavra]=1
    return dicionario

print(contagemPalavras(frase))