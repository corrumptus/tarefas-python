"""
Ex. 1

Pergunta:
    Construa um algoritmo que calcule a média aritmética de um conjunto de
    números inteiros, pares, fornecidos pelo usuário. O valor de parada será 0. O
    usuário poderá entrar números ímpares, porém, eles não devem ser considerados
    nos cálculos.

Resposta:
    MEDIA = 0
    CONTADOR = 0

    while True:
        num = int(input("Digite um numero inteiro\n"))

        if num == 0:
            break
        if num%2 == 0:
            MEDIA += num
            CONTADOR += 1

    if not CONTADOR:
        CONTADOR = 1

    print(MEDIA/CONTADOR)
"""

"""
Ex. 2

Pergunta:
    Desenvolva um gerador de tabuada, capaz de gerar a tabuada de qualquer
    número inteiro entre 1 a 10. O usuário deve informar de qual numero ele deseja
    ver a tabuada. A saída deve ser conforme o exemplo abaixo:
        a. Tabuada de 5:
        b. 5 X 1 = 5
        c. 5 X 2 = 10
        d. ...
        e. 5 X 10 = 50

Resposta:
    num = int(input("Digite um numero inteiro\n"))

    for i in range(num):
        print(f"{num} X {i+1} = {num*(i+1)}")
"""

"""
Ex. 3

Pergunta:
    Elabore um programa que peça dois números, base e expoente, calcule e mostre
    o primeiro número elevado ao segundo número.

Resposta:
    base = float(input("Digite um numero\n"))
    expoente = float(input("Digite um numero\n"))

    if not expoente and not base:
        print("erro: indefinição matematica")
    else:
        print(base**expoente)
"""

"""
Ex. 4

Pergunta:
    A série de Fibonacci é formada pela seqüência 0,1,1,2,3,5,8,13,21,34,55,... Faça
    um programa capaz de gerar a série até o n-ésimo termo.

Resposta:
    NUM1 = 0
    NUM2 = 1

    n = int(input("Digite qual é o n-ésimo termo\n"))

    if n == 1:
        print(f"{NUM1}")
    elif n > 2:
        print(f"{NUM1}\n{NUM2}")
        for i in range(n-2):
            NUM1, NUM2 = NUM2, NUM1+NUM2
            print(NUM2)
    else:
        print("número inválido")
"""

"""
Ex. 5

Pergunta:
    A série de Fibonacci é formada pela seqüência 0,1,1,2,3,5,8,13,21,34,55,... Faça
    um programa que gere a série até que o valor seja maior que 500.

Resposta:
    NUM1 = 0
    NUM2 = 1

    print("0\n1")

    while NUM2 < 500:
        NUM1, NUM2 = NUM2, NUM1+NUM2
        print(NUM2)
"""

"""
Ex. 6

Pergunta:
    Faça um programa que calcule o fatorial de um número inteiro fornecido pelo
    usuário. Ex.: 5!=5.4.3.2.1=120

Resposta:
    FATORIAL = 1

    num = int(input("Digite um numero inteiro\n"))

    if num >= 0:
        for i in range(num):
            FATORIAL *= i+1

        print(FATORIAL)
    else:
        print("numero invalido")
"""

"""
Ex. 7

Pergunta:
    Elabore um programa que mostre os n termos da Série a seguir:
        a. S = 1/1 + 2/3 + 3/5 + 4/7 + 5/9 + ... + n/m.
    Imprima no final a soma da série. (Leia o valor de n)

Resposta:
    CONTADOR = 0

    n = int(input("Digite um numero inteiro\n"))

    if n > 0:
        for i in range(n):
            CONTADOR += (i+1)/(1+2*i)
            print(f"{i+1}/{(1+2*i)}")

        print(CONTADOR)
    else:
        print("quantidade invalida de termos")
"""

"""
Ex. 8

Pergunta:
    Elabore um programa que peça para n pessoas a sua idade, ao final o programa
    devera verificar se a média de idade da turma varia entre 0 e 25,26 e 60 e maior
    que 60; e então, dizer se a turma é jovem, adulta ou idosa, conforme a média
    calculada. (Leia o valor de n)

Resposta:
    MEDIA = 0

    QUANTIDADE = int(input("Digite a quantidade de pessoas\n"))

    for i in range(QUANTIDADE):
        MEDIA += int(input("Digite a idade\n"))

    if not QUANTIDADE:
        QUANTIDADE = 1

    MEDIA /= QUANTIDADE

    if MEDIA >= 65:
        print("turma idosa")
    elif MEDIA >= 25:
        print("turma adulta")
    elif MEDIA >= 0:
        print("turma jovem")
    else:
        print("erro")
"""

