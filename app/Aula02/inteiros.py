#Exercícios

'''
Inteiros (`int`)

1. Escreva um programa que soma dois números inteiros inseridos pelo usuário.
2. Crie um programa que receba um número do usuário e calcule o resto da divisão desse número por 5.
3. Desenvolva um programa que multiplique dois números fornecidos pelo usuário e mostre o resultado.
4. Faça um programa que peça dois números inteiros e imprima a divisão inteira do primeiro pelo segundo.
5. Escreva um programa que calcule o quadrado de um número fornecido pelo usuário.
'''

# 1. Escreva um programa que soma dois números inteiros inseridos pelo usuário.
print("1. Escreva um programa que soma dois números inteiros inseridos pelo usuário.")
num1 = int(input("Digite o primeiro número inteiro: "))
num2 = int(input("Digite o segundo número inteiro: "))
soma = num1 + num2
print("A soma dos dois números é:", soma)

# 2. Crie um programa que receba um número do usuário e calcule o resto da divisão desse número por 5.
print("2. Crie um programa que receba um número do usuário e calcule o resto da divisão desse número por 5.")
num = int(input("Digite um número: "))
resto = num % 5
print("O resto da divisão desse número por 5 é:", resto)

# 3. Desenvolva um programa que multiplique dois números fornecidos pelo usuário e mostre o resultado.
print("3. Desenvolva um programa que multiplique dois números fornecidos pelo usuário e mostre o resultado.")
num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))
resultado = num1 * num2
print("O resultado da multiplicação é:", resultado)

# 4. Faça um programa que peça dois números inteiros e imprima a divisão inteira do primeiro pelo segundo.
print("4. Faça um programa que peça dois números inteiros e imprima a divisão inteira do primeiro pelo segundo.")
num1 = int(input("Digite o primeiro número inteiro: "))
num2 = int(input("Digite o segundo número inteiro: "))
divisao_inteira = num1 // num2
print("A divisão inteira do primeiro número pelo segundo é:", divisao_inteira)

# 5. Escreva um programa que calcule o quadrado de um número fornecido pelo usuário.
print("5. Escreva um programa que calcule o quadrado de um número fornecido pelo usuário.")
num = int(input("Digite um número para calcular o quadrado: "))
quadrado = num ** 2
print("O quadrado do número fornecido é:", quadrado)


