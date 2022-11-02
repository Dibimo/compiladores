import sys
from Analisador import Analisador
from Automato import Automato
from utilitarios import retorna_linhas_arquivo
from utilitarios import print_lexemas


automato_geral = Automato('./automatos/automatos.automato')
linhas = retorna_linhas_arquivo('exemplo.exm')

# print(linhas)

lexemas = []
for l in linhas:
    if(l == ''):
        continue
    lexemas.append(automato_geral.analizar_entrada(l))

if('-lexemas' in sys.argv):
    print_lexemas(lexemas)

print()
print()
print()

asd = Analisador(lexemas)
asd.iniciar()

# if('erro' in lexemas):
#     print('ERRO de sintaxe')
# else:

