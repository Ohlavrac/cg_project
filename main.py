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

def square_colored():
    glColor3f(1, 0, 0)
    glBegin(GL_TRIANGLE_FAN)
    glVertex2f(1, 1)
    glVertex2f(1, -1)
    glVertex2f(-1, -1)
    glVertex2f(-1, 1)
    glEnd()

def square_draw():
    glColor3f(1, 0, 0)
    glBegin(GL_LINES)
    for i in edge:
        for vertexs in i:
            glVertex2iv(vertices[vertexs])
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
    
    gluPerspective(100, display[0]/display[1], 1, 10)
    glTranslatef(0.0, 0.0, -5)
    current_action = ''
    

    while (True):
        for event in pygame.event.get():
            
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
                
            if pygame.key.get_pressed()[K_r]:
                current_action = 'ROTACIONANDO...'
                glRotatef(5, 0, 0, 1)
                
            elif pygame.key.get_pressed()[K_s]:
                glTranslatef(0, -1, 0)
            elif pygame.key.get_pressed()[K_w]:
                glTranslatef(0, 1, 0)
            elif pygame.key.get_pressed()[K_a]:
                glTranslatef(-1, 0, 0)
            elif pygame.key.get_pressed()[K_d]:
                glTranslatef(1, 0, 0)
                
            elif pygame.key.get_pressed()[K_q]:
                current_action = 'AUMENTANDO...'
                glScalef(1.1 , 1.1, 1.1)
                
            elif pygame.key.get_pressed()[K_e]:
                current_action = 'DIMINUINDO...'
                glScalef(0.8 , 0.8, 0.8)
            else:
                current_action = ''
                
        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
        square_colored()
        text(1, 550, current_action)
        pygame.display.flip()

main()