clientes = []
#funçção para cadastrar e armazenar o cliente na lista acima e validar cpf existente ou não
def cadastrar_cliente():
    print("\n=== Bem Vindo ao Cadastro de Cliente ===")
 
    nome_cliente = input("Digite seu nome: ")
    cpf_cliente = input("Insira seu CPF somente com os numeros(11 digitos): ")
    
    while len(cpf_cliente) != 11:
        print("CPF deve ter 11 dígitos")
        cpf_cliente = input("CPF: ")

    cpf_cliente = int(cpf_cliente)

    for cliente in clientes:
        if cliente["cpf"] == cpf_cliente:
            print("CPF já cadastrado!")
            return

    telefone_cliente = input("Telefone: ")
    endereco_cliente = input("Endereço: ")

    cliente = {
        "nome": nome_cliente,
        "cpf": cpf_cliente,
        "telefone": telefone_cliente,
        "endereco": endereco_cliente
    }

    clientes.append(cliente)

    print("Cliente cadastrado com sucesso!")

#Mostra quantidade e clientes cadastrados ou não
def listar_clientes():
    print("\n=== Clientes Cadastrados ===")

    if len(clientes) == 0:
        print("Nenhum cliente cadastrado.")
        return

    for cliente in clientes:
        print("Nome:", cliente["nome"], "| CPF:", cliente["cpf"])
