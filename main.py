import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *

vertices = (
    (1, 1),
    (1, -1),
    (-1, -1),
    (-1, 1),
)

edge = (
    (0, 1),
    (1, 2),
    (2, 3),
    (3, 0),
)

def square_draw():
    glBegin(GL_LINES)
    for i in edge:
        for vertexs in i:
            glVertex2iv(vertices[vertexs])
    glEnd()

def main():
    pygame.init()
    display = (800, 600)

    pygame.display.set_mode(display, DOUBLEBUF|OPENGL)
    pygame.display.set_caption('Projeto Computação Grafica')
    
    gluPerspective(40, display[0]/display[1], 1, 10)
    glTranslatef(0.0, 0.0, -5)

    while (True):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
                
        square_draw()
        pygame.display.flip()

main()