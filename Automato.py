from dicionario import retorna_dicionario

class Automato:
    def __init__(self, nomeAutomato):
        self.estados = {}
        self.acoes = {}
        self.acoesOriginal = {}
        self.classes = {}
        self.classes_simbolos = ''
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
            if l in '##':
                continue
            if('on' in l):
                estado = l.split('|')[1].strip()
                self.acoes[estado] = funcoes[l.split('|')[2].strip()]
                self.acoesOriginal[estado] = funcoes[l.split('|')[2].strip()]
                continue

            if('estado inicial' in l):
                self.estado_inicial = l.split(':')[1].strip()
                continue

            if('estado final' in l):
                self.estado_final = l.split(':')[1].strip().split(' ')
                continue

            if ('classe' in l):
                estado = l.split(' ')[0]
                classe = l.split(' ')[2]
                self.classes[estado] = classe
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
        self.classes_simbolos = ''
        # entrada = entrada.replace(' ', '')
        estado_atual = self.estado_inicial
        for e in entrada:
            if(e in ' '):
                estado_atual = self.estado_inicial
                continue
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
                self.adiciona_classe_simbolo(estado_atual)
        return self.retorna_classe_simbolo()

    def adiciona_classe_simbolo(self, estado):
        self.classes_simbolos += self.classes[estado] + ' '

    def retorna_classe_simbolo(self):
        return self.classes_simbolos

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
