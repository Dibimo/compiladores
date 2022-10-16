from Analisador import Analisador
from Automato import Automato
from utilitarios import retorna_linhas_arquivo


automato_geral = Automato('./automatos/automato_geral.automato')
linhas = retorna_linhas_arquivo('exemplo.exm')

# print(linhas)

lexemas = []
for l in linhas:
    lexemas.append(automato_geral.analizar_entrada(l))

asd = Analisador(lexemas)
asd.iniciar()
# print(automato_geral.analizar_entrada('teste.'))

