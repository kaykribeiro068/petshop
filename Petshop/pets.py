from clientes import clientes

pets = []
#Cadrastra o pet e logo apos valida o cpf do dono para armazenar em "pets"
def cadastrar_pet():
    print("\n=== Cadastro de Pet ===")

    nome = input("Nome do pet: ")
    especie = input("Espécie: ")

    cpf_dono = input("CPF do dono: ")

    while len(cpf_dono) != 11:
        print("CPF inválido")
        cpf_dono = input("CPF do dono: ")

    cpf_dono = int(cpf_dono)

    dono_encontrado = False

    for cliente in clientes:
        if cliente["cpf"] == cpf_dono:
            dono_encontrado = True

    if not dono_encontrado:
        print("Cliente não encontrado. Cadastre o cliente primeiro.")
        return

    pet = {
        "nome": nome,
        "especie": especie,
        "cpf_dono": cpf_dono,
        "total_servicos": 0
    }

    pets.append(pet)

    print("Pet cadastrado com sucesso!")

#Mostra total de pets cadastrados e localiza os mesmos
def listar_pets():
    print("\n=== Lista de Pets ===")

    if len(pets) == 0:
        print("Nenhum pet cadastrado.")
        return

    for pet in pets:
        print(
            "Nome:", pet["nome"],
            "| Espécie:", pet["especie"],
            "| Total gasto:", pet["total_servicos"]
        )
