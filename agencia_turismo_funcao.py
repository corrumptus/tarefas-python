"""
Texto suporte:
    Você foi contratado para construir um sistema de uma agência de turismo.
    No seu sistema deve ser possível:

    1. Cadastrar um cliente contendo: nome e idade. Não deve ser possível cadastrar
    um aluno com mesmo nome e a idade deve ser superior a 18 anos.

    2. Cadastrar um destino de viagem: nome, valor da diária, número mínimo de diárias.

    3. Cadastrar uma viagem: deve ser salvo o nome do cliente, o destino e número de diárias.
    O valor total da viagem também deverá ser salvo na viagem cadastrada. Em cada cliente também
    deverá ser salvo o valor total gasto na agência.

    4. Listar as viagens já salvas, categorizadas por destino. Ex: devem ser listadas todas as
    viagens feitas com destino na Cidade X, depois, todas as viagens feitas para a cidade Z, e
    assim por diante.

    5. Listar os clientes.

    6. Contabilizar a pontuação de cada cliente. Com o intuito de fidelizar os clientes na agência
    foi criado um programa de pontuação. A cada 1000 reais em viagens, o cliente deve receber 100
    pontos. Quando ele totalizar 1500 pontos ele pode escolher uma cidade de destino e ganhará 3
    diárias para esse local. Após calcular a pontuação exibir uma tabela com a lista de pontos por
    cliente. Dica: utilizar um dicionário. Destacar os clientes que estão ganhar a viagem.

    7. Informar o destino mais procurado pelos clientes.

    8. Informar o destino para o qual mais diárias foram vendidas.

    9. Efetuar o pagamento de gastos do cliente: o cliente informa o nome e o sistema exibe
    quanto ele está devendo para a agência. O cliente informa o valor que irá pagar e esse valor
    é abatido das faturas em aberto.

    10. Avaliar status dos clientes: o sistema deve verificar os clientes que possuem mais de
    R$10.000,00 em viagens ainda não pagos. Quando esse valor for atingido não deve ser possível
    mais vender viagens para esse cliente.
"""

def pode_viajar(clientes: dict[dict], nome: str) -> bool:
    if clientes[nome]["divida"] > 10000:
        return False
    return True

def cadastrar_cliente(clientes: dict[dict]) -> bool:
    nome: str = input("Digite o nome do cliente\n")
    if nome in clientes:
        return False

    idade: int = int(input("Digite a idade do cliente\n"))
    if idade <= 18:
        return False

    clientes[nome] = {"idade": idade, "divida": 0, "pontos": 0}
    return True

def cadastrar_destino(destinos: dict[dict]) -> bool:
    nome: str = input("Digite o nome do destino\n")
    if nome in destinos:
        return False

    valor_diaria: float = float(input("Digite o valor da diaria"))
    if valor_diaria < 0:
        return False

    minimo_diarias: int = int(input("Digite o número mínimo de diárias"))
    if minimo_diarias < 0:
        return False

    destinos[nome] = {"valorFiaria": valor_diaria, "minimoDiarias": minimo_diarias}
    return True

def cadastrar_viagem(clientes: dict[dict], destinos: dict[dict], viagens: list[dict]) -> str:
    nome_cliente: str = input("Digite o nome do cliente\n")
    if nome_cliente not in clientes:
        return "Cliente não Cadastrado"

    if not pode_viajar(clientes, nome_cliente):
        return "Cliente com divida muito alta, não pode viajar"

    nome_destino: str = input("Digite o nome do destino\n")
    if nome_destino not in destinos:
        return "Destino não Cadastrado"

    minimo_diarias: int = destinos[nome_destino]["minimoDiarias"]
    valor_diarias: float = destinos[nome_destino]["valorDiaria"]

    diarias: int = int(input("Digite o número mínimo de diárias"))
    if diarias < minimo_diarias:
        return f"Número de diárias menos do que {minimo_diarias}"

    divida_cliente: float = clientes[nome_cliente]["divida"]
    if divida_cliente > 10_000:
        return "Cliente com divida acima de R$10000"

    valor_total: float = valor_diarias*diarias

    viagens.append({
        "nomeCliente": nome_cliente,
        "nomeDestino": nome_destino,
        "numeroDiarias": diarias,
        "valorTotal": valor_total
    })

    clientes[nome_cliente]["divida"] += valor_total

    return "Viagem cadastrada com sucesso"