"""
Ex. 9

Pergunta:
    Escrever um programa que gere aleatoriamente números entre 0 e 100. Ao gerar
    o número 50, o programa deverá ser encerrado, imprimindo na tela uma
    mensagem informando a quantidade de números pares que foram gerados.

Resposta:
    from random import randint

    CONTADOR = 0

    while randint(0, 100) != 50:
        CONTADOR += 1

    print(CONTADOR)
"""

"""
Ex. 10

Pergunta:
    Escrever um programa que gere aleatoriamente números entre 0 e 100. Ao gerar
    o número 88, o programa deverá ser encerrado, imprimindo na tela uma
    mensagem informando a quantidade de números que foram gerados, a soma e a
    média dos números.

Resposta:
    from random import randint

    NUMERO = 0
    CONTADOR = 0
    SOMA = 0

    while (NUMERO := randint(0, 100)) != 88:
        SOMA += NUMERO
        CONTADOR += 1

    print(CONTADOR)
    print(SOMA)

    if not CONTADOR:
        CONTADOR = 1

    print(SOMA/CONTADOR)
"""

"""
Ex. 11

Pergunta:
    Duas fabricantes de calçado disputam o mercado no Brasil. A empresa A tem
    produção de 10.000 pares/mês e um crescimento mensal de 15%. A empresa B,
    de 8.000 pares/mês e tem um crescimento mensal de 20%. Determinar o número
    de meses necessários para que a empresa B supere o número de pares
    produzidos pela empresa A.

Resposta:
    PARES_INICIAIS_A = 10000
    PARES_INICIAIS_B = 8000
    CRESCIMENTO_A = 0.15
    CRESCIMENTO_B = 0.20
    MESES = 0

    while PARES_INICIAIS_A*(1+CRESCIMENTO_A)**MESES > PARES_INICIAIS_B*(1+CRESCIMENTO_B)**MESES:
        MESES += 1

    print(MESES)
"""

"""
Ex. 12

Pergunta:
    Fazer um programa que gere números aleatórios entre 0 e 100 até o número 45
    ser gerado. Quando isso ocorrer, dizer quantos números menores que 10
    precisaram ser gerados até encontrar o 45.

Resposta:
    from random import randint

    CONTADOR = 0

    while (num := randint(0, 100)) != 45:
        if num < 10:
            CONTADOR += 1

    print(CONTADOR)
"""

"""
Ex. 13

Pergunta:
    Um vendedor de carros recebe comissão de 10% a cada carro vendido com o
    valor até R$10.000,00 e comissão de 11% sobre os carros vendidos que custem
    mais R$10.000,00.
    Faça um programa que leia do vendedor a quantidade de carros que o ele
    vendeu. Depois, para cada carro vendido leia o valor do carro e a modelo do
    carro.
    No fim exiba:
        a. Quanto o vendedor receberá de comissão;
        b. O modelo do carro mais caro;
        c. A quantidade de carros que custam mais que R$20.000,00 e menos que
        R$30.000,00;
        d. O preço médio dos carros.

Resposta:
    COMISSAO = 0
    VALOR_MODELO_MAIS_CARO = 0
    MODELO_MAIS_CARO = ""
    QUANTIDADE_CARROS_ENTRE_20000_30000 = 0
    SOMA_VALOR_CARROS = 0

    NUMERO_CARROS = int(input("Digite o numero de vendas\n"))

    for i in range(NUMERO_CARROS):
        valor = int(input("Digite o valor do carro\n"))
        nome = input("Digite o nome do carro\n")

        COMISSAO += valor * (0.11 if valor > 10000 else 0.1)

        if VALOR_MODELO_MAIS_CARO < valor:
            VALOR_MODELO_MAIS_CARO = valor
            MODELO_MAIS_CARO = nome

        if 20000 <= valor < 30000:
            QUANTIDADE_CARROS_ENTRE_20000_30000 += 1

        SOMA_VALOR_CARROS += valor

    if NUMERO_CARROS == 0:
        NUMERO_CARROS = 1

    print(COMISSAO)
    print(MODELO_MAIS_CARO)
    print(QUANTIDADE_CARROS_ENTRE_20000_30000)
    print(SOMA_VALOR_CARROS/NUMERO_CARROS)
"""

