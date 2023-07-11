"""
Ex. 1

Pergunta:
    Escreva um programa em Python que lê 2 números e escreve o valor do maior.

Resposta:
    numero1 = float(input("Digite o primeiro número\n"))
    numero2 = float(input("Digite o segundo número\n"))

    if numero1 > numero2:
        print(numero1)
    else:
        print(numero2)
"""

"""
Ex. 2

Pergunta:
    Escreva um programa em Python que lê 3 números e escreve o valor do maior.

Resposta:
    numero1 = float(input("Digite o primeiro número\n"))
    numero2 = float(input("Digite o segundo número\n"))
    numero3 = float(input("Digite o terceiro número\n"))

    if numero1 > numero2 and numero1 > numero3:
        print(numero1)
    elif numero2 > numero3:
        print(numero2)
    else:
        print(numero3)
"""

"""
Ex. 3

Pergunta:
    Escreva um programa em Python que lê 5 valores e conta quantos destes valores
    são maiores que 10, escrevendo esta informação na tela.

Resposta:
    CONTADOR = 0

    num = float(input("Digite um número\n"))
    if num > 10:
        print(str(num) + " é maior que 10")
        CONTADOR += 1

    num = float(input("Digite um número\n"))
    if num > 10:
        print(str(num) + " é maior que 10")
        CONTADOR += 1

    num = float(input("Digite um número\n"))
    if num > 10:
        print(str(num) + " é maior que 10")
        CONTADOR += 1

    num = float(input("Digite um número\n"))
    if num > 10:
        print(str(num) + " é maior que 10")
        CONTADOR += 1

    num = float(input("Digite um número\n"))
    if num > 10:
        print(str(num) + " é maior que 10")
        CONTADOR += 1

    print(str(CONTADOR) + " números são maiores do que 10")
"""

"""
Ex. 4

Pergunta:
    Escreva um programa que calcula o valor de lotes imobiliários em duas cidades, 
    São Paulo e Curitiba. O programa deve perguntar qual o tamanho do lote (lado e 
    comprimento). A partir desses valores, calcule e exiba quantos metros quadrados 
    tem o lote. Pergunte em que cidade está localizado o lote (São Paulo ou Curitiba). 
    Depois, calcule e exiba o valor do lote sabendo que, se estiver em São 
    Paulo custará R$ 500,00 o metro quadrado e se estiver em Curitiba custará R$ 
    450,00 o metro quadrado.

Resposta:
    base = float(input("Digite o comprimento do lote\n"))
    altura = float(input("Digite a largura do lote\n"))

    print(str(base*altura)+"m²")

    local = input("Digite aonde fica o lote(São Paulo ou Curitiba)\n")
    if local == "São Paulo":
        print("R$"+str(base*altura*500))
    elif local == "Curitiba":
        print("R$"+str(base*altura*450))
    else:
        print("Local inválido")
"""

"""
Ex. 5

Pergunta:
    Escreva um programa que permita ao usuário digitar a nota do aluno na prova, a 
    nota do aluno nos trabalhos e a freqüência do mesmo. O calculo da nota do aluno 
    é calculada sabendo que a prova tem peso de 70% e o trabalho de 30%. A partir 
    dos dados abaixo indique se o aluno está aprovado, reprovado ou em recuperação.
        - Aprovado: média >= 6.0 e freqüência >= 75%
        - Recuperação: média >= 4.0 e média < 6.0 e freqüência >= 75%
        - Reprovado: média < 4.0 ou freqüência < 75%

Resposta:
    prova = float(input("Digite a nota da prova(0-10)\n"))
    trabalhos = float(input("Digite a nota dos trabalhos(0-10)\n"))
    frequencia = float(input("Digite a frequencia do aluno(0-100)\n"))

    media = (0.7*prova) + (0.3*trabalhos)

    if media >= 6 and frequencia >= 75:
        print("Aprovado")
    elif media >= 4 and frequencia >= 75:
        print("Recuperação")
    else:
        print("Reprovado")
"""

"""
Ex. 6

Pergunta:
    O índice de Massa Corporal (IMC) é uma fórmula que indica se um adulto está 
    acima do peso, se está obeso ou abaixo do peso ideal considerado saudável. A 
    fórmula para calcular o Índice de Massa Corporal é: 
    IMC = peso / (altura)²
    Faça um programa que calcule o IMC de uma pessoa.
    A partir do IMC, A Organização Mundial de Saúde usa um critério simples: 
        IMC em adultos       Condição
        abaixo de 18,5       abaixo do peso
        entre 18,5 e 25      peso normal
        entre 25 e 30        acima do peso
        acima de 30          obeso
    Faça um programa que leia a altura e peso do usuário e determine o IMC da pessoa e
    indique qual a sua condição.

Resposta:
    peso = float(input("Digite o peso\n"))
    altura = float(input("Digite a altura\n"))

    IMC = peso / altura**2

    if IMC > 30:
        print("obeso")
    elif IMC > 25:
        print("acima do peso")
    elif IMC > 18.5:
        print("peso normal")
    else:
        print("abaixo do peso")
"""

