"""
Texto suporte:
    Você foi contratado para construir um sistema para uma fábrica de doces.
    No seu sistema deve ser possível:

    1. Cadastrar um doce contendo: nome, valor e categoria. Não deve ser possível
    cadastrar um doce com mesmo nome. Também só podem ser cadastrados doces
    com valor superior a 10 reais.

    2. Listar os doces por categoria. O sistema deve informar uma categoria e
    todos os doces que estão nesta categoria. Depois, informa a próxima categoria
    e os doces que estão nesta segunda categoria e assim por diante.

    3. Cadastrar um cliente com: nome e faturas em aberto. Quando o cliente
    é cadastrado o valor de faturas em aberto deve ser zero.

    4. Listar os clientes.

    5. Registrar uma venda: uma venda deve ser possível armazenar o cliente que
    está fazendo a compra e uma lista de doces comprados com suas respectivas
    quantidades. O sistema deve listar os produtos e seus preços. O cliente deve
    escolher o item que deseja e a quantidade. Deve ser salvo, além da lista
    de produtos e suas quantidades, o valor total da venda. Esse valor total 
    também deve ser salvo nas faturas em aberto do cliente.

    6. Listar todas as vendas realizadas.

    7. Apagar um doce do sistema. Caso alguma venda já tenha sido realizada
    para esse doce não será possível apagar o doce.

    8. Listar o produto mais caro da categoria “bala”.

    9. Listar todas todas as vendas de um determinado cliente. O usuário deve
    informar o nome do cliente.

    10. Cliente pagando fatura: o sistema deve perguntar o nome do cliente.
    Caso o cliente esteja cadastrado o sistema deve exibir o valor em aberto
    e perguntar quanto da dívida será paga. O valor pago será abatido
    da fatura em aberto.
"""

import os.path

def verifica_arquivos(doces_path: str, clientes_path: str, vendas_path: str) -> None:
    if not os.path.isfile(doces_path):
        with open(doces_path, "w", encoding="utf-8") as arquivo:
            arquivo.write("nome,valor,categoria\n")

    if not os.path.isfile(clientes_path):
        with open(clientes_path, "w", encoding="utf-8") as arquivo:
            arquivo.write("nome,fatura\n")

    if not os.path.isfile(vendas_path):
        with open(vendas_path, "w", encoding="utf-8") as arquivo:
            arquivo.write("cliente,doces,quantidades,valorTotal\n")

def carrega_doces(path: str) -> dict[str, dict[str]]:
    doces: dict[str, dict[str]] = {}

    with open(path, "r", encoding="utf-8") as arquivo:
        for linha in arquivo.readlines():
            doce: list[str] = linha.split(",")

            nome_doce: str = doce[0]
            valor_doce: float = float(doce[1])
            categoria_doce: str = doce[2]

            doces[nome_doce] = {"valor": valor_doce, "categoria": categoria_doce}

    return doces

def carrega_clientes(path: str) -> dict[str, list[float]]:
    dicionario_clientes: dict[str, list[float]] = {}

    with open(path, "r", encoding="utf-8") as arquivo:
        for linha in arquivo.readlines():
            cliente: list[str] = linha.split(",")

            nome_cliente: str = cliente[0]
            faturas_cliente: list[float] = [float(fatura) for fatura in cliente[1].split("|")]

            dicionario_clientes[nome_cliente] = faturas_cliente

    return dicionario_clientes

def carrega_vendas(path: str) -> list[dict[str]]:
    vendas: list[dict[str]] = []

    with open(path, "r", encoding="utf-8") as arquivo:
        linhas_arquivo: list[list[str]] = [linha.split(",") for linha in arquivo.readlines()]

    for venda in linhas_arquivo:
        nome_cliente: str = venda[0]
        doces: list[str] = venda[1].split("|")
        quantidades: list[str] = venda[2].split("|")
        valor_total: float = float(venda[3])

        doces_quantidades: dict[str, int] = {}

        for i, doce in enumerate(doces):
            doces_quantidades[doce] = quantidades[i]

        vendas.append(
            {
            "cliente": nome_cliente,
            "doces": doces_quantidades,
            "valorTotal": valor_total
            }
        )

    return vendas

def atualiza_doces(path:str, doces: dict[str, dict[str]]) -> None:
    header: str = "nome,valor,categoria\n"
    linhas_arquivo: list[str] = []

    for doce, infos in doces:
        linhas_arquivo.append(f"{doce},{infos['valor']},{infos['categoria']}")

    with open(path, "w", encoding="utf-8") as arquivo:
        arquivo.write(header)
        arquivo.write("\n".join(linhas_arquivo))

