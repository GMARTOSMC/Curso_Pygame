# Importamos la librería pygame y los módulos que creamos
import pygame
import constantes
from personaje import Personaje

# Creo el objeto jugador y le paso las coordenadas

jugador = Personaje(250, 250)

# Para inicializar pygame

pygame.init()

# Creamos la ventana con las constantes que definimos en el fichero constantes.py

ventana = pygame.display.set_mode((constantes.ANCHO_VENTANA,
                                   constantes.ALTO_VENTANA))
# Para renombrar la ventana

pygame.display.set_caption('Curso Pygame')

# Bucle principal del juego

run = True

while run == True:

    # Dibujamos al personaje jugador usando la función dibujar() que creamos en el fichero personaje.py

    jugador.dibujar(ventana)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    # Para actualizar la pantalla con los cambios que se den
    pygame.display.update()
