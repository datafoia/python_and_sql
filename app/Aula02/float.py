'''
Números de Ponto Flutuante (`float`)

1. Escreva um programa que receba dois números flutuantes e realize sua adição.
2. Crie um programa que calcule a média de dois números flutuantes fornecidos pelo usuário.
3. Desenvolva um programa que calcule a potência de um número (base e expoente fornecidos pelo usuário).
4. Faça um programa que converta a temperatura de Celsius para Fahrenheit.
5. Escreva um programa que calcule a área de um círculo, recebendo o raio como entrada.
'''

# 1. Escreva um programa que receba dois números flutuantes e realize sua adição.
print("1. Escreva um programa que receba dois numeros flutuantes e realize sua adicao.")
num1 = float(input("Digite o primeiro número flutuante: "))
num2 = float(input("Digite o segundo número flutuante: "))
soma = num1 + num2
print("A soma dos dois números é:", soma)

# 2. Crie um programa que calcule a média de dois números flutuantes fornecidos pelo usuário.
print("2. Crie um programa que calcule a média de dois números flutuantes fornecidos pelo usuário.")
num1 = float(input("Digite o primeiro número flutuante: "))
num2 = float(input("Digite o segundo número flutuante: "))
media = (num1 + num2) / 2
print("A média dos dois números é:", media)

# 3. Desenvolva um programa que calcule a potência de um número (base e expoente fornecidos pelo usuário).
print("3. Desenvolva um programa que calcule a potência de um número (base e expoente fornecidos pelo usuário).")
base = float(input("Digite a base: "))
expoente = float(input("Digite o expoente: "))
potencia = base ** expoente
print("A potência é: ", potencia)

# 4. Faça um programa que converta a temperatura de Celsius para Fahrenheit.
print("4. Faça um programa que converta a temperatura de Celsius para Fahrenheit.")
celsius = float(input("Digite a temperatura em C°: ")) 
fahrenheit = (celsius*1.8) + 32
print(f"A temperatura em de {celsius} °C é igual a {fahrenheit} °F")

# 5. Escreva um programa que calcule a área de um círculo, recebendo o raio como entrada.
print("5. Escreva um programa que calcule a área de um círculo, recebendo o raio como entrada.")
raio = float(input("Digite o raio do círculo: "))
pi = 3.14159
area = 2*pi*(raio**2)
print(f"A área do círculo é: {area}")
