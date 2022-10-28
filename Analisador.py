from asyncio.windows_events import NULL


class Analisador:
    def __init__(self, entrada : list):
      self.codigo = entrada
      self.linha_atual = NULL
      self.token_atual = NULL

      self.quantidade_linhas = len(entrada)
      self.tamanho_linha = NULL

      self.linha_ponteiro = 0
      self.token_ponteiro = 0

      self.tabela_simbolos = {}
      self.erro = False

      self.temComeco = False


    def iniciar(self):
        while(self.linha_ponteiro < self.quantidade_linhas and not self.erro):
            self.proxima_linha()
            self.proximo_token()
            self.regra_comeco()

    def regra_comeco(self):
        token, valor = self.token_atual
        if(token == 'int' or token == 'float'): # se for  declaração de variavel1
            self.tipo = valor
            self.proximo_token()
            self.r_declaracao_id()
            return
        if(not self.temComeco):
            self.temComeco = token == 'ini'

        if(self.temComeco):
            self.r_comeco()

        # else:
        #     # self.erro = True
        #     print('Erro')


    def r_comeco(self):
        token, valor = self.token_atual
        # self.proximo_token()
        self.r_programa()
        # else:
        #     print('Esperado inicio de programa')


    def r_programa(self):
        token, valor = self.token_atual
        if(token == 'esc'):
            self.proximo_token()
            self.r_escrever()

        if(token == 'ler'):
            self.proximo_token()
            self.r_ler()

        if(token == 'id'):
            pass


    def r_escrever(self):
        token, valor = self.token_atual
        if(token == 'id'):
            if(valor in self.tabela_simbolos.keys()):
                self.proximo_token()
                if(self.r_endl()):
                    print(self.tabela_simbolos[valor]['valor'])
                else:
                    print('Esperado final de linha')
            else:
                print('Variavel não declarada')
        else:
            print('Esperado identificador')


    def r_ler(self):
        token, valor = self.token_atual
        if(token == 'id'):
            if(valor in self.tabela_simbolos.keys()):
                self.proximo_token()
                if(self.r_endl()):
                    temp = input()
                    if(type(temp) == 'float' and self.tabela_simbolos[valor]['tipo'] == 'int'):
                        print('Tipos não compativeis')
                        exit(0)
                    self.tabela_simbolos[valor]['valor'] = temp
                else:
                    print('Esperado final de linha')
            else:
                print('Variavel não declarada')
        else:
            print('Esperado identificador')

    def r_declaracao_id(self):
        token, valor = self.token_atual
        if(token == 'id'):
            self.tabela_simbolos[valor] = {}
            self.tabela_simbolos[valor]['tipo'] = self.tipo
            self.id = valor
            self.proximo_token()
            self.r_declaracao_att()
        else:
            print(f'Esperado identificador')

    def r_declaracao_att(self):
        token, valor = self.token_atual
        if(token == '='):
            self.proximo_token()
            self.r_declaracao_valor()
        else:
            print('Esperado símbolo de atribuição')

    def r_declaracao_valor(self):
            token, valor = self.token_atual
            if(token == 'num' or token == 'numr'):
                if(self.tabela_simbolos[self.id]['tipo'] == 'INT' and ',' in valor):
                    print('Não é póssivel passar um valor real para uma váriavel inteira')
                    return
                self.tabela_simbolos[self.id]['valor'] =  valor
                self.proximo_token()
                self.r_endl()
            else:
                print('Esperado valor numerico')

    def r_endl(self):
        token, valor = self.token_atual
        if(token == '.'):
            return True
        else:
            print('Esperado ponto final')


    def proximo_token(self):
        if(self.token_ponteiro < self.tamanho_linha):
            self.token_atual = self.linha_atual[self.token_ponteiro]
            self.token_ponteiro += 1
        else:
            self.token_ponteiro = 0
            self.proxima_linha()

    def proxima_linha(self):
        if(self.linha_ponteiro  < self.quantidade_linhas):
            self.linha_atual = self.codigo[self.linha_ponteiro]
            self.tamanho_linha = len(self.linha_atual)
            self.linha_ponteiro += 1
            self.token_ponteiro = 0
            self.token_atual = self.linha_atual[self.token_ponteiro]


