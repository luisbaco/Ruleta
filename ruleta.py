"""
Módulo que define la clase Ruleta, que representa gráficamente la rueda de ruleta.
"""

import pygame
import math
import random
from config import WIDTH, HEIGHT, RADIUS

CENTER = (WIDTH // 2, HEIGHT // 2)
ANGLE_PER_SECTOR = 360 / 37

NUMERO_ORDEN = [
    0, 32, 15, 19, 4, 21, 2, 25, 17, 34, 6,
    27, 13, 36, 11, 30, 8, 23, 10, 5, 24,
    16, 33, 1, 20, 14, 31, 9, 22, 18, 29,
    7, 28, 12, 35, 3, 26
]

RED = (200, 0, 0)
BLACK = (0, 0, 0)
GREEN = (0, 150, 0)
WHITE = (255, 255, 255)

class Ruleta:
    def __init__(self):
        self.angulo_actual = 0
        self.velocidad = 0
        self.numero_resultado = None
        self.girando = False
        self.bola_angulo = 0
        self.bola_velocidad = 0

    def lanzar_bola(self):
        self.velocidad = random.uniform(15, 20)
        self.bola_velocidad = self.velocidad * 2.5
        self.numero_resultado = random.choice(NUMERO_ORDEN)
        self.girando = True

    def actualizar(self):
        if self.girando:
            self.angulo_actual += self.velocidad
            self.bola_angulo += self.bola_velocidad

            self.velocidad *= 0.98
            self.bola_velocidad *= 0.96

            if self.velocidad < 0.1:
                self.girando = False
                self.ajustar_angulo_final()

    def ajustar_angulo_final(self):
        indice_ganador = NUMERO_ORDEN.index(self.numero_resultado)
        angulo_objetivo = (360 - (indice_ganador * ANGLE_PER_SECTOR)) % 360
        self.angulo_actual = angulo_objetivo
        self.bola_angulo = angulo_objetivo  # sincroniza también la bola

    def obtener_resultado(self):
        return self.numero_resultado

    def animacion_finalizada(self):
        return not self.girando

    def dibujar(self, pantalla):
        for i, numero in enumerate(NUMERO_ORDEN):
            angulo_inicio = math.radians(i * ANGLE_PER_SECTOR + self.angulo_actual)
            angulo_fin = math.radians((i + 1) * ANGLE_PER_SECTOR + self.angulo_actual)

            color = (
                GREEN if numero == 0 else
                RED if numero in {
                    1, 3, 5, 7, 9, 12, 14, 16, 18,
                    19, 21, 23, 25, 27, 30, 32, 34, 36
                } else BLACK
            )

            x1, y1 = CENTER
            x2 = CENTER[0] + RADIUS * math.cos(angulo_inicio)
            y2 = CENTER[1] + RADIUS * math.sin(angulo_inicio)
            x3 = CENTER[0] + RADIUS * math.cos(angulo_fin)
            y3 = CENTER[1] + RADIUS * math.sin(angulo_fin)

            pygame.draw.polygon(pantalla, color, [(x1, y1), (x2, y2), (x3, y3)])

            fuente = pygame.font.SysFont(None, 28)
            numero_texto = fuente.render(str(numero), True, WHITE)
            angulo_texto = math.radians((i + 0.5) * ANGLE_PER_SECTOR + self.angulo_actual)
            x_text = CENTER[0] + (RADIUS * 0.92) * math.cos(angulo_texto)
            y_text = CENTER[1] + (RADIUS * 0.92) * math.sin(angulo_texto)
            pantalla.blit(numero_texto, numero_texto.get_rect(center=(x_text, y_text)))

        # Bola animada (si la ruleta está en marcha o ya hay resultado)
        if self.numero_resultado is not None:
            radio_bola = RADIUS * 0.65
            angulo_bola_rad = math.radians(self.bola_angulo)
            bola_x = CENTER[0] + radio_bola * math.cos(angulo_bola_rad)
            bola_y = CENTER[1] + radio_bola * math.sin(angulo_bola_rad)
            pygame.draw.circle(pantalla, WHITE, (int(bola_x), int(bola_y)), 10)
