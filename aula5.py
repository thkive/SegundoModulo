def pagamento(horas,valor,dias):
    salario = (horas * valor)* dias
    return salario

horas = int(input("Digite o numero de horas trabalhadas por dia: "))
valor = float(input("Digite o valor pago por hora: "))
dias = int(input("Digite o numero de dias trabalhados: "))

salario_total = pagamento(horas, valor,dias)

print(f"O valor o salario é de {salario_total}")
