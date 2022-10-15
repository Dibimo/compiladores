from dicionario import retorna_dicionario

class Automato:
    def __init__(self, nomeAutomato):
        self.estados = {}
        self.acoes = {}
        self.acoesOriginal = {}
        self.classes = {}
        self.classes_simbolos = ''

        with open(nomeAutomato) as file:
            lines = file.readlines()
            lines = [line.rstrip() for line in lines]
        for l in lines:
            if l in '##':
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
        self.classes_simbolos = ''
        entrada_array = entrada.split(' ')
        estado_atual = self.estado_inicial
        for simbolo in entrada_array:
            estado_atual = self.estado_inicial
            self.classes_simbolos += ' '
            for e in simbolo:
                if(not estado_atual + e in self.estados or estado_atual == 'qm'):
                    return (False, e)

                estado_atual = self.estados[estado_atual + e]

                if(estado_atual in self.estado_final):
                    if(e in '.'):
                        self.classes_simbolos += ' '
                    self.adiciona_lexima(estado_atual)

        return self.retorna_leximas()

    def adiciona_lexima(self, estado):
        if (not self.classes[estado] in self.classes_simbolos):
            self.classes_simbolos += self.classes[estado]

    def retorna_leximas(self):
        return self.classes_simbolos

    def retorna_tupla(self):
        return (self.tipo, self.valor, self.id)
