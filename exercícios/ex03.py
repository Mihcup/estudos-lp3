frase = input('Digite uma frase: ')

#definindo a função
def contadorVogaisConsoantes (frase):
    frase = frase.lower()
    #removendo os espaços para que eles não sejam contados
    frase = frase.replace(" ","")
    #removendo acentos e cedilhas
    frase = frase.replace("á","a")
    frase = frase.replace("à","a")
    frase = frase.replace("ã","a")
    frase = frase.replace("é","e")
    frase = frase.replace("ê","e")
    frase = frase.replace("í","i")
    frase = frase.replace("ó","o")
    frase = frase.replace("ô","o")
    frase = frase.replace("ú","u")
    frase = frase.replace("ç","c")
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

#chamando a função
print(contadorVogaisConsoantes(frase))
