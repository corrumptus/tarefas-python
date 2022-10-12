def menu():
    print('1 - Carregar dados do arquivo')
    print('2 - Listar todos os dados')
    print('3 - Listar a média de clockspeed de cada empresa')
    print('4 - Determinar a empresa com mais modelos de CPU')
    print('5 - Listar a CPU mais utilizada por cada empresa')
    print('6 - Criar uma nova coluna que classifica se as CPUs em Lento(<2200), Rápida(>=2200, <2800) e Super rápida(>=2800)')
    print('7 - Contar quantas versões existem da CPU Snapdragon')
    print('8 - Determinar qual é a versão mais rápida dentre as CPUs Dimensity')
    print('9 - Listar quais CPUs as empresas usam')
    print('10 - Criar um arquivo com uma lista de todos os dados da apple')
    print('11 - Listar qual é a configuração mais usada por cada empresa')
    print('12 - Determinar qual é o maior clockspeed de cada empresa')
    print('13 - Cadastrar um novo dispositivo')
    print('14 - Determinar qual é o maior clockspeed com o maior número de núcleos de cada empresa')
    o = int(input('Digite a opção desejada: '))
    return o

def Carregadados(a):
    arq = open(a, 'r')
    matriz = []
    arq.readline()
    for i in arq:
        i = i.replace('\n','')
        i = i.replace('Â\xa0','')
        dados = i.split(',')
        matriz.append(dados)
    can = True
    return matriz, can

def Mediadeclock(m):
    dickclock = criadick(Vfab, 0)
    dickquantclock = criadick(Vfab, 0)
    for i in Vfab:
        for j in range(len(m)):
            if m[j][1] == i:
                dickclock[i] += int(m[j][8])
                dickquantclock[i] += 1
        dickclock[i] = dickclock[i]/dickquantclock[i]
    return dickclock

def Quantosprocessadores(m):
    dickfab = criadick(Vfab, 0)
    for i in Vfab:
        for j in range(len(m)):
            if m[j][1] == i:
                dickfab[i] += 1
    vet = ['', 0]
    for i in range(len(Vfab)):
        if vet[1] < dickfab[Vfab[i]]:
            vet = [Vfab[i], dickfab[Vfab[i]]]
    return vet

def QualGPUmais(m):
    dickGPUs = criadick(Vfab, [])
    vetGPU = buscausada(m, Vfab, dickGPUs)
    return vetGPU

def CategorizaClock(m):
    arq = open(arquivo, 'w')
    matriz = []
    for i in range(len(m)):
        for j in range(len(m[i])):
            m[i][j] = str(m[i][j])
    for i in range(len(m)):
        if int(m[i][8]) < 2200:
            matriz.append(','.join(m[i]) + ',' + 'Lento')
            m[i].append('Lento')
        elif int(m[i][8]) >= 2200 and int(m[i][8]) < 2800:
            matriz.append(','.join(m[i]) + ',' + 'Rápido')
            m[i].append('Rápido')
        elif int(m[i][8]) >= 2800:
            matriz.append(','.join(m[i]) + ',' + 'Super rápido')
            m[i].append('Super Rápido')
    arq.write('\n'.join(matriz))
    R_arq = Carregadados(arquivo)
    return

def Contasnap(m):
    vetsnap = []
    for i in range(len(m)):
        if 'Snapdragon' in m[i][2]:
            if m[i][2] not in vetsnap:
                vetsnap.append(m[i][2])
    return vetsnap

def Qualdimensitymais(m):
    Vdimensity = ['', 0]   
    for i in range(len(m)):
        if 'Dimensity' in m[i][2]:
            if Vdimensity[1] < int(m[i][8]):
                Vdimensity[0] = m[i][2]
                Vdimensity[1] = int(m[i][8])
    return Vdimensity

def Cpusname(m):
    dickCPUs = criadick(Vfab, '')
    for i in Vfab:
        for j in range(len(m)):
            if m[j][1] == i:
                dickCPUs[i] += m[j][2] + '  '
    return dickCPUs

def Listarapple(m):
    apple = open(arquivo2, 'w')
    matriz = []
    for i in range(len(m)):
        if m[i][1] == 'Apple':
            matriz.append(m[i][2] + ',' + str(m[i][8]) + ',' + m[i][9])
    apple.write('\n'.join(matriz))
    return apple

def Coreconfig(m):
    dickCOREs = criadick(Vfab, [])
    vetCORE = buscausada(m, Vfab, dickCOREs)
    return vetCORE

def Maiorclock(m):
    Arqu, nothing = Carregadados('ML_ALL_benchmarks.csv')
    Vclocks = vetorfab(Arqu)
    dickCLOCKs = criadick(Vclocks, '')
    for i in Vclocks:
        matriz = ['',0]
        for j in range(len(Arqu)):
            if Arqu[j][1] == i:
                if matriz[1] < int(Arqu[j][4]):
                    matriz[0] = Arqu[j][0]
                    matriz[1] = int(Arqu[j][4])
        dickCLOCKs[i] = matriz[0]
    return dickCLOCKs, Vclocks

