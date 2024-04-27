
#  Cria chaves sem valor (valor nulo: none) ou com um valor padrão

d1 = dict.fromkeys(["nome", "telefone"])  # {"nome": None, "telefone": None}
print(d1)

d2 = dict.fromkeys(["nome", "telefone"], "cep")  # {"nome": "vazio", "telefone": "cep"}
print(d2)
