import string
def retorna_dicionario(chave):
    dicionario = {
        '[a-z]': string.ascii_lowercase,
        '[A-Z]': string.ascii_uppercase,
        '[0-9]': string.digits,
        'espaco': ' ',
        '[*]': string.digits + string.ascii_letters + '.=' + string.whitespace,
        '[a-z][0-9]': string.ascii_lowercase + string.ascii_uppercase + string.digits,
    }
    if '*' in chave:
        valor = []
        chaves_atuais = dicionario.keys()
        for c in chaves_atuais:
            if(not c in chave):
                valor += dicionario[c]

        dicionario[chave] = valor
    if chave in dicionario:
        return dicionario[chave]
    return chave