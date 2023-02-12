import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *

verticies = (
    (1, -1, -1),
    (1, 1, -1),
    (-1, 1, -1),
    (-1, -1, -1),
    (1, -1, 1),
    (1, 1, 1),
    (-1, -1, 1),
    (-1, 1, 1)
)

edges = (
    (0,1),
    (0,3),
    (0,4),
    (2,1),
    (2,3),
    (2,7),
    (6,3),
    (6,4),
    (6,7),
    (5,1),
    (5,4),
    (5,7)
)

def square3d():
    glBegin(GL_LINES)
    for edge in edges:
        for vertex in edge:
            glVertex3fv(verticies[vertex])
    glEnd()

    
def text(x, y, text):            
    font = pygame.font.SysFont('arial', 20)                                    
    textSurface = font.render(text, True, (255, 255, 66, 255), (0, 0, 0))
    textData = pygame.image.tostring(textSurface, "RGBA", True)
    glWindowPos2d(x, y)
    glDrawPixels(textSurface.get_width(), textSurface.get_height(), GL_RGBA, GL_UNSIGNED_BYTE, textData)

def main():
    pygame.init()
    display = (1200, 600)

    screen = pygame.display.set_mode(display, DOUBLEBUF|OPENGL)
    pygame.display.set_caption('Projeto Computação Grafica')
    
    glMatrixMode(GL_PROJECTION)
    gluPerspective(45, display[0]/display[1], 0.1, 50.0)

    glMatrixMode(GL_MODELVIEW)
    glTranslatef(0, 0, -5)
    current_action = ''

    while (True):
        for event in pygame.event.get():
            
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
                
            if pygame.key.get_pressed()[K_r]:
                current_action = 'ROTACIONANDO...'
                glRotatef(5, 1, 0, 1)
            
            elif pygame.key.get_pressed()[K_j]:
                glRotatef(5, 0, -1, 0)
            elif pygame.key.get_pressed()[K_i]:
                glRotatef(5, 0, 1, 0)
            elif pygame.key.get_pressed()[K_l]:
                glRotatef(5, -1, 0, 0)
            elif pygame.key.get_pressed()[K_k]:
                glRotatef(5, 1, 0, 0)
                
            elif pygame.key.get_pressed()[K_s]:
                glTranslatef(0, -1, 0)
            elif pygame.key.get_pressed()[K_w]:
                glTranslatef(0, 1, 0)
            elif pygame.key.get_pressed()[K_a]:
                glTranslatef(-1, 0, 0)
            elif pygame.key.get_pressed()[K_d]:
                glTranslatef(1, 0, 0)
            elif pygame.key.get_pressed()[K_f]:
                glTranslatef(0, 0, 1)
            elif pygame.key.get_pressed()[K_g]:
                glTranslatef(0, 0, -1)
                
            elif pygame.key.get_pressed()[K_q]:
                current_action = 'AUMENTANDO...'
                glScalef(1.1 , 1.1, 1.1)
                
            elif pygame.key.get_pressed()[K_e]:
                current_action = 'DIMINUINDO...'
                glScalef(0.8 , 0.8, 0.8)
                
            elif pygame.key.get_pressed()[K_v]:
                gluLookAt(0, 0, 0, 1, 0, 1, 0, 0, 1)
            else:
                current_action = ''
                    
                
        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
        square3d()
        text(1, 550, current_action)
        pygame.display.flip()

main()