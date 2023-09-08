import random


class Carta:
    def __init__(self, pinta: str, valor: str):
        self.pinta = pinta
        self.valor = valor
        self.tapada = False

    def __str__(self):
        if self.tapada:
            return "Carta tapada"
        else:
            return f'{self.valor} de {self.pinta}'

