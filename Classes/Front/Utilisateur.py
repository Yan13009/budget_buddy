import pygame 
from pygame.locals import *

pygame.init()

BK = pygame.display.set_mode((1000, 700))
pygame.display.set_caption("Budget_buddy")
image = pygame.image.load('Classes/Images/background.jpg')
image = pygame.transform.scale(image, (1000, 700))



running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    BK.blit(image, (0, 0))
    pygame.display.flip()

