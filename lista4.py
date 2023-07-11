"""
Ex. 1

Pergunta:
    Faça um programa que gera aleatoriamente números entre 1 e 10 em uma lista com 5
    elementos. Depois exiba:
        - o maior elemento da lista
        - o menor elemento da lista
        - informe se existem mais números ímpares ou pares na lista

Resposta:
    from random import randint

    lista = []
    MAIOR = 0
    MENOR = 10
    QUANTIDADE_PARES = 0

    for i in range(5):
        lista.append(randint(1, 10))

    for i in range(5):
        if MAIOR < lista[i]:
            MAIOR = lista[i]

        if MENOR > lista[i]:
            MENOR = lista[i]

        if lista[i]%2 == 0:
            QUANTIDADE_PARES += 1

    print(MAIOR)
    print(MENOR)

    if QUANTIDADE_PARES > 2:
        print("pares")
    else:
        print("impares")
"""

"""
Ex. 2

Pergunta:
    Gere uma lista de 30 números aleatórios entre 1 e 100. Não pode haver
    número repetido na lista.

Resposta:
    from random import randint

    lista = []

    while len(lista) < 30:
        n = randint(1, 100)

        if n not in lista:
            lista.append(n)
"""

"""
Ex. 3

Pergunta:
    Faça o cadastro de alunos e suas notas. Você deve criar uma lista para o nome dos
    alunos e uma para as notas. Depois exiba o nome do aluno que tem a maior nota. Calcule
    a média das notas dos alunos e crie uma nova lista somente com o nome dos alunos que
    estão acima da média de todos os alunos.

Resposta:
    lista_nomes = []
    lista_notas = []
    MAIOR_NOTA = 0
    NOME_MAIOR_NOTA = ""
    lista_acima_media = []
    SOMA_MEDIAS = 0

    while True:
        nome = input("Digite o nome\n")
        nota1 = float(input("Digite a primeira nota\n"))
        nota2 = float(input("Digite a segunda nota\n"))
        nota3 = float(input("Digite a terceira nota\n"))

        lista_nomes.append(nome)
        lista_notas.append([nota1, nota2, nota3])

        SOMA_MEDIAS += (nota1+nota2+nota3)/3

        if input("Deseja cadastrar mais um aluno?(s/n)") == "n":
            break

    SOMA_MEDIAS /= len(lista_notas)

    for i, notas in enumerate(lista_notas):
        MEDIA = 0

        for j in range(3):
            MEDIA += notas[j]

            if MAIOR_NOTA < notas[j]:
                MAIOR_NOTA = notas[j]
                nomemaisnota = lista_nomes[i]

        if MEDIA/3 > SOMA_MEDIAS:
            lista_acima_media.append(lista_nomes[i])

    print(nomemaisnota)
"""

"""
Ex. 4

Pergunta:
    Faça um programa para cadastrar os alunos. Para cada aluno deve ser cadastrado seu
    nome, nota de prova, nota de trabalho e frequência. Crie um menu no qual o usuário pode:
        - inserir um novo aluno
        - listar os dados de todos os alunos
        - calcular a média final do aluno considerando que a prova tem peso de 70%
        e o trabalho de 30%.
        - dado o nome de um aluno informar sua média final
        - criar uma lista com o nome de todos os alunos que tiveram média maior que 8
        - informar o status de cada aluno. O status deve ser:
            • Aprovado: média final >= 6 e frequência >= 75%
            • IFA: 4 <= média final < 6 e frequência >=75%
            • Reprovado: média < 4 ou frequência <75%

Resposta:
    lista_nomes = []
    lista_notas = []
    lista_frequencia = []
    lista_media_maior_8 = []

    while True:
        print("1 - inserir novo aluno")
        print("2 - listar todos")
        print("3 - calcular a media final de um aluno")
        print("4 - mostrar a media final de um aluno especificado")
        print("5 - lista dos alunos com media maior que 8")
        print("6 - informar o status de cada aluno")
        print("0 - sair")

        opcao = int(input("Digite a opcao\n"))

        if opcao == 0:
            break

        if opcao == 1:
            nome = input("Digite o nome\n")
            if nome not in lista_nomes:
                lista_nomes.append(nome)

                notaprova = float(input("Digite a nota da prova\n"))
                notatraba = float(input("Digite a nota do trabalho\n"))
                frequencia = float(input("Digite a frequencia\n"))

                lista_notas.append([notaprova, notatraba])
                lista_frequencia.append(frequencia)

        elif opcao == 2:
            for i, nome in enumerate(lista_nomes):
                notas = lista_notas[i]
                frequencia = lista_frequencia[i]

                print("-------------------------------------")
                print(f"nome: {nome}")
                print(f"nota de prova: {notas[0]}")
                print(f"nota de trabalho: {notas[1]}")
                print(f"frequencia: {frequencia}")

        elif opcao == 3:
            notaprova = float(input("Digite a nota da prova\n"))
            notatrabalho = float(input("Digite a nota do trabalho\n"))

            print(f"A media final é {0.7*notaprova + 0.3*notatrabalho}")

        elif opcao == 4:
            ACHOU = False
            nome_pessoa = input("Digite o nome\n")

            for i, nome in enumerate(lista_nomes):
                notas = lista_notas[i]

                if nome_pessoa == nome:
                    print(f"A media final de {nome} é {0.7*notas[0] + 0.3*notas[1]}")
                    ACHOU = True
                    break

            if not ACHOU:
                print("Não encontrado")

        elif opcao == 5:
            for i, notas in enumerate(lista_notas):
                if 0.7*notas[0] + 0.3*notas[1] > 8:
                    lista_media_maior_8.append(lista_nomes[i])

        elif opcao == 6:
            for i, nome in enumerate(lista_nomes):
                media = 0.7*lista_notas[i][0] + 0.3*lista_notas[i][1]
                frequencia = lista_frequencia[i]

                if media >= 6 and frequencia >= 75:
                    print(nome + ": aprovado")
                elif media >= 4 and frequencia >= 75:
                    print(nome + ": recuperação")
                else:
                    print(nome + ": reprovado")
"""

