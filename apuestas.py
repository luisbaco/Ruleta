# apuesta.py
"""
Módulo que define la clase Apuesta, encargada de evaluar diferentes tipos de apuestas
en una ruleta de casino.
"""

class Apuesta:
    def __init__(self, tipo, valor, monto):
        """
        Inicializa una apuesta.

        :param tipo: Tipo de apuesta (e.g., "número", "color", etc.).
        :param valor: Valor elegido para la apuesta (número, color, etc.).
        :param monto: Cantidad apostada.
        """
        self.tipo = tipo
        self.valor = valor
        self.monto = monto

    def evaluar(self, numero_ganador):
        """
        Evalúa si la apuesta es ganadora según el número de la ruleta.

        :param numero_ganador: Número que ha salido en la ruleta.
        :return: (bool, ganancia). True si se ganó la apuesta, junto a la ganancia obtenida.
        """
        if self.tipo == "número":
            if int(self.valor) == numero_ganador:
                return True, self.monto * 35  # Paga 35 a 1

        elif self.tipo == "color":
            rojo = {1, 3, 5, 7, 9, 12, 14, 16, 18,
                    19, 21, 23, 25, 27, 30, 32, 34, 36}
            negro = {2, 4, 6, 8, 10, 11, 13, 15, 17,
                     20, 22, 24, 26, 28, 29, 31, 33, 35}

            if self.valor == "rojo" and numero_ganador in rojo:
                return True, self.monto * 2
            elif self.valor == "negro" and numero_ganador in negro:
                return True, self.monto * 2

        elif self.tipo == "paridad":
            if numero_ganador == 0:
                return False, 0
            if self.valor == "par" and numero_ganador % 2 == 0:
                return True, self.monto * 2
            elif self.valor == "impar" and numero_ganador % 2 != 0:
                return True, self.monto * 2

        elif self.tipo == "docena":
            if self.valor == "1-12" and 1 <= numero_ganador <= 12:
                return True, self.monto * 3
            elif self.valor == "13-24" and 13 <= numero_ganador <= 24:
                return True, self.monto * 3
            elif self.valor == "25-36" and 25 <= numero_ganador <= 36:
                return True, self.monto * 3

        elif self.tipo == "columna":
            columna_1 = {1, 4, 7, 10, 13, 16, 19, 22, 25, 28, 31, 34}
            columna_2 = {2, 5, 8, 11, 14, 17, 20, 23, 26, 29, 32, 35}
            columna_3 = {3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36}

            if self.valor == "1ª columna" and numero_ganador in columna_1:
                return True, self.monto * 3
            elif self.valor == "2ª columna" and numero_ganador in columna_2:
                return True, self.monto * 3
            elif self.valor == "3ª columna" and numero_ganador in columna_3:
                return True, self.monto * 3

        return False, 0
