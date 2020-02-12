import operator


class Processo(object):
    def __init__(self, name, burst, tcheg):
        self.name = name
        self.burst = burst
        self.tcheg = tcheg


def printProcManual(lista):
    print('Proc || Burst || T.Chegada')
    for i in lista:  # Printando os processos com o burst e o TChegada
        if int(i.burst) > 9:
            print(f'P{i.name + 1}       {i.burst}        {i.tcheg}')
        else:
            print(f'P{i.name + 1}        {i.burst}        {i.tcheg}')
    print(27 * '-')

# FUNÇÕES P/ O ROOUND ROBIN


def findWaitingTime(processes, n, burstT, waitT, quantum):
    rest_burstT = [0] * n

    # Copiando o tempo de burst para o rt[]
    for i in range(n):
        rest_burstT[i] = burstT[i]
    t = 0

    # Continuar executando até que todos terminem...
    while(1):
        done = True

        # Percorrendo todos os processos, um por um
        for i in range(n):
            # Se o burst ainda for maior que 0, ele precisa ser processado mais...
            if (rest_burstT[i] > 0):
                done = False  # Ainda existe algum processo pendente

                if (rest_burstT[i] > quantum):
                    t += quantum

                    # Diminuindo o tempoBurst pelo Quntum
                    rest_burstT[i] -= quantum

                # Se o burst for <= o quantum, último ciclo para o processo...
                else:
                    t = t + rest_burstT[i]

                    #  O tempo de espera é o tempo atual menos o tempo usado por este processo
                    waitT[i] = t - burstT[i]

                    # Quando o tempo for totalmente executado, ele agora é 0
                    rest_burstT[i] = 0

        # Quando todos os processos terminarem...
        if done is True:
            break


def findTurnAroundTime(processes, n, burstT, waitT, tat):
    # Calculando o tempo TurnAround
    for i in range(n):
        tat[i] = burstT[i] + waitT[i]


def findavgTime(processes, n, burstT, quantum):
    waitT = [0] * n
    tat = [0] * n

    # Função para achar o tempo de espera dos processos RR
    findWaitingTime(processes, n, burstT,
                    waitT, quantum)

    # Função para achar o Turn Around dos processos RR
    findTurnAroundTime(processes, n, burstT,
                       waitT, tat)

    total_waitT = 0
    total_turnA = 0

    print('\n' + 27 * '-')
    print('Proc || Burst || Quantum')
    for i in range(n):  # Printando os processos com o burst e o Quantum
        total_waitT = total_waitT + waitT[i]
        total_turnA = total_turnA + tat[i]
        print(f'{i+1}\t {burstT[i]}\t   {quantum}')
    print(27 * '-')

    # Tempo de Espera
    for i in range(n):
        print(f'P{i+1} Tempo de Espera: {waitT[i]}')
    print(27 * '-')

    # TurnAround
    for i in range(n):
        print(f'P{i+1} TurnAround: {tat[i]}')
    print(27 * '-')

    print(f'Espera Média: {total_waitT / n}')
    print(f'TurnAround Médio: {total_turnA / n}')


def menu():
    print('Algorítmos'.center(24, ' '))
    print('\
0 - Sair\n\
1 - FCFS\n\
2 - SJF\n\
3 - Round Robin')


