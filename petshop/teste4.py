pets = []

while True:
        nome = input("Digite o nome do seu pet: ")
        especie = input("Digite a espécie do seu animal: ")

        cpf = input("CPF do dono: ")
        while len(cpf) < 11:
           print("CPF deve ter pelo menos 11 caracteres")
           cpf = input("CPF do dono: ")

        cpf = int(cpf)

        pet = {
        "nome": nome,
        "especie": especie,
        "cpf_dono": cpf,
        "total_servicos": 0
    }

        pets.append(pet)

        print("Cadastro realizado com sucesso :)!!")
        print(pets)

        continuar = input("Deseja cadastrar outro pet? (s/n): ")

        if continuar == "n":
         break

