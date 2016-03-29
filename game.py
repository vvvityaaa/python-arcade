import boards
import bad_guys
import poodle

# needed for the game itself
import sys
import pygame


class Game:

    def __init__(self):
        # create and setup the game
        pygame.init()

    def event(self, event):
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_LEFT:
                left = True
            if event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT:
                right = True

            if event.type == pygame.KEYUP and event.key == pygame.K_RIGHT:
                right = False
            if event.type == pygame.KEYUP and event.key == pygame.K_LEFT:
                left = False


def main():
    game = Game()
    size = (640, 480)
    speed = [2, 2]
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("Poodle Jump")
    black = 18, 18, 18
    screen.fill(black)
    boards.build_boards(screen)
    pood = poodle.Poodle(55, 55)
    left = right = False
    while 1:
        for event in pygame.event.get():
            game.event(event)


if __name__ == "__main__":
    main()