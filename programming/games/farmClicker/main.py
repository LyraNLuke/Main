import pygame
import sys

# -- Init --
pygame.init()
WIDTH, HEIGHT = 1280, 720
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Farm Clicker")
clock = pygame.time.Clock()

# -- Game Loop --
while True:
    # 1. Handle input
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
            
    # 2. Update game state
    # nothing yet
    
    # 3. Render
    screen.fill((100, 180, 100)) # green background
    pygame.display.flip()
    
    clock.tick(60) # limit to 60 FPS