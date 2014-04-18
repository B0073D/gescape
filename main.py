__author__ = 'Tim Suess'
# This is a genetic algorithm and Dijkstra test.

import pygame
import settings
import sys

#pygame init things
pygame.init()
screen = pygame.display.set_mode(settings.size)
myfont = pygame.font.SysFont("monospace", 15)
label = myfont.render(str(0), 1, (255, 255, 0))


def main():  # Main loop
    print "ZOMG a loop!"
    while 1:
        screen.fill(settings.black)
        pygame.draw.circle(screen, settings.red, (10,10), 2)
        pygame.display.flip()

        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        sys.exit()

if __name__ == "__main__":
    main()