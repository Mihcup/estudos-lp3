from math import pow
faixas ={
    "Baixo peso": (0,18.4), 
    "Peso normal": (18.5,24.9), 
    "Excesso de peso": (25.0,29.9),
    "Obesidade de Classe 1": (30.0,34.9),
    "Obesidade de Classe 2": (35.0,39.9),
    "Obesidade de Classe 3": (40.0,float('inf'))
}

def calcular_imc(peso,altura):
    imc = round((peso/pow(altura,2)),1)
    #coloquei uma casa decimal, pois a classificação indicada possui apenas uma casa decimal 
    for classificacao, (min,max) in faixas.items():
        if imc>=min and imc<=max:
            classificacao_pessoa = classificacao
            print(classificacao)
    frase = perda_ou_ganho(classificacao_pessoa,altura=altura,peso=peso)
    return imc,classificacao_pessoa,frase

def perda_ou_ganho(classificacao, peso, altura): 
    if classificacao == "Peso normal": 
        status="Como seu IMC está ideal, não há necessidade de perder ou ganhar peso, mas cuide sempre de sua saúde"
    elif classificacao == "Baixo peso":
        min = round(((pow(altura,2)*18.5) - peso),2)
        max = round(((pow(altura,2)*24.9) - peso),2)
        status = f"Você deve ganhar de {min}kg a {max}kg"
    else: 
        max = round((peso - (pow(altura,2)*18.5)),2)
        min = round((peso - (pow(altura,2)*24.9)),2)
        status = f'Você deve perder de {min}kg a {max}kg'
    
    return status

