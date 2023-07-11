"""
Ex. 1

Pergunta:
    Faça um programa para informatizar o cadastro de produtos em uma loja. Você deve cadastrar
    produtos até o preço 0 ser cadastrado. Cada produto deve ser armazenado com as seguintes
    informações: nome, preço, quantidade e categoria (“L” para luxo e “C” para comum). Depois de
    cadastrados os produtos informe:
        - a quantidade de produtos de luxo com preço menor que R$ 2000,00.
        - o preço médios dos produtos de luxo.
        - o nome do produto mais caro com quantidade menor que 50.
        - o percentual de produtos que custam entre R$ 100,0 e R$ 200,00.
        - o nome do produto comum mais barato.

Resposta:
    QUANTIDADE_LUXO_MAIOR_2000 = 0

    SOMA_PRECO_LUXO = 0
    QUANTIDADE_PRODUTOS_LUXO = 0

    PRECO_PRODUTO_CARO_QUANTIDADE_MENOR_50 = 0
    NOME_PRODUTO_CARO_QUANTIDADE_MENOR_50 = ""

    QUANTIDADE_PRODUTOS_ENTRE_100_200 = 0
    QUANTIDADE_TOTAL_PRODUTOS = 0

    PRECO_PRODUTO_COMUM_MAIS_BARATO = 0
    NOME_PRODUTO_COMOM_MAIS_BARATO = ""

    while True:
        preco = float(input("Digite o preço do produto\n"))
        if preco == 0:
            break
        nome  = input("Digite o nome do produto\n")
        quantidade = int(input("Digite a quantidade do produto\n"))
        categoria = input("Digite a categoria do produto(l/c)\n")

        if categoria == "l" and preco < 2000:
            QUANTIDADE_LUXO_MAIOR_2000 += 1

        SOMA_PRECO_LUXO += preco
        QUANTIDADE_PRODUTOS_LUXO += 1

        if (quantidade < 50 and
        (PRECO_PRODUTO_CARO_QUANTIDADE_MENOR_50 == 0 or
        PRECO_PRODUTO_CARO_QUANTIDADE_MENOR_50 < preco)):
            PRECO_PRODUTO_CARO_QUANTIDADE_MENOR_50 = preco
            NOME_PRODUTO_CARO_QUANTIDADE_MENOR_50 = nome

        if 100 < preco < 200:
            QUANTIDADE_PRODUTOS_ENTRE_100_200 += 1
        QUANTIDADE_TOTAL_PRODUTOS += 1

        if (categoria == "c" and
        (PRECO_PRODUTO_COMUM_MAIS_BARATO == 0 or
        PRECO_PRODUTO_COMUM_MAIS_BARATO > preco)):
            PRECO_PRODUTO_COMUM_MAIS_BARATO = preco
            NOME_PRODUTO_COMOM_MAIS_BARATO = nome

    if not QUANTIDADE_PRODUTOS_LUXO:
        QUANTIDADE_PRODUTOS_LUXO = 1

    if not QUANTIDADE_TOTAL_PRODUTOS:
        QUANTIDADE_TOTAL_PRODUTOS = 1

    print(QUANTIDADE_LUXO_MAIOR_2000)
    print(SOMA_PRECO_LUXO/QUANTIDADE_PRODUTOS_LUXO)
    print(NOME_PRODUTO_CARO_QUANTIDADE_MENOR_50)
    print(QUANTIDADE_PRODUTOS_ENTRE_100_200/QUANTIDADE_TOTAL_PRODUTOS*100)
    print(NOME_PRODUTO_COMOM_MAIS_BARATO)
"""