def listar_viagens_por_destino(viagens: list[dict]) -> None:
    destinos_viagens: dict[str, list[dict[str]]] = {}

    for viagem in viagens:
        destino: str = viagem["nomeDestino"]

        if destino not in destinos_viagens:
            destinos_viagens[destino] = []

        destinos_viagens[destino].append(
            f"""
            Cliente: {viagem["nomeCliente"]}
            Número de diárias: {viagem["numeroDiarias"]}
            Valor total: {viagem["valorTotal"]}
            """
        )

    for destino in destinos_viagens:
        print(f"-----------{destino}-----------")
        print("\n\n".join(destino))

def listar_clientes(clientes: dict[dict]) -> None:
    for cliente, infos in clientes:
        print(f"{cliente}({infos['idade']}): {infos['divida']}")

def listar_pontos(clientes: dict[dict]) -> None:
    for cliente, infos in clientes:
        print(f"{cliente}: {int(infos['pontos']/100)}")

def destino_mais_procurado(viagens: list[dict]) -> str:
    destinos_visitas: dict[str, int] = {}
    max_quantidade = -1
    max_nome = ""

    for viagem in viagens:
        nome_destino: str = viagem["nomeDestino"]

        if nome_destino not in destinos_visitas:
            destinos_visitas[nome_destino] = 0

        destinos_visitas[nome_destino] += 1

    for destino, visitas in destinos_visitas:
        if max_quantidade < visitas:
            max_quantidade = visitas
            max_nome = destino

    return max_nome

def destino_mais_diarias(viagens: list[dict]) -> str:
    destinos = {}
    max_quantidade = 0
    max_nome = ""

    for viagem in viagens:
        nome_destino: str = viagem["nomeDestino"]

        if nome_destino not in destinos:
            destinos[nome_destino] = 0

        destinos[nome_destino] += viagem["numeroDiarias"]

    for destino, diarias in destinos:
        if max_quantidade < diarias:
            max_quantidade = diarias
            max_nome = destino

    return max_nome

def pagar_divida(clientes: dict[dict]) -> None:
    nome: str = input("Digite o nome do cliente\n")
    if nome not in clientes:
        print("Cliente não encontrado")
        return

    dinheiro: float = float(input("Digite a quantia recebida"))
    if dinheiro < 0:
        print("Valor inválido")
        return

    cliente: dict[str] = clientes[nome]
    troco: float = dinheiro - cliente["divida"]

    if troco == 0:
        cliente["divida"] = 0
        cliente["pontos"] += int(dinheiro/10)
    elif troco > 0:
        print(f"Troco: {troco}")
        cliente["divida"] = 0
        cliente["pontos"] += int(dinheiro/10)
    else:
        print(f"Restam R${-troco} em dividas")
        cliente["divida"] -= dinheiro
        cliente["pontos"] += int(dinheiro/10)

def obtem_opcao() -> int:
    print("1- Cadastrar um cliente")
    print("2- Cadastrar um destino")
    print("3- Cadastrar uma viagem")
    print("4- Listar viagens por destino")
    print("5- Listar clientes")
    print("6- Listar a pontuação de cada cliente")
    print("7- Destino mais procurado")
    print("8- Destino com mais diárias")
    print("9- Efetuar um pagamento")
    print("0- sair")
    return int(input("Digite a opção\n"))

if __name__ == '__main__':
    dict_clientes: dict[dict] = {}
    dict_destinos: dict[dict] = {}
    list_viagens: list[dict] = []

    while (opcao := obtem_opcao()) != 0:
        if opcao == 1:
            resultado: bool = cadastrar_cliente(dict_clientes)
            if resultado:
                print("Cliente cadastrado com sucesso")
            else:
                print("Cliente não cadastrado")
        elif opcao == 2:
            resultado: bool = cadastrar_destino(dict_destinos)
            if resultado:
                print("Destino cadastrado com sucesso")
            else:
                print("Destino não cadastrado")
        elif opcao == 3:
            resultado: str = cadastrar_viagem(dict_clientes, dict_destinos, list_viagens)
            print(resultado)
        elif opcao == 4:
            listar_viagens_por_destino(list_viagens)
        elif opcao == 5:
            listar_clientes(dict_clientes)
        elif opcao == 6:
            listar_pontos(dict_clientes)
        elif opcao == 7:
            resultado: str = destino_mais_procurado(list_viagens)
            print(resultado)
        elif opcao == 8:
            resultado: str = destino_mais_diarias(list_viagens)
            print(resultado)
        elif opcao == 9:
            pagar_divida(dict_clientes)