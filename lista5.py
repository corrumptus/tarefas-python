"""
Ex. Exercício hotel

Pergunta:
    Considere o cenário de um Hotel. Faça um programa para cadastrar e
    gerenciar os hóspedes. Para cada hóspede deve ser cadastrado:
    nome, idade, e quarto (1 - simples, 2 - luxo , ou 3 - presidencial).
    Construa um menu onde é possível:
    - Incluir novos hóspedes(incluir um hospede por vez).
    O sistema não deve permitir o cadastrado de dois hóspedes com o mesmo nome.
    Se isso ocorrer, o sistema deve informar que não é possível cadastrar o hóspede.
    Exemplo: se o nome “Maria” estiver cadastrado não pode ser possível cadastrar “MARIA”.
    - Listar todos os dados dos hóspedes cadastrados.
    - Atualizar um hóspede a partir do nome. O usuário deve digitar o nome e
    o sistema deve perguntar a nova idade e o novo tipo de quarto do hóspede.
    Caso o usuário digite o nome de um hóspede que não exista o sistema deve
    informar que o hóspede não existe.
    - Exibir os hóspedes de determinado tipo de quarto: O sistema pergunta qual o tipo de quarto.
    O usuário deve informar o tipo de quarto para o qual está buscando a lista de hóspedes.
    O sistema deve exibir na tela os nomes dos hóspedes que são do tipo de quarto que o usuário
    escolheu.
    - Exibir a quantidade de hóspedes que tiveram seus dados atualizados.
    - Informar a média de idade dos hóspedes de quartos do tipo “simples”.
    - Informar o nome do hóspede mais velho.

Resposta:
    lista_hospedes = [] # [[nome, idade, quarto, atualizado], ...]

    while True:
        print("1 - Inserir novo hospede")
        print("2 - Listar todos os hospedes")
        print("3 - Atualizar um hospede")
        print("4 - Exibir hospedes em determinado tipo de quarto")
        print("5 - Exibir a quantidade de hospedes que tiveram os dados atualizados")
        print("6 - Exibir a média de idade dos hospedes de quarto simples")
        print("7 - Exibir o nome do hospede mais velho")
        print("0 - sair")
        op = int(input("Digite a opção\n"))

        if op == 0:
            break

        if op == 1:
            CADASTRADO = False

            nome = input("Digite o nome\n").lower()

            for i, hospede in enumerate(lista_hospedes):
                if nome == hospede[0]:
                    CADASTRADO = True

            if not CADASTRADO:
                idade = int(input("Digite a idade\n"))
                quarto = int(input("Digite o tipo de quarto(1-simples|2-luxo|3-presidencial)\n"))
                ATUALIZADO = False
                lista_hospedes.append([nome, idade, quarto, ATUALIZADO])
            else:
                print("Cliente já cadastrado")

        elif op == 2:
            for i, hospede in enumerate(lista_hospedes):
                print(f"nome: {hospede[0].title()}")
                print(f"idade: {hospede[1]}")
                print(f"quarto: {hospede[2]}")

        elif op == 3:
            ENCONTRADO = False

            nome = input("Digite o nome\n").lower()

            for i, hospede in enumerate(lista_hospedes):
                if nome == hospede[0]:
                    idade = int(input("Digite a idade\n"))
                    quarto = int(input("Digite o quarto(1-simples|2-luxo|3-presidencial)\n"))
                    ATUALIZADO = True
                    lista_hospedes[i] = [nome, idade, quarto,   ATUALIZADO]
                    ENCONTRADO = True

            if not ENCONTRADO:
                print("Cliente não encontrado")

        elif op == 4:
            quarto = int(input("Digite o tipo de quarto(1-simples|2-luxo|3-presidencial)\n"))

            for i, hospede in enumerate(lista_hospedes):
                if hospede[2] == quarto:
                    print(hospede[0].title())

        elif op == 5:
            QUANTIDADE = 0

            for i, hospede in enumerate(lista_hospedes):
                if hospede[3]:
                    QUANTIDADE += 1

            print(QUANTIDADE)

        elif op == 6:
            SOMA = 0
            QUANTIDADE = 0

            for i, hospede in enumerate(lista_hospedes):
                if hospede[2] == 1:
                    SOMA += hospede[1]
                    QUANTIDADE += 1

            if QUANTIDADE == 0:
                QUANTIDADE = 1

            print(SOMA/QUANTIDADE)

        elif op == 7:
            IDADE = 0
            NOME = ""

            for i, hospede in enumerate(lista_hospedes):
                if IDADE < hospede[1]:
                    IDADE = hospede[1]
                    NOME = hospede[0]

            print(NOME)
"""

