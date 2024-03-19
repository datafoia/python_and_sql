'''
1. Escreva um programa que converta a temperatura de Celsius para Fahrenheit. 
O programa deve solicitar ao usuário a temperatura em Celsius e, utilizando try-except, garantir que a entrada seja numérica, tratando qualquer ValueError. 
Imprima o resultado em Fahrenheit ou uma mensagem de erro se a entrada não for válida.

2. Crie um programa que verifica se uma palavra ou frase é um palíndromo (lê-se igualmente de trás para frente, desconsiderando espaços e pontuações). 
Utilize try-except para garantir que a entrada seja uma string. 
Dica: Utilize a função isinstance() para verificar o tipo da entrada.

3. Desenvolva uma calculadora simples que aceite duas entradas numéricas e um operador (+, -, *, /) do usuário. 
Use try-except para lidar com divisões por zero e entradas não numéricas. 
Utilize if-elif-else para realizar a operação matemática baseada no operador fornecido. 
Imprima o resultado ou uma mensagem de erro apropriada.

4. Escreva um programa que solicite ao usuário para digitar um número. 
Utilize `try-except` para assegurar que a entrada seja numérica e utilize `if-elif-else` para classificar o número como "positivo", "negativo" ou "zero". 
Adicionalmente, identifique se o número é "par" ou "ímpar".

5. Crie um script que solicite ao usuário uma lista de números separados por vírgula. 
O programa deve converter a string de entrada em uma lista de números inteiros. 
Utilize try-except para tratar a conversão de cada número e validar que cada elemento da lista convertida é um inteiro. 
Se a conversão falhar ou um elemento não for um inteiro, imprima uma mensagem de erro. 
Se a conversão for bem-sucedida para todos os elementos, imprima a lista de inteiros.
'''

#1. Escreva um programa que converta a temperatura de Celsius para Fahrenheit. 
#O programa deve solicitar ao usuário a temperatura em Celsius e, utilizando try-except, garantir que a entrada seja numérica, tratando qualquer ValueError. 
#Imprima o resultado em Fahrenheit ou uma mensagem de erro se a entrada não for válida.
try:
    celsius = float(input('Digite o valor da temperatura em Celsius: '))
    fahreint = float(celsius * 1.8) + 32
    print(f'{celsius}°C é igual a {fahreint}F°.')
except ValueError:
    print("Por favor, digite um número válido para temperatura.")

#2. Crie um programa que verifica se uma palavra ou frase é um palíndromo (lê-se igualmente de trás para frente, desconsiderando espaços e pontuações). 
#Utilize try-except para garantir que a entrada seja uma string. 
#Dica: Utilize a função isinstance() para verificar o tipo da entrada.
entrada = input('Digite uma palavra: ')
if isinstance(entrada, str):
    formatado = entrada.replace(" ","").lower()
    if formatado == formatado[::-1]:
        print(f'{entrada} é um palíndromo')
    else:
        print(f'{entrada} não é um palíndromo')
else:
    print("Entrada inválida. Por favor, digite uma palavra ou frase.")

# 3. Desenvolva uma calculadora simples que aceite duas entradas numéricas e um operador (+, -, *, /) do usuário. 
# Use try-except para lidar com divisões por zero e entradas não numéricas. 
# Utilize if-elif-else para realizar a operação matemática baseada no operador fornecido. 
# Imprima o resultado ou uma mensagem de erro apropriada.

try:
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))
    operador = input("Digite o operador (+, -, *, /): ")
    if operador == '+':
        resultado = num1 + num2
    elif operador == '-':
        resultado = num1 - num2
    elif operador == '*':
        resultado = num1 * num2
    elif operador == '/' and num2 != 0:
        resultado = num1 / num2
    else:
        print("Operador inválido ou divisão por zero.")
    print("Resultado:", resultado)
except ValueError:
    print("Erro: Entrada inválida. Certifique-se de inserir números.")

# 4. Escreva um programa que solicite ao usuário para digitar um número. 
# Utilize `try-except` para assegurar que a entrada seja numérica e utilize `if-elif-else` para classificar o número como "positivo", "negativo" ou "zero". 
# Adicionalmente, identifique se o número é "par" ou "ímpar".
try:
    numero = int(input("Digite um número: "))
    if numero > 0:
        print("Positivo")
    elif numero < 0:
        print("Negativo")
    else:
        print("Zero")
    if numero % 2 == 0:
        print("Par")
    else:
        print("Ímpar")
except ValueError:
    print("Por favor, digite um número inteiro válido.")

#5. Crie um script que solicite ao usuário uma lista de números separados por vírgula. 
#O programa deve converter a string de entrada em uma lista de números inteiros. 
#Utilize try-except para tratar a conversão de cada número e validar que cada elemento da lista convertida é um inteiro. 
#Se a conversão falhar ou um elemento não for um inteiro, imprima uma mensagem de erro. 
#Se a conversão for bem-sucedida para todos os elementos, imprima a lista de inteiros.
    
entrada_lista = input("Digite uma lista de números separados por vírgula: ")
numeros_str = entrada_lista.split(",")
numeros_int = []
try:
    for num in numeros_str:
        numeros_int.append(int(num.strip()))
    print("Lista de inteiros:", numeros_int)
except ValueError:
    print("Erro: certifique-se de que todos os elementos são números inteiros válidos.")