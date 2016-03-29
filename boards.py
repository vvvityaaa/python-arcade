import pygame

PLATFORM_WIDTH = 32
PLATFORM_HEIGHT = 32
PLATFORM_COLOR = "#FF6262"

level = [
       "-------------------------",
       "-                       -",
       "-                       -",
       "-                       -",
       "-            --         -",
       "-                       -",
       "--                      -",
       "-                       -",
       "-                   --- -",
       "-                       -",
       "-                       -",
       "-      ---              -",
       "-                       -",
       "-   -----------        -",
       "-                       -",
       "-                -      -",
       "-                   --  -",
       "-                       -",
       "-                       -",
       "-------------------------"]


def build_boards(screen):

    x = 0
    y = 0
    for row in level:
        for col in row:
            if col == "-":

                pf = pygame.Surface((PLATFORM_WIDTH, PLATFORM_HEIGHT))
                pf.fill(pygame.Color(PLATFORM_COLOR))
                screen.blit(pf, (x, y))

            x += PLATFORM_WIDTH
        y += PLATFORM_HEIGHT
        x = 0
