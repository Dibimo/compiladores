from os import terminal_size
from pickle import FALSE
from dicionario import retorna_dicionario

class Automato:
    def __init__(self, nomeAutomato):
        self.estados = {}
        with open(nomeAutomato) as file:
            lines = file.readlines()
            lines = [line.rstrip() for line in lines]
        for l in lines:
            if('estado inicial' in l):
                self.estado_inicial = l.split(':')[1].strip()
                continue
            if('estado final' in l):
                self.estado_final = l.split(':')[1].strip()
                continue
            estado = l.split('|')[0].strip()
            terminais =  retorna_dicionario(l.split('|')[1].strip())
            destino = l.split('|')[2].strip()
            for t in terminais:
                self.estados[estado + t] = destino


    def analizar_entrada(self, entrada):
        entrada = entrada.replace(' ', '')
        estado_atual = self.estado_inicial
        for e in entrada:
            if(not estado_atual + e in self.estados):
                return False
            estado_atual = self.estados[estado_atual + e]
            if(estado_atual == 'qm'):
                return False
        if(estado_atual in self.estado_final):
            return True
        return False
