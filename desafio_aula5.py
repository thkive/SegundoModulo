def menu():
    print("MENU".center(40, '-'))
    print("1 - Calcular pagamento")
    print("2 - Ver ajuda")
    print("3 - Sair")
    print("--------------------------")

    while True:
        try:
            opcao = int(input("Digite uma opcao: "))
            print("--------------------------")
            return opcao
        except ValueError:
            print("Opção Invalida. Tente novamente!")


def pagamento(horas, valor, dias):
    salario = horas * valor * dias
    return salario

    
def mostrar_ajuda():

    print("Calculo do Salario".center(40, '-'))
    print("Horas trabalhadas x Valor da hora x Dias trabalhados")


def sistema():
    while True:
        opcao = menu()

        if opcao == 1:
            horas = int(input("Digite o numero de horas trabalhadas por dia: "))
            valor = float(input("Digite o valor pago por hora: "))
            dias = int(input("Digite o numero de dias trabalhados: "))

            salario = pagamento(horas, valor, dias)

            print("---------------------------------------------------")
            print(f"O valor a ser pago do salario é de {salario} reais")

        elif opcao == 2:
            mostrar_ajuda()
        
        elif opcao == 3:
            print("Volte Sempre")
            break
        
        else:
            print("Opção Invalida. Tente Novamente.")

sistema()