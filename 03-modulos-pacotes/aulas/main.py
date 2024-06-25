"""
parece importação de biblioteca 
"""
import matematica #importando um módulo  -> tem várias opções que são do python
#importa tudo do módulo desse jeito 
from matematica import PI as PI_MAT,somar #aqui fala especificamente o que eu querio importar  
#desse jeito consegue importar sem precisar "chmar" o módulo antes -> somar(10,10)
#from matematica import * (para importar tudo) -> acesso direto 
 
from estatistica.descritiva import media, maximo, minimo
from estatistica.inferencial import VALOR
print(matematica.PI) #para coseguir acessar coloca o nome do módulo e dps o que vc quer 
print(matematica.somar(10,10))
print(somar(9,9)) #por causa do from não prevcisa coliocar o matematica. 

PI = 99
print(PI_MAT,PI)

# from matematica import somar as somar_mat, PI as PI_MAT -> mais usado para classe -> pq ela pode ter o mesmo nome nesse módulo e no módulo importado
# no modulo define as funcoes e classes  

"""
módulos com 100 funções -> quebra em 3 módulos diferentes -> pacotes 
pacotes -> entre médio e grande -> em algumas situações só 
pacotes são pastas -> sempre num diretório
python não entede como um pacote, precisa colocar um arquivo especial dentro dela -> para o python reconhecer como pacote
"""

