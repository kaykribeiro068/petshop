from pets import pets
#dicionario com opçoes, nomes e valores dos serviços
servicos_disponiveis = {
    1: {"nome": "Banho", "preco": 80},
    2: {"nome": "Tosa", "preco": 100},
    3: {"nome": "Consulta", "preco": 120},
    4: {"nome": "Hospedagem", "preco": 150}
}

servicos_realizados = 0
faturamento_total = 0

#Lista os serviços para a escolha e registra, realiza o relatorio de quanto pet "X" gastou
def mostrar_servicos():
    print("\n=== Serviços Disponíveis ===")

    for codigo in servicos_disponiveis:
        nome = servicos_disponiveis[codigo]["nome"]
        preco = servicos_disponiveis[codigo]["preco"]

        print(codigo, "-", nome, "- R$", preco)


def registrar_servico():

    global servicos_realizados
    global faturamento_total

    if len(pets) == 0:
        print("Nenhum pet cadastrado.")
        return

    nome_pet = input("Nome do pet: ")

    pet_encontrado = None

    for pet in pets:
        if pet["nome"].lower() == nome_pet.lower():
            pet_encontrado = pet

    if pet_encontrado is None:
        print("Pet não encontrado.")
        return

    mostrar_servicos()

    codigo = int(input("Escolha o serviço: "))

    if codigo not in servicos_disponiveis:
        print("Serviço inválido")
        return

    preco = servicos_disponiveis[codigo]["preco"]

    pet_encontrado["total_servicos"] += preco

    servicos_realizados += 1
    faturamento_total += preco

    print("Serviço registrado!")
    print("Total gasto pelo pet:", pet_encontrado["total_servicos"])
