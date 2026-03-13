from clientes import cadastrar_cliente, listar_clientes
from pets import cadastrar_pet, listar_pets
from servicos import registrar_servico
from relatorios import mostrar_relatorios


def menu():

    while True:

        print("\n=== SISTEMA PETSHOP ===")
        print("1 - Cadastrar cliente")
        print("2 - Cadastrar pet")
        print("3 - Registrar serviço")
        print("4 - Listar clientes")
        print("5 - Listar pets")
        print("6 - Relatórios")
        print("7 - Sair")

        opcao = input("Escolha: ")

        if opcao == "1":
            cadastrar_cliente()

        elif opcao == "2":
            cadastrar_pet()

        elif opcao == "3":
            registrar_servico()

        elif opcao == "4":
            listar_clientes()

        elif opcao == "5":
            listar_pets()

        elif opcao == "6":
            mostrar_relatorios()

        elif opcao == "7":
            print("Sistema encerrado")
            break

        else:
            print("Opção inválida")


menu()
