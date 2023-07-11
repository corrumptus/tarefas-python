"""
Texto suporte:
    Você foi contratado para construir um sistema de uma auto escola.
    No seu sistema deve ser possível:

    1. Cadastrar um aluno contendo: nome, idade e sexo.
    Não deve ser possível cadastrar um aluno com mesmo nome.

    2. Listar os alunos por faixa de idade:
    Listar todos os animais que tem idade entre 18 e 25 anos(JOVEM),
    depois listar os que possuem entre 25 e 65 anos (ADULTO) e
    por fim os que possuem mais de 65 anos (IDOSOS).

    3. Cadastrar um veículo com: nome e quantidade de aulas.

    4. Listar os veículos.

    5. Registrar uma aula: em cada aula salva dever ser possível salvar o nome do aluno e
    qual o carro será utilizado na aula.
    Além disso armazene a data em que será realizada a aula.
    Considerando que cada aula custe R$ 30,00,
    a cada aula inserida deve ser amazenado o valor que o aluno está devendo para a escola.

    6. Listar todas as aulas cadastradas.

    7. Informar o valor que foi arrecadado com aulas para pessoas com mais de 65 anos.

    8. Informar qual a aula que ocorreu para pessoa mais jovem.
    Importante: Não basta procurar na lista de alunos,
    pois pode ser que ele esteja cadastrado mas que nunca tenha tido aula.

    9. Aluno efetuar pagamento das aulas: O sistema deve perguntar o nome do aluno e,
    caso ele esteja cadastrado, informar o valor pendente pelas aulas.
    Se o aluno efetuar o pagamento, abater o valor pago do valor pendente.
"""

alunos: dict[str] = {}
carros: dict[str, int] = {}
aulas: list[dict[str]] = []

while True:
    print("1 - Cadastrar um aluno")
    print("2 - Listar alunos por faixa etaria")
    print("3 - Cadastrar um veiculo")
    print("4 - Listar todos os veiculos")
    print("5 - Cadastrar uma aula")
    print("6 - Listar todas as aulas cadastradas")
    print("7 - Valor arrecadado com aulas para pessoas com mais de 65 anos")
    print("8 - Aula da pessoa mais jovem")
    print("9 - Efetuar um pagamento")
    print("0 - sair")
    opcao: int = int(input("Digite a opção desejada\n"))

    if opcao == 0:
        break

    if opcao == 1:
        nome: str = input("Digite o nome do aluno\n")
        if nome in alunos:
            print("Aluno já cadastrado")
            continue

        idade: int = int(input("Digite a idade do aluno\n"))
        if idade >= 18:
            print("Idade inválida")
            continue

        sexo: str = input("Digite o sexo do aluno (H/M)\n")
        if sexo not in ["H", "M", "h", "m"]:
            print("Sexo inválido")
            continue

        alunos[nome] = {"idade": idade, "sexo": sexo.upper(), "divida": 0}

    elif opcao == 2:
        print("Jovens")
        for aluno, infos in alunos:
            if infos["idade"] > 18 and infos["idade"] < 25:
                print(f"{aluno}({infos['sexo']}): {infos['idade']}")

        print("\nAdulto")
        for aluno, infos in alunos:
            if infos["idade"] >= 25 and infos["idade"] < 65:
                print(f"{aluno}({infos['sexo']}): {infos['idade']}")

        print("\nIdoso")
        for aluno, infos in alunos:
            if infos["idade"] >= 65:
                print(f"{aluno}({infos['sexo']}): {infos['idade']}")

    elif opcao == 3:
        nome: str = input("Digite o nome do veiculo\n")
        if nome not in carros:
            print("Veiculo já cadastrado")

        aulas: int = int(input("Digite a quantidade de aulas do veiculo\n"))
        carros[nome] = aulas

    elif opcao == 4:
        for carro, aulas in carros.items():
            print(f"{carro}: {aulas}")

    elif opcao == 5:
        nome_aluno: str = input("Digite o nome do aluno\n")
        if nome_aluno not in alunos:
            print("Aluno não cadastrado")
            continue

        nome_carro: str = input("Digite o nome do carro\n")
        if nome_carro not in carros:
            print("Carro não cadastrado")
            continue

        data_aula: str = input("Digite a data da aula\n")
        if len(data_aula) not in [8, 10]:
            print("Data inválida")
            continue

        AULA_JA_EXISTE = False
        for aula in aulas:
            is_aluno_equals: bool = aula["nomeAluno"] == nome_aluno
            is_carro_equals: bool = aula["nomeCarro"] == nome_carro
            is_data_equals: bool = aula["dataAula"] == data_aula

            if is_aluno_equals and is_carro_equals and is_data_equals:
                AULA_JA_EXISTE = True
                break

        if AULA_JA_EXISTE:
            print("Aula já cadastrada")
            continue

        aulas.append({"nomeAluno": nome_aluno, "nomeCarro": nome_carro, "dataAula": data_aula})
        alunos[nome_aluno]["divida"] += 30
        carros[nome_carro] += 1

    elif opcao == 6:
        for aula in aulas:
            print(f"{aula['nomeAluno']} - {aula['nomeCarro']} - {aula['dataAula']}")

    elif opcao == 7:
        TOTAL_OBTIDO_COM_MAIS_VELHOS = 0

        for aula in aulas:
            nome_aluno: str = aula["nomeAluno"]
            idade_aluno: int = alunos[nome_aluno]["idade"]

            if idade_aluno >= 65:
                TOTAL_OBTIDO_COM_MAIS_VELHOS += 30

        print(TOTAL_OBTIDO_COM_MAIS_VELHOS)

    elif opcao == 8:
        IDADE_ALUNO_MAIS_JOVEM = 200
        AULA_DO_ALUNO_MAIS_JOVEM = {}

        for aula in aulas:
            nome_aluno: str = aula["nomeAluno"]
            idade_aluno: int = alunos[nome_aluno]["idade"]

            is_idade_minima: bool = idade_aluno == 17
            is_aluno_mais_jovem: bool = idade_aluno < IDADE_ALUNO_MAIS_JOVEM

            if is_idade_minima or is_idade_minima:
                IDADE_ALUNO_MAIS_JOVEM = idade_aluno
                AULA_DO_ALUNO_MAIS_JOVEM = {
                    "nomeAluno": nome_aluno,
                    "nomeCarro": aula["nomeCarro"],
                    "dataAula": aula["dataAula"]
                }

            if is_idade_minima:
                break

        print(f"""
               --------Aula--------
               Aluno: {AULA_DO_ALUNO_MAIS_JOVEM["nomeAluno"]}
               Idade: {idade_aluno}
               Carro: {AULA_DO_ALUNO_MAIS_JOVEM["nomeCarro"]}
               data: {AULA_DO_ALUNO_MAIS_JOVEM["dataAula"]}
               """)

    elif opcao == 9:
        nome = input("Digite o nome do aluno\n")
        if nome not in alunos:
            print("Aluno não cadastrado")
            continue

        print(f"divida: R${alunos[nome]['divida']}")

        valorRecebido = int(input("Digite o valor recebido\n"))
        if valorRecebido < 0:
            print("Valor inválido")
            continue

        divida: int = alunos[nome]["divida"]

        if valorRecebido == divida:
            alunos[nome]["divida"] = 0
            print("divida quitada")

        elif valorRecebido < divida:
            alunos[nome]["divida"] -= valorRecebido
            print(f"sobram R${alunos[nome]['divida']} de divida")

        else:
            alunos[nome]["divida"] = 0
            print(f"troco: {valorRecebido - alunos[nome]['divida']}")
