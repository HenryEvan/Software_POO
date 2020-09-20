def x():

    print('\nVer atuais questões e atribuições para professores:\n')
            
    __atrib = open('.\Gerenciamento\Indicações.txt','r')
    __n_indic = len(__atrib.readlines())
    __atrib.close()
    __atrib = open('.\Gerenciamento\Indicações.txt','r')
    __lines = []

    for i in range(__n_indic):
        __atr_alvo = __atrib.readline()
        __atr_spli = __atr_alvo.split('-')
        if (__atr_alvo != '') and (i != 0):
            __prof = __atr_spli[0]
            __Q_L = __atr_spli[1]
            __line_edit = (f'{i} - {__prof}: {__Q_L}')
            print(__line_edit,end='')
            __lines.append(__line_edit)
            
    __atrib.close()
    __atrib = open('.\Gerenciamento\Indicações.txt','r')
    __mod_linh = int(input('\nQual linha você deseja mudar? '))
    print(f'\n{__lines[__mod_linh-1]}')
    __atrib.close()

    __atrib = open('.\Gerenciamento\Indicações.txt','r')
    for i in range(__mod_linh):
        __atrib.readline()
        if (i+1) == __mod_linh:
            __alvo_1 = __atrib.readline()
            __alvo_final = __alvo_1.split('-')
            __entrada_write = input(f'{__alvo_final[0]}: ')
        if (__mod_linh == 0):
            __alvo_1 = __atrib.readline()
            __alvo_final = __alvo_1.split('-')
            __entrada_write = input(f'{__alvo_final[0]}: ')
    
    __atrib.close()
    __atrib = open('.\Gerenciamento\Indicações.txt','w')
    __atribl = open('.\Gerenciamento\Indicações.txt','r')

    __nuvem_da_tristeza_kkkk = []
    __cummulus_nimbus = 0
    
    for i in range(__mod_linh):
        __atribl.readline()
        if (i+1) == __mod_linh:
            __nuvem_da_tristeza_kkkk.append(__entrada_write)
        __nuvem_da_tristeza_kkkk.append(__atribl.readline()[3::])
        __cummulus_nimbus += 1

    print(__nuvem_da_tristeza_kkkk)

    for i in range(__cummulus_nimbus):
        __escritor_anderson = (f'{__nuvem_da_tristeza_kkkk[i]}')
        __atrib.write(__escritor_anderson)
x()