"""
Ex. 5

Pergunta:
    Faça uma lista com 50 posições imaginando que cada elemento da lista seja uma
    pessoa. Em cada posição você deve gerar randomicamente a idade dessa pessoa. Feito
    isso informe:
        - qual a população de jovens. Considerar jovens as pessoas entre 1 e 20 anos
        - qual o percentual de idosos. Considerar idosos as pessoas acima de 60 anos.
        - considerando que o corona vírus não causou a morte de nenhuma pessoa abaixo de 10
        anos de idade no mundo, informe qual o percentual de pessoas que não tem risco de morte
        pelo covid-19.
        - considerando que a taxa de mortalidade para pessoas idosas segundo o texto abaixo em
        itálico, informe a probabilidade de haver algum óbito na população: “Enquanto entre 0 e 49
        anos ela não passa de 1%, entre 50 e 59 fica em 1,3%, entre 60 e 69 vai para 3,6%, entre
        70 e 79 anos sobe para 8% e acima dos 80 chega a 14,8%” (fonte:
        https://agenciabrasil.ebc.com.br/saude/noticia/2020-03/idosos-formam-publico-maispreocupante-do-novo-coronavirus)

Resposta:
    from random import randint

    QUANTIDADE_JOVENS = 0

    QUANTIDADE_IDOSOS = 0

    QUANTIDADE_PESSOAS_MENOS_10_ANOS = 0

    PROBABILIDADE_1_MORTO = 0

    listapessoas = []
    for i in range(50):
        idade = randint(0, 100)
        listapessoas.append(idade)

        if idade > 1 or idade < 20:
            QUANTIDADE_JOVENS += 1
        if idade > 60:
            QUANTIDADE_IDOSOS += 1
        if idade < 10:
            QUANTIDADE_PESSOAS_MENOS_10_ANOS += 1

    print(QUANTIDADE_JOVENS)
    print(QUANTIDADE_IDOSOS*2)
    print(QUANTIDADE_PESSOAS_MENOS_10_ANOS*2)

    for i in range(50):
        PROBABILIDADE = 1

        # jovem: 1%*85,2%       = 0.00852
        # idoso: 99%*14,8%      = 0.14652
        # jovem-idoso: 1%*14,8% = 0.00148
        # nenhum: 99%*85,2%     = 0.84348
        # 1 morto = jovem + idoso = 0.00852 + 0.14652 = 0.15504

        for j in range(50):
            if listapessoas[i] < 50:
                PROBABILIDADE *= (1*int(j != i) - (1/100)*(-1)**(int(j==i)))
            elif listapessoas[i] < 60:
                PROBABILIDADE *= (1*int(j != i) - (1.3/100)*(-1)**(int(j==i)))
            elif listapessoas[i] < 70:
                PROBABILIDADE *= (1*int(j != i) - (3.6/100)*(-1)**(int(j==i)))
            elif listapessoas[i] < 80:
                PROBABILIDADE *= (1*int(j != i) - (8/100)*(-1)**(int(j==i)))
            elif listapessoas[i] <= 100:
                PROBABILIDADE *= (1*int(j != i) - (14.8/100)*(-1)**(int(j==i)))

        PROBABILIDADE_1_MORTO += PROBABILIDADE

    print(PROBABILIDADE_1_MORTO)
"""