"""
Ex. 2

Pergunta:
    Faça um programa para informatizar o cadastro dos jogadores de futebol em um time. Você deve
    cadastrar os jogadores com as seguintes informações: nome, idade, peso e time. Após terminado o
    cadastro, perguntar se o usuário deseja cadastrar mais jogadores. Caso ele responda “sim” outro
    cadastro deve ser efetuado. Do contrário, deve ser informado:
        - média de idade dos jogadores do “corinthians” com mais de 80 quilos.
        - o percentual de jogadores que tem menos de 20 anos.
        - o nome do jogador mais novo e com peso maior que 70 quilos.
        - a quantidade de jogadores do “santos” com idade maior que 20 ou com peso menor ou igual a
        65 quilos.

Resposta:
    SOMA_IDADE_CORINTHIANS_MAIS_80_QUILOS = 0
    QUANTIDADE_JOGADORES_CORINTHIANS = 0

    QUANTIDADE_JOGADORES_MENOS_20_ANOS = 0
    QUANTIDADE_TOTAL_JOGADORES = 0

    IDADE_JOGADOR_MAIS_NOVO_MAIS_70_QUILOS = 0
    NOME_JOGADOR_MAIS_NOVO_MAIS_70_QUILOS = ""

    QUANTIDADE_JOGADORES_SANTOS_MAIOR_20_ANOS_PESO_MENOR_IGUAL_65 = 0

    while True:
        nome = input("Digite o nome\n")
        idade = int(input("Digite a idade\n"))
        peso = float(input("Digite o peso\n"))
        time = input("Digite o time\n")

        if time == "corinthians" and peso > 80:
            SOMA_IDADE_CORINTHIANS_MAIS_80_QUILOS += idade
            QUANTIDADE_JOGADORES_CORINTHIANS += 1

        if idade < 20:
            QUANTIDADE_JOGADORES_MENOS_20_ANOS += 1
        QUANTIDADE_TOTAL_JOGADORES += 1

        if (peso > 70 and
        (IDADE_JOGADOR_MAIS_NOVO_MAIS_70_QUILOS == 0 or
        IDADE_JOGADOR_MAIS_NOVO_MAIS_70_QUILOS > idade)):
            IDADE_JOGADOR_MAIS_NOVO_MAIS_70_QUILOS = idade
            NOME_JOGADOR_MAIS_NOVO_MAIS_70_QUILOS = nome

        if time == "santos" and (idade > 20 or peso <= 65):
            QUANTIDADE_JOGADORES_SANTOS_MAIOR_20_ANOS_PESO_MENOR_IGUAL_65 += 1

        if input("Deseja cadastrar mais jogadores? (sim/nao)\n") == "nao":
            break

    if not QUANTIDADE_JOGADORES_CORINTHIANS:
        QUANTIDADE_JOGADORES_CORINTHIANS = 1
    if not QUANTIDADE_TOTAL_JOGADORES:
        QUANTIDADE_TOTAL_JOGADORES = 1

    print(SOMA_IDADE_CORINTHIANS_MAIS_80_QUILOS/QUANTIDADE_JOGADORES_CORINTHIANS)
    print(QUANTIDADE_JOGADORES_MENOS_20_ANOS/QUANTIDADE_TOTAL_JOGADORES*100)
    print(NOME_JOGADOR_MAIS_NOVO_MAIS_70_QUILOS)
    print(QUANTIDADE_JOGADORES_SANTOS_MAIOR_20_ANOS_PESO_MENOR_IGUAL_65)
"""