def fcfs01():
    burst = input('Burst Manual ou por Arquivo(M/A)? ')
    lista = []
    # MANUAL
    if burst == 'M' or burst == 'm':
        n = int(input("Quantidade de Processos: "))
        # burst e tempo de chegada manual
        for i in range(n):
            b = int(input("P" + str(i + 1) + " Burst:"))
            t = int(input("P" + str(i + 1) + " Tempo de Chegada:"))
            proc = Processo(i, b, t)
            lista.append(proc)

        print('\n' + 27 * '-')
        printProcManual(lista)

        # TEMPO DE ESPERA
        acumulo = 0
        listaTA = []
        esperaMedia = 0
        for i in range(len(lista)):
            if int(lista[i].tcheg) == 0:
                print(f'P{i+1}) Tempo de Espera: {lista[i].tcheg + acumulo}')
                esperaMedia += (lista[i].tcheg + acumulo)
                # Somando os tempos para usar de espera
                acumulo += int(lista[i].burst)
                listaTA.append(acumulo)
            else:
                print(f'P{i+1}) Tempo de Espera: {acumulo - lista[i].tcheg}')
                esperaMedia += (acumulo - lista[i].tcheg)
                # Somando os tempos para usar de espera
                acumulo += int(lista[i].burst)
                listaTA.append(acumulo - lista[i].tcheg)
        print(27 * '-')
        # TURNAROUND
        acumulo = 0
        for i in range(len(listaTA)):
            print(f'P{i+1}) TurnAround: {listaTA[i]}')
            acumulo += listaTA[i]
        print(27 * '-')
        print(f'Espera Média: {esperaMedia / len(listaTA)}')
        print(f'TurnAround Médio: {acumulo/len(listaTA)}')

    # AUTOMÁTICO
    elif burst == 'A' or burst == 'a':
        # Caso o nome do arquivo for outro, mudar na linha abaixo
        leitor = open('fcfs01.txt', 'r')
        p = leitor.readlines()
        n = len(p)
        for i in range(len(p)):
            # Trabalhando com o que está escrito no arquivo
            especs = (p[i].replace('@', '').replace(
                '&', '').replace('\n', '').split(';'))
            name = especs[0]
            b = especs[1]
            t = especs[2]
            proc = Processo(name, b, t)
            lista.append(proc)
        lista.sort(key=operator.attrgetter('tcheg'), reverse=False)

        print('\n' + 27 * '-')

        print('Proc || Burst || T.Chegada')
        for i in lista:  # Printando os processos com o burst e o TChegada
            print(f'{i.name}\t {i.burst}\t   {i.tcheg}')
        print(27 * '-')

        # TEMPO DE ESPERA
        acumulo = 0
        listaTA = []
        esperaMedia = 0
        for i in lista:
            if i.tcheg == 0:
                print(f'{i.name}) Tempo de Espera: {i.tcheg + acumulo}')
                esperaMedia += (i.tcheg + acumulo)
                # Somando os tempos para usar de espera
                acumulo += i.burst
                listaTA.append(acumulo)
            else:
                a = acumulo - int(i.tcheg)
                print(f'{i.name}) Tempo de Espera: {a}')
                esperaMedia += (acumulo - int(i.tcheg))
                # Somando os tempos para usar de espera
                acumulo += int(i.burst)
                listaTA.append(acumulo - int(i.tcheg))
        print(27 * '-')
        # TURNAROUND
        acumulo = 0
        for i in range(len(listaTA)):
            print(f'P{i+1}) TurnAround: {listaTA[i]}')
            acumulo += listaTA[i]
        print(27 * '-')
        print(f'Espera Média: {esperaMedia / len(listaTA)}')
        print(f'TurnAround Médio: {acumulo/len(listaTA)}')

def fcfs02():
    burst = input('Burst Manual ou por Arquivo(M/A)? ')
    lista = []
    # MANUAL
    if burst == 'M' or burst == 'm':
        n = int(input("Quantidade de Processos: "))
        # burst e tempo de chegada manual
        for i in range(n):
            b = int(input("P" + str(i + 1) + " Burst:"))
            t = int(input("P" + str(i + 1) + " Tempo de Chegada:"))
            proc = Processo(i, b, t)
            lista.append(proc)

        print('\n' + 27 * '-')
        printProcManual(lista)

        # TEMPO DE ESPERA
        acumulo = 0
        listaTA = []
        esperaMedia = 0
        for i in range(len(lista)):
            if int(lista[i].tcheg) == 0:
                print(f'P{i+1}) Tempo de Espera: {lista[i].tcheg + acumulo}')
                esperaMedia += (lista[i].tcheg + acumulo)
                # Somando os tempos para usar de espera
                acumulo += int(lista[i].burst)
                listaTA.append(acumulo)
            else:
                print(f'P{i+1}) Tempo de Espera: {acumulo - lista[i].tcheg}')
                esperaMedia += (acumulo - lista[i].tcheg)
                # Somando os tempos para usar de espera
                acumulo += int(lista[i].burst)
                listaTA.append(acumulo - lista[i].tcheg)
        print(27 * '-')
        # TURNAROUND
        acumulo = 0
        for i in range(len(listaTA)):
            print(f'P{i+1}) TurnAround: {listaTA[i]}')
            acumulo += listaTA[i]
        print(27 * '-')
        print(f'Espera Média: {esperaMedia / len(listaTA)}')
        print(f'TurnAround Médio: {acumulo/len(listaTA)}')

    # AUTOMÁTICO
    elif burst == 'A' or burst == 'a':
        # Caso o nome do arquivo for outro, mudar na linha abaixo
        leitor = open('fcfs02.txt', 'r')
        p = leitor.readlines()
        n = len(p)
        for i in range(len(p)):
            # Trabalhando com o que está escrito no arquivo
            especs = (p[i].replace('@', '').replace(
                '&', '').replace('\n', '').split(';'))
            name = especs[0]
            b = especs[1]
            t = especs[2]
            proc = Processo(name, b, t)
            lista.append(proc)
        lista.sort(key=operator.attrgetter('tcheg'), reverse=False)

        print('\n' + 27 * '-')

        print('Proc || Burst || T.Chegada')
        for i in lista:  # Printando os processos com o burst e o TChegada
            print(f'{i.name}\t {i.burst}\t   {i.tcheg}')
        print(27 * '-')

        # TEMPO DE ESPERA
        acumulo = 0
        listaTA = []
        esperaMedia = 0
        for i in lista:
            if i.tcheg == 0:
                print(f'{i.name}) Tempo de Espera: {i.tcheg + acumulo}')
                esperaMedia += (i.tcheg + acumulo)
                # Somando os tempos para usar de espera
                acumulo += i.burst
                listaTA.append(acumulo)
            else:
                a = acumulo - int(i.tcheg)
                print(f'{i.name}) Tempo de Espera: {a}')
                esperaMedia += (acumulo - int(i.tcheg))
                # Somando os tempos para usar de espera
                acumulo += int(i.burst)
                listaTA.append(acumulo - int(i.tcheg))
        print(27 * '-')
        # TURNAROUND
        acumulo = 0
        for i in range(len(listaTA)):
            print(f'P{i+1}) TurnAround: {listaTA[i]}')
            acumulo += listaTA[i]
        print(27 * '-')
        print(f'Espera Média: {esperaMedia / len(listaTA)}')
        print(f'TurnAround Médio: {acumulo/len(listaTA)}')


