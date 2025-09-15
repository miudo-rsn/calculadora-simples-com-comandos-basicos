# Solicita o primeiro número ao usuário e o converte para um número decimal (float)
primeiro_numero = float(input('Digite o primeiro número:'))

# Solicita o sinal da operação desejada ao usuário
sinal_operacao = input('Digite o sinal da operação:')

# Solicita o segundo número ao usuário e o converte para um número decimal (float)
segundo_numero = float(input('Digite o segundo número:'))

# Verifica qual operação foi escolhida e realiza o cálculo correspondente

# Se o sinal for de adição
if sinal_operacao == "+":
   print(f'Resultado da Operação = {primeiro_numero + segundo_numero}')

# Se o sinal for de subtração
elif sinal_operacao == "-":
  print(f'Resultado da Operação = {primeiro_numero - segundo_numero}')

# Se o sinal for de multiplicação (usando 'x' ou '*')
elif sinal_operacao == "x" or sinal_operacao == "*":
   print(f'Resultado da Operação = {primeiro_numero * segundo_numero}')

# Se o sinal for de divisão (usando ':' ou '/') e o segundo número não for zero
elif sinal_operacao == ":" or sinal_operacao == "/" and segundo_numero != 0:
   print(f'Resultado da Operação = {primeiro_numero / segundo_numero}')

# Se o sinal for de divisão (usando ':' ou '/') e o segundo número for zero
elif sinal_operacao == ":" or sinal_operacao == "/" and segundo_numero == 0:
   print("Divisão Indefinida")

# Se o sinal for de porcentagem e o segundo número não for zero
elif sinal_operacao == "%" and segundo_numero != 0:
   print(f'Resultado da operação = {((primeiro_numero * segundo_numero) / 100)}')

# Se o sinal for de porcentagem e o segundo número for zero
elif sinal_operacao == "%" and segundo_numero == 0:
   print("Operação Indefinida")
