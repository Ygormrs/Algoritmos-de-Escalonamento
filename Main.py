from funcoes import *

# MAIN


while True:
    # Chamando o Menu
    menu()

    typeAlg = int(input('Escolha o algorítmo: '))

    if typeAlg == 0:
        break

    # Caso o usuário entre com uma opção errada
    while typeAlg < 1 or typeAlg > 5:
        print('Opção Inválida, escolha os números de 1 até 5!')
        typeAlg = input('Escolha o algorítmo:\n')

    # FCFS
    if typeAlg == 1:
        typeAlg2 = int(input('1 - FCFS01\n2 - FCFS02 '))
        if typeAlg2 == 0:
            break
        # Caso o usuário entre com uma opção errada
        while typeAlg2 < 1 or typeAlg2 > 2:
            print('Opção Inválida, escolha os números de 1 ou 2!')
            typeAlg2 = input(':FCFS01 OU FCFS02')
        
        if typeAlg2 == 1:
            fcfs01()
        if typeAlg2 == 2:
            fcfs02()
    
            
    # SJF
    if typeAlg == 2:
        typeAlg2 = int(input('1 - SJF01\n2 - SJF02\n3 - SJF03 '))
        if typeAlg2 == 0:
            break
        # Caso o usuário entre com uma opção errada
        while typeAlg2 < 1 or typeAlg2 > 3:
            print('Opção Inválida, escolha os números de 1 até 3!')
            typeAlg2 = input(':SJF01 / SJF02 / SJF03')
        if typeAlg2 == 1:
            sjf01()
        if typeAlg2 == 2:
            sjf02()
        if typeAlg2 == 3:
            sjf03()


    # Round Robin (RR)
    if typeAlg == 3:
        typeAlg2 = int(input('1 - RR01\n2 - RR02\n3 - RR03 '))
        if typeAlg2 == 0:
            break
        # Caso o usuário entre com uma opção errada
        while typeAlg2 < 1 or typeAlg2 > 3:
            print('Opção Inválida, escolha os números de 1 até 3!')
            typeAlg2 = input(':RR01 / RR02 / RR03')
        if typeAlg2 == 1:
            rr01()
        if typeAlg2 == 2:
            rr02()
        if typeAlg2 == 3:
            rr03()
