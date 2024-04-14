frase = input('Entre com uma frase :)')

def contagemPalavras(frase):
    frase = frase.lower()
    dicionario = {}
    palavras = frase.split()
    print(palavras)
    for palavra in palavras: 
        if palavra in dicionario.keys():
            dicionario[palavra]+=1
        else:
            dicionario[palavra]=1
    return dicionario

print(contagemPalavras(frase))