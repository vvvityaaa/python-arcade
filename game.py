import boards
import bad_guys
import poodle

# needed for the game itself
import sys, pygame


class Game:

    def __init__(self):
        # create and setup the game
        pygame.init()

    def event(self, event):
            if event.type == pygame.QUIT:
                sys.exit()
            #filling screen
            size = (width, height) = (320, 240)
            speed = [2, 2]
            screen = pygame.display.set_mode(size)
            black = 18, 18, 18
            screen.fill(black)

def main():
    game = Game();
    while 1:
        for event in pygame.event.get():
            game.event(event)


if __name__=="__main__":
    main()