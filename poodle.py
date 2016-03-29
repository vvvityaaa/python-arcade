import pygame

MOVE_SPEED = 7
POODLE_WIDTH = 22
POODLE_HEIGHT = 32
COLOR = "#888888"


class Poodle(pygame.sprite.Sprite):

    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.xvel = 0
        self.startX = x
        self.startY = y
        self.image = pygame.Surface((POODLE_WIDTH, POODLE_HEIGHT))
        self.image.fill(pygame.Color(COLOR))
        self.rect = pygame.Rect(x, y, POODLE_WIDTH, POODLE_HEIGHT)

    def update(self,  left, right):
        if left:
            self.xvel = -MOVE_SPEED

        if right:
            self.xvel = MOVE_SPEED

        if not(left or right):
            self.xvel = 0

        self.rect.x += self.xvel

    def draw(self, screen):
        screen.blit(self.image, (self.rect.x, self.rect.y))