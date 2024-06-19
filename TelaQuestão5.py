import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
import math

# Inicializa o Pygame
pygame.init()

# Configurações da janela
display = (800, 600)
pygame.display.set_mode(display, DOUBLEBUF | OPENGL)
gluOrtho2D(0, display[0], 0, display[1])

# Função para desenhar um círculo
def draw_circle(x, y, radius, num_segments):
    glBegin(GL_TRIANGLE_FAN)
    for i in range(num_segments):
        theta = 2.0 * math.pi * i / num_segments
        dx = radius * math.cos(theta)
        dy = radius * math.sin(theta)
        glVertex2f(x + dx, y + dy)
    glEnd()

# Função para desenhar o pássaro
def draw_bird(x, y, size):
    # Corpo do pássaro
    glColor3f(1.0, 1.0, 0.0)  # Amarelo
    draw_circle(x, y, size, 100)
    
    # Asa do pássaro
    glColor3f(0.0, 0.0, 1.0)  # Azul
    glBegin(GL_TRIANGLES)
    glVertex2f(x, y)
    glVertex2f(x - size, y + size / 2)
    glVertex2f(x - size, y - size / 2)
    glEnd()
    
    # Bico do pássaro
    glColor3f(1.0, 0.5, 0.0)  # Laranja
    glBegin(GL_TRIANGLES)
    glVertex2f(x + size, y)
    glVertex2f(x + size / 2, y + size / 4)
    glVertex2f(x + size / 2, y - size / 4)
    glEnd()
    
    # Olho do pássaro
    glColor3f(0.0, 0.0, 0.0)  # Preto
    draw_circle(x + size / 4, y + size / 4, size / 8, 20)

# Função principal do loop
def main():
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == QUIT:
                running = False

        glClear(GL_COLOR_BUFFER_BIT)
        
        draw_bird(400, 300, 50)  # Desenha o pássaro no centro da tela com tamanho 50

        pygame.display.flip()
        pygame.time.wait(10)

    pygame.quit()

if __name__ == "__main__":
    main()
