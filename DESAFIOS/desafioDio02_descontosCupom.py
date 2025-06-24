# Dicionário com os valores de desconto
descontos = {
    "DESCONTO10": 0.10,
    "DESCONTO20": 0.20,
    "SEM_DESCONTO": 0.00
}

# Entrada do usuário
preco = float(input('Digite o preço: ').strip())
cupom = input('Entre com o cupom: ').strip()

saida = preco * (1 - descontos[cupom])
print(f'{saida:.2f}')
