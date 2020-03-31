import pygame
#importa funciones especificas de la libreria pygame

class Tablero():

    # Funcion constrcutra (se ejecuta al crear el objeto)
    def __init__(self,window,color=(255,255,255)):

        self._window = window

        self._window

        self

        self._color = color

        self._recuadros = []
    

    def _newLine(self,init,final,grosor):
        pygame.draw.line(self._window,self._color,init,final,grosor)


    def _draw_lines(self):
        self._newLine((30,30),(630,30),3)
        self._newLine((30,30),(30,630),3)
        self._newLine((30,630),(630,630),3)
        self._newLine((630,30),(630,630),3)
        self._newLine((230,60),(230,600),1)
        self._newLine((430,60),(430,600),1)
        self._newLine((60,240),(600,240),1)
        self._newLine((60,420),(600,420),1)


    #Funcion publica para actualizar el estado del tablero
    def Update(self):

        self._draw_lines()


class Game():


    def __init__(self,widht,height,players):

        self.widht = widht
        self.height = height



        self.window = pygame.display.set_up((self.widht,self.height))


    def update(self):

        pygame.display.update()