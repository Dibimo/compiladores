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


    def check_int(s):
        if s[0] in ('-', '+'):
            return s[1:].isdigit()
        return s.isdigit()

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
                lexemas.append(('id', pilha))

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
                if('..' in pilha or '==' in pilha):
                    pilha = pilha[:-1]
                if(lexema != '' and pilha != ''):
                    lexemas.append((lexema, pilha))
                    lexema = ''
                    pilha = ''

            if(e != " "):
                pilha += e


        if(lexema != ''): # salvando o ??ltimo lexema, se for o caso
            if('..' in pilha):
                pilha = '.'
            if(lexema != '' and pilha != ''):
                lexemas.append((lexema, pilha))

        if (not estado_atual in self.estado_final):
            lexemas.append(('id', pilha))
        return lexemas
