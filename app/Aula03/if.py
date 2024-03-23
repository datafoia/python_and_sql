'''
1. Você está analisando um conjunto de dados de vendas e precisa garantir que todos os registros tenham valores positivos para quantidade e preço. 
Escreva um programa que verifique esses campos e imprima "Dados válidos" se ambos forem positivos ou "Dados inválidos" caso contrário.

2. Imagine que você está trabalhando com dados de sensores IoT. 
Os dados incluem medições de temperatura. Você precisa classificar cada leitura como 'Baixa', 'Normal' ou 'Alta'. 
Considerando que:
Temperatura < 18°C é 'Baixa'
Temperatura >= 18°C e <= 26°C é 'Normal'
Temperatura > 26°C é 'Alta'

3. Você está analisando logs de uma aplicação e precisa filtrar mensagens com severidade 'ERROR'. 
Dado um registro de log em formato de dicionário como log = {'timestamp': '2021-06-23 10:00:00', 'level': 'ERROR', 'message': 'Falha na conexão'}, 
escreva um programa que imprima a mensagem se a severidade for 'ERROR'.

4. Escreva um programa que solicite ao usuário para digitar um número. 
Utilize `try-except` para assegurar que a entrada seja numérica e utilize `if-elif-else` para classificar o número como "positivo", "negativo" ou "zero". 
Adicionalmente, identifique se o número é "par" ou "ímpar".

5. Crie um script que solicite ao usuário uma lista de números separados por vírgula. 
O programa deve converter a string de entrada em uma lista de números inteiros. 
Utilize try-except para tratar a conversão de cada número e validar que cada elemento da lista convertida é um inteiro. 
Se a conversão falhar ou um elemento não for um inteiro, imprima uma mensagem de erro. 
Se a conversão for bem-sucedida para todos os elementos, imprima a lista de inteiros.
'''

# Exercício 1: Verificação de Qualidade de Dados
quantidade = 10
preco = 5

if quantidade > 0 and preco > 0:
    print('Dados válidos')
else:
    print('Dados inválidos')

# Exercício 2: Classificação de Dados de Sensor
temperatura = 22
if temperatura < 18:
    print('Baixa')
elif temperatura >= 18 and temperatura <= 26:
    print('Normal')
else:
    print('Alta')

# Exercício 3: Filtragem de Logs por Severidade
log = {'timestamp': '2021-06-23 10:00:00', 'level': 'ERROR', 'message': 'Falha na conexão'}
if log['level'] == 'ERROR':
    print(log['message'])

# Exercício 4: Validação de Dados de Entrada
idade = 25
email = 'datafoia@gmail.com'

if not 18 <= idade <= 65:
    print('Idade fora do intervalo permitido')
elif '@' not in email or '.' not in email:
    print('Email inválido')
else:
    print('Dados de usuários válidos')

# Exercício 5: Detecção de Anomalias em Dados de Transações
transacoes = [
    {'valor': 12000, 'hora': 20},
    {'valor': 5000, 'hora': 16}
]
for transacao in transacoes:
    if transacao['valor'] > 10000 or transacao['hora'] < 9 or transacao['hora'] > 18:
        print('Transação suspeita')
    else:
        print('Transação normal')
