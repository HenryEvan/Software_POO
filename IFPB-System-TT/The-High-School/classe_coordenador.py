# Importações:

import os

# Classe Coordenador:

class Coordenador:

    # Inicializações:

    def __init__(self): # Ok!
    
        self.__Mani_MateProf = ['composição']      # Criar Manipulação de Matéria e Professor em RAM     
        self.__Mani_Ques = ['composição']          # Criar Manipulação de Questões em RAM
        self.__Mani_HistProv = ['composição']      # Criar Manipulação de Histórico de Provas em RAM
        self.__Mani_ListQuest = ['']               # Criar Manipulação de Lista de Questões em RAM
       
    def set_start_arquivos(self): # Ok!

        os.mkdir('.\Gerenciamento') #ListExProv

        self.__Arm_MateProf = open('.\Gerenciamento\MateProf.txt','w')     # Criar Armazem Matéria e Professor
        self.__Arm_Ques = open('.\Gerenciamento\Ques.txt','w')             # Criar Armazem Questões
        self.__Arm_HistProv = open('.\Gerenciamento\HistProv.txt','w')     # Criar Armazem Histórico de Provas
        self.__Arm_ListQuest = open('.\Gerenciamento\ListQues.txt','w')    # Criar Armazem Lista de Questões
        self.__Arm_ListExProv = open('.\Gerenciamento\ListExProv.txt','w') # Criar Armazem Lista de Exercicios ou Provas

    def get_tam_senhas(self): # Ok!
        self.__escanear_senhas = open('.\Senhas\Matrículas coordenadores.txt','r')  # escanear senhas
        self.__número_senhas = len(self.__escanear_senhas.readlines())              # quantidade senhas
        return self.__número_senhas    

    def set_autenticação_coor(self, entrada_senha): # Ok!
        self.__escanear_senhas = open('.\Senhas\Matrículas coordenadores.txt','r')  # escanear senhas
        self.__entrada_senha = entrada_senha                                        # pegar entrada da senha digitada
        __contador = Coordenador().get_tam_senhas()
        for i in range(__contador):                                                 # loop para testar senhas
            self.__scan = self.__escanear_senhas.readline().split('-')              # quebrar a linha lida
#        senha_alvo = scan[8:14] (Segurança: Definir tamanho de senha.)             # "Códigos para restrição de tipo de senha, caso necessário"
#        nome_alvo = scan[15::] (Ou mantenha um split+[x] para autoadaptação.)
            self.__senha_alvo = self.__scan[1]
            self.__nome_alvo = self.__scan[2]
            if self.__entrada_senha == self.__senha_alvo:                           # Comparador de aprovação
                self.__resposta = '1'+self.__nome_alvo
                __contador = 0
                return self.__resposta
            else:                                                                   # Comparador de negação
                self.__resposta = '0'
                __contador = 0
                return self.__resposta

    # Retornos de Informações:

    def get_tamanho_sistema(self): # Ok!
        
        variavel_a = len(self.__Mani_MateProf)
        variavel_b = len(self.__Mani_Ques)
        variavel_c = len(self.__Mani_HistProv)
        variavel_d = len(self.__Mani_ListQuest)
        __soma_variaveis = variavel_a + variavel_b + variavel_c + variavel_d
        if __soma_variaveis == 0:
            self.__resposta = 0
        if (variavel_a == 0) or (variavel_b == 0) or (variavel_c == 0) or (variavel_d == 0):
            if __soma_variaveis != 0:
                self.__resposta = 1
        if (variavel_a != 0) and (variavel_b != 0) and (variavel_c != 0) and (variavel_d != 0):
            self.__resposta = 2             
        return self.__resposta

    def get_professores_cadastrados(self):
        ler_matérias = open('.\Gerenciamento\MateProf.txt','r')
        
    # Login:

    def info_menu_coordenador(nome): # Ok!
        print(f'\nBem-vindo ao sistema Coordenador {nome}.\n')
        Coordenador.set_nome(nome)

    def login_coordenador(self, nome): # Ok!
        Coordenador.info_menu_coordenador(nome)
        self.__nome_global = None
        print('Menu:\n\n1 - Visualizar Todas Questões\n2 - Cadastrar Disciplina\n3 - Cadastrar Professor a Disciplina\n4 - Atribuir Avaliadores a Questões\n5 - Deslogar\n\n')
        __entrada_pós_login = input('> ')

        if __entrada_pós_login == '1':
            print('\n'*49)
            Coordenador().visualizar_todas_questões()
            Coordenador().login_coordenador(Coordenador.get_nome())
           
        if __entrada_pós_login == '2':
            print('\n'*49)
            print('Falta implementar do arquivo x.')
#            Coordenador().cadastrar_discipl()
            Coordenador().login_coordenador(Coordenador.get_nome())
            
        if __entrada_pós_login == '3':
            print('\n'*49)
            print('Falta implementar do arquivo x.')
#            Coordenador().cadastrar_discipl()
            Coordenador().login_coordenador(Coordenador.get_nome())     
            
        if __entrada_pós_login == '4':
            print('\n'*49)
            print('\nVer atuais questões e atribuições para professores:\n')
            
            __atrib = open('.\Gerenciamento\Indicações.txt','r')
            __n_indic = len(__atrib.readlines())
            __atrib.close()
            __atrib = open('.\Gerenciamento\Indicações.txt','r')

            for i in range(__n_indic):
                __atr_alvo = __atrib.readline()
                __atr_spli = __atr_alvo.split('-')
                if (__atr_alvo != ''):
                    __prof = __atr_spli[0]
                    __Q_L = __atr_spli[1]
                    print(f'{i} - {__prof}: {__Q_L}',end='')
                    
            __atrib.close()
            print('\n'*4)

            __atrib = open('.\Gerenciamento\Indicações.txt','r')
            __mod_linh = int(input('Qual linha você deseja mudar? '))
            print('Lembrete... Indicações tem que estar preenchido para isso não crashar.. Corrigir..\nOlhar arquivo X para implementar correção.. Já funcional..')
            for i in range(__mod_linh):
                __atr_alvo = __atrib.readline()
                __atr_spli = __atr_alvo.split('-')
                if (__mod_linh == i):
                    __prof = __atr_spli[0]
                    __Q_L = __atr_spli[1]
                    print(f'{i} - {__prof}: {__Q_L}',end='')
            __atrib.close()
            
            __entr = input('> ')
            
            Coordenador().cadastrar_avaliad(__entr, __mod_linh, __n_indic) 
            Coordenador().login_coordenador(Coordenador.get_nome())

        if __entrada_pós_login == '5':
            print('\n'*49)
            Coordenador.deslogar()
          
        # Opções:

    def visualizar_todas_questões(self):
        __list_quest_2 = open('.\Gerenciamento\Ques.txt','r')
        self.__tamanho_quest_2 = len(__list_quest_2.readlines())
        __list_quest_2.close()
        __list_quest_2 = open('.\Gerenciamento\Ques.txt','r')     
        for i in range(self.__tamanho_quest_2):
            __splited_q_2 = __list_quest_2.readline().split('-')
            __QX = __splited_q_2[0]
            __MX = __splited_q_2[1]
            __AFX = __splited_q_2[2]
            __PX = __splited_q_2[3]
            __RX = __splited_q_2[4]
            __NX = __splited_q_2[5]
            __ATRX = __splited_q_2[6]
            __SITX = __splited_q_2[7]
            if __AFX == '1':
                print(f'\n\nIndice no Banco de Dados: {__QX}\nMatéria: {__MX}\nTipo de Questão A&F: {__AFX}\n\nPergunta: {__PX}\n\nResposta: {__RX}\n\nUsuário Criador: {__NX}')
                print('\n',('~'*30))
            if __AFX == '2':
                print(f'\n\nIndice no Banco de Dados: {__QX}\nMatéria: {__MX}\nTipo de Questão A&F: {__AFX}\n\nPergunta: {__PX}\n\nResposta: {__RX}\n\nUsuário Criador: {__NX}')
                print('\n',('~'*30))

    def cadastrar_discipl(self):
        self.__global_met = None
        __matérias_arq = open('.\Gerenciamento\MateProf.txt','r')
        print(__matérias_arq.read())
        __matérias_arq.close()
        __matérias_arq = open('.\Gerenciamento\MateProf.txt','w')
        print('\n\nModificações:\n\n')
        __strmdf = string
        if __strmdf != '': 
            __matérias_arq.write(__strmdf)

    def cadastrar_avaliad(self, string, m_string, tam):
        self.__global_met_3 = None
        __matérias_arq_3 = open('.\Gerenciamento\Indicações.txt','r')
        print('\n\n',__matérias_arq_3.read())
        __matérias_arq_3.close()
        __matérias_arq_3 = open('.\Gerenciamento\Indicações.txt','w')
        print('\n\nModificações:\n\n')
        __strmdf_3 = string
        __tamn_3 = tam
        __m_string = m_string
        
        if __strmdf_3 != '':
            for i in range(int(__tamn_3)):
                __strmdf_3 = (f'{__strmdf_3}')
                
                __matérias_arq_3.write(__strmdf_3) 

    def deslogar():
        print('\n\nDeslogando e saindo...\n')

    # Outros:

    def clear():
        print('\n'*49)

    def set_nome(nome):
        global __nome
        __nome = nome

    def get_nome():
        return __nome

