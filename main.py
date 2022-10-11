from enum import auto
from Automato import Automato


automato_variavel  = Automato('nomes_variaveis copy.automato')
automato_comeco_final = Automato('comeco_final.automato')

with open('programa1.exm') as file:
    lines = file.readlines()
    lines = [line.rstrip() for line in lines]

for l in lines:
    eh_variavel = automato_variavel.analizar_entrada(l)
    eh_comeco = automato_comeco_final.analizar_entrada(l)
    if(eh_variavel):
        print('variavel')
        continue
    print('não variavel')