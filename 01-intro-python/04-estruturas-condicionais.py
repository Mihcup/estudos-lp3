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

# operador ternário: 
idade = 20 
#status  #conteudo de status depender da idade 
status = 'Maior de idade' if idade>=18 else 'Menor de idade'
'''
resume tal codigo: 
if idade>=18:
    status = 'maior de idade'
else
    status = 'menor de idade'
'''


# match case - para substituir o uso de elif, e pode ser entendido como o switch case, porém + poderoso que ele
dia = 3
match dia:
    case 1: 
        print('Domingo')
    case 2: 
       print('Segunda')
    case 3: 
        print('Terça')
    case _: 
        print('Inválido') 
#case _ -> default 

#imprimir: 
# 1 e 7 - fim de semana
# 2, 3, 4, 5, 6 - dia útil
# avaliar várias coisas, agrupando cases
# | -> não é um or (mas parece) só ñ retorna um booleano

match dia:
    case 1 | 7:
        print('fim de semana')
    case 2 | 3 | 4 | 5 | 6: 
        print('dia útil')
    case _: 
        print('dia inválido')