# Importamos la librería pygame y los módulos que creamos
import pygame
import constantes
import personaje

# Para inicializar pygame

pygame.init()

pygame.display.set_mode((constantes.ANCHO_VENTANA,
                         constantes.ALTO_VENTANA))
# Para renombrar la ventana

pygame.display.set_caption('Curso Pygame')

# Bucle principal del juego

run = True

while run == True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
