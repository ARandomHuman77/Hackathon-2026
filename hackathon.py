import pygame, sys
from pygame.locals import QUIT

WIDTH = 400
HEIGHT = 400

WHITE = (255, 255, 255)

#hi 

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Testing')

clock = pygame.time.Clock()


print ("testing if this saves")


while True:
    clock.tick(60)

    # Fill the screen with the background color... this will cover any previous drawings...
    screen.fill(WHITE)

    
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit() # Exits the program gracefully without freezing
            sys.exit()


    pygame.display.flip()