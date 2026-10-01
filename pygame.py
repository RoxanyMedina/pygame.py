import pygame

pygame.init()

janela = pygame.display.set_mode((400,300))
pygame.display.set_caption("Meu primeiro game")

# Cor RGB 0 a 255 para cada cor
COR_AZUL = (50, 120, 200)
COR_VERMELHO = (255, 0, 0)

# Posição do quadrado
quadrado_x = 180
quadraodo_y = 130
quadrado_largura = 40
quadrado_altura = 40

# Velocidade de movimento do quadrado (Em pixels por frame)
velocidade = 5
deve_continuar = True

# Criando um relogio para controlar a velocidade (FPS)
relogio = pygame.time.Clock()

# Loop do jogo
while deve_continuar:
    relogio.ttick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            deve_continuar = False

    teclas = pygame.key.get_pressed()

    if teclas[pygame.K_LEFT]:
        quadrado_x -= velocidade

    if teclas[pygame.K_RIGHT]:
        quadrado_x += velocidade

    if 