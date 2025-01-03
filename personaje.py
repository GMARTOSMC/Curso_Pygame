import pygame
import constantes

class Personaje:
    # x e y son las coordenadas en las que inicializamos el personaje
    def __init__(self, x, y):
        # pygame.Rect para crear el rectángulo que será nuestro personaje.
        self.forma = pygame.Rect(0, 0, constantes.ANCHO_PERSONAJE,
                                       constantes.ALTO_PERSONAJE)
        # Para que al inicializar se mueva a las coordenadas que le demos
        self.forma.center = (x,y)

    # Para dibujar nuestro personaje

    def dibujar (self, interfaz):
        pygame.draw.rect(interfaz, constantes.COLOR_PERSONAJE, self.forma)
