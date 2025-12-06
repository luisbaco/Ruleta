# interfaz.py

import pygame
import pygame_gui
from config import WIDTH, HEIGHT

class Interfaz:
    def __init__(self, pantalla, gestor_ui):
        self.pantalla = pantalla
        self.gestor_ui = gestor_ui

        # Panel lateral para controles
        panel_rect = pygame.Rect(WIDTH - 260, 50, 220, 400)

        self.combo_tipo = pygame_gui.elements.UIDropDownMenu(
            options_list=[
                "Pleno", "Color", "Par/Impar", "Docena", "Columna", "Alta/Baja"
            ],
            starting_option="Pleno",
            relative_rect=pygame.Rect(panel_rect.left, panel_rect.top, 200, 30),
            manager=gestor_ui
        )

        self.input_valor = pygame_gui.elements.UITextEntryLine(
            relative_rect=pygame.Rect(panel_rect.left, panel_rect.top + 40, 200, 30),
            manager=gestor_ui
        )
        self.input_valor.set_text("17")

        self.input_monto = pygame_gui.elements.UITextEntryLine(
            relative_rect=pygame.Rect(panel_rect.left, panel_rect.top + 80, 200, 30),
            manager=gestor_ui
        )
        self.input_monto.set_text("10")

        self.boton_tirar = pygame_gui.elements.UIButton(
            relative_rect=pygame.Rect(panel_rect.left, panel_rect.top + 120, 200, 40),
            text="Tirar",
            manager=gestor_ui
        )

        self.texto_saldo = pygame_gui.elements.UILabel(
            relative_rect=pygame.Rect(panel_rect.left, panel_rect.top + 180, 200, 30),
            text="Saldo: €0",
            manager=gestor_ui
        )

        self.label_mensaje = pygame_gui.elements.UILabel(
            relative_rect=pygame.Rect(panel_rect.left, panel_rect.top + 230, 200, 100),
            text="",
            manager=gestor_ui
        )

    def obtener_datos_apuesta(self):
        """
        Retorna (tipo, valor, monto) si la entrada es válida; None si no lo es.
        """
        try:
            tipo = self.combo_tipo.selected_option.lower().replace("/", "_")
            valor = self.input_valor.get_text().strip()
            monto = int(self.input_monto.get_text())

            if tipo == "pleno" and not valor.isdigit():
                return None
            if tipo == "pleno" and not (0 <= int(valor) <= 36):
                return None
            if monto <= 0:
                return None

            return tipo, valor, monto
        except Exception:
            return None

    def actualizar_saldo(self, nuevo_saldo):
        self.texto_saldo.set_text(f"Saldo: €{nuevo_saldo}")

    def mostrar_mensaje(self, texto):
        self.label_mensaje.set_text(texto)
