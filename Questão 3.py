# Entrada de dados
horas_mes = float(input("Digite o total de horas trabalhadas no mês: "))
valor_hora = float(input("Digite o valor da hora de trabalho: "))

# Jornada padrão (40 horas semanais * 4 semanas)
horas_normais = 40 * 4

# Cálculo
if horas_mes > horas_normais:
    horas_extras = horas_mes - horas_normais
    salario_normal = horas_normais * valor_hora
    salario_extra = horas_extras * (valor_hora * 1.5)
    salario_total = salario_normal + salario_extra
else:
    salario_total = horas_mes * valor_hora

# Saída
print(f"Salário total: R$ {salario_total:.2f}")