# if, if/else, if/elif/else

#if
#bloco precisa estar endentado e depois dos dois pontos - tipo a chave
idade = 20 
if idade >=18: 
    print('Maior de idade')

#if/else
if idade >=18: 
    print('Maior de idade')
else: 
    print('Menor de idade')

#if/elif/else
# criança  = 0-12
# adolescente = 13 - 17
# adulto = 18 - 59
# idoso = 60+ 
if idade<=12: 
    print('Criança')
elif idade<=17:
    print('Adolescente')
elif idade<=59: 
    print('Adulto')
else: 
    print('Idoso') 

#exemplo de if aninhado - não é bom assim 
email = 'admin@gmail.com'
senha = '123'

#ruim
if email == 'admin@gmail.com':
    if senha=='123':
    #aqui é um and
        print('Acesso permitido')
    else:
        print('Inválido')
else:
    print('Inválido')

#bom
if email=='admin@gmail.com' and senha=='123': 
    print('Acesso permitido')
else:
    print('Inválido')

#entrada numero
# 1 - Domingo 
# 2 - Segunda
# 3 - Terça
# 4 - Quarta
# 5 - Quinta
# 6 - Sexta
# 7 - Sábado na balada
dia = 4
#manutenção do código é melhor 
dias = {
    1: 'Domingo', 
    2: 'Segunda', 
    3: 'Terça', 
    4: 'Quarta',
    5: 'Quinta', 
    6: 'Sexta',
    7: 'Sábado'
}

if dia in dias: 
    print(dias[dia])

#ñ tem switch case - match (mais poderoso)
