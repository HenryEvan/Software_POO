# Importações:

import os
from detalhes import Detalhes
from classe_coordenador import Coordenador
from classe_professor import Professor

# Atribuições:

chamar_detalhes = Detalhes()
chamar_coordenador = Coordenador()
chamar_professor = Professor()

# Metadados:

versão = chamar_detalhes.get_versão()
autores = chamar_detalhes.get_autores()

# Funções:

def clear(): # Ok!
    print('\n'*49)

def get_tamanho_matrícula_prof(): # Ok!
    __escanear_matrícula = open('.\Senhas\Matrículas professores.txt','r') # Retorna a quantidade de matrículas de professores cadastradas
    __tamanho_matrícula = len(__escanear_matrícula.readlines())
    return __tamanho_matrícula

def comparar_matrícula_prof(matrícula_entrada): # Ok!
    __escanear_matrícula = open('.\Senhas\Matrículas professores.txt','r') # Compara matrículas cadastradas com alguma entrada
    __contador_matrícula = get_tamanho_matrícula_prof()
    for i in range(__contador_matrícula):
        __matrícula_alvo = __escanear_matrícula.readline()[:4]             # Limitador do tamanho da matrícula
        if (matrícula_entrada == __matrícula_alvo):            
            __contador_matrícula = 0
            __resposta = 1            
            return __resposta            
        if (matrícula_entrada != __matrícula_alvo):
            __resposta = 0            
    return __resposta

def get_tamanho_matrícula_coor(): # Ok!
    __escanear_matrícula = open('.\Senhas\Matrículas coordenadores.txt','r') # Retorna a quantidade de matrículas de coordenadores cadastradas
    __tamanho_matrícula = len(__escanear_matrícula.readlines())
    return __tamanho_matrícula

def comparar_matrícula_coor(matrícula_entrada): # Ok!
    __escanear_matrícula = open('.\Senhas\Matrículas coordenadores.txt','r') # Compara matrículas cadastradas com alguma entrada
    __contador_matrícula = get_tamanho_matrícula_coor()
    for i in range(__contador_matrícula):
        __matrícula_alvo = __escanear_matrícula.readline()[:7]             # Limitador do tamanho da matrícula
        if (matrícula_entrada == __matrícula_alvo):            
            __contador_matrícula = 0
            __resposta = 1            
            return __resposta            
        if (matrícula_entrada != __matrícula_alvo):
            __resposta = 0            
    return __resposta

# Menu Principal: ESTÁ TODO OK!

def info(): # Menu de informações do sistema de arquivos.
    print('\n'+'~'*50)
    print(f'\n\n\nBanco de Questões de Alana University.\nAutores: {autores}.\nVersão do Projeto: {versão}\n\n')
    if (chamar_coordenador.get_tamanho_sistema() == 0):
        print('Seja muito bem vindo.\nEstado do sistema: Vazio\n\n')          
    if (chamar_coordenador.get_tamanho_sistema() == 1):
        print('Seja muito bem vindo.\nEstado do sistema: Incompleto\n\n')
    if (chamar_coordenador.get_tamanho_sistema() == 2):
        print('Seja muito bem vindo.\nEstado do sistema: Completo\n\n')

def menu(): # Menu para escolhas de entrar ou sair do programa.
    info()
    global __saida
    __saida = 0
    print('\nOpções:\n\n1 - Logar\n2 - Sair\n\n')
    entrada_inicial = input('> ')
    if entrada_inicial == '1':
        clear()
        login()
    if entrada_inicial == '2':
        eexit()

