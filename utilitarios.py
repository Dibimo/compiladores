def retorna_linhas_arquivo(arquivo : str) -> list:
    with open(arquivo) as file:
        lines = file.readlines()
        lines = [line.rstrip() for line in lines]
    return lines

def print_lexemas(lexemas : list):
    quantidade_linhas = len(lexemas)
    for i in range(0, quantidade_linhas):
        print(f'Linha: {i + 1}', end=" -> ")
        print(lexemas[i])