"""
Ex. 3

Pergunta:
    Faça um programa para informatizar o cadastro dos pacientes em um hospital. Você deve
    cadastrar os pacientes com as seguintes informações: nome, idade, sexo (M ou F) e peso. Após
    terminado o cadastro, perguntar se o usuário deseja cadastrar mais alunos. Caso ele responda “sim”
    outro cadastro deve ser efetuado. Do contrário, deve ser informado:
        - o nome do paciente mais velho e com peso maior que 50 quilos.
        - peso médio dos pacientes do sexo feminino com mais de 30 anos.
        - a quantidade de pacientes do sexo masculino ou com idade menor que 45 anos.
        - o percentual de pacientes (masculino ou feminino) que são idosos (mais de 59 anos).
    
Resposta:
    IDADE_PACIENTE_MAIS_VELHO_MAIS_50_QUILOS = 0
    NOME_PACIENTE_MAIS_VELHO_MAIS_50_QUILOS = ""

    SOMA_PESO_MULHERES_MAIS_30_ANOS = 0
    QUANTIDADE_PESO_MULHERES_MAIS_30_ANOS = 0

    QUANTIDADE_HOMENS_MENOS_45_ANOS = 0

    QUANTIDADE_PACIENTES_IDOSOS_MAIS_59_ANOS = 0
    QUANTIDADE_TOTAL_PACIENTES = 0

    while True:
        nome = input("Digite o nome\n")
        idade = int(input("Digite a idade\n"))
        sexo = input("Digite o sexo(h/m)\n")
        peso = float(input("Digite o peso\n"))

        if (peso > 50 and
        (IDADE_PACIENTE_MAIS_VELHO_MAIS_50_QUILOS == 0 or
        IDADE_PACIENTE_MAIS_VELHO_MAIS_50_QUILOS < idade)):
            IDADE_PACIENTE_MAIS_VELHO_MAIS_50_QUILOS = idade
            NOME_PACIENTE_MAIS_VELHO_MAIS_50_QUILOS = nome

        if sexo == "m" and idade > 30:
            SOMA_PESO_MULHERES_MAIS_30_ANOS += peso
            QUANTIDADE_PESO_MULHERES_MAIS_30_ANOS += 1

        if sexo == "h" and idade < 45:
            QUANTIDADE_HOMENS_MENOS_45_ANOS += 1

        if idade > 59:
            QUANTIDADE_PACIENTES_IDOSOS_MAIS_59_ANOS += 1
        QUANTIDADE_TOTAL_PACIENTES += 1

        if input("Deseja cadastrar mais alunos?(s/n)") == "n":
            break

    if not QUANTIDADE_PESO_MULHERES_MAIS_30_ANOS:
        QUANTIDADE_PESO_MULHERES_MAIS_30_ANOS = 1
    if not QUANTIDADE_TOTAL_PACIENTES:
        QUANTIDADE_TOTAL_PACIENTES = 1

    print(NOME_PACIENTE_MAIS_VELHO_MAIS_50_QUILOS)
    print(SOMA_PESO_MULHERES_MAIS_30_ANOS/QUANTIDADE_PESO_MULHERES_MAIS_30_ANOS)
    print(QUANTIDADE_HOMENS_MENOS_45_ANOS)
    print(QUANTIDADE_PACIENTES_IDOSOS_MAIS_59_ANOS/QUANTIDADE_TOTAL_PACIENTES*100)
"""

"""
Ex. 4

Pergunta:
    Leia o valor de elementos da série, imprima a mesma e calcule o valor:
        S = 2/4 - 3/9 + 4/16 - 5/25 + 6/36 - .... + n/m.

Resposta:
    S = 0

    n = int(input("Digite o numero de elementos\n"))

    for i in range(n):
        S = (2+i)*(-1)**i/(2+i)**2
        print(f"{(2+i)*(-1)**i}/{(2+i)**2}")

    print(S if n >= 0 else "numero invalido")
"""

"""
Ex. 5

Pergunta:
    Faça um programa que, a partir de um número inserido pelo usuário,
    informe se ele é primo ou não.

Resposta:
    PRIMO = True

    num = int(input("Digite um numero\n"))

    if num == 0 and num == 1:
        PRIMO = False

    for i in range(2, num):
        if num%i == 0:
            PRIMO = False
            break

    if PRIMO:
        print("primo")
    else:
        print("nao primo")
"""

"""
Ex. 6

Pergunta:
    Faça um programa que leia um número digitado pelo usuário. Depois, informe todos os
    números primos gerados até o número digitado pelo usuário.

Resposta:
    num = int(input("Digite um numero\n"))

    for i in range(2, num):
        PRIMO = True

        for j in range(2, i):
            if i%j == 0:
                PRIMO = False
                break

        if PRIMO:
            print(i)
"""