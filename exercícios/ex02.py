n = int(input('Entre com um valor inteiro:'))

def tabuada(numero): 
    tabuada = []
    for i in range(1,11,1): 
        tabuada.append(i*numero)
    return tabuada 

print(tabuada(n))