"""
Ex. 7

Pergunta:
    Escrever um algoritmo para ler as dimensões de uma cozinha (comprimento, 
    largura e altura), calcular e escrever a quantidade de caixas de azulejos para 
    azulejar todas as paredes (considere que não será descontada a área ocupada por 
    portas e janelas). Cada caixa de azulejos possui 2 metros quadrados.

Resposta:
    comprimento = float(input("Digite o comprimento\n"))
    largura = float(input("Digite a largura\n"))
    altura = float(input("Digite a altura\n"))

    area = 2*altura*(comprimento + largura)

    if area%2 == 0:
        print(area/2)
    else:
        print(int(area/2)+1)
"""

"""
Ex. 8

Pergunta:
    A prefeitura de Quixeramubim abriu uma linha de crédito para os funcionários
    estatutários. O valor máximo da prestação não poderá ultrapassar 30% do salário
    bruto. Fazer um algoritmo que permita entrar com o salário bruto e o valor da
    prestação, e informar se o empréstimo pode ou não ser concedido.

Resposta:
    salario_bruto = float(input("Digite o salário bruto\n"))
    prestacao = float(input("Digite o valor da prestação\n"))

    if prestacao > 0.3*salario_bruto:
        print("empréstimo concedido")
    else:
        print("empréstimo não concedido")
"""

"""
Ex. 9

Pergunta:
    Faça um programa que leia um numerador e um denominador. Depois, calcule o
    resultado da divisão, MOD (%).

Resposta:
    num = float(input("Digite o numerador\n"))
    dem = float(input("Digite o denominador\n"))

    if dem != 0:
        print(num/dem)
        print(num%dem)
    else:
        print("erro: divisão por 0")
"""

"""
Ex. 10

Pergunta:
    Escreva um programa para ler um valor inteiro e verificar se este valor é par ou impar.

Resposta:
    num = int(input("Digite um numero inteiro\n"))

    if num%2 == 0:
        print("par")
    else:
        print("impar")
"""

"""
Ex. 11

Pergunta:
    Escrever um programa que determine se um número inteiro pode ser divisível por
    três. Imprima uma mensagem.

Resposta:
    num = int(input("Digite um numero inteiro\n"))

    if num%3 == 0:
        print("divisível por 3")
    else:
        print("não divisível por 3")
"""

"""
Ex. 12

Pergunta:
    Escreva um algoritmo que leia um número e informe se ele é divisível por 10,
    por 5 ou por 2 ou se não é divisível por nenhum deles.

Resposta:
num = float(input("Digite um numero\n"))

if num%2 == 0 and num%5 == 0:
    print("divisível por 2, 5 e 10")
elif num%2 == 0:
    print("divisível por 2")
elif num%5 == 0:
    print("divisível por 5")
else:
    print("não divisível por 2, 5 e 10")
"""

"""
Ex. 13

Pergunta:
    Escrever um programa que permita ao usuário digitar três números inteiros. Após
    a leitura, o programa deve verificar se os três valores podem formar um triângulo.
    Caso possam, o programa deve imprimir uma mensagem especificando se o
    triângulo é eqüilátero (três lados iguais), isósceles (dois lados iguais) ou escaleno
    (todos os lados diferentes). Obs.: Para que três lados formem um triângulo,
    o comprimento de cada um dos lados tem que ser menor que a soma dos outros
    dois.

Resposta:
lado1 = float(input("Digite o tamanho do primeiro lado\n"))
lado2 = float(input("Digite o tamanho do segundo lado\n"))
lado3 = float(input("Digite o tamanho do terceiro lado\n"))

if lado1 >= lado2 + lado3 or lado2 >= lado1 + lado3 or lado3 >= lado1 + lado2:
    print("Os tamanhos não formam um triangulo")
elif lado1 == lado2 == lado3:
    print("triangulo equilatero")
elif (lado1 == lado2) or (lado2 == lado3) or (lado3 == lado1):
    print("triangulo isosceles")
else:
    print("triangulo escaleno")
"""

"""
Ex. 14

Pergunta:
    Escrever um programa que leia a idade de três indivíduos e determine se a soma
    das três idades é maior ou igual a 100 anos. Se for, o programa deve imprimir a
    mensagem “maior ou igual a 100”, ou a mensagem “menor que 100” deve ser
    impressa.

Resposta:
    idadeF = int(input("Digite a primeira idade\n"))
    idadeS = int(input("Digite a segunda idada\n"))
    idadeT = int(input("Digite a terceira idade\n"))

    if idadeF + idadeS + idadeT >= 100:
        print("maior ou igual a 100")
    else:
        print("meor que 100")
"""

