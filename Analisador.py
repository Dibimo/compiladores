from asyncio.windows_events import NULL


class Analisador:
    def __init__(self, entrada : list):
        self.aux = {
            '+': 'mais',
            '-': 'menos',
            '=': 'att',
            '.': 'endl'
        }
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
        self.temFinal = False

        self.variavel_reatribuicao = ''



    def iniciar(self):
        while(self.linha_ponteiro < self.quantidade_linhas and not self.erro):
            self.proxima_linha()
            self.proximo_token()
            self.comeco()

        if(self.temComeco and self.temFinal):
            print('Compilado com sucesso')
        else:
            if(not self.temComeco):
                print('Esperado ínicio de programa')
                return
            if(not self.temFinal):
                print('Esperado final de programa')

    def comeco(self):
        self.executar_func(self.get_token_classe())


    def f_int(self):
        self.executar_regra('id', 'Esperado variável')

    def f_float(self):
        self.executar_regra('id', 'Esperado variável')

    def f_id(self):
        self.executar_regra('= . + -', 'Esperado atribuição ou finalização de linha')

    def f_att(self):
        self.executar_regra('id num numr', 'Esperado esperado número ou váriavel')

    def f_num(self):
        self.executar_regra('+ - .', 'Esperado esperado operador ou finalização de linha')

    def f_numr(self):
        self.executar_regra('+ - .', 'Esperado esperado operador ou finalização de linha')

    def f_mais(self):
        self.executar_regra('id num numr', 'Esperado variável ou número')

    def f_menos(self):
        self.executar_regra('id num numr', 'Esperado variável ou número')

    def f_esc(self):
        self.executar_regra('id num numr', 'Esperado variável ou número')

    def f_ler(self):
        self.executar_regra('id', 'Esperado variável')

    def f_endl(self):
        return

    def f_ini(self):
        self.proximo_token()
        self.iniciar_programa()

    def f_fim(self):
        self.finalizar_programa()

    def iniciar_programa(self):
        self.temComeco = True
        return

    def finalizar_programa(self):
        self.temFinal = True
        return

    def executar_regra(self, classes_esperadas, mensagem_erro):
        self.proximo_token()
        self.verifica_token(classes_esperadas, mensagem_erro)
        self.executar_func(self.get_token_classe())

    def executar_func(self, nome_metodo):
        nome_metodo = self.converte_nome_func(nome_metodo)
        self.__getattribute__(f'f_{nome_metodo}')()


    def converte_nome_func(self,nome_metodo):
        if(nome_metodo in self.aux):
            return self.aux[nome_metodo]
        return nome_metodo

    def verifica_token(self, classes_esperadas: str, mensagem_erro = 'Erro'):
        if(not self.get_token_classe() in classes_esperadas):
            print(mensagem_erro)
            print(f'Linha {self.linha_ponteiro}: {self.linha_atual}')
            print(f'{mensagem_erro}, próximo de "{self.get_token_valor()}"')
            exit(0)

    def get_token_classe(self):
        return self.token_atual[0]

    def get_token_valor(self):
        return self.token_atual[1]

    def proximo_token(self):
        if(self.token_ponteiro < self.tamanho_linha):
            self.token_atual = self.linha_atual[self.token_ponteiro]
            self.token_ponteiro += 1
        else:
            pass
            # self.token_ponteiro = 0
            # self.proxima_linha()

    def proxima_linha(self):
        if(self.linha_ponteiro  < self.quantidade_linhas):
            self.linha_atual = self.codigo[self.linha_ponteiro]
            self.tamanho_linha = len(self.linha_atual)
            self.linha_ponteiro += 1
            self.token_ponteiro = 0
            self.token_atual = self.linha_atual[self.token_ponteiro]


