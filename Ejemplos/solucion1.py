class Jugador:
    def __init__(self, nombre, puntos):
        self.nombre = nombre
        self.puntos = puntos
    
    def obtener_nombre(self):
        return self.nombre
    
    def incrementar_puntos(self, cantidad):
        self.puntos += cantidad


jugador2 = Jugador("María", 5)
print(jugador2.obtener_nombre())  # Salida: María

jugador2.incrementar_puntos(3)
print(jugador2.puntos)  # Salida: 8

""" 
En este código, se crea una nueva instancia de la clase "Jugador" llamada "jugador2" 
con el nombre "María" y 5 puntos. Luego se llama al método "obtener_nombre" de la instancia 
"jugador2" y se muestra el resultado en la consola (que debería ser "María"). 
A continuación, se llama al método "incrementar_puntos" de la instancia "jugador2" y se pasa 
un valor de 3 como argumento para incrementar los puntos. Por último, se imprime el valor 
actual de los puntos de la instancia "jugador2" en la consola (que debería ser 8).

"""