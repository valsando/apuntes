import pygame, sys
pygame.init()
# colores:
BLACK = 0,0,0
WHITE = 255,255,255
RED = 255,0,0
BLUE = 0,0,255
GREEN = 0,255,0

#tamaño de la pantalla
size = (800, 500)

screen = pygame.display.set_mode(size)


while True:
    for event in pygame.event.get():
            #print(event)
        if event.type == pygame.QUIT:
            sys.exit()
        #color de fondo
    screen.fill(GREEN)
                    ##ZONA DE DIBUJO ##
    pygame.draw.line(screen, BLACK, [0,200], [600,200], 10)

        #actualizar la pantalla
    pygame.display.flip()
