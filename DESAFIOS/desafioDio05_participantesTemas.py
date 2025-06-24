# Dicionário para agrupar participantes por tema
eventos = {}

# Entrada do número de participantes
n = int(input().strip())

# TODO: Crie um loop para armazenar participantes e seus temas:
for i in range(n):
    linha = input().strip()   #  Participante , Tema

    # Encontra a posição da vírgula para separar participante e tema
    posicao_virgula = linha.rfind(',')  # posição da última ocorrência do caracter

    # Separa o nome do participante do tema escolhido
    participante = linha[:posicao_virgula]
    tema = linha[posicao_virgula + 2:]
    print('0', tema, participante)              # APAGAR
    # Separando os participantes
    if tema in eventos:
       eventos[tema].append(participante)   # cria uma lista dentro do "value" do dicionário
       print('1', eventos)                      # APAGAR
    else:
       eventos[tema] = [participante]
       print('2', eventos)                      # APAGAR
    print(40 * '-')                             # APAGAR
    #  print(eventos)  {'Fotografia': ['Lucas', 'Carlos'], 'Viagem': ['Ana']}

# Exibe os grupos organizados
for tema, participantes in eventos.items():
    print(f"{tema}: {', '.join(participantes)}")
