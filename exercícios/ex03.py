frase = input('Digite uma frase: ')
#https://wiki.python.org.br/ContaLetras
def contadorVogaisConsoantes (frase):
    contador = {
        'vogais' : 0, 
        'consoantes': 0
    }
    for i in frase: 
        if i in 'aeiou': 
            contador['vogais']+=1 
        else: 
            contador['consoantes']+=1 
    
    return contador 

print(contadorVogaisConsoantes(frase))
