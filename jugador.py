"""
Módulo que define la clase Jugador para la simulación de ruleta.
Gestiona el saldo del jugador, las apuestas activas y las ganancias.
"""

class Jugador:
    def __init__(self, saldo_inicial):
        """
        Inicializa un nuevo jugador con un saldo dado.
        """
        self.saldo = saldo_inicial
        self.apuestas = []  # Lista de apuestas activas

    def apostar(self, tipo, valor, monto):
        """
        Registra una apuesta si el jugador tiene saldo suficiente y el valor es válido.

        :param tipo: Tipo de apuesta (ej: 'pleno', 'color', etc.)
        :param valor: Valor apostado (número, 'rojo', 'par', etc.)
        :param monto: Cantidad de dinero apostada
        :return: True si la apuesta fue registrada, False en caso de error
        """
        if monto <= 0:
            return False

        if self.saldo < monto:
            return False

        # Validación específica por tipo
        if tipo == "pleno":
            if not (0 <= valor <= 36):
                return False
        elif tipo == "color":
            if valor not in ["rojo", "negro"]:
                return False
        elif tipo == "paridad":
            if valor not in ["par", "impar"]:
                return False
        elif tipo == "mitad":
            if valor not in ["1-18", "19-36"]:
                return False
        else:
            # Tipo no reconocido
            return False

        self.apuestas.append({'tipo': tipo, 'valor': valor, 'monto': monto})
        self.saldo -= monto
        return True

    def limpiar_apuestas(self):
        """
        Elimina todas las apuestas activas.
        """
        self.apuestas.clear()

    def ganar(self, monto):
        """
        Suma las ganancias al saldo.

        :param monto: Cantidad ganada
        """
        self.saldo += monto

    def obtener_apuestas(self):
        """
        Devuelve la lista de apuestas activas.
        """
        return self.apuestas

    def obtener_saldo(self):
        """
        Devuelve el saldo actual del jugador.
        """
        return self.saldo
