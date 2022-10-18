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


    def iniciar(self):
        while(self.linha_ponteiro < self.quantidade_linhas and not self.erro):
            self.proxima_linha()
            self.proximo_token()
            self.regra_1()

    def regra_1(self):
        token, valor = self.token_atual
        if(token == 'int' or token == 'float'):
            self.tipo = valor
            self.proximo_token()
            self.regra_2()
            return
        if(token == 'ini'):
            self.regra_6()
        else:
            self.erro = True
            print('Erro')

    def regra_2(self):
        token, valor = self.token_atual
        if(token == 'id'):
            self.tabela_simbolos[valor] = {}
            self.tabela_simbolos[valor]['tipo'] = self.tipo
            self.id = valor
            self.proximo_token()
            self.regra_3()
        else:
            print(f'Esperado identificador de variavel, recebido {token}')

    def regra_3(self):
        token, valor = self.token_atual
        if(token == '='):
            self.proximo_token()
            self.regra_4()

    def regra_4(self):
        token, valor = self.token_atual
        if(token == 'num' or token == 'numr'):
            if(self.tabela_simbolos[self.id]['tipo'] == 'INT' and ',' in valor):
                print('Não é póssivel passar um valor real para uma váriavel inteira')
                return
            self.tabela_simbolos[self.id]['valor'] =  valor
            self.proximo_token()
            self.regra_5()

    def regra_5(self):
        token, valor = self.token_atual
        if(token == 'endl'):
            return
        else:
            print('Esperado ponto final')


    def regra_6(self):
        token, valor = self.token_atual
        if(token == 'ini'):
            self.proximo_token()
            self.regra_7()
        else:
            print('Esperado começo de programa')

    def regra_7(self):
        token, valor = self.token_atual
        if(token == 'esc'):
            self.proximo_token()
            self.regra_8()

    def regra_8(self):
        self.proximo_token()
        token, valor = self.token_atual
        if(token == 'id'):
            print(self.tabela_simbolos[valor]['valor'])
            exit(0)


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


