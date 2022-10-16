from dicionario import retorna_dicionario

class Automato:
    def __init__(self, nomeAutomato):
        self.estados = {}
        self.acoes = {}
        self.acoesOriginal = {}
        self.classes = {}
        self.classes_simbolos = ''
        self.tabela_simbolos = {}

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

            if('retrocede' in l):
                teste = l.replace('retrocede: ', '')
                self.estados_retrocede = teste.split(' ')
                continue

            if ('classe' in l):
                estado = l.split(' ')[0]
                classe = l.split(' ')[2]
                self.classes[estado] = classe.replace(' ', '')
                continue

            estado = l.split('|')[0].strip()
            terminais =  retorna_dicionario(l.split('|')[1].strip())
            destino = l.split('|')[2].strip()
            for t in terminais:
                self.estados[estado + t] = destino


    def analizar_entrada(self, entrada : str):
        self.classes_simbolos = ''
        estado_atual = self.estado_inicial
        lexemas = []
        lexema = ''
        i = 0
        houve_troca_estado = False
        pilha = ''
        while(i < len(entrada)):
            e = entrada[i]

            if(not (estado_atual + e) in self.estados or estado_atual == 'qm'):
                return (False, e)

            proximo_estado = self.estados[estado_atual + e]

            houve_troca_estado = estado_atual != proximo_estado
            estado_atual = proximo_estado
            i += 1
            if(estado_atual in self.estado_final and houve_troca_estado):
                lexema = self.classes[estado_atual]


            if(estado_atual in self.estados_retrocede):
                i -= 1
                estado_atual = self.estado_inicial

            if(estado_atual == self.estado_inicial):
                if('..' in pilha):
                    pilha = '.'
                lexemas.append((lexema, pilha))
                lexema = ''
                pilha = ''

            if(e != " "):
                pilha += e


        if(lexema != ''): # salvando o último lexema, se for o caso
            if('..' in pilha):
                pilha = '.'
            lexemas.append((lexema, pilha))

        if (not estado_atual in self.estado_final):
            return 'erro'
        return lexemas

    def retorna_tupla_simbolo(self):
        if('int' in self.classes_simbolos or 'float' in self.classes_simbolos):
            id_v = self.classes_simbolos.split(' ')[1]
            tipo = self.classes_simbolos.split(' ')[0]
            valor_inicial = self.classes_simbolos.split(' ')[4]
            return (id_v, tipo, valor_inicial)

        if('ini' in self.classes_simbolos or 'fim' in self.classes_simbolos):
            return (self.classes_simbolos)

    def adiciona_lexema(self, estado):
        if (not self.classes[estado] in self.classes_simbolos):
            self.classes_simbolos += self.classes[estado]

    def retorna_lexemas(self):
        return self.classes_simbolos

