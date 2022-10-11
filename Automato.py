from asyncio.windows_events import NULL
from os import terminal_size
from pickle import FALSE
from dicionario import retorna_dicionario

class Automato:
    def __init__(self, nomeAutomato):
        self.estados = {}
        self.acoes = {}
        self.acoesOriginal = {}
        funcoes = {
            'registrar_tipo': self.registrar_tipo,
            'registrar_id': self.registrar_id,
            'registrar_valor': self.registrar_valor,
        }

        self.tipo = ''
        self.valor = ''
        self.id = ''
        self.pilha = ''

        with open(nomeAutomato) as file:
            lines = file.readlines()
            lines = [line.rstrip() for line in lines]
        for l in lines:
            if('on' in l):
                estado = l.split('|')[1].strip()
                self.acoes[estado] = funcoes[l.split('|')[2].strip()]
                self.acoesOriginal[estado] = funcoes[l.split('|')[2].strip()]
                continue

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
        self.tipo = ''
        self.id = ''
        self.valor = ''
        self.pilha = ''
        entrada = entrada.replace(' ', '')
        estado_atual = self.estado_inicial
        for e in entrada:


            if(not estado_atual + e in self.estados):
                return False

            if(not e in '=.'):
                self.pilha += e

            estado_atual = self.estados[estado_atual + e]

            if(estado_atual == 'qm'):
                return False

            if(estado_atual in self.acoes):
                self.acoes[estado_atual]()

        if(estado_atual in self.estado_final):
            return True
        return False

    def registrar_tipo(self):
        if(self.tipo == ''):
            self.tipo = self.pilha
            self.pilha = ''

    def registrar_id(self):
        if(self.id == ''):
            self.id = self.pilha
            self.pilha = ''

    def registrar_valor(self):
        if(self.valor == ''):
            self.valor = self.pilha
            self.pilha = ''

    def retorna_tupla(self):
        return (self.tipo, self.valor, self.id)
