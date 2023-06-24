# Práctica: Incorporación de mecánicas de juego al proyecto del videojuego

class Enemigo:
    def __init__(self):
        print("Enemigo creado")
        
    def mover(self):
        print("Moviendo enemigo")
        
class Obstáculo:
    def __init__(self):
        print("Obstáculo creado")
        
    def colisionar(self):
        print("Colisión con obstáculo")
        
class ObjetoRecolectable:
    def __init__(self):
        print("Objeto recolectable creado")
        
    def recolectar(self):
        print("Objeto recolectado")
        
# Incorporar las mecánicas de juego en el proyecto
enemigo = Enemigo()
obstaculo = Obstáculo()
objeto_recolectable = ObjetoRecolectable()

enemigo.mover()
obstaculo.colisionar()
objeto_recolectable.recolectar()

"""
En este código, se definen las clases "Enemigo", "Obstáculo" y "ObjetoRecolectable", 
cada una con sus respectivos métodos y lógica asociada. Luego, se crea una instancia de 
cada una de estas clases y se llama a los métodos correspondientes para simular las mecánicas de juego.
"""