def sjf01():
    burst = input('Burst Manual ou por Arquivo(M/A)? ')
    # MANUAL
    if burst == 'M' or burst == 'm':
        n = int(input("Quantidade de Processos: "))
        lista = []
        # burst e tempo de chegada manual
        for i in range(n):
            b = int(input("P" + str(i + 1) + " Burst: "))
            t = int(input("P" + str(i + 1) + " Tempo de Chegada: "))
            proc = Processo(i, b, t)
            lista.append(proc)

        print('\n' + 27 * '-')
        printProcManual(lista)

        lista.sort(key=operator.attrgetter('burst'), reverse=False)
        lista.sort(key=operator.attrgetter('tcheg'), reverse=False)

        # TEMPO DE ESPERA
        acumulo = 0
        listaTA = []
        esperaMedia = 0
        for i in lista:
            if i.tcheg == 0:
                print(f'P{int(i.name)+1}) Tempo de Espera: {i.tcheg + acumulo}')
                esperaMedia += (i.tcheg + acumulo)
                # Somando os tempos para usar de espera
                acumulo += (i.burst)
                listaTA.append(acumulo)
            else:
                print(f'P{int(i.name)+1} Tempo de Espera: {acumulo - i.tcheg}')
                esperaMedia += (acumulo - i.tcheg)
                # Somando os tempos para usar de espera
                acumulo += (i.burst)
                listaTA.append(acumulo - i.tcheg)
        print(27 * '-')

        # TurnAround
        tAround = 0
        c = 0
        for i in lista:
            print(f'P{int(i.name)+1} TurnAround: {tAround + (i.burst - i.tcheg)}')
            tAround += (i.burst - i.tcheg)
            c += tAround
        print(27 * '-')
        print(f'Espera Média: {esperaMedia / len(listaTA)}')
        print(f'TurnAround Médio: {c / len(lista)}')

    # AUTOMÁTICO
    elif burst == 'A' or burst == 'a':
        # Caso o nome do arquivo for outro, mudar na linha abaixo
        lista = []
        leitor = open('sjf01.txt', 'r')
        p = leitor.readlines()
        n = len(p)
        for i in range(len(p)):
            # Trabalhando com o que está escrito no arquivo
            especs = (p[i].replace('@', '').replace(
                '&', '').replace('\n', '').split(';'))
            name = especs[0]
            b = int(especs[1])
            t = int(especs[2])
            proc = Processo(name, b, t)
            lista.append(proc)
        # Ordenando os processos em ordem de tempo de chegada e burst
        print('\n' + 27 * '-')

        print('Proc || Burst || T.Chegada')
        for i in lista:  # Printando os processos com o burst e o TChegada
            print(f'{i.name}\t {i.burst}\t   {i.tcheg}')
        print(27 * '-')

        lista.sort(key=operator.attrgetter('burst'), reverse=False)
        lista.sort(key=operator.attrgetter('tcheg'), reverse=False)

        # TEMPO DE ESPERA
        acumulo = 0
        listaTA = []
        esperaMedia = 0
        for i in lista:
            if i.tcheg == 0:
                print(f'{i.name}) Tempo de Espera: {int(i.tcheg) + acumulo}')
                esperaMedia += (int(i.tcheg) + acumulo)
                # Somando os tempos para usar de espera
                acumulo += (int(i.burst))
                listaTA.append(acumulo)
            else:
                print(f'{i.name} Tempo de Espera: {acumulo - int(i.tcheg)}')
                esperaMedia += (acumulo - int(i.tcheg))
                # Somando os tempos para usar de espera
                acumulo += int((i.burst))
                listaTA.append(acumulo - int(i.tcheg))
        print(27 * '-')

        # TurnAround
        tAround = 0
        c = 0
        for i in lista:
            print(f'{i.name} TurnAround: {tAround + (int(i.burst) - int(i.tcheg))}')
            tAround += (int(i.burst) - int(i.tcheg))
            c += tAround
        print(27 * '-')
        print(f'Espera Média: {esperaMedia / len(listaTA)}')
        print(f'TurnAround Médio: {c / len(lista)}')