def Cadastra(m):
    arqu = open(arquivo, 'a')
    matriz = []
    matriz.append(str(len(m)+1))
    matriz.append(input('Qual é a empresa? '))
    matriz.append(input('Qual é o nome da CPU? '))
    matriz.append(input('Qual é o geekbench single? '))
    matriz.append(input('Qual é o geekbench multi? '))
    matriz.append(input('Qual é o Antutu9? '))
    matriz.append(input('Qual é o a quantidade de núcleos? '))
    matriz.append(input('Qual é a configuração dos núcleos?(colocar parenteses e discriminar todos via +) '))
    matriz.append(input('Qual é o Clockspeed? '))
    matriz.append(input('Qual é a GPU? '))
    arqu.write(','.join(matriz))
    arqu.close()
    CategorizaClock(m)
    return

def MaisCPUmaisCORE(m):
    dickCOREs = criadick(Vfab, 0)
    dickCLOCKs = criadick(Vfab, 0)
    for i in Vfab:
        matriz = 0
        for j in range(len(m)):
            if m[j][1] == i:
                if matriz < int(m[j][6]):
                    matriz = int(m[j][6])
        dickCOREs[i] = matriz
    for i in Vfab:
        for j in range(len(m)):
            if m[j][1] == i:
                if m[j][6] == dickCOREs[i]:
                    if dickCLOCKs[i] < int(m[j][8]):
                        dickCLOCKs[i] = int(m[j][8])
    return dickCOREs, dickCLOCKs

def vetorfab(m):
    Vfab = []
    for i in range(len(m)):
        if m[i][1] not in Vfab:
            Vfab.append(m[i][1])
    return Vfab

def criadick(v, tipo):
    dick = {}
    for i in v:
        dick[i] = tipo
    return dick

def buscausada(m, V, dick):
    vet = []
    for i in V:
        for j in range(len(m)):
            if m[j][1] == i:
                existe = False
                for k in range(len(dick[i])):
                    if m[j][9] == dick[i][k][0]:
                        existe = True
                        break
                if existe == True:
                    dick[i][k][1] += 1
                else:
                    dick[i].append([m[j][9], 1])
        vet.append(['', 0])
        for l in range(len(dick[i])):
            if vet[len(vet)-1][1] < dick[i][l][1]:
                vet[len(vet)-1][0] = dick[i][l][0]
                vet[len(vet)-1][1] = dick[i][l][1]
    return vet

def Cria_arquivo(m):
    Trata_arq(m)
    W = open(arquivo, 'w')
    return

def Trata_arq(m):
    arq = open(arquivo, 'w')
    matriz = []
    for i in range(len(m)):
        matriz1 = []
        for j in range(len(m[i])):
            matriz1.append(m[i][j])
        ','.join(matriz1)
        matriz.append(matriz1)
        if i != len(m):
            arq.append(matriz+'\n')
        else:
            arq.append(matriz)
    return

opcao = 1
arquivo = "smartphone_cpu_stats.csv"
arquivo2 = "Produtos_apple.csv"
can = False
while opcao != 0:
    opcao = menu()
    if opcao == 1:
        R_arq, can = Carregadados(arquivo)
        Vfab = vetorfab(R_arq)
    elif opcao == 2:
        for i in range(len(R_arq)):
            print(R_arq[i])
    elif opcao == 3:
        Clocks = Mediadeclock(R_arq)
        for i in Clocks:
            print('a média do clockspeed da fabricante ' + i + ' é de: ' + str(Clocks[i]))
    elif opcao == 4:
        quantos = Quantosprocessadores(R_arq)
        print('a fabricante com mais processadores é: ' + quantos[0] + ' com ' + str(quantos[1]) + ' processadores.')
    elif opcao == 5:
        GPUs = QualGPUmais(R_arq)
        for i in range(len(GPUs)):
            print('a empresa: ' + Vfab[i] + ' tem como a GPU mais usada: ' + GPUs[i][0] + ' com ' + str(GPUs[i][1]) + ' aparições')
    elif opcao == 6:
        if can == True:
            CategorizaClock(R_arq)
            for i in range(len(R_arq)):
                print(R_arq[i])
    elif opcao == 7:
        Snap = Contasnap(R_arq)
        print('existem ' + str(len(Snap)) + ' versões da cpu Snapdragon')
    elif opcao == 8:
        Dimensity = Qualdimensitymais(R_arq)
        print('A versão mais rápido das cpus dimensity é a: ' + Dimensity[0] + ' com ' + str(Dimensity[1]) + ' de clockspeed')
    elif opcao == 9:
        CPUs = Cpusname(R_arq)
        for i in Vfab:
            print('A empresa ' + i + ' usa as cpus: ' + str(CPUs[i].strip().replace('  ', ', ')) + '\n')
    elif opcao == 10:
        Apple = Listarapple(R_arq)
    elif opcao == 11:
        COREs = Coreconfig(R_arq)
        for i in range(len(COREs)):
            print('a empresa: ' + Vfab[i] + ' tem como a Core config mais usada: ' + COREs[i][0] + ' com ' + str(COREs[i][1]) + ' aparições')
    elif opcao == 12:
        Clock, Vclock = Maiorclock(R_arq)
        for i in Vclock:
            print('O melhor dispositivo em termos de clockspeed da empresa: ' + i + ' é o ' + Clock[i])
    elif opcao == 13:
        Cadastra(R_arq)
    elif opcao == 14:
        Cores, CLOCKs = MaisCPUmaisCORE(R_arq)
        for i in Vfab:
            print('A empresa: ' + i + ' tem como o maior número de núcleos e clockspeed, juntos, '+ str(Cores[i]) + ' ' + str(CLOCKs[i]))