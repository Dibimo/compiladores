class ASD:
    def __init__(self, entrada):
      self.entrada = entrada
      self.tamanhoEntrada = len(entrada)
      self.contador = 0
      self.token = ''

    def prox_token(self):
        if (self.token == '$'):
            return
        self.token = self.entrada[self.contador]
        self.contador += 1

    def regraF(self):
        if (self.token == '('):
            self.prox_token()
            self.regraE()
            if(self.token == ')'):
                self.prox_token()
            else: raise Exception(f"Error de compilação token: {self.token}")
        else:
            if (self.token == 'a' or self.token == 'b'):
                self.prox_token()
            else: raise Exception(f"Error de compilação token: {self.token}")

    def regraT(self):
        self.regraF()
        if (self.token == '*'):
            self.prox_token()
            self.regraT()



    def regraE(self):
        self.regraT()
        if (self.token == '+'):
            self.prox_token()
            self.regraE()

    def iniciar(self):
        self.prox_token()
        self.regraE()
        if(self.token == '$'):
            print('Compilado com sucesso')
        else:
            print('Erro de compilação')