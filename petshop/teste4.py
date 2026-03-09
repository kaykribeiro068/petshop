pets = []
def cadastrar_pet():
#cadastrar pet, espécie e cpf do dono
 while True:
        nome = input("Digite o nome do seu pet: ")
        especie = input("Digite a espécie do seu animal: ")

        cpf = input("CPF do dono: ")
       #verificar a quantidade de caracteres do cpf
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
        #jogar o dicionário pet na lista pets
        pets.append(pet)

        print("Cadastro realizado com sucesso :)!!")
        print(pets)

        #continuar o serviço
        continuar = input("Deseja cadastrar outro pet? (s/n): ")

        if continuar == "n":
         break
cadastrar_pet()



