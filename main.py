import pygame
import pygame_gui
from config import WIDTH, HEIGHT, FPS
from jugador import Jugador
from ruleta import Ruleta
from apuestas import Apuesta
from interfaz import Interfaz

def main():
    pygame.init()
    pantalla = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Simulador de Ruleta")
    reloj = pygame.time.Clock()

    gestor_ui = pygame_gui.UIManager((WIDTH, HEIGHT))
    interfaz = Interfaz(pantalla, gestor_ui)

    jugador = Jugador(saldo_inicial=1000)
    interfaz.actualizar_saldo(jugador.saldo)

    ruleta = Ruleta()
    corriendo = True
    girando_ruleta = False
    apuesta_actual = None
    resultado_obtenido = None

    while corriendo:
        tiempo = reloj.tick(FPS) / 1000

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                corriendo = False

            if evento.type == pygame_gui.UI_BUTTON_PRESSED:
                if evento.ui_element == interfaz.boton_tirar and not girando_ruleta:
                    datos = interfaz.obtener_datos_apuesta()
                    if datos:
                        tipo, valor, monto = datos
                        if jugador.saldo < monto:
                            interfaz.mostrar_mensaje("Saldo insuficiente.")
                            continue

                        apuesta_actual = Apuesta(tipo, valor, monto)
                        jugador.realizar_apuesta(monto)
                        interfaz.actualizar_saldo(jugador.saldo)

                        ruleta.lanzar_bola()  # Inicia animación
                        girando_ruleta = True

            gestor_ui.process_events(evento)

        gestor_ui.update(tiempo)
        pantalla.fill((0, 100, 0))  # Fondo verde casino

        ruleta.actualizar()
        ruleta.dibujar(pantalla)

        if girando_ruleta and ruleta.animacion_finalizada():
            resultado_obtenido = ruleta.obtener_resultado()
            exito, ganancia = apuesta_actual.evaluar(resultado_obtenido)
            if exito:
                jugador.actualizar_saldo(ganancia)
            interfaz.actualizar_saldo(jugador.saldo)

            mensaje = (
                f"Resultado: {resultado_obtenido} | Ganancia: €{ganancia}"
                if exito else f"Resultado: {resultado_obtenido} | Perdiste €{apuesta_actual.monto}"
            )
            interfaz.mostrar_mensaje(mensaje)
            girando_ruleta = False

        gestor_ui.draw_ui(pantalla)
        pygame.display.flip()

    pygame.quit()

if __name__ == "__main__":
    main()
