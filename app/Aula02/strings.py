'''
Textos (Strings)

1. Escreva um programa que receba uma string do usuário e a converta para maiúsculas.
2. Crie um programa que receba o nome completo do usuário e imprima o nome com todas as letras minúsculas.
3. Desenvolva um programa que peça ao usuário para inserir uma frase e, em seguida, imprima esta frase sem espaços em branco no início e no final.
4. Faça um programa que peça ao usuário para digitar uma data no formato "dd/mm/aaaa" e, em seguida, imprima o dia, o mês e o ano separadamente.
5. Escreva um programa que concatene duas strings fornecidas pelo usuário.
'''

# 1. Escreva um programa que receba uma string do usuário e a converta para maiúsculas.
print("1. Escreva um programa que receba uma string do usuário e a converta para maiúsculas.")
texto = str(input("Digite uma palavra: "))
maiuscula = texto.upper()
print(maiuscula)

# 2. Crie um programa que receba o nome completo do usuário e imprima o nome com todas as letras minúsculas.
print("2. Crie um programa que receba o nome completo do usuário e imprima o nome com todas as letras minúsculas.")
nome_completo = input("Digite seu nome completo: ")
nome_minusculo = nome_completo.lower()
print("Seu nome em letras minúsculas é:", nome_minusculo)

# 3. Desenvolva um programa que peça ao usuário para inserir uma frase e, em seguida, imprima esta frase sem espaços em branco no início e no final.
print("3. Desenvolva um programa que peça ao usuário para inserir uma frase e, em seguida, imprima esta frase sem espaços em branco no início e no final.")
frase = input("Digite uma frase: ")
frase_sem_espacos = frase.strip()
print("Frase sem espaços em branco no início e no final:", frase_sem_espacos)


# 4. Faça um programa que peça ao usuário para digitar uma data no formato "dd/mm/aaaa" e, em seguida, imprima o dia, o mês e o ano separadamente.
print("4. Faça um programa que peça ao usuário para digitar uma data no formato 'dd/mm/aaaa' e, em seguida, imprima o dia, o mês e o ano separadamente.")
data = input("Digite uma data no formato 'dd/mm/aaaa': ")
dia, mes, ano = data.split('/')
print("Dia:", dia)
print("Mês:", mes)
print("Ano:", ano)

# 5. Escreva um programa que concatene duas strings fornecidas pelo usuário.
print("5. Escreva um programa que concatene duas strings fornecidas pelo usuário.")
string1 = input("Digite a primeira string: ")
string2 = input("Digite a segunda string: ")
concatenada = string1 + string2
print("As strings concatenadas são:", concatenada)