def sjf02():
    burst = input('Burst Manual ou por Arquivo(M/A)? ')
    # MANUAL
    if burst == 'M' or burst == 'm':
        n = int(input("Quantidade de Processos: "))
        lista = []
        # burst e tempo de chegada manual
        for i in range(n):
            b = int(input("P" + str(i + 1) + " Burst: "))
            t = int(input("P" + str(i + 1) + " Tempo de Chegada: "))
            proc = Processo(i, b, t)
            lista.append(proc)

        print('\n' + 27 * '-')
        printProcManual(lista)

        lista.sort(key=operator.attrgetter('burst'), reverse=False)
        lista.sort(key=operator.attrgetter('tcheg'), reverse=False)

        # TEMPO DE ESPERA
        acumulo = 0
        listaTA = []
        esperaMedia = 0
        for i in lista:
            if i.tcheg == 0:
                print(f'P{int(i.name)+1}) Tempo de Espera: {i.tcheg + acumulo}')
                esperaMedia += (i.tcheg + acumulo)
                # Somando os tempos para usar de espera
                acumulo += (i.burst)
                listaTA.append(acumulo)
            else:
                print(f'P{int(i.name)+1} Tempo de Espera: {acumulo - i.tcheg}')
                esperaMedia += (acumulo - i.tcheg)
                # Somando os tempos para usar de espera
                acumulo += (i.burst)
                listaTA.append(acumulo - i.tcheg)
        print(27 * '-')

        # TurnAround
        tAround = 0
        c = 0
        for i in lista:
            print(f'P{int(i.name)+1} TurnAround: {tAround + (i.burst - i.tcheg)}')
            tAround += (i.burst - i.tcheg)
            c += tAround
        print(27 * '-')
        print(f'Espera Média: {esperaMedia / len(listaTA)}')
        print(f'TurnAround Médio: {c / len(lista)}')

    # AUTOMÁTICO
    elif burst == 'A' or burst == 'a':
        # Caso o nome do arquivo for outro, mudar na linha abaixo
        lista = []
        leitor = open('sjf02.txt', 'r')
        p = leitor.readlines()
        n = len(p)
        for i in range(len(p)):
            # Trabalhando com o que está escrito no arquivo
            especs = (p[i].replace('@', '').replace(
                '&', '').replace('\n', '').split(';'))
            name = especs[0]
            b = int(especs[1])
            t = int(especs[2])
            proc = Processo(name, b, t)
            lista.append(proc)
        # Ordenando os processos em ordem de tempo de chegada e burst
        print('\n' + 27 * '-')

        print('Proc || Burst || T.Chegada')
        for i in lista:  # Printando os processos com o burst e o TChegada
            print(f'{i.name}\t {i.burst}\t   {i.tcheg}')
        print(27 * '-')

        lista.sort(key=operator.attrgetter('burst'), reverse=False)
        lista.sort(key=operator.attrgetter('tcheg'), reverse=False)

        # TEMPO DE ESPERA
        acumulo = 0
        listaTA = []
        esperaMedia = 0
        for i in lista:
            if i.tcheg == 0:
                print(f'{i.name}) Tempo de Espera: {int(i.tcheg) + acumulo}')
                esperaMedia += (int(i.tcheg) + acumulo)
                # Somando os tempos para usar de espera
                acumulo += (int(i.burst))
                listaTA.append(acumulo)
            else:
                print(f'{i.name} Tempo de Espera: {acumulo - int(i.tcheg)}')
                esperaMedia += (acumulo - int(i.tcheg))
                # Somando os tempos para usar de espera
                acumulo += int((i.burst))
                listaTA.append(acumulo - int(i.tcheg))
        print(27 * '-')

        # TurnAround
        tAround = 0
        c = 0
        for i in lista:
            print(f'{i.name} TurnAround: {tAround + (int(i.burst) - int(i.tcheg))}')
            tAround += (int(i.burst) - int(i.tcheg))
            c += tAround
        print(27 * '-')
        print(f'Espera Média: {esperaMedia / len(listaTA)}')
        print(f'TurnAround Médio: {c / len(lista)}')

