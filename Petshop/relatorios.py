import servicos
from clientes import clientes
from pets import pets

#Importa partes dos outros arquivos e realiza relatorios de cada etapa solicitada
def mostrar_relatorios():
    
    print("\n=== RELATÓRIOS DO PETSHOP ===")

    total_clientes = len(clientes)
    total_pets = len(pets)

    print("Total de clientes cadastrados:", total_clientes)
    print("Total de pets cadastrados:", total_pets)
    print("Total de serviços realizados:", servicos.servicos_realizados)
    print("Faturamento total: R$", servicos.faturamento_total)