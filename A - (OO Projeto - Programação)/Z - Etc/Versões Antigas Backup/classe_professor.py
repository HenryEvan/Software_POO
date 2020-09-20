# Importações:

import os
from classe_coordenador import Coordenador
chamar_coordenador = Coordenador()

# Classe Professor:

class Professor:

    def __init__(self):

        self.x = None

    # Autenticações:

    def get_tam_senhas(self): # Ok!
        self.__escanear_senhas = open('.\Senhas\Matrículas professores.txt','r')    # escanear senhas
        self.__número_senhas = len(self.__escanear_senhas.readlines())              # quantidade senhas
        return self.__número_senhas    

    def set_autenticação_prof(self, entrada_senha): # Ok!
        self.__escanear_senhas = open('.\Senhas\Matrículas professores.txt','r')    # escanear senhas
        self.__entrada_senha = entrada_senha                                        # pegar entrada da senha digitada
        __contador = Professor().get_tam_senhas()
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

    # Login:

    def info_menu_professor(nome):
        print(f'\nBem-vindo ao sistema Professor {nome}.\n')
        Professor.set_nome(nome)

    def login_professor(self, nome): # Ok!
        Professor.info_menu_professor(nome)
        print('Menu:\n\n1 - Cadastrar Questão\n2 - Minhas Questões\n3 - Gerar exercício ou prova\n4 - Acessar provas anteriores e gabaritos\n5 - Avaliar questões de outros professores\n6 - Deslogar\n\n')
        __entrada_pós_login = input('> ')

        if __entrada_pós_login == '1':
            Professor.clear()
            Professor().cadastrar_quest()
            print('\nQuestão cadastrada com sucesso.\nVoltando ao menu...\n\n')
            Professor.clear()
            Professor().login_professor(Professor.get_nome())

        if __entrada_pós_login == '2':
            Professor.clear()
            print('Verificar as suas questões do sistema:\n\n')
            __minhas_questões = Professor().minhas_questões(Professor.get_nome())
            print(f'Suas Questões do sistema são as: {__minhas_questões}\nVoltando ao menu...\n\n')
            Professor().login_professor(Professor.get_nome())            

        if __entrada_pós_login == '3':
            Professor.clear()
            print('Gerar Exercício ou Prova:\n\n1 - Exercício\n2 - Prova\n')
            __exouprov_entrada = input('> ')
            if __exouprov_entrada == '1':
                __exouprov_defin = 'Prova'
                __temp_nome = 'seu exercício'
            if __exouprov_entrada == '2':
                __exouprov_defin = 'Exercício'
                __temp_nome = 'sua prova'
            print(f'\n\nEscolha o nome de {__temp_nome}:\n')
            __nome_de_exouprov = input('> ')
            print(f'\n\nEscolha as questões de uma matéria para formar {__temp_nome}:\n\n')
            __matéria_escolhida = input('Matéria: ')
#           __matéria_escolhida_dp = []
#           __questões_buscador = open('.\Gerenciamento\Ques.txt','r')
#           __contador_de_questões = __questões_buscador.read()
#           __contar_questões = __contador_de_questões.replace('\n','')
#           __n_de_quest = len(__contar_questões)
#           __questões_buscador.close()
#           __leitor_alvo_leitura = open('.\Gerenciamento\Ques.txt','r')
#           for i in range(__n_de_quest):
#               leitura_2 = __leitor_alvo_leitura.readline()
#               if leitura_2 != '':
#                   alvo_splitado_2 = leitura_2.split('-')
#                   if (alvo_splitado_2[7] == 1):
#                       __matéria_escolhida_dp[i] = alvo_splitado_2[0]
#           qnt_dp = len(__matéria_escolhida_dp)
            print(f'\n\nQuestões disponíveis de {__matéria_escolhida}:\n\n')