def sjf03():
    burst = input('Burst Manual ou por Arquivo(M/A)? ')
    # MANUAL
    if burst == 'M' or burst == 'm':
        n = int(input("Quantidade de Processos: "))
        lista = []
        # burst e tempo de chegada manual
        for i in range(n):
            b = int(input("P" + str(i + 1) + " Burst: "))
            t = int(input("P" + str(i + 1) + " Tempo de Chegada: "))
            proc = Processo(i, b, t)
            lista.append(proc)

        print('\n' + 27 * '-')
        printProcManual(lista)

        lista.sort(key=operator.attrgetter('burst'), reverse=False)
        lista.sort(key=operator.attrgetter('tcheg'), reverse=False)

        # TEMPO DE ESPERA
        acumulo = 0
        listaTA = []
        esperaMedia = 0
        for i in lista:
            if i.tcheg == 0:
                print(f'P{int(i.name)+1}) Tempo de Espera: {i.tcheg + acumulo}')
                esperaMedia += (i.tcheg + acumulo)
                # Somando os tempos para usar de espera
                acumulo += (i.burst)
                listaTA.append(acumulo)
            else:
                print(f'P{int(i.name)+1} Tempo de Espera: {acumulo - i.tcheg}')
                esperaMedia += (acumulo - i.tcheg)
                # Somando os tempos para usar de espera
                acumulo += (i.burst)
                listaTA.append(acumulo - i.tcheg)
        print(27 * '-')

        # TurnAround
        tAround = 0
        c = 0
        for i in lista:
            print(f'P{int(i.name)+1} TurnAround: {tAround + (i.burst - i.tcheg)}')
            tAround += (i.burst - i.tcheg)
            c += tAround
        print(27 * '-')
        print(f'Espera Média: {esperaMedia / len(listaTA)}')
        print(f'TurnAround Médio: {c / len(lista)}')

    # AUTOMÁTICO
    elif burst == 'A' or burst == 'a':
        # Caso o nome do arquivo for outro, mudar na linha abaixo
        lista = []
        leitor = open('sjf03.txt', 'r')
        p = leitor.readlines()
        n = len(p)
        for i in range(len(p)):
            # Trabalhando com o que está escrito no arquivo
            especs = (p[i].replace('@', '').replace(
                '&', '').replace('\n', '').split(';'))
            name = especs[0]
            b = int(especs[1])
            t = int(especs[2])
            proc = Processo(name, b, t)
            lista.append(proc)
        # Ordenando os processos em ordem de tempo de chegada e burst
        print('\n' + 27 * '-')

        print('Proc || Burst || T.Chegada')
        for i in lista:  # Printando os processos com o burst e o TChegada
            print(f'{i.name}\t {i.burst}\t   {i.tcheg}')
        print(27 * '-')

        lista.sort(key=operator.attrgetter('burst'), reverse=False)
        lista.sort(key=operator.attrgetter('tcheg'), reverse=False)

        # TEMPO DE ESPERA
        acumulo = 0
        listaTA = []
        esperaMedia = 0
        for i in lista:
            if i.tcheg == 0:
                print(f'{i.name}) Tempo de Espera: {int(i.tcheg) + acumulo}')
                esperaMedia += (int(i.tcheg) + acumulo)
                # Somando os tempos para usar de espera
                acumulo += (int(i.burst))
                listaTA.append(acumulo)
            else:
                print(f'{i.name} Tempo de Espera: {acumulo - int(i.tcheg)}')
                esperaMedia += (acumulo - int(i.tcheg))
                # Somando os tempos para usar de espera
                acumulo += int((i.burst))
                listaTA.append(acumulo - int(i.tcheg))
        print(27 * '-')

        # TurnAround
        tAround = 0
        c = 0
        for i in lista:
            print(f'{i.name} TurnAround: {tAround + (int(i.burst) - int(i.tcheg))}')
            tAround += (int(i.burst) - int(i.tcheg))
            c += tAround
        print(27 * '-')
        print(f'Espera Média: {esperaMedia / len(listaTA)}')
        print(f'TurnAround Médio: {c / len(lista)}')


