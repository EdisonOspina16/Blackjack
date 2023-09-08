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


class Baraja:
    def __init__(self):
        self.cartas = []
        self.revolver()

    def revolver(self):
        pintas = ['CORAZÓN', 'TRÉBOL', 'DIAMANTE', 'ESPADA']
        valores = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']

    def repartir_carta(self, tapada: bool) -> Carta:
        carta = self.cartas.pop()
        carta.tapada = tapada
        return carta

