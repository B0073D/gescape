__author__ = 'Tim Suess'
# This is a genetic algorithm and Dijkstra test.

import pygame
import settings
import sys
import path
import random

#pygame init things
pygame.init()
screen = pygame.display.set_mode(settings.size)
myfont = pygame.font.SysFont("monospace", 15)
label = myfont.render(str(0), 1, (255, 255, 0))


def main():  # Main loop
    navmap = []
    tmp_map = []
    for i in xrange(settings.width):
        tmp_row = []
        for ii in xrange(settings.height):
            tmp_row.append(0)
        tmp_map.append(tmp_row)
    navmap.append(tmp_map)
    tmp_map = []
    for i in xrange(settings.width):
        tmp_row = []
        for ii in xrange(settings.height):
            if random.randint(1, 25) == 1:
                tmp_row.append(1)
            else:
                tmp_row.append(0)
        tmp_map.append(tmp_row)
    navmap.append(tmp_map)
    # print navmap
    navmap = path.Dijkstra(navmap, settings.origin, settings.target)
    navmap.generate_map()
    print navmap.map

    while 1:
        screen.fill(settings.black)
        for row in range(settings.width):
            for node in range(settings.height):
                node_weight = navmap.map[0][row][node]

                if node_weight < 255:
                    colour = node_weight, 0, 0
                elif node_weight < 510:
                    colour = 255, node_weight - 255, 0
                elif node_weight < 765:
                    colour = 255, 255, node_weight - 510
                else:
                    colour = 0, 0, 0
                if navmap.map[1][row][node] == 0:
                    pygame.draw.circle(screen, colour, (row, node), 1)

        for node in navmap.get_path():
            pygame.draw.circle(screen, settings.green, (node[0], node[1]), 1)

        pygame.display.flip()

        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        sys.exit()

if __name__ == "__main__":
    main()