def rr01():
    burst = input('Burst Manual ou por Arquivo(M/A)? ')
    # MANUAL
    if burst == 'M' or burst == 'm':
        n = int(input("Quantidade de Processos: "))
        q = int(input('Quantum: '))
        listaIDS = []
        listaBurst = []

        for i in range(n):
            b = int(input("P" + str(i + 1) + " Burst: "))
            listaIDS.append(i + 1)
            listaBurst.append(b)
        findavgTime(listaIDS, n, listaBurst, q)
        print('\n' + 27 * '-')

    # AUTOMÁTICO
    if burst == 'A' or burst == 'a':
        # Caso o nome do arquivo for outro, mudar na linha abaixo
        lista = []
        leitor = open('rr01.txt', 'r')
        p = leitor.readlines()
        n = len(p)
        listaIDS = []
        listaBurst = []
        name = ''

        for i in range(len(p)):
            # Trabalhando com o que está escrito no arquivo
            especs = (p[i].replace('@', '').replace(
                '&', '').replace('\n', '').split(';'))
            name = especs[0]
            b = int(especs[1])
            q = int(especs[4])
            listaBurst.append(b)
        findavgTime(listaIDS, n, listaBurst, q)
        print('\n' + 27 * '-')

def rr02():
    burst = input('Burst Manual ou por Arquivo(M/A)? ')
    # MANUAL
    if burst == 'M' or burst == 'm':
        n = int(input("Quantidade de Processos: "))
        q = int(input('Quantum: '))
        listaIDS = []
        listaBurst = []

        for i in range(n):
            b = int(input("P" + str(i + 1) + " Burst: "))
            listaIDS.append(i + 1)
            listaBurst.append(b)
        findavgTime(listaIDS, n, listaBurst, q)
        print('\n' + 27 * '-')

    # AUTOMÁTICO
    if burst == 'A' or burst == 'a':
        # Caso o nome do arquivo for outro, mudar na linha abaixo
        lista = []
        leitor = open('rr02.txt', 'r')
        p = leitor.readlines()
        n = len(p)
        listaIDS = []
        listaBurst = []
        name = ''

        for i in range(len(p)):
            # Trabalhando com o que está escrito no arquivo
            especs = (p[i].replace('@', '').replace(
                '&', '').replace('\n', '').split(';'))
            name = especs[0]
            b = int(especs[1])
            q = int(especs[4])
            listaBurst.append(b)
        findavgTime(listaIDS, n, listaBurst, q)
        print('\n' + 27 * '-')

def rr03():
    burst = input('Burst Manual ou por Arquivo(M/A)? ')
    # MANUAL
    if burst == 'M' or burst == 'm':
        n = int(input("Quantidade de Processos: "))
        q = int(input('Quantum: '))
        listaIDS = []
        listaBurst = []

        for i in range(n):
            b = int(input("P" + str(i + 1) + " Burst: "))
            listaIDS.append(i + 1)
            listaBurst.append(b)
        findavgTime(listaIDS, n, listaBurst, q)
        print('\n' + 27 * '-')

    # AUTOMÁTICO
    if burst == 'A' or burst == 'a':
        # Caso o nome do arquivo for outro, mudar na linha abaixo
        lista = []
        leitor = open('rr03.txt', 'r')
        p = leitor.readlines()
        n = len(p)
        listaIDS = []
        listaBurst = []
        name = ''

        for i in range(len(p)):
            # Trabalhando com o que está escrito no arquivo
            especs = (p[i].replace('@', '').replace(
                '&', '').replace('\n', '').split(';'))
            name = especs[0]
            b = int(especs[1])
            q = int(especs[4])
            listaBurst.append(b)
        findavgTime(listaIDS, n, listaBurst, q)
        print('\n' + 27 * '-')
