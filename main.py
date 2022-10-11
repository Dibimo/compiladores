from Automato import Automato


automato_teste = Automato('nomes_variaveis copy.automato')
tabela_simbolos = []

automato_teste.analizar_entrada('int a = 10.')
tabela_simbolos.append(automato_teste.retorna_tupla())

automato_teste.analizar_entrada('float b = 11,4.')
tabela_simbolos.append(automato_teste.retorna_tupla())

automato_teste.analizar_entrada('int c = 0.')
tabela_simbolos.append(automato_teste.retorna_tupla())


print(tabela_simbolos)
