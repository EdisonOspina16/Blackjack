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


class Mano:
    def __init__(self):
        self.cartas = []

    def recibir_carta(self, carta):
        self.cartas.append(carta)

    def calcular_valor(self):
        valor = sum([10 if carta.valor in ['J', 'Q', 'K'] else int(carta.valor) for carta in self.cartas])
        ases = [carta for carta in self.cartas if carta.valor == 'A']
        for _ in ases:
            if valor > 21:
                valor -= 10
        return valor


class Blackjack:
    def __init__(self):
        self.jugador = None
        self.fichas = 0
        self.baraja = None

    def registrar_jugador(self, nombre):
        self.jugador = nombre
        self.fichas = 100
        self.baraja = Baraja()

    def iniciar_juego(self, apuesta):
        self.fichas -= apuesta
        self.baraja.revolver()

        mano_jugador = Mano()
        mano_casa = Mano()

        if mano_jugador.calcular_valor() == 21:
            print('¡Blackjack! Ganaste la mano.')
            self.fichas += apuesta * 2
            self.menu()
        else:
            self.hacer_jugada_jugador(mano_jugador, mano_casa, apuesta)

    def hacer_jugada_jugador(self, mano_jugador, mano_casa, apuesta):

    def hacer_jugada_casa(self, mano_jugador, mano_casa, apuesta):
        mano_casa.cartas[1].tapada = False


    def mostrar_mano(self, nombre, cartas):
        pass



