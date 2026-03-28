import pygame
import sys

pygame.init()
screen = pygame.display.set_mode((500, 400))
pygame.display.set_caption("a game screen")

doingitsjob = True
while doingitsjob:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            doingitsjob = False

    screen.fill((10, 92, 200))

    pygame.draw.rect(screen, (0, 256, 0), (59, 100, 400, 200))

    pygame.display.flip()

pygame.quit()
sys.exit()
#alba2c00l