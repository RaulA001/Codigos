class fruta:
    def __init__(self, nome, tipo, preço, estado, tempo):
        self.Nome = nome
        self.Tipo = tipo
        self.Preço = preço
        self.Estado = estado
        self.Tempo = tempo
    def envelecer(self, estado):
        t = self.tempo
        s = 0
        if 3 < t < 4:
            s = 1
        else:
            s = 2
        t += 1

        if s == 0:
            self.Estado = 'verde'
        elif s == 1:
            self.Estado = 'maduro'
        else:
            self.Estado = 'poder'

    def __get__(self, instance, owner):


a = fruta('nome', 'tipo', 'preço', 'estado', 'tempo')

