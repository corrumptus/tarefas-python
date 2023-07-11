"""
Texto Suporte:
    Faça um programa em python que receba três strings
    - verifique se a primeira string é um CPF no formato xxx.xxx.xxx-xx.
    
    - verifique se a segunda string é uma data válida no formato DD/MM/AAAA. 
    O Ano deve estar entre 1900 e 2020.

    - verifique se a terceira string é um palíndromo. Um palíndromo é uma
    sequência de caracteres na qual a leitura é idêntica se feita da direita
    para esquerda ou da esquerda para a direita. Exemplo: OVO. Considerar
    também frases complexas nas quais os espaços e pontuação devem ser
    ignorados. Ex: SUBI NO ONIBUS.
"""

str1: str = input("Digite um CPF\n")
str2: str = input("Digite uma data entre 01/01/1900 e 01/01/2020")
str3: str = input("Digite um palíndromo (Ex.: OVO, SUBI NO ONIBUS)\n")
IS_CPF: bool = True
IS_DATE_BET_1900_2020: bool = True
IS_PALINDROME: bool = True

if len(str1) == 14:
    for i, char in enumerate(str1):
        if i in [3, 7] and char != ".":
            IS_CPF = False
            break
        if i == 11 and char != "-":
            IS_CPF = False
            break
        if i not in [3, 7, 11] and char not in "0123456789":
            IS_CPF = False
            break
else:
    IS_CPF = False

if len(str2) == 10:
    for i, char in enumerate(str2):
        if i in [2, 5] and char != "/":
            IS_DATE_BET_1900_2020 = False
            break
        if i not in [2, 5] and char not in "0123456789":
            IS_DATE_BET_1900_2020 = False
            break
else:
    IS_DATE_BET_1900_2020 = False
if IS_DATE_BET_1900_2020:
    if int(str2[0:2]) > 31 or int(str2[0:2]) < 0:
        IS_DATE_BET_1900_2020 = False
    if int(str2[3:5]) > 12 or int(str2[3:5]) < 0:
        IS_DATE_BET_1900_2020 = False
    if int(str2[6:]) > 2020 or int(str2[6:]) < 1900:
        IS_DATE_BET_1900_2020 = False
    if int(str2[3:5]) == 2 and int(str2[6:])%4 == 0 and int(str2[0:2]) > 29:
        IS_DATE_BET_1900_2020 = False
    if int(str2[3:5]) == 2 and int(str2[6:])%4 != 0 and int(str2[0:2]) > 28:
        IS_DATE_BET_1900_2020 = False
    if int(str2[3:5]) in [1, 3, 5, 7, 8, 10, 12] and int(str2[0:2]) > 31:
        IS_DATE_BET_1900_2020 = False
    if int(str2[3:5]) in [4, 6, 9, 11] and int(str2[0:2]) > 30:
        IS_DATE_BET_1900_2020 = False

str3 = str3.replace(" ", "")
for i, char in enumerate(str3):
    if str3[len(str3) - 1 - i] != char:
        IS_PALINDROME = False
        break

print(f"string 1 {'é' if IS_CPF else 'não é'} um cpf")
print(f"string 2 {'é' if IS_DATE_BET_1900_2020 else 'não é'} uma data válida")
print(f"string 3 {'é' if IS_PALINDROME else 'não é'} um palindromo")
