banco = ""
nome = ""
idade = ""
conta = ""
numero = 0

while True:
    print("-------------------------")
    print("***Bem vindo ao Menu:***")
    print("1 - Cadastrar banco:")
    print("2 - Cadastrar cliente:")
    print("3 - Ver dados cadastrados")
    print("4 - Sair do sistema")
    print("--------------------------")

    opcao = int(input("Digite a opção desejada: "))
    
    if opcao == 1:
        print("-------------------------")
        banco = input("Digite o nome do seu banco: ")
        conta = input("Digite o tipo de conta: ")
        print("Banco cadastrado.")
    elif opcao == 2:
        print("-------------------------")
        if banco:
            nome = input("Digite seu nome: ")
            idade = int(input("Digite sua idade: "))
            numero = int(input("Digite se numero de telefone: "))
            print("Cliente cadastrado")
        else:
            print("Banco não cadastrado")
    elif opcao == 3:
        print("-------------------------")
        if banco and nome:
            print("Banco: ", banco)
            print("Conta: ", conta)
            print("Nome: ", nome)
            print("Idade: ", idade)
            print("Telefone: ", numero)
        else:
            print("Dados não cadastrados")
    elif opcao == 4:
        ("-------------------------")
        print("***Volte Sempre***")
        break
    else: 
        print("Opção invalida, digite novamente.")
print("**********************")
