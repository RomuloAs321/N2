import pygame  
# Importa a biblioteca Pygame para a criação de jogos e multimídia

from pygame.locals import *
# Importa todas as constantes e funções locais do Pygame                           

from OpenGL.GL import *
# Importa todas as funções e constantes do OpenGL relacionadas à renderização               

from OpenGL.GLUT import *   
# Importa todas as funções e constantes do GLUT (OpenGL Utility Toolkit)                   

from OpenGL.GLU import gluOrtho2D         
# Importa a função gluOrtho2D da GLU (OpenGL Utility Library) para definir projeção ortográfica              

pygame.init()                             
# Inicializa todos os módulos do Pygame

display = (800, 600)                      
# Define a resolução da janela (largura, altura)

pygame.display.set_mode(display, DOUBLEBUF | OPENGL) 
# Cria uma janela com buffer duplo (DOUBLEBUF) e suporte a OpenGL

glClearColor(0.0, 0.0, 0.0, 1.0)          
# Define a cor de fundo da tela (preto) com transparência total

glMatrixMode(GL_PROJECTION)               
# Define a matriz de projeção como a matriz atual

glLoadIdentity()                          
# Reseta a matriz de projeção para a matriz identidade

gluOrtho2D(0, display[0], 0, display[1])  
# Define uma projeção ortográfica 2D com as dimensões da janela

glMatrixMode(GL_MODELVIEW)                
# Define a matriz de modelagem/visualização como a matriz atual

glLoadIdentity()                          
# Reseta a matriz de modelagem/visualização para a matriz identidade

def draw_horse(x, y, scale=1.0):
    # Função para desenhar um cavalo

    glPushMatrix()           
    # Salva a matriz atual

    glTranslatef(x, y, 0)    
    # Translada o cavalo para a posição (x, y)

    glScalef(scale, scale, 1)  
    # Escala o cavalo

    glColor3f(0.55, 0.27, 0.07)  
    # Define a cor do corpo (marrom)

    glBegin(GL_POLYGON)       
    # Começa a definição de um polígono

    glVertex2f(-40, 0)        
    # Define o primeiro vértice do polígono

    glVertex2f(40, 0)         
    # Define o segundo vértice do polígono

    glVertex2f(40, 30)        
    # Define o terceiro vértice do polígono

    glVertex2f(-40, 30)       
    # Define o quarto vértice do polígono

    glEnd()                   
    # Termina a definição do polígono

    glColor3f(0.55, 0.27, 0.07)  
    # Define a cor da cabeça (marrom)

    glBegin(GL_POLYGON)       
    # Começa a definição de um polígono

    glVertex2f(30, 30)        
    # Define o primeiro vértice do polígono

    glVertex2f(50, 30)        
    # Define o segundo vértice do polígono

    glVertex2f(50, 50)        
    # Define o terceiro vértice do polígono

    glVertex2f(30, 50)        
    # Define o quarto vértice do polígono

    glEnd()                   
    # Termina a definição do polígono

    glColor3f(0.55, 0.27, 0.07)  
    # Define a cor das orelhas (marrom)

    glBegin(GL_TRIANGLES)     
    # Começa a definição de um triângulo

    glVertex2f(45, 50)        
    # Define o primeiro vértice do triângulo

    glVertex2f(50, 60)        
    # Define o segundo vértice do triângulo

    glVertex2f(50, 50)        
    # Define o terceiro vértice do triângulo

    glEnd()                   
    # Termina a definição do triângulo

    glBegin(GL_TRIANGLES)     
    # Começa a definição de um triângulo

    glVertex2f(35, 50)        
    # Define o primeiro vértice do triângulo

    glVertex2f(30, 60)        
    # Define o segundo vértice do triângulo

    glVertex2f(30, 50)        
    # Define o terceiro vértice do triângulo

    glEnd()                   
    # Termina a definição do triângulo

    glColor3f(0.55, 0.27, 0.07)  
    # Define a cor das pernas (marrom)

    glBegin(GL_POLYGON)       
    # Começa a definição de um polígono

    glVertex2f(-30, 0)        
    # Define o primeiro vértice do polígono

    glVertex2f(-20, 0)        
    # Define o segundo vértice do polígono

    glVertex2f(-20, -30)      
    # Define o terceiro vértice do polígono

    glVertex2f(-30, -30)      
    # Define o quarto vértice do polígono

    glEnd()                   
    # Termina a definição do polígono

    glBegin(GL_POLYGON)       
    # Começa a definição de um polígono

    glVertex2f(20, 0)         
    # Define o primeiro vértice do polígono

    glVertex2f(30, 0)         
    # Define o segundo vértice do polígono

    glVertex2f(30, -30)       
    # Define o terceiro vértice do polígono

    glVertex2f(20, -30)       
    # Define o quarto vértice do polígono

    glEnd()                   
    # Termina a definição do polígono

    glBegin(GL_POLYGON)       
    # Começa a definição de um polígono

    glVertex2f(-10, 0)        
    # Define o primeiro vértice do polígono

    glVertex2f(0, 0)          
    # Define o segundo vértice do polígono

    glVertex2f(0, -30)        
    # Define o terceiro vértice do polígono

    glVertex2f(-10, -30)      
    # Define o quarto vértice do polígono

    glEnd()                   
    # Termina a definição do polígono

    glBegin(GL_POLYGON)       
    # Começa a definição de um polígono

    glVertex2f(10, 0)         
    # Define o primeiro vértice do polígono

    glVertex2f(20, 0)         
    # Define o segundo vértice do polígono

    glVertex2f(20, -30)       
    # Define o terceiro vértice do polígono

    glVertex2f(10, -30)       
    # Define o quarto vértice do polígono

    glEnd()                   
    # Termina a definição do polígono

    glPopMatrix()             
    # Restaura a matriz anterior

def main():                               
    # Função principal do loop

    running = True                       
    # Define uma variável de controle para o loop principal
    
    while running:                        
        # Loop principal do programa
        
        for event in pygame.event.get():  
            # Itera sobre todos os eventos do Pygame
            
            if event.type == QUIT:        
                # Se o evento for de saída (fechar a janela)
                
                running = False           
                # Define running como False para encerrar o loop

        glClear(GL_COLOR_BUFFER_BIT)      
        # Limpa a tela

        draw_horse(400, 300, 1.0)
        # Desenha o cavalo na posição (400, 300) com escala 1.0

        pygame.display.flip()             
        # Atualiza a tela com o que foi desenhado
        
        pygame.time.wait(10)              
        # Aguarda por 10 milissegundos para controlar a taxa de atualização

    pygame.quit()                         
    # Encerra o Pygame

if __name__ == "__main__":                
    # Verifica se o script está sendo executado diretamente
    
    main()                                
    # Chama a função principal para iniciar o programa