def login():
    print('\nLogin:\n\n1 - Professor\n2 - Coordenador\n3 - Voltar\n\n')
    entrada_login = input('> ')
    
    if entrada_login == '1': # Se o usuário digitar '1' ele entrará para o login de professores.
        clear()
        print(f'\n\nLogin: Professor\nEntre com espaço para retornar.\n\n')
        matrícula_entrada = input('Matrícula: ')        
        if (matrícula_entrada != ' '):
            login_erro_contador = 0
            loop_teste_a = comparar_matrícula_prof(matrícula_entrada)
            while loop_teste_a == 0: # Autenticando matrícula.
                clear()
                print('\n\nLogin: Professor\nEntre com espaço para retornar.\n')
                print('\nMatrícula não encontrada.\nTente novamente.\n')
                matrícula_entrada = input('Matrícula: ')
                login_erro_contador += 1
                if matrícula_entrada == ' ': # Retorno na autenticação da matrícula.
                    clear()
                    loop_teste_a = 2
                    login()
                if login_erro_contador >= 2: # Falha na autenticação da matrícula
                    print('\nTentativas limite ultrapassadas.\nSaindo do sistema.')
                    eexit()
                    loop_teste_a = 2               
            if comparar_matrícula_prof(matrícula_entrada) == 1: # Autenticação da matrícula concluida.
                clear()
                print(f'\n\nLogin: Professor\nEntre com espaço para retornar.\n\nMatrícula: {matrícula_entrada}\n')
                entrada_pw = input('Senha: ')
                if entrada_pw != ' ':
                    login_erro_contador_2 = 0
                    loop_teste_a2 = chamar_professor.set_autenticação_prof(entrada_pw)[:1]
                    while loop_teste_a2 == '0': # Autenticação de senha.
                        clear()
                        print(f'\n\nLogin: Professor\nEntre com espaço para retornar.\n\nSenha incorreta, tente novamente.\n\nMatrícula: {matrícula_entrada}\n')
                        entrada_pw = input('Senha: ')
                        login_erro_contador_2 += 1
                        if entrada_pw == ' ': # Retorno na autenticação de senha.
                            clear()
                            loop_teste_a2 = '2'
                            login()
                        if login_erro_contador_2 >= 2: # Falha na autenticação de senha.
                            print('\nTentativas limite ultrapassadas.\nSaindo do sistema.')
                            eexit()
                            loop_teste_a2 = '2'
                    if chamar_professor.set_autenticação_prof(entrada_pw)[:1] == '1': # Autenticação de senha concluida.
                        clear()
                        nome = chamar_professor.set_autenticação_prof(entrada_pw)[1::].replace('\n','')
                        chamar_professor.login_professor(nome)                   
                if entrada_pw == ' ':
                    clear()
                    login()                                
        if (matrícula_entrada == ' '): # Retornos
            clear()
            login()
            
    if entrada_login == '2': # Se o usuário digitar '2' ele entrará para o login de coordenadores, com as mesmas lógicas-login de professores.
        clear()
        print(f'\n\nLogin: Coordenador\nEntre com espaço para retornar.\n\n')
        matrícula_entrada = input('Matrícula: ')        
        if (matrícula_entrada != ' '):
            login_erro_contador = 0
            loop_teste_b = comparar_matrícula_coor(matrícula_entrada)
            while loop_teste_b == 0:
                clear()
                print(f'\n\nLogin: Coordenador\nEntre com espaço para retornar.\n')                
                print('\nMatrícula não encontrada.\nTente novamente.\n')
                matrícula_entrada = input('Matrícula: ')
                login_erro_contador += 1
                if matrícula_entrada == ' ':
                    clear()
                    loop_teste_b = 2
                    login()
                if login_erro_contador >= 2:
                    print('\nTentativas limite ultrapassadas.\nSaindo do sistema.')
                    eexit()
                    loop_teste_b = 2                
            if comparar_matrícula_coor(matrícula_entrada) == 1:
                clear()
                print(f'\n\nLogin: Coordenador\nEntre com espaço para retornar.\n\nMatrícula: {matrícula_entrada}\n')
                entrada_pw = input('Senha: ')
                if entrada_pw != ' ':
                    login_erro_contador_2 = 0
                    loop_teste_b2 = chamar_coordenador.set_autenticação_coor(entrada_pw)[:1]
                    while loop_teste_b2 == '0':
                        clear()
                        print(f'\n\nLogin: Coordenador\nEntre com espaço para retornar.\n\nSenha incorreta, tente novamente.\n\nMatrícula: {matrícula_entrada}\n')
                        entrada_pw = input('Senha: ')
                        login_erro_contador_2 += 1
                        if entrada_pw == ' ':
                            clear()
                            loop_teste_b2 = '2'
                            login()
                        if login_erro_contador_2 >= 2:
                            print('\nTentativas limite ultrapassadas.\nSaindo do sistema.')
                            eexit()
                            loop_teste_b2 = '2'
                    if chamar_coordenador.set_autenticação_coor(entrada_pw)[:1] == '1':
                        clear()
                        nome = chamar_coordenador.set_autenticação_coor(entrada_pw)[1::].replace('\n','')
                        chamar_coordenador.login_coordenador(nome)
                if entrada_pw == ' ':
                    clear()
                    login()
                
                
        if (matrícula_entrada == ' '):
            clear()
            login()

    if entrada_login == '3': # # Se o usuário digitar '3' ele voltará ao menu inicial.
        clear()
        menu()

def eexit():
    __saida = 1
    print('\n\nAté mais.\n\n')
    print('~'*50+'\n')