"""
Ex. 15

Pergunta:
    Crie um algoritmo que leia a idade de uma pessoa e informe a sua classe eleitoral:
        a. não eleitor (abaixo de 16 anos);
        b. eleitor obrigatório (entre a faixa de 18 e menor de 65 anos);
        c. eleitor facultativo (eleitor entre 16 até 18 anos ou eleitor maior de 65
        anos, inclusive).

Resposta:
    idade = int(input("Digite uma idade\n"))

    if 18 <= idade < 65:
        print("eleitor obrigatorio")
    elif (16 <= idade < 18) or idade >= 65:
        print("eleitor facultativo")
    else:
        print("não eleitor")
"""

"""
Ex. 16

Pergunta:
    Escreva um algoritmo que dada a idade de uma pessoa, determine
    sua classificação segundo o seguinte:
        a. maior de idade;
        b. menor de idade;
        c. pessoa idosa (idade superior ou igual a 65 anos).

Resposta:
    idade = int(input("Digite uma idade\n"))

    if idade < 18:
        print("menor de idade")
    elif idade < 65:
        print("maior de idade")
    else:
        print("idoso")
"""

"""
Ex. 17

Pergunta:
    Escrever um programa que permita ao usuário digitar uma data (dia e mês), em
    seguida, o programa deve calcular a quantidade de dias que falta para o final do
    ano. Suponha que todos os meses do ano possuem 30 dias.

Resposta:
    dia = int(input("Digite um dia\n"))
    mes = int(input("Digite um mes\n"))

    if 0 <= dia <= 30 and 1 <= mes <= 12:
        print(f"faltam {30-dia+(12-mes)*30} dias")
    else:
        print("data invalida")
"""

"""
Ex. 18

Pergunta:
    Escrever um programa que permita ao usuário digitar o dia e mês de seu
    aniversário e a data de hoje (dia e mês), em seguida, o programa deve calcular
    quantos dias faltam entre a data de hoje e a data do próximo aniversário. Suponha
    todos os meses com 30 dias.

Resposta:
    dia = int(input("Digite o dia do aniversario\n"))
    mes = int(input("Digite o mes do aniversario\n"))

    if 0 <= dia <= 30 and 1 <= mes <= 12:
        dia_hoje = int(input("Digite o dia de hoje\n"))
        mes_hoje = int(input("Digite o mes de hoje\n"))

        if 0 <= dia_hoje <= 30 and 1 <= mes_hoje <= 12:
            print(f"faltam {30+dia-dia_hoje+(12+mes-mes_hoje)*60} dias para o proximo aniversario")
        else:
            print("data invalida")
    else:
        print("data de aniversario invalida")
"""

"""
Ex. 19

Pergunta:
    Escreva um programa que permita ao usuário digitar a idade, o sexo, e o salário
    de um indivíduo. Analise os dados de entrada e imprima uma das possíveis
    mensagens abaixo:
        - Masculino, com mais de 18 anos.
        - Feminino, com salário acima de R$ 50.000,00 e com idade acima de 40 anos.
        - Masculino ou feminino e idade entre 20 e 30 anos.
        - Não se encaixa em nenhuma das possibilidades anteriores.

Resposta:
    idade = int(input("Digite uma idade\n"))
    sexo = input("Digite um sexo(m/f)\n")
    salario = float(input("Digite um salario\n"))

    if sexo == 'm' and idade > 18:
        print("Masculino, com mais de  18 anos.")
    elif sexo == 'f' and salario > 50000 and idade > 40:
        print("Feminino, com salário acima de R$ 50.000,00 e com idade acima de 40 anos.")
    elif idade >= 20 or idade < 30:
        print("Masculino ou feminino e idade entre 20 e 30 anos.")
    else:
        print("Não se encaixa em nenhuma das possibilidades anteriores.")
"""

"""
Ex. 20

Pergunta:
    Um motorista de taxi deseja calcular o rendimento de seu carro na praça.
    Sabendo-se que o preço do combustível é de R$2,50, escreva um programa em C
    para ler:
        - a marcação do odômetro no início do dia
        - a marcação no final do dia
        - o número de litros de combustível gasto
        - o valor total (R$) recebido dos passageiros.
    Calcule e escreva a média do consumo em Km/l e o lucro líquido do dia. Se o
    lucro líquido no dia for inferior a R$ 100,00 exiba a mensagem que o
    taxista precisa melhorar seu desempenho.

Resposta:
    marcacao_inicio = float(input("Digite a marcacao inicial do odometro\n"))
    marcacao_fim = float(input("Digite a marcacao final do odometro\n"))
    litros = float(input("Digite a quantidade de litros gastos\n"))
    valor_recebido = float(input("Digite o valor recebido\n"))

    print(f"a media de consumo foi de {(marcacao_fim-marcacao_inicio)/litros}")
    print(f"o lucro liquido foi de {valor_recebido - 2.5*litros}")

    if valor_recebido - 2.5*litros < 100:
        print("o taxista precisa melhorar seu desempenho")
"""