def atualiza_clientes(path: str, clientes: dict[str, list[float]]) -> None:
    header: str = "nome,fatura\n"
    linhas_arquivo: list[str] = []

    for cliente, faturas in clientes:
        linhas_arquivo.append(f"{cliente},{'|'.join(faturas)}")

    with open(path, "w", encoding="utf-8") as arquivo:
        arquivo.write(header)
        arquivo.write("\n".join(linhas_arquivo))

def atualiza_vendas(path: str, vendas: list[dict[str]]) -> None:
    header: str = "cliente,doces,quantidades,valorTotal\n"
    linhas_arquivo: list[str] = []

    for venda in vendas:
        nome_cliente: str = venda["cliente"]
        doces: list[str] = venda["doces"].keys()
        quantidades: list[int] = venda["doces"].values()
        valor_total: float = venda["valorTotal"]

        linhas_arquivo.append(
            f"{nome_cliente},{'|'.join(doces)},{'|'.join(quantidades)},{valor_total}"
        )

    with open(path, "w", encoding="utf-8") as arquivo:
        arquivo.write(header)
        arquivo.write("\n".join(linhas_arquivo))

def cadastrar_doce(path: str, doces: dict[str, dict[str]]) -> str:
    nome: str = input("Digite o nome\n")
    if nome in doces:
        return "Doce já cadastrado"

    valor: float = float(input("Digite o preço(deve ser maior que 10 reais)\n"))
    if valor < 10:
        return "Doce muito barato"

    categoria: str = input("Digite a categoria\n")

    doces[nome] = {"valor": valor, "categoria": categoria}
    atualiza_doces(path, doces)

    return "Doce cadastrado com sucesso"

def listar_doces_por_categoria(doces: dict[str, dict[str]]) -> None:
    categorias: dict[str, list[str]] = {}

    for doce, infos in doces:
        categoria: str = infos["categoria"]
        valor: float = infos["valor"]

        if categoria not in categorias:
            categorias[categoria] = []

        categorias[categoria].append(f"{doce}: R${valor}")

    for categoria, lista_doces in categorias:
        print(str.format(
            """
            --------{}--------
            {}
            {}
            """,
            categoria,
            "\n".join(lista_doces),
            "-"*(len(categoria)+16)
        ))

def cadastrar_cliente(path: str, clientes: dict[str, list[float]]) -> str:
    nome: str = input("Digite o nome\n")
    if nome in clientes:
        return "Cliente já cadastrado"

    clientes[nome] = []
    atualiza_clientes(path, clientes)
    return "Cliente cadastrado com sucesso"

def listar_clientes(clientes: dict[str, list[float]]) -> None:
    for cliente, faturas in clientes:
        print(str.format(
            """
            --------{}--------
            {}
            {}
            """,
            cliente,
            "\n".join(faturas),
            "-"*(len(faturas)+16)
        ))

def cadastrar_venda(
    clientes_path: str, vendas_path: str,
    doces: dict[str, dict[str]], clientes: dict[str, list[float]], vendas: list[dict[str]]
) -> str:
    pedido: dict[str, int] = {}
    valor_total: float = 0

    nome_cliente: str = input("Digite o nome do cliente\n")
    if nome_cliente not in clientes:
        return "Cliente não cadastrado"

    while True:
        listar_doces_por_categoria(doces)
        nome_doce: str = input("Digite o nome do doce\n")
        if nome_doce not in doces:
            print("Doce inválido")
            continue

        quantidade: int = int(input("Digite a quantidade\n"))
        if nome_doce not in pedido:
            pedido[nome_doce] = 0

        pedido[nome_doce] += quantidade
        valor_total += doces[nome_doce]["valor"]*quantidade

        if input("Deseja continuar?(S/N)") == "N":
            break

    vendas.append({"cliente": nome_cliente, "doces": pedido, "valorTotal": valor_total})
    clientes[nome_cliente].append(valor_total)

    atualiza_clientes(clientes_path, clientes)
    atualiza_vendas(vendas_path, vendas)

    return "Venda cadastrada com sucesso"

def listar_vendas(vendas: list[dict[str]]) -> None:
    for i, venda in vendas.items():
        doces_quantidades = [f"{doce}: {quantidade}" for doce, quantidade in venda["doces"].items()]
        print(str.format(
            """
            --------{}--------
            Cliente: {}
            {}
            Valor total: {}
            {}
            """,
            i,
            venda["cliente"],
            "\n".join(doces_quantidades),
            venda["valorTotal"],
            "-"*(len(str(i))+16)
        ))

def excluir_doce(path: str, doces: dict[str, dict[str]], vendas: list[dict[str]]) -> str:
    nome: str = input("Digite o nome do doce\n")
    if nome not in doces:
        return "Doce não cadastrado"

    for venda in vendas:
        if nome in venda["doces"]:
            return "Doce já participou de uma venda, não pode ser removido"

    doces.pop(nome)
    atualiza_doces(path, doces)
    return "Doce removido com sucesso"

