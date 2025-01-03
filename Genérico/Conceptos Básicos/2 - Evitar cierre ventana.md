
Para evitar que se cierre la ventana al instante, hacemos un bucle while que contendrá toda la lógica del juego, usa un bucle for que recorre todos los eventos de la librería pygame. para registrar todo lo que hace  el jugador, como mover el ratón, pulsar teclas, etc.

Con una variable inicializada en True que controla el bucle while. 

***pygame.even.get()*** en en bucle for es lo que controla lo que hace el jugador.

Por último, verificamos si se activa el evento ***pygame.QUIT*** el cual se activa cuando el usuario intenta cerrar la ventana haciendo click en la x o con alt + F4 y si eso sucede, cerramos el while poniendo la variable en False. Ejemplo:

```python
run = True  
  
while run == True:  
    for event in pygame.event.get():  
        if event.type == pygame.QUIT:
	        run = False
```





