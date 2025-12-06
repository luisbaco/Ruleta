# bola.py
"""
Módulo que gestiona la animación de la bola en la ruleta.
Simula un movimiento circular decreciente hasta detenerse sobre el número ganador.
"""

import math
import random
from config import CENTER, RADIUS, ANGLE_PER_SECTOR, NUMERO_ORDEN


class Bola:
    def __init__(self):
        """
        Inicializa la bola fuera de movimiento.
        """
        self.angulo = 0
        self.radio_actual = RADIUS - 20
        self.velocidad = 0
        self.girando = False
        self.posicion = CENTER

    def iniciar(self):
        """
        Comienza la animación de la bola.
        """
        self.angulo = random.uniform(0, 360)
        self.velocidad = random.uniform(20, 30)
        self.girando = True
        self.radio_actual = RADIUS - 20

    def actualizar(self, ruleta_angulo, ruleta_girando):
        """
        Actualiza la posición de la bola en relación a la ruleta.

        :param ruleta_angulo: Ángulo actual de la ruleta.
        :param ruleta_girando: Si la ruleta está girando.
        """
        if self.girando:
            self.angulo += self.velocidad
            self.velocidad *= 0.96  # Frena la bola
            if self.velocidad < 0.5:
                self.girando = False
            self.radio_actual -= 0.3  # Se acerca al centro

            if self.radio_actual < 40:
                self.radio_actual = 40  # Límite interno

        # Bola en ángulo relativo a la ruleta
        total_angulo = self.angulo - ruleta_angulo
        rad = math.radians(total_angulo)
        x = CENTER[0] + math.cos(rad) * self.radio_actual
        y = CENTER[1] + math.sin(rad) * self.radio_actual
        self.posicion = (int(x), int(y))

    def dibujar(self, pantalla):
        """
        Dibuja la bola en pantalla.

        :param pantalla: Superficie de pygame.
        """
        import pygame
        pygame.draw.circle(pantalla, (255, 255, 255), self.posicion, 8)

    def esta_girando(self):
        """
        Indica si la bola aún está girando.

        :return: True si girando, False si parada.
        """
        return self.girando
