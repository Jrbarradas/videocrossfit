import pygame
import random
import sys

# Inicializa o Pygame
pygame.init()

# Configurações da tela
screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
width, height = pygame.display.get_surface().get_size()
pygame.display.set_caption("Ganso Travesso")

# Carrega a imagem do ganso
goose = pygame.image.load("goose.png")
goose_rect = goose.get_rect()

# Velocidade e direção do ganso
speed = 8
direction = [random.choice([-1, 1]), random.choice([-1, 1])]

# Loop principal
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
            running = False

    # Movimenta o ganso
    goose_rect.x += direction[0] * speed
    goose_rect.y += direction[1] * speed

    # Verifica colisão com as bordas
    if goose_rect.left < 0 or goose_rect.right > width:
        direction[0] *= -1
    if goose_rect.top < 0 or goose_rect.bottom > height:
        direction[1] *= -1

    # Atualiza a tela
    screen.fill((255, 255, 255))  # Fundo branco
    screen.blit(goose, goose_rect)
    pygame.display.flip()
    pygame.time.delay(30)

pygame.quit()
sys.exit()