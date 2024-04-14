conteudo = input('Entre com uma frase: ')

#função
def palindromo(conteudo):
    tamanho = len(conteudo)
    conteudo = conteudo.lower()
    conteudo = conteudo.replace(" ","")
    contrario= conteudo[::-1]
    if contrario==conteudo:
        return 'É um palíndromo'
    else: 
        return 'Não é um palíndromo'

#chamando a função
print(palindromo(conteudo))