#Crie programa que o usuário digita o seu nome e retorna o número de caracteres

'''
nome = input("Digite seu nome: ")
qtd_caracteres_nome = len(nome)
print(nome)
print("Número de caracteres:" + str(qtd_caracteres_nome))
'''

#Desafio

"""
1) Solicitar ao usuário que digite seu nome
2) Solicitar ao usuário que digite o valor de seu salário (Converter a entrada para float)
3) Solicite ao usuário que digite o percentual do bônus recebido (Converter a entrada para float)
4) Calcule o valor do bônus
5) Calcule o salário do usuário + bônus
6) Imprima uma mensagem personalizada incluindo o nome do usuário, salário e bônus
"""

nome = input("Digite seu nome: ")
salario = input("Digite seu salário: ")
bonus = input("Digite o percentual do bonus recebido: ")

salario_float = float(salario)
bonus_float = float(bonus) / 100


bonus_calculado = round(salario_float * bonus_float,2)
salario_final = salario_float + bonus_calculado

print("Olá " + nome + ", seu salário é de R$" + str(salario_float) + " e você recebeu um bônus de R$" + str(bonus_calculado) + ", totalizando R$" + str(salario_final))
