# Entrada de dados
numero_conta = input("Digite o número da conta: ")
saldo = float(input("Digite o saldo atual: "))
debito = float(input("Digite o valor do débito: "))
credito = float(input("Digite o valor do crédito: "))

# Cálculo do saldo atual
saldo_atual = saldo - debito + credito

# Saída do saldo atual
print(f"\nConta: {numero_conta}")
print(f"Saldo atual: R$ {saldo_atual:.2f}")

# Verificação do saldo
if saldo_atual >= 0:
    print("Saldo Positivo")
else:
    print("Saldo Negativo")