'''
Booleanos (`bool`)

1. Escreva um programa que avalie duas expressões booleanas inseridas pelo usuário e retorne o resultado da operação AND entre elas.
2. Crie um programa que receba dois valores booleanos do usuário e retorne o resultado da operação OR.
3. Desenvolva um programa que peça ao usuário para inserir um valor booleano e, em seguida, inverta esse valor.
4. Faça um programa que compare se dois números fornecidos pelo usuário são iguais.
5. Escreva um programa que verifique se dois números fornecidos pelo usuário são diferentes.
'''

# 1. Escreva um programa que avalie duas expressões booleanas inseridas pelo usuário e retorne o resultado da operação AND entre elas.
print("1. Escreva um programa que avalie duas expressões booleanas inseridas pelo usuário e retorne o resultado da operação AND entre elas.")
expressao1 = input("Digite a primeira expressão booleana (True ou False): ").lower()
expressao2 = input("Digite a segunda expressão booleana (True ou False): ").lower()
resultado_and = expressao1 and expressao2
print("O resultado da operação AND entre as duas expressões é:", resultado_and)

# 2. Crie um programa que receba dois valores booleanos do usuário e retorne o resultado da operação OR.
print("2. Crie um programa que receba dois valores booleanos do usuário e retorne o resultado da operação OR.")
valor1 = input("Digite o primeiro valor booleano (True ou False): ").lower()
valor2 = input("Digite o segundo valor booleano (True ou False): ").lower()
resultado_or = valor1 or valor2
print("O resultado da operação OR entre os dois valores é:", resultado_or)

# 3. Desenvolva um programa que peça ao usuário para inserir um valor booleano e, em seguida, inverta esse valor.
print("3. Desenvolva um programa que peça ao usuário para inserir um valor booleano e, em seguida, inverta esse valor.")
valor = input("Digite um valor booleano (True ou False): ").lower()
valor_booleano = valor == 'true'
valor_invertido = not valor_booleano
print("O valor invertido é:", valor_invertido)

# 4. Faça um programa que compare se dois números fornecidos pelo usuário são iguais.
print("4. Faça um programa que compare se dois números fornecidos pelo usuário são iguais.")
numero1 = float(input("Digite o primeiro número: "))
numero2 = float(input("Digite o segundo número: "))
comparacao = numero1 == numero2
print(f"Os numeros são iguais: {comparacao}")

# 5. Escreva um programa que verifique se dois números fornecidos pelo usuário são diferentes.
print("5. Escreva um programa que verifique se dois números fornecidos pelo usuário são diferentes.")
numero1 = float(input("Digite o primeiro número: "))
numero2 = float(input("Digite o segundo número: "))
comparacao = numero1 != numero2
print(f"Os numeros são diferentes: {comparacao}")
