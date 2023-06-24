import pygame
import os

# Inicializar Pygame
pygame.init()

# Obtener la ruta absoluta del directorio actual
current_dir = os.path.dirname(os.path.abspath(__file__))

# Definir dimensiones de la ventana del juego
ANCHO = 800
ALTO = 600

# Crear la ventana del juego
ventana = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Mi Juego")

# Cargar imágenes y sonidos
fondo = pygame.image.load(os.path.join(current_dir, "fondo.jpg"))
jugador_img = pygame.image.load(os.path.join(current_dir, "jugador.jpg"))
enemigo_img = pygame.image.load(os.path.join(current_dir, "enemigo.jpg"))
sonido_disparo = pygame.mixer.Sound(os.path.join(current_dir, "disparo.mp3"))

# Definir clases de objetos del juego
class Jugador(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = jugador_img
        self.rect = self.image.get_rect()
        self.rect.center = (ANCHO // 2, ALTO - 50)
    
    def update(self):
        # Actualizar la posición del jugador
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.rect.x -= 5
        if keys[pygame.K_RIGHT]:
            self.rect.x += 5

class Enemigo(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = enemigo_img
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
    
    def update(self):
        # Actualizar la posición del enemigo
        self.rect.y += 2

# Crear grupos de sprites
jugador_grupo = pygame.sprite.Group()
enemigo_grupo = pygame.sprite.Group()

# Crear instancias de objetos del juego
jugador = Jugador()
jugador_grupo.add(jugador)

# Variables de juego
puntuacion = 0
reloj = pygame.time.Clock()

# Bucle principal del juego
jugando = True
while jugando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            jugando = False
        
        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_SPACE:
                # Realizar acción al presionar la tecla espacio (disparo, por ejemplo)
                sonido_disparo.play()

    # Actualizar el estado del juego
    jugador_grupo.update()
    enemigo_grupo.update()

    # Colisiones
    colisiones = pygame.sprite.spritecollide(jugador, enemigo_grupo, True)
    for enemigo in colisiones:
        puntuacion += 1
    
    # Dibujar elementos en la ventana del juego
    ventana.blit(fondo, (0, 0))
    jugador_grupo.draw(ventana)
    enemigo_grupo.draw(ventana)

    # Actualizar la ventana del juego
    pygame.display.flip()

    # Controlar la velocidad de actualización del juego
    reloj.tick(60)

# Finalizar Pygame
pygame.quit()
