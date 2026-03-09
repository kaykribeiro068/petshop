clientes = []
pets = []
servicos = []

def cadastrar_clientes():
    while True:
        print("\n== Cadastro de Clientes ==")

        nome = input("Digite seu nome: ")
        cpf = input("Digite seu cpf(11 digitos): ")
        while len(cpf) < 11:
            
            print("cpf deve ter exatamnete 11 digitos")
            cpf = input("digite novamente o seu cpf")
        cpf = int(cpf) 
       

        # verificar se já existe
        for cliente in clientes:
            if cliente["cpf"] == cpf:
                print("cpf já cadastrado!")
                return

        telefone = int (input("Digite seu telefone: "))
        endereco = input("Digite seu endereço: ")

        cliente = {
            "nome": nome,
            "cpf": cpf,
            "telefone": telefone,
            "endereco": endereco
        }

        clientes.append(cliente)
        print("Cliente devidamente cadastrado")

        continuar = input("Deseja cadastrar outro cliente? (s/n): ")

        if continuar.lower() != "s":
            break


cadastrar_clientes()