"""
Ex. Exercício vendas

Pergunta:
    Faça um programa para gerenciar as vendas de produtos em uma empresa de eletrônicos.
    Para o cadastro de produtos você deve implementar as seguintes funções:
    - cadastro de produto com nome, valor e quantidade em estoque
    - listar todos os produtos
    Você também deve gerenciar as vendas:
    - cadastro de vendas. Deve ser registrado produto foi vendido, a quantidade e
    o nome do cliente que comprou o produto.
    Considere que a venda só terá um produto envolvido.
    Você deve verificar se existe disponibilidade do produto no estoque.
    A cada venda a quantidade em estoque deve ser atualizada.
    Uma venda só poderá ser realizada para um produto já cadastrado.
    Caso o usuário tente lançar uma venda para produto não cadastrado,
    o sistema deve permitir o cadastro do produto e posterior lançamento da venda.
    - gerar relatório de vendas informando todas as vendas realizadas
    - informar o nome do cliente que mais gastou
    - considerando que a empresa paga de imposto 20% sobre o faturamento, calcule:
    o valor total que ela irá faturar e qual o valor do imposto que deve ser pago
    - informe o nome produto mais vendido

Resposta:
    lista_produtos = []
    lista_vendas = []
    lista_clientes_valores = []

    while True:
        print("1 - Cadastrar produtos")
        print("2 - Listar produtos")
        print("3 - Cadastrar vendas")
        print("4 - Listar todas as vendas")
        print("5 - Mostrar o cliente que mais gastou")
        print("6 - Calcular e mostrar receita")
        print("7 - Mostrar o produto mais vendido")
        print("0 - sair")
        op = int(input("Digite a opção\n"))

        if op == 0:
            break

        if op == 1:
            CADASTRADO = False
            nome = input("Digite o nome\n")
            for produto in lista_produtos:
                if produto[0] == nome:
                    CADASTRADO = True
                    break
            if CADASTRADO:
                print("Produto já cadastrado")
                continue

            valor = float(input("Digite o valor\n"))
            if valor < 0:
                print("Valor inválido")
                continue

            quantidade = int(input("Digite a quantidade\n"))
            if quantidade < 0:
                print("Valor inválido")
                continue

            lista_produtos.append([nome, valor, quantidade])

        elif op == 2:
            for produto in lista_produtos:
                print(f"nome: {produto[0]}")
                print(f"valor: {produto[1]}")
                print(f"quantidade: {produto[2]}")

        elif op == 3:
            ENCONTRADO = False

            nome = input("Digite o nome do produto\n")

            for produto in lista_produtos:
                if nome == produto[0]:
                    ENCONTRADO = True

                    quantidade = int(input("Digite a quantidade\n"))
                    if quantidade <= produto[2]:
                        produto[2] -= quantidade

                        nome_cliente = input("Digite o nome do cliente\n")

                        lista_vendas.append([nome, quantidade, nome_cliente])

                        preco_total = produto[1]*quantidade

                        CLIENTE_EXISTE = False

                        for cliente in lista_clientes_valores:
                            if cliente[0] == nome_cliente:
                                cliente[1] += preco_total
                                CLIENTE_EXISTE = True

                        if not CLIENTE_EXISTE:
                            lista_clientes_valores.append([nome_cliente, preco_total])

                        break

                    print("Estoque insuficiente")

            if not ENCONTRADO:
                print("Produto Não encontrado. Cadastre o produto:\n")
                valor = float(input("Digite o valor do produto\n"))
                quantidade_produto = int(input("Digite a quantidade do produto\n"))

                lista_produtos.append([nome, valor, quantidade_produto])

                if quantidade >= quantidade_produto:
                    nome_cliente = input("Digite o nome do cliente\n")

                    lista_vendas.append([nome, quantidade, nome_cliente])
                    lista_produtos[-1][1] -= quantidade
                else:
                    print("Estoque insuficiente")


        elif op == 4:
            for venda in lista_vendas:
                print(f"nome do produto: {venda[0]}")
                print(f"quantidade do produto: {venda[1]}")
                print(f"nome do cliente: {venda[2]}")

        elif op == 5:
            MAIOR_VALOR = 0
            NOME_MAIOR_VALOR = ""

            for cliente in lista_clientes_valores:
                if MAIOR_VALOR < cliente[1]:
                    MAIOR_VALOR = cliente[1]
                    NOME_MAIOR_VALOR = cliente[0]

            print(NOME_MAIOR_VALOR)

        elif op == 6:
            FATURAMENTO = 0

            for cliente in lista_clientes_valores:
                FATURAMENTO += cliente[1]

            print(f"faturamento: {FATURAMENTO}")
            print(f"imposto: {FATURAMENTO/5}")

        elif op == 7:
            lista_nome_produtos = []
            lista_quantidade_total_produtos = []

            for venda in lista_vendas:
                if venda[0] in lista_nome_produtos:
                    for i, nome in enumerate(lista_nome_produtos):
                        if nome == venda[0]:
                            lista_quantidade_total_produtos[i] += venda[1]
                else:
                    lista_nome_produtos.append(venda[0])
                    lista_quantidade_total_produtos.append(venda[1])

            QUANTIDADE_PRODUTO_MAIS_COMPRADO = 0
            PRODUTO_MAIS_COMPRADO = ""

            for i, quantidade in enumerate(lista_quantidade_total_produtos):
                if QUANTIDADE_PRODUTO_MAIS_COMPRADO < quantidade:
                    QUANTIDADE_PRODUTO_MAIS_COMPRADO = quantidade
                    PRODUTO_MAIS_COMPRADO = lista_nome_produtos[i]

            print(PRODUTO_MAIS_COMPRADO)
"""