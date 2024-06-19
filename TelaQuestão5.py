# Importa o módulo pygame para criar a aplicação
import pygame  
# Importa as constantes do pygame
from pygame.locals import *  
# Importa as funções OpenGL
from OpenGL.GL import *  
# Importa as funções OpenGL Utility
from OpenGL.GLU import *  

# Importa o módulo math para operações matemáticas
import math  
# Inicializa o Pygame
pygame.init()

# Configurações da janela
display = (800, 600)  # Define o tamanho da janela
 # Configura o modo da janela com OpenGL
pygame.display.set_mode(display, DOUBLEBUF | OPENGL) 
# Define a projeção ortográfica 2D
gluOrtho2D(0, display[0], 0, display[1])  

# Função para desenhar um círculo
def draw_circle(x, y, radius, num_segments):
    # Inicia o desenho de um triângulo
    glBegin(GL_TRIANGLE_FAN)  
    # Loop para desenhar os segmentos do círculo
    for i in range(num_segments):  
        # Calcula o ângulo do segmento atual
        theta = 2.0 * math.pi * i / num_segments  
        # Calcula a coordenada x do ponto no círculo
        dx = radius * math.cos(theta)  
        # Calcula a coordenada y do ponto no círculo
        dy = radius * math.sin(theta) 
         # Adiciona o ponto ao círculo
        glVertex2f(x + dx, y + dy) 
    # Finaliza o desenho do círculo
    glEnd()  

# Função para desenhar o pássaro
def draw_bird(x, y, size):
    # Corpo do pássaro
    # Define a cor para amarelo
    glColor3f(1.0, 1.0, 0.0)  
    # Desenha o corpo do pássaro como um círculo
    draw_circle(x, y, size, 100)  
    
    # Asa do pássaro
    # Define a cor para azul
    glColor3f(0.0, 0.0, 1.0)  
    # Inicia o desenho de triângulos
    glBegin(GL_TRIANGLES)  
    # Define o vértice central da asa
    glVertex2f(x, y)  
    # Define o vértice superior esquerdo da asa
    glVertex2f(x - size, y + size / 2)  
    # Define o vértice inferior esquerdo da asa
    glVertex2f(x - size, y - size / 2)  
    # Finaliza o desenho da asa
    glEnd()  
    
    # Bico do pássaro
    # Define a cor para laranja
    glColor3f(1.0, 0.5, 0.0)
    # Inicia o desenho de triângulos
    glBegin(GL_TRIANGLES) 
    # Define o vértice central do bico
    glVertex2f(x + size, y) 
    # Define o vértice superior direito do bico
    glVertex2f(x + size / 2, y + size / 4)  
     # Define o vértice inferior direito do bico
    glVertex2f(x + size / 2, y - size / 4) 
    # Finaliza o desenho do bico
    glEnd()  
    
    # Olho do pássaro
    # Define a cor para preto
    glColor3f(0.0, 0.0, 0.0) 
    # Desenha o olho do pássaro como um círculo
    draw_circle(x + size / 4, y + size / 4, size / 8, 20) 

# Função principal do loop
def main():
    # Define a variável para controlar o loop principal
    running = True  
    # Loop principal do programa
    while running:  
        # Loop para lidar com os eventos do pygame
        for event in pygame.event.get():  
            # Verifica se o evento é de fechar a janela
            if event.type == QUIT:  
                # Define a variável para encerrar o loop
                running = False  
        # Limpa o buffer de cor
        glClear(GL_COLOR_BUFFER_BIT)  
        # Desenha o pássaro no centro da tela com tamanho 50
        draw_bird(400, 300, 50)  
        # Atualiza a tela
        pygame.display.flip()  
        # Aguarda um curto período de tempo para controlar a taxa de atualização
        pygame.time.wait(10)  
    # Finaliza o pygame
    pygame.quit()  

if __name__ == "__main__":
    main()  # Chama a função principal se este script for executado como o programa principal