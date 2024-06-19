import pygame                             
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLUT import *   
from OpenGL.GLU import gluOrtho2D         

# Inicializa todos os módulos do Pygame
pygame.init()                             
# Configurações da janela
# Define a resolução da janela (largura, altura)
display = (800, 600)                      
# Cria uma janela com buffer duplo (DOUBLEBUF) e suporte a OpenGL
pygame.display.set_mode(display, DOUBLEBUF | OPENGL) 

# Configurações do OpenGL
# Define a cor de fundo da tela (preto) com transparência total
glClearColor(0.0, 0.0, 0.0, 1.0)          
# Define a matriz de projeção como a matriz atual
glMatrixMode(GL_PROJECTION)               
# Reseta a matriz de projeção para a matriz identidade
glLoadIdentity()                          
# Define uma projeção ortográfica 2D com as dimensões da janela
gluOrtho2D(0, display[0], 0, display[1])  
# Define a matriz de modelagem/visualização como a matriz atual
glMatrixMode(GL_MODELVIEW)                
# Reseta a matriz de modelagem/visualização para a matriz identidade
glLoadIdentity()                          
# Define o tamanho dos pontos que serão desenhados como 5 pixels
glPointSize(5.0)                          

# Variáveis para armazenar a cor e o tamanho dos pontos
point_color = (1.0, 0.0, 0.0)  # Cor inicial dos pontos (vermelho)
point_size = 5.0               # Tamanho inicial dos pontos
shape = GL_POINTS              # Forma inicial (pontos)

# Cria uma lista vazia para armazenar as coordenadas dos pontos clicados
points = []                               

# Função principal do loop
# Define a função principal do programa
def main():                               
    global point_size, point_color, shape
    # Variável para controlar o loop principal
    running = True                       
    # Início do loop principal
    while running:                        
        # Itera sobre todos os eventos do Pygame
        for event in pygame.event.get():  
            # Se o evento for de sair (fechar a janela)
            if event.type == QUIT:        
                # Define running como False para encerrar o loop
                running = False           
            # Se o evento for de clicar o mouse
            elif event.type == MOUSEBUTTONDOWN: 
                # Obtém as coordenadas do clique do mouse
                x, y = event.pos          
                # Adiciona o ponto à lista (invertendo a coordenada y)
                points.append((x, display[1] - y)) 
            # Se o evento for pressionar uma tecla
            elif event.type == KEYDOWN:
                # Se a tecla for "c", muda a cor dos pontos
                if event.key == K_c:
                    point_color = (0.0, 1.0, 0.0)  # Muda a cor para verde
                # Se a tecla for "+", aumenta o tamanho dos pontos
                elif event.key == K_PLUS or event.key == K_EQUALS:
                    point_size += 1.0
                # Se a tecla for "-", diminui o tamanho dos pontos
                elif event.key == K_MINUS:
                    point_size = max(1.0, point_size - 1.0)
                # Se a tecla for "r", reseta a lista de pontos
                elif event.key == K_r:
                    points.clear()
                # Se a tecla for "t", muda a forma para triângulos
                elif event.key == K_t:
                    shape = GL_TRIANGLES
                # Se a tecla for "q", muda a forma para quadrados (quadriláteros)
                elif event.key == K_q:
                    shape = GL_QUADS
                # Se a tecla for "p", muda a forma para pontos
                elif event.key == K_p:
                    shape = GL_POINTS
                    
        # Limpa a tela
        glClear(GL_COLOR_BUFFER_BIT)  
        
        # Define o tamanho dos pontos
        glPointSize(point_size)
        # Define a cor dos pontos
        glColor3f(*point_color)

        # Inicia a definição de pontos a serem desenhados
        if shape == GL_POINTS:
            glBegin(GL_POINTS)
        elif shape == GL_TRIANGLES:
            glBegin(GL_TRIANGLES)
        elif shape == GL_QUADS:
            glBegin(GL_QUADS)
        elif shape == GL_LINE_STRIP:
            glBegin(GL_LINE_STRIP)
        else:
            glBegin(GL_POINTS)

        # Itera sobre todos os pontos armazenados
        for point in points:              
            # Define um vértice (ponto) nas coordenadas armazenadas
            glVertex2f(point[0], point[1]) 
        # Finaliza a definição dos pontos
        glEnd()                           

        # Desenha linhas conectando os pontos na ordem em que foram clicados
        if len(points) > 1:
            glColor3f(1.0, 1.0, 1.0)  # Define a cor das linhas (branco)
            glBegin(GL_LINE_STRIP)    # Inicia a definição de uma linha contínua
            for point in points:
                glVertex2f(point[0], point[1])
            glEnd()

        # Atualiza a tela com o que foi desenhado
        pygame.display.flip()
        # Aguarda por 10 milissegundos para controlar a taxa de atualização
        pygame.time.wait(10)  

    # Encerra o Pygame
    pygame.quit()                         

# Verifica se o script está sendo executado diretamente
if __name__ == "__main__":
    # Chama a função principal para iniciar o programa       
    main()                       
