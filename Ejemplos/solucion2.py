# Práctica: Desarrollo de un juego sencillo utilizando la estructura básica

class MiJuego(Juego):
    def iniciar(self):
        print("Iniciando el juego...")
        # Lógica de inicio del juego
    
    def ejecutar(self):
        print("Ejecutando el juego...")
        # Lógica principal del juego
        
    def finalizar(self):
        print("Finalizando el juego...")
        # Lógica de finalización del juego
        
# Crear una instancia de MiJuego
mi_juego = MiJuego()

# Llamar a los métodos de la instancia
mi_juego.iniciar()
mi_juego.ejecutar()
mi_juego.finalizar()

"""
En este código, se crea una nueva clase llamada "MiJuego" que hereda de la clase "Juego". 
Luego, se implementan los métodos iniciar, ejecutar y finalizar con la lógica correspondiente para el juego. 
Finalmente, se crea una instancia de "MiJuego" llamada "mi_juego" y se llaman a los métodos correspondientes 
para iniciar, ejecutar y finalizar el juego.
"""