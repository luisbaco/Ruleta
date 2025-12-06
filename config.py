# config.py
"""
Módulo de configuración para la simulación de ruleta de casino.
Contiene constantes de color, dimensiones, y pagos de apuestas.
"""

# Dimensiones de pantalla
WIDTH, HEIGHT = 1000, 800
CENTER = (WIDTH // 2, HEIGHT // 2)
RADIUS = 300

# Colores RGB
GREEN = (0, 128, 0)
RED = (200, 0, 0)
BLACK = (20, 20, 20)
WHITE = (255, 255, 255)
GOLD = (255, 215, 0)
GRAY = (100, 100, 100)
BG_COLOR = (34, 139, 34)  # Fondo verde estilo casino

# Alias para compatibilidad con ruleta.py
ROJO = RED
NEGRO = BLACK
VERDE = GREEN

# Fuente (pygame_gui manejará UI por separado)
FONT_NAME = 'arial'

# Ruleta
NUMEROS = list(range(37))
NUMERO_ORDEN = [
    0, 32, 15, 19, 4, 21, 2, 25, 17, 34,
    6, 27, 13, 36, 11, 30, 8, 23, 10, 5,
    24, 16, 33, 1, 20, 14, 31, 9, 22, 18,
    29, 7, 28, 12, 35, 3, 26
]
SECTORES = len(NUMERO_ORDEN)
ANGLE_PER_SECTOR = 360 / SECTORES

# Pagos (ratios de ganancia)
PAYOUTS = {
    "pleno": 35,
    "color": 1,
    "par_impar": 1,
    "docena": 2,
    "columna": 2,
    "falta_pasa": 1
}

# Inicialización del jugador
SALDO_INICIAL = 1000
APUESTA_MINIMA = 10

# Fotogramas por segundo para el bucle principal
FPS = 60
