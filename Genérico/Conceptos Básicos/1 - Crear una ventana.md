
Hay que especificar primero el ancho y luego el alto. Además de usar pygame.display con los Por ejemplo:

```python
width = 800
height = 600
```


No tiene por qué llamarse en inglés, son variables al final, lo importante es el orden primero el ancho, luego el alto. Obviamente que el nombre de la variable tenga sentido.

Después creamos una varialbe que contiene la función de la ventana: ***pygame.display.setmode((parametros_de_la_ventana))***

Por ejemplo con los parámetros anteriores:

```python
width = 800  
height = 600  
pygame.display.set_mode((width, height))
```