"""
Ex. 6

Pergunta:
    Gere uma lista com 10 posições com números entre 1 e 15. Ordene essa lista.

Resposta:
    from random import randint

    lista = []

    for i in range(10):
        lista.append(randint(1, 15))

    print(lista)

    for i in range(10, 0, -1):
        for j in range(0, i-1):
            if lista[j] > lista[j+1]:
                lista[j], lista[j+1] = lista[j+1], lista[j]

    print(lista)
"""

"""
Ex. 7

Pergunta:
    Faça um programa com um menu de opções onde o usuário pode gerenciar listas. Ele 
    irá cadastrar duas listas e irá manipulá-las de acordo com as opções:
        opção 1 - inserir elementos na Lista 1. Os elementos na Lista 1 devem ser inseridos de um 
        em um. A quantidade máxima de elementos que essa lista deve suportar é de 5 elementos.
        opção 2 - inserir elementos na Lista 2. Diferentemente da Lista 1, nesta segunda lista o 
        usuário deve digitar um número e serão inseridos na lista, além do número digitado, mais 4 
        elementos sendo que o segundo é o dobro do primeiro, o terceiro é o dobro do segundo e 
        assim sucessivamente, até completar 5 elementos nesta lista.
        opção 3 - exibir o conteúdo das duas listas anteriores.
        opção 4 - criar e exibir uma nova lista que é composta pela união dos elementos da duas 
        listas anteriores. Essa será chamada de ListaUniao.
        opção 5 - criar e exibir uma lista composta pela intersecção dos elementos das duas listas.
        opção 6 - encontrar o maior valor das duas listas e somar esse valor aos elementos da 
        primeira lista.
        opção 7 - multiplicar os elementos de cada posição da primeira lista pelo valor do elemento 
        na segunda lista, criando e exibindo uma nova lista. Ex: se a primeira lista for [1,2,3,4,5] e 
        a segunda for [1,2,4,8,16] o resultado da terceira lista será [1,4,12,32,80].
        opção 8 - zerar o conteúdo das duas listas.
        opção 9 - ordenar a ListaUniao em ordem decrescente. Essa opção só poderá ser chamada 
        se a opção 4 já tiver sido chamada.

Resposta:
    lista1 = []
    lista2 = []
    OPCAO_4_PREVIAMENTE_ATIVADA = False

    while True:
        print("1 - Popular lista 1")
        print("2 - Popular lista 2")
        print("3 - Exibir conteúdo das listas")
        print("4 - Criar e exibir a lista união")
        print("5 - Criar e exibir a lista intersecção")
        print("6 - Localizar o maior elemento e somar na lista 1")
        print("7 - Multiplicação das listas de forma linear")
        print("8 - Zerar as duas listas")
        print("9 - Ordenar a lista união decrescentemente")
        print("0 - sair")
        opcao = int(input("Digite a opção\n"))

        if opcao == 0:
            break

        if opcao == 1:
            for i in range(5):
                lista1.append(int(input("Digite um número\n")))
        elif opcao == 2:
            lista2.append(int(input("Digite um número\n")))

            for i in range(1, 5):
                lista2.append(lista2[i-1]*2)
        elif opcao == 3:
            print(lista1)
            print(lista2)
        elif opcao == 4:
            ListaUniao = []

            for i in range(5):
                if lista1[i] not in ListaUniao:
                    ListaUniao.append(lista1[i])

                if lista2[i] not in ListaUniao:
                    ListaUniao.append(lista2[i])

            print(ListaUniao)
            OPCAO_4_PREVIAMENTE_ATIVADA = True
        elif opcao == 5:
            ListaInterseccao = []

            for i in range(5):
                if lista1[i] == lista2[i]:
                    ListaInterseccao.append(lista1[i])
            print(ListaInterseccao)
        elif opcao == 6:
            num = lista1[0]

            for i in range(1, 5):
                if num < lista1[i]:
                    num = lista1[i]

            for i in range(5):
                if num < lista2[i]:
                    num = lista2[i]

            for i in range(5):
                lista1[i] *= num
        elif opcao == 7:
            ListaMult = []

            for i in range(5):
                ListaMult.append(lista1[i]*lista2[i])

            print(ListaMult)
        elif opcao == 8:
            for i in range(5):
                lista1[i] = 0
                lista2[i] = 0
        elif opcao == 9 and OPCAO_4_PREVIAMENTE_ATIVADA:
            print(ListaUniao)

            for i in range(10, 0, -1):
                for j in range(0, i-1):
                    if ListaUniao[j] < ListaUniao[j+1]:
                        ListaUniao[j], ListaUniao[j+1] = ListaUniao[j+1], ListaUniao[j]

            print(ListaUniao)
"""