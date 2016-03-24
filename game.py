import boards
import bad_guys
import poodle

# needed for the game itself
import sys, pygame

# create and setup the game
pygame.init()
size = width, height = 320, 240
speed = [2, 2]
screen = pygame.display.set_mode(size)
black = 18, 18, 18

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    # just display a black box
    screen.fill(black)