def bala_mais_cara(doces: dict[str, dict[str]]) -> str:
    valor: float = 10
    nome: str = ""

    for doce, infos in doces.items():
        valor_doce: float = infos["valor"]

        if infos["categoria"] == "bala" and valor < valor_doce:
            valor = valor_doce
            nome = doce

    return nome

def listar_compras_cliente(clientes: dict[str, list[float]], vendas: list[dict[str|dict[int]|float]]) -> None:
    nome: str = input("Digite o nome\n")
    if nome not in clientes:
        return

    doces_quantidades: dict[str, int] = {}

    for venda in vendas:
        if venda["cliente"] != nome:
            continue

        for doce, quantidade in venda["doces"]:
            if doce not in doces_quantidades:
                doces_quantidades[doce] = 0

            doces_quantidades[doce] += quantidade
    print(str.format(
        """
        --------{}--------
        {}
        {}
        """,
        nome,
        "\n".join([f"{doce}: {quantidade}" for doce, quantidade in doces_quantidades]),
        "-"*(len(nome)+16)
    ))

def pagar_faturas(path: str, clientes: dict[str, list[float]]) -> str:
    nome: str = input("Digite o nome\n")
    if nome not in clientes:
        return "Cliente não cadastrado"

    print("\n".join(clientes[nome]))

    quantidade_faturas: int = 0

    valor_pago: float = float(input("Digite o valor pago"))
    if valor_pago < 0:
        return "Valor inválido"

    if valor_pago == 0:
        return "Foram pagas 0 faturas com sucesso"

    for i, faturas in enumerate(clientes[nome]):
        if faturas[i] <= valor_pago:
            quantidade_faturas += 1
            valor_pago -= faturas[i]

        else:
            faturas[i] -= valor_pago
            exclui_faturas_nulas(clientes[nome])
            atualiza_clientes(path, clientes)
            return f"""
                        Foram pagas {quantidade_faturas} faturascom sucesso.
                        Abatido {valor_pago} da {i+1} fatura({faturas[i+1]}).
                    """

def exclui_faturas_nulas(faturas: list[int]) -> None:
    while True:
        if faturas[0] != 0:
            return

        faturas.pop(0)

def obtem_opcao() -> int:
    print("1- Cadastrar um doce")
    print("2- Listar doces por categoria")
    print("3- Cadastrar um cliente")
    print("4- Listar clientes")
    print("5- Cadastrar uma venda")
    print("6- Listar vendas")
    print("7- Excluir um doce do sistema")
    print("8- Mostrar a bala mais cara")
    print("9- Listar compras de um cliente")
    print("10- Pagamento de fatura")
    print("0- Sair")
    return int(input("Digite a opção escolhida\n"))

if __name__ == "__main__":
    DOCES_PATH: str = "doces.csv"
    CLIENTES_PATH: str = "clientes.csv"
    VENDAS_PATH: str = "vendas.csv"

    verifica_arquivos(DOCES_PATH, CLIENTES_PATH, VENDAS_PATH)

    dict_doces: dict[str, dict[str]] = carrega_doces(DOCES_PATH)
    dict_clientes: dict[str, list[float]] = carrega_clientes(CLIENTES_PATH)
    dict_vendas: list[dict[str]] = carrega_vendas(VENDAS_PATH)

    while (opcao := obtem_opcao()) != 0:
        if opcao == 1:
            resultado: str = cadastrar_doce(DOCES_PATH, dict_doces)
            print(resultado)

        elif opcao == 2:
            listar_doces_por_categoria(dict_doces)

        elif opcao == 3:
            resultado: str = cadastrar_cliente(CLIENTES_PATH, dict_clientes)

            print(resultado)

        elif opcao == 4:
            listar_clientes(dict_clientes)

        elif opcao == 5:
            resultado: str = cadastrar_venda(
                CLIENTES_PATH, VENDAS_PATH, dict_doces, dict_clientes, dict_vendas
            )

            print(resultado)

        elif opcao == 6:
            listar_vendas(dict_vendas)

        elif opcao == 7:
            resultado: str = excluir_doce(DOCES_PATH, dict_doces, dict_vendas)

            print(resultado)

        elif opcao == 8:
            print(bala_mais_cara(dict_doces))

        elif opcao == 9:
            listar_compras_cliente(dict_clientes, dict_vendas)

        elif opcao == 10:
            resultado:str = pagar_faturas(CLIENTES_PATH, dict_clientes)

            print(resultado)

        else:
            print("Opção inválida")
