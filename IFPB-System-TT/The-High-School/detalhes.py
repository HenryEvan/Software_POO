# Detalhes:

class Detalhes:

    def __init__(self):
        
        self.__autores = 'Anderson Henrique e Felipe Cardoso'
        self.__versão = None
                       
    def get_versão(self):

        __versão_visu_1 = open('versão.txt','r')
        self.__versão = __versão_visu_1.readline()[9::]
        return self.__versão
        
    def get_autores(self):

        return self.__autores
