#Tabela informando serviços e preços fixos
servicos_disponiveis = {
    1: {'nome': 'Banho', 'preco': 80},
    2: {'nome': 'Tosa', 'preco': 100},
    3: {'nome': 'Consulta', 'preco': 120},
    4: {'nome': 'Hospedagem', 'preco': 150}
}
#informa os serviços disponivel mostrando o layout para o client
def mostrar_servicos():
    print("\n=== Serviços Disponíveis ===")
    for codigo in servicos_disponiveis:
        nome = servicos_disponiveis[codigo]['nome']
        preco = servicos_disponiveis[codigo]['preco']
        print(codigo, "-", nome, "- R$", preco)


def escolher_servico():
    codigo = int(input("Digite o número do serviço desejado: "))
    
    if codigo in servicos_disponiveis:
        return servicos_disponiveis[codigo]['preco']
    else:
        print("Serviço inválido.")
        return 0


def main():
    total = 0
    opcao = 0

    while opcao != 2:
        print("\n=== MENU ===")
        print("1 - Registrar serviço")
        print("2 - Finalizar atendimento")

        opcao = int(input("Escolha uma opção: "))

        if opcao == 1:
            mostrar_servicos()
            preco = escolher_servico()
            total = total + preco
            print("Total até agora: R$", total)

        elif opcao == 2:
            print("\nAtendimento finalizado.")
            print("Valor total: R$", total)

        else:
            print("Opção inválida.")


main()