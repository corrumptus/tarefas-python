"""
Texto suporte:
    Faça um sistema para:
    - receber como entrada um arquivo como o enviado em anexo (poltronas.dat) e exibir em tela 
    a disponibilidade de poltronas.
    - permitir ao usuário comprar poltronas (no máximo 4) fornecendo linha (número) e coluna 
    (letra). O sistema deve verificar se a poltrona solicita está liberada ou não (dica: faça
    uma função para essa verificação). Após realizada a venda, aplicar o protocolo da COVID-19, 
    bloqueando as poltronas conforme necessidade. Cada vez que uma venda for realizada deve 
    ser atualizado o arquivo poltronas.dat
    - Gerar um relatório texto informando quantas poltronas estão vendidas, livres e bloqueadas. 
    Exibir também o mapa das poltronas.
"""

import os.path

def verifica_arq(path: str) -> None:
    if os.path.isfile(path):
        return

    with open(path, "w", encoding="utf-8") as arquivo:
        lines: list[str] = ["00000000000000"]*10

        arquivo.write("\n".join(lines))

def verificaStringPedido(inputString: str) -> bool:
    lista_de_poltronas = inputString.split(" ")

    if len(lista_de_poltronas) > 4:
        return False

    for poltrona in lista_de_poltronas:
        if len(poltrona) > 2:
            return False
        if poltrona[0] not in "ABCDEFGHIJKLMN":
            return False
        if poltrona[1] not in "0123456789":
            return False

    return True

def printPoltronas(path: str) -> None:
    print("A B C D E F G H I J K L M N")

    with open(path, "r", encoding="utf-8") as arquivo:
        linhas = arquivo.readlines()

    for i, linha in enumerate(linhas):
        linha = linha.replace("\n", "")

        print(f"{' '.join(linha)} {i}")

    print("\n")

def poltronasRequeridas() -> list[str]:
    compradas: str = input("Digite o ID das poltronas separadas por espaço. Ex: \"A1 A2\"\n")

    if verificaStringPedido(compradas):
        return compradas.split(" ")

    return []

def poltronas_livres(path:str, lista_poltronas: list[str]) -> bool:
    with open(path, "r", encoding="utf-8") as arquivo:
        linhas: list[str] = arquivo.readlines()

    for poltrona in lista_poltronas:
        linha: int = int(poltrona[1])
        coluna: int = ord(poltrona[2]) - 65

        if linhas[linha][coluna] != "0":
            return False

    return True

def comprarPoltronas(path: str, lista_poltronas: list[str]) -> None:
    with open(path, "r", encoding="utf-8") as arquivo:
        linhas: list[str] = arquivo.readlines()

    for poltrona in lista_poltronas:
        linha: int = int(poltrona[1])
        coluna: int = ord(poltrona[2]) - 65

        linhas[linha] = linhas[linha][:coluna] + "X" + linhas[linha][coluna+1:]

    with open(path, "w", encoding="utf-8") as arquivo:
        arquivo.write("".join(linhas))

def bloquearPoltronaslaterais(path: str) -> None:
    with open(path, "r", encoding="utf-8") as arquivo:
        linhas: list[str] = arquivo.readlines()

    for i in range(10):
        linha: str = linhas[i]

        for j in range(14):
            if linha[j] != "X":
                continue

            if j > 0 and linha[j-1] == "0":
                linhas[i] = linha[:j-1] + "B" + linha[j:]

            if j < len(linha)-2 and linha[j+1] == "0":
                linhas[i] = linha[:j+1] + "B" + linha[j+2:]

    with open(path, "w", encoding="utf-8") as arquivo:
        arquivo.write("".join(linhas))

def gerarRelatorio(path: str) -> None:
    livres: int = 0
    vendidas: int = 0
    bloqueadas: int = 0

    with open(path, "r", encoding="utf-8") as arquivo:
        linhas: list[str] = arquivo.readlines()

    printPoltronas(path)

    for linha in linhas:
        for char in linha:
            if char == "0":
                livres += 1

            elif char == "X":
                vendidas += 1

            elif char == "B":
                bloqueadas += 1

    print(f"Livres: {livres}\nVendidas: {vendidas}\nBloqueadas: {bloqueadas}\n")

if __name__ == "__main__":
    POLTRONAS_PATH: str = "poltronas.dat"

    verifica_arq(POLTRONAS_PATH)

    while True:
        printPoltronas(POLTRONAS_PATH)
        print("1- Comprar poltronas (max: 4)")
        print("2- Gerar um relatório")
        print("0- Sair")
        opcao: int = int(input("Digite a opção\n"))

        if opcao == 1:
            poltronas: list[str] = poltronasRequeridas()

            if poltronas_livres(POLTRONAS_PATH, poltronas):
                comprarPoltronas(POLTRONAS_PATH, poltronas)
                bloquearPoltronaslaterais(POLTRONAS_PATH)
                print("Compra realizada com sucesso\n")
            else:
                print("Uma das poltronas já foram compradas, tente novamente\n")

        elif opcao == 2:
            gerarRelatorio(POLTRONAS_PATH)

        else:
            print("Opção inválida\n")
