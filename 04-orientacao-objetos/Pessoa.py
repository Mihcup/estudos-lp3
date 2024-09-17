class Pessoa: 
    def __init__(self, nome, prontuario, idade): 
        self.__nome = nome 
        self.__prontuario = prontuario 
        self.__idade = idade
    
    def getNome (self): 
        return self.__nome
    
    def setNome (self, nome): 
        self.__nome = nome 

    def getProntuario(self): 
        return self.__prontuario
    
    def setProntuario (self, prontuario): 
        self.__prontuario= prontuario

    def getIdade(self): 
        return self.__idade
    
    def setIdade(self, idade): 
        self.__idade = idade  