#            for i in range(qnt_dp):
            print(Professor().listar_todas_questões_met())
            __quantidade_de_questões = int(input('\nSerão quantas questões? '))
            __questões_escolhidas = []
            for i in range(__quantidade_de_questões):
                __questões_escolhidas.append(input(f'\nIndice da questão n.{i+1}: '))
            confirm_dp = input('\n\nConfirma?\n\n1 - Sim\n2 - Não\n\n')
            if confirm_dp == '1':
                Professor().gerarexouprov(__exouprov_defin, __nome_de_exouprov, __matéria_escolhida, __questões_escolhidas, __quantidade_de_questões)
                Professor.clear()
                print(f'Bem, {__temp_nome} foi criado com sucesso.\nVoltando ao menu...\n\n')
                Professor().login_professor(Professor.get_nome())
            if confirm_dp == '2':
                print('\nVoltando ao menu...\n\n')
                Professor().login_professor(Professor.get_nome())

        if __entrada_pós_login == '4':
            Professor.clear()
            Professor().acessar_hist()
            print('\nVoltando ao menu...\n\n')
            Professor().login_professor(Professor.get_nome())

            
        if __entrada_pós_login == '5':
            Professor.clear()
            Professor().avaliar_quest()

        if __entrada_pós_login == '6':
            Professor.clear()
            Professor().deslogar()

    # Opções:

    def cadastrar_quest(self): # ----------------------------------------------------------------------------------------------
        __atribuição = [0, 0, 0]
        __situação = 3        
        __questões_buscador = open('.\Gerenciamento\Ques.txt','r')                             # Len de quantidade de questões.
        __contador_de_questões = __questões_buscador.read()
        __contar_questões = __contador_de_questões.replace('\n','')
        self.__n_de_quest = len(__contar_questões)
        __questões_buscador.close()
        print('Criar uma questão:\n\n1 - Questão Aberta\n2 - Questão Fechada\n')               # Cria uma questão.
        __primeira_entrada = input('> ')
        if __primeira_entrada == '1':
            __tipo_de_questão = '1'
            Professor.clear()
            print('Pergunta:\n')
            __pergunta = input('> ')
            Professor.clear()
            print(f'Pergunta:\n{__pergunta}\n\nResposta:\n')
            __resposta = input('> ')
            __recomendação = input('\n\nQual é a matéria recomendada para essa questão? ')
            Professor.clear()         
        if __primeira_entrada == '2':
            __tipo_de_questão = '2'
            Professor.clear()
            __numero_de_respostas = int(input('Quantas respostas terá na questão? '))
            Professor.clear()
            print(f'Quantas respostas terá na questão? {__numero_de_respostas}\n\nPergunta:\n')
            __pergunta = input('> ')
            Professor.clear()
            __resposta = []
            print(f'\nPergunta:\n{__pergunta}')
            for i in range(__numero_de_respostas):           
                print(f'\n{i+1}° Resposta:\n')
                __resposta.append(input('> '))
            __recomendação = input('\n\nQual é a matéria recomendada para essa questão? ')
            __atribuição.append(int(input('\n\nQual é o número da marcação correta? ')))
            Professor.clear()
            
        __leitor_alvo_leitura = open('.\Gerenciamento\Ques.txt','r')
        __leitor_alvo_escrita = open('.\Gerenciamento\Ques.txt','a')
        __barramento_de_questões = '0'
        __indice_linha = 1
        while __barramento_de_questões == '0':
            __alvo_linha = __leitor_alvo_leitura.readline()
            if (__alvo_linha == ''):
                __string_escritora = (f'Q{__indice_linha}-{__recomendação}-{__tipo_de_questão}-{__pergunta}-{__resposta}-{__nome}-{__atribuição}-{__situação}\n')
                __leitor_alvo_escrita.write(__string_escritora)             
                __barramento_de_questões = '1'
            __indice_linha += 1
        __leitor_alvo_leitura.close()
        __leitor_alvo_escrita.close()

    def minhas_questões(self, nome_alvo): # ----------------------------------------------------------------------------------
        __minhas_questões_indices = []
        __questões_buscador = open('.\Gerenciamento\Ques.txt','r')                             # Len de quantidade de questões.
        __contador_de_questões = __questões_buscador.read()
        __contar_questões = __contador_de_questões.replace('\n','')
        self.__n_de_quest = len(__contar_questões)
        __questões_buscador.close()

        __leitor_alvo_leitura = open('.\Gerenciamento\Ques.txt','r')
        for i in range(self.__n_de_quest):
            leitura = __leitor_alvo_leitura.readline()
            if leitura != '':
                alvo_splitado = leitura.split('-')
                if alvo_splitado[5] == nome_alvo:
                    __minhas_questões_indices.append(alvo_splitado[0])

        __indices = __minhas_questões_indices
        return __indices
        __questões_buscador.close()
        __leitor_alvo_leitura.close()

    def gerarexouprov(self, tipo, nome, materia, questoes, num): # -----------------------------------------------------------------------------------------------
        __ListExProv_ler = open('.\Gerenciamento\ListExProv.txt','r')
        __ListExProv_escrever = open('.\Gerenciamento\ListExProv.txt','a')
        __nome_dp = nome
        __materia_dp = materia
        __questões_dp = questoes
        __quantidade_de_questões = num
        __tipo = tipo
        self.__barramento_dp = '0'
        __indice_linha_dp = 1
        while self.__barramento_dp == '0':
            __alvo_linha_dp = __ListExProv_ler.readline()
            if (__alvo_linha_dp == ''):
                __string_escritora_dp = (f'{__nome_dp}-{__materia_dp}-{__questões_dp}-{__quantidade_de_questões}-{__tipo}\n')
                __ListExProv_escrever.write(__string_escritora_dp)             
                self.__barramento_dp = '1'
            __indice_linha_dp += 1
        __ListExProv_ler.close()
        __ListExProv_escrever.close()

    def listar_todas_questões_met(self):
        __list_quest = open('.\Gerenciamento\Ques.txt','r')
        self.__tamanho_quest = len(__list_quest.readlines())
        __list_quest.close()
        __list_quest = open('.\Gerenciamento\Ques.txt','r')
        __todas_quest = []
        for i in range(self.__tamanho_quest):
            __splited_q = __list_quest.readline().split('-')
            __todas_quest.append(__splited_q[0])
        return __todas_quest

    def acessar_hist(self):
        __hist_quest = open('.\Gerenciamento\ListExProv.txt','r')
        self.__tamanho_hist = len(__hist_quest.readlines())
        __hist_quest.close()
        __hist_quest = open('.\Gerenciamento\ListExProv.txt','r')
        
        print('Acessando histórico de atividades:\n\nDeseja rever todo o conteúdo?\n\n1 - Sim\n2 - Não\n')
        ent_rever = input('> ')
        if ent_rever == '1':
            Professor.clear()
            for i in range(self.__tamanho_hist):
                __splited_h = __hist_quest.readline().split('-')
                __tp = __splited_h[4]
                __nm = __splited_h[0]
                __mt = __splited_h[1]
                __nmm = __splited_h[3]
                __q_v = __splited_h[2]
                print(f'\n\nTipo de Atividade: {__tp}\nNome da Atividade: {__nm}\nMatéria: {__mt}\nBanco de Questões Usadas: {__q_v}\n\n')
        if ent_rever == '2':
            Professor.clear()

    def avaliar_quest(self):
        __indicações_minhas = open('.\Gerenciamento\Indicações.txt','r')
        self.__t_i = len(__indicações_minhas.readlines())
        __indicações_minhas.close()
        __indicações_minhas = open('.\Gerenciamento\Indicações.txt','r')
        
        print('\n\nAcessando questões para correção:\n\n')
        __quebrar = __indicações_minhas.readline().split('-')
        print(f'Você precisa corrigir as questões: {__quebrar[1]}')
                
    # Funcionalidades:

    def clear():
        print('\n'*49)

    def set_nome(nome):
        global __nome
        __nome = nome

    def get_nome():
        return __nome

Professor().login_professor('Anderson')
