'''
Módulo - qualquer arquivo .py 
pode importar qualquer coisa para outros arquivos 
arquvi matematica.py -> funções matemáticas e tentar usar isso desse módulo em outro módulo 
'''
#import estatistica.descritiva
#print(estatistica.descritiva.maximo([10, 9, 8]))

PI = 3.14159

#só definir as funções, não vai usar aqui -> por causa do módulo 
#ao invés de imprimir, retornar o valor 
#definição 
def somar(n1,n2):
    return n1+n2

def subtrair(n1,n2):
    return n1-n2
