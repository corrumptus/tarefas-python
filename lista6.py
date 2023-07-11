"""
Ex. 1

Pergunta:
    Faça um programa que gere a matriz abaixo. 
        0, 0, 0, 0, 0, 0, 0, 0 
        1, 1, 1, 1, 1, 1, 1, 1 
        0, 0, 0, 0, 0, 0, 0, 0 
        1, 1, 1, 1, 1, 1, 1, 1
        0, 0, 0, 0, 0, 0, 0, 0 
        1, 1, 1, 1, 1, 1, 1, 1
        0, 0, 0, 0, 0, 0, 0, 0 
        1, 1, 1, 1, 1, 1, 1, 1
Resposta:
    matriz = []
    for i in range(8):
        matriz.append([])
        for j in range(8):
            if i%2 == 0:
                matriz[i].append("0")
            else:
                matriz[i].append("1")
    for i in range(8):
        print(", ".join(matriz[i]))
"""

"""

Ex. 2
Pergunta:
    Faça um programa que gere a matriz abaixo. 
        0, 1, 0, 1, 0, 1, 0, 1 
        0, 1, 0, 1, 0, 1, 0, 1
        0, 1, 0, 1, 0, 1, 0, 1
        0, 1, 0, 1, 0, 1, 0, 1
        0, 1, 0, 1, 0, 1, 0, 1 
        0, 1, 0, 1, 0, 1, 0, 1
        0, 1, 0, 1, 0, 1, 0, 1
        0, 1, 0, 1, 0, 1, 0, 1
Resposta:
    matriz = []
    for i in range(8):
        matriz.append([])
        for j in range(8):
            if j%2 == 0:
                matriz[i].append("0")
            else:
                matriz[i].append("1")
    for i in range(8):
        print(", ".join(matriz[i]))
"""

"""
Ex. 3
Pergunta:
    Faça um programa que gere a matriz abaixo. 
        0, 1, 0, 1, 0, 1, 0, 1 
        1, 0, 1, 0, 1, 0, 1, 0 
        0, 1, 0, 1, 0, 1, 0, 1
        1, 0, 1, 0, 1, 0, 1, 0 
        0, 1, 0, 1, 0, 1, 0, 1
        1, 0, 1, 0, 1, 0, 1, 0 
        0, 1, 0, 1, 0, 1, 0, 1
        1, 0, 1, 0, 1, 0, 1, 0
Resposta:
    matriz = []
    for i in range(8):
        matriz.append([])
        for j in range(8):
            if (i+j)%2 == 0:
                matriz[i].append("0")
            else:
                matriz[i].append("1")
    for i in range(8):
        print(", ".join(matriz[i]))
"""

"""
Ex. 4
Pergunta:
    Faça um programa que gere a matriz abaixo. 
        0, 1, 2, 3, 4, 5, 6, 7 
        7, 6, 5, 4, 3, 2, 1, 0 
        2, 3, 4, 5, 6, 7, 8, 9
        9, 8, 7, 6, 5, 4, 3, 2 
        4, 5, 6, 7, 8, 9, 10, 11
        11, 10, 9, 8, 7, 6, 5 , 4
        6, 7, 8, 9, 10, 11, 12, 13 
        13, 12, 11, 10, 9, 8, 7, 6
Resposta:
    matriz = []
    for i in range(8):
        matriz.append([])
        for j in range(8):
            if i%2 == 0:
                matriz[i].append(str(j+i))
            else:
                matriz[i].append(str(6+i-j))
    for i in range(8):
        print(", ".join(matriz[i]))
"""

"""
Ex. 5

Pergunta:
    Faça um programa que gere a matriz abaixo. 
        2, 0, 0, 0, 0, 0, 0, 0
        1, 2, 0, 0, 0, 0, 8, 0 
        1, 1, 2, 0, 0, 0, 0, 0 
        1, 1, 1, 2, 0, 0, 0, 0 
        1, 1, 1, 1, 2, 0, 0, 0 
        1, 1, 1, 1, 1, 2, 0, 0 
        1, 1, 1, 1, 1, 1, 2, 0 
        1, 1, 1, 1, 1, 1, 1, 2
Resposta:
    matriz = []
    for i in range(8):
        matriz.append([])
        for j in range(8):
            if j == i:
                matriz[i].append("2")
            elif j > i:
                matriz[i].append("0")
            else:
                matriz[i].append("1")
    matriz[1][6] = "8"
    for i in range(8):
        print(", ".join(matriz[i]))
"""

"""
Ex. 6

Pergunta:
    Faça um programa que gere a matriz abaixo. 
        0, 1, 1, 1, 1, 1, 1, 8 
        1, 0, 1, 1, 1, 1, 8, 2
        1, 1, 0, 1, 1, 8, 2, 2
        1, 1, 1, 0, 8, 2, 2, 2
        1, 1, 1, 8, 0, 2, 2, 2 
        1, 1, 8, 2, 2, 0, 2, 2
        1, 8, 2, 2, 2, 2, 0, 2
        8, 2, 2, 2, 2, 2, 2, 0 
    Depois de gerada a matriz, faça a sua transposta.
Resposta:
    matriz = []
    for i in range(8):
        matriz.append([])
        for j in range(8):
            if j == i:
                matriz[i].append("0")
            elif j < 7-i:
                matriz[i].append("1")
            elif j == 7-i:
                matriz[i].append("8")
            else:
                matriz[i].append("2")
    for i in range(8):
        print(", ".join(matriz[i]))
    for i in range(8):
        for j in range(8):
            matriz[i][j], matriz[j][i] = matriz[j][i], matriz[i][j]
    for i in range(8):
        print(", ".join(matriz[i]))
"""

"""
Ex. 7

Pergunta:
    Faça um programa para cadastrar as notas de Português, Matemática, Física, Geografia e 
    História dos alunos de um colégio. As notas devem estar todas registradas em uma matriz. 
    Depois de criada a matriz, calcule:
        - a média de cada um dos alunos
        - a média de cada uma das disciplinas
        - a maior nota em cada disciplina
        - aumente em 10% a nota de cada um dos alunos de Matemática.
          Importante: a nota máxima final não pode ser superior a 10.
Resposta:
    alunos = []

    while True:
        portugues = float(input("Digite a nota de Português\n"))
        matematica = float(input("Digite a nota de Matemática\n"))
        fisica = float(input("Digite a nota de Física\n"))
        geografia = float(input("Digite a nota de Geografia\n"))
        historia = float(input("Digite a nota de História dos alunos\n"))

        alunos.append([portugues, matematica, fisica, geografia, historia])

        if input("Digite \"S\" para cadastrar um novo aluno\n") != "S":
            break

    media_disciplina = [0, 0, 0, 0, 0]
    maior_nota = [0, 0, 0, 0, 0]

    for i, aluno in enumerate(alunos):
        MEDIA = 0
        for j in range(5):
            MEDIA += aluno[j]
            media_disciplina[j] += aluno[j]
            if maior_nota[j] < aluno[j]:
                maior_nota[j] = aluno[j]
        print(MEDIA/5)

        if aluno[1]*1.1 > 10:
            aluno[1] = 10
        else:
            aluno[1] = aluno[1]*1.1
    for i in range(5):
        print(media_disciplina[i]/len(alunos))

    for i in range(5):
        print(maior_nota[i])

    print("Novas notas em matemática:")
    for aluno in alunos:
        print(aluno[1])
"""