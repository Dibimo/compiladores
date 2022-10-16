def retorna_linhas_arquivo(arquivo : str) -> list:
    with open(arquivo) as file:
        lines = file.readlines()
        lines = [line.rstrip() for line in lines]
    return lines