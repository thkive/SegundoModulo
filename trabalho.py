lista = []


def menu():
    print("MENU".center(40, '-'))
    print("1 - Cadastrar filme")
    print("2 - Ver filmes cadastrados")
    print("3 - Sair")
    print("--------------------------")

    while True:
        try:
            opcao = int(input("Digite uma opcao: "))
            return opcao
        except ValueError:
            print("Opção Invalida. Tente novamente!")
            
def cadastrar_filme():    
    
    contador = 0
    while contador < 3:
        try:
            
            print("------------------------------------")
            nome = input("Digite seu nome: ")
            filme = input("Digite o nome do filme: ")            
            nota = int(input("Digite uma nota para o filme de 0 a 10: "))
            if nota < 0 or nota > 10:
                print("-------------------------------------------")
                print("Nota invalida, digite uma nota entre 0 e 10")
                continue
            print("-----------------------------------")              

            print (f"Nome: {nome}")
            print(f"Nome do filme: {filme}")
            print(f"Nota do filme: {nota}")
            
            cadastro = {"nome": nome,"filme": filme, "nota": nota}
            lista.append(cadastro)


            contador = contador + 1
            
        except ValueError:
            print("Valores invalidos. Digite novamente.")
    
def mostrar_historico(lista):
    print("Historico de Filmes".center(40, '-'))

    if not lista:
        print("Nenhum aluno registrado ainda.")
    else:
        for cadastro in lista:
            print(f"Nome: {cadastro['nome']} |Filme: {cadastro['filme']} | Nota do filme: {cadastro['nota']}")
    print('-'*40)
    
def sistema():
    
    while True:
        opcao = menu()
        
        if opcao == 1:
            cadastrar_filme()
        elif opcao == 2:
            mostrar_historico(lista)
        elif opcao == 3:
            print("Saindo do sistema")
            break
        else:
            print("Opção invalida. Tente novamente.")
            
sistema()