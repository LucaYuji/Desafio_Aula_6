# Desafio
# Crie um sistema de calculadora
# Concatenar as saídas
# soma, divisao, multiplicação, subtração
# utilizar input()  print() +, -, /, **, *, //

print('Calculadora')
primeiro = float(input('Digite um número: '))
segundo = float(input('Digite outro número: '))
soma = primeiro + segundo
subtração = primeiro - segundo
divisao = primeiro / segundo
divisao_inteira = primeiro // segundo
exponencial = primeiro ** segundo
multiplicaçao = primeiro * segundo
print('''Soma = {}; 
Subtração = {}; 
Divisão = {}; 
Divisão inteira = {}; 
Exponencial = {}; 
Multiplicação = {};'''. format(soma, subtração, divisao, divisao_inteira, exponencial, multiplicaçao))