#importa la libreria pygame
import pygame
#importa funciones especificas de la libreria pygame
from pygame.locals import *
from pygame.time import*
#importa desde config todo
from config import *


#poner a correr el juego
def main():
    #ancho y alto
    width = 900
    height = 660
    title = "Tik Tak Toe"
    run = True
    #crea un reloj
    clock = Clock()
    # cuantas veces por segundo quiero actualizar
    fps = 30
    #pantalla
    window = pygame.display.set_mode((width,height))

    # titulo de la ventana
    pygame.display.set_caption(title)

    triqui = Tablero(window)
        

    while run:      

        triqui.Update()

        #me devuelve una lista de todos los eventos
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False


        #actualiza la pantalla
        pygame.display.update()
        #detenga el tiempo en un intervalo que permita que solo se ejecute esto 30 veces por segundo
        clock.tick(fps)

if __name__ == "__main__":
    main() 
    