"""
Ex. 14

Pergunta:
    Faça um programa que gere números aleatórios entre 0 e 50 até o número 32 ser
    gerado. Quando isso ocorrer, informar:
        a. A soma de todos os números gerados;
        b. A quantidade de números gerados que é impar;
        c. O menor número gerado.
    
Resposta:
    from random import randint

    SOMA = 0
    IMPARES = 0
    MENOR = 50

    while (num := randint(0, 50)) != 32:
        SOMA += num

        if num%2 == 1:
            IMPARES += 1

        MENOR = min(MENOR, num)

    print(SOMA)
    print(IMPARES)
    print(MENOR)
"""

"""
Ex. 15

Pergunta:
    Criar um algoritmo que leia os limites inferior e superior de um intervalo e
    imprima todos os números pares no intervalo aberto e seu somatório. Suponha
    que os dados digitados são para um intervalo crescente, ou seja, o primeiro valor
    e menor que o segundo.

Resposta:
    SOMA = 0

    menor = int(input("Digite o menor numero do intervalo aberto\n"))
    maior = int(input("Digite o maior numero do intervalo aberto\n"))

    for i in range(menor+1, maior):
        if i%2 == 0:
            SOMA += i
            print(i)

    print(SOMA)
"""

"""
Ex. 16

Pergunta:
    Criar um algoritmo que leia um numero (NUM), e depois leia NUM números
    inteiros e imprima o maior deles. Suponha que todos os números lidos serão
    positivos.

Resposta:
    MAIOR = -1

    QUANTIDADE = int(input("Digite a quantidade de numeros\n"))

    for i in range(QUANTIDADE):
        numero = int(input("Digite um numero\n"))

        MAIOR = max(MAIOR, numero)

    print(MAIOR)
"""

"""
Ex. 17

Pergunta:
    Faça um programa que receba a idade, peso e altura de N pessoas. Calcule e
    mostre:
        a. A média das idades das N pessoas
        b. A quantidade de pessoas com peso superior a 90 quilos e altura inferior a
        1,50 m.
        c. A percentagem de pessoas com idade entre 10 e 30 anos entre as pessoas
        que medem mais de 1,90 m.
    Pergunte ao usuário do programa quantas pessoas serão cadastradas (valor de N).

Resposta:
    SOMA_IDADE = 0
    PESO_ALTURA = 0
    IDADE_ALTURA = 0

    QUANTIDADE = int(input("Digite a quantidade de pessoas\n"))

    for i in range(QUANTIDADE):
        idade = int(input("Digite a idade\n"))
        peso = float(input("Digite o peso\n"))
        altura = float(input("Digite o altura\n"))

        SOMA_IDADE += idade

        if peso > 90 and altura < 1.5:
            PESO_ALTURA += 1

        if (10 <= idade < 30) and altura > 1.9:
            IDADE_ALTURA += 1

    if QUANTIDADE == 0:
        QUANTIDADE = 1

    print(SOMA_IDADE/QUANTIDADE)
    print(PESO_ALTURA)
    print((IDADE_ALTURA/QUANTIDADE)*100)
"""

"""
Ex. 18

Pergunta:
    Dado um pais A, com 5000000 de habitantes e uma taxa de natalidade de 3% ao
    ano, e um pais B com 7000000 de habitantes e uma taxa de natalidade de 2% ao
    ano, escrever um algoritmo que seja capaz de calcular e iterativamente e no fim
    imprimir o tempo necessário para que a população do pais A ultrapasse a
    população do pais B.

Resposta:
    POPULACAO_A = 5000000
    POPULACAO_B = 7000000
    TAXA_A = 0.03
    TAXA_B = 0.02
    ANO = 0

    while POPULACAO_A*(1+TAXA_A)**ANO < POPULACAO_B*(1+TAXA_B)**ANO:
        ANO += 1

    print(ANO)
"""

"""
(fonte: Fundamentos da Programação de Computadores - Ana Fernanda Gomes Ascencio / Edilene Aparecida
Veneruchi de Campos - Pearson + Lista de Exercícios do Professor Pedro Nobile, professora Silvana Affonso
de Lara e Professor Saulo Santos)
"""