import pygame

# Inicializar Pygame
pygame.init()

# Definir dimensiones de la ventana del juego
ANCHO = 800
ALTO = 600

# Crear la ventana del juego
ventana = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Mi Juego")

# Cargar una imagen
imagen = pygame.image.load("C:\Users\dsaav\OneDrive\Workspaces\Taller de Pygame\Ejemplos\jugador.png")

nuevo_ancho = 200  # Nuevo ancho deseado
nuevo_alto = 200  # Nuevo alto deseado
imagen_redimensionada = pygame.transform.scale(imagen, (nuevo_ancho, nuevo_alto))

# Posición inicial de la imagen en la ventana
x = 100
y = 100

# Bucle principal del juego
while True:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            exit()

    # Dibujar la imagen en la ventana de juego
    ventana.blit(imagen_redimensionada, (x, y))

    # Actualizar la pantalla
    pygame.display.flip()