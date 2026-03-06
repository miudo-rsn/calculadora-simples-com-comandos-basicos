print("Operações disponíveis: +  -  *  x  /  :  %")
print("")

primeiro_numero = float(input("Digite o primeiro número: ").replace(",", "."))
sinal_operacao = input("Digite o sinal da operação: ")
segundo_numero = float(input("Digite o segundo número: ").replace(",", "."))

if sinal_operacao == "+":
    print(f"Resultado da operação = {primeiro_numero + segundo_numero}")

elif sinal_operacao == "-":
    print(f"Resultado da operação = {primeiro_numero - segundo_numero}")

elif sinal_operacao == "x" or sinal_operacao == "*":
    print(f"Resultado da operação = {primeiro_numero * segundo_numero}")

elif (sinal_operacao == ":" or sinal_operacao == "/") and segundo_numero != 0:
    print(f"Resultado da operação = {primeiro_numero / segundo_numero}")

elif (sinal_operacao == ":" or sinal_operacao == "/") and segundo_numero == 0:
    print("Divisão indefinida (não é possível dividir por zero)")

elif sinal_operacao == "%" and segundo_numero != 0:
    print(f"Resultado da operação = {(primeiro_numero * segundo_numero) / 100}")

elif sinal_operacao == "%" and segundo_numero == 0:
    print("Operação indefinida")

else:
    print("Operação inválida")
