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
clock = pygame.time.Clock()


def main():  # Main loop
    navmap = []
    tmp_map = []

    # Generates input map
    for i in xrange(settings.width):
        tmp_row = []
        for ii in xrange(settings.height):
            tmp_row.append(0)
        tmp_map.append(tmp_row)
    navmap.append(tmp_map)

    # Generates obstacle map
    tmp_map = []
    for i in xrange(settings.width):
        tmp_row = []
        for ii in xrange(settings.height):
            if random.randint(1, settings.obstacle_ratio) == 1:
                tmp_row.append(1)
            else:
                tmp_row.append(0)
        tmp_map.append(tmp_row)
    navmap.append(tmp_map)

    # Generates navigation map
    navmap = path.Dijkstra(navmap, settings.origin, settings.target)
    navmap.generate_map()
    if settings.debug > 0:
        print navmap.map

    # Generate path
    pathnodes = navmap.get_path()

    while 1:
        # Black screen fill
        screen.fill(settings.black)

        # Draw navigation map
        for row in range(settings.width):
            for node in range(settings.height):
                node_weight = navmap.map[0][row][node]
                if node_weight < 0:
                    colour = 0, 0, 255
                elif node_weight < 255:
                    colour = node_weight, 0, 0
                elif node_weight < 510:
                    colour = 255, node_weight - 255, 0
                elif node_weight < 765:
                    colour = 255, 255, node_weight - 510
                else:
                    colour = 0, 0, 0

                # Draw obstacles
                if navmap.map[1][row][node] == 0:
                    pygame.draw.circle(screen, colour, (row, node), 1)

        # Draw path
        for node in pathnodes:
            pygame.draw.circle(screen, settings.green, (node[0], node[1]), 1)

        # Draw start and end of path
        pygame.draw.circle(screen, settings.green, (settings.origin[0], settings.origin[1]), 2)
        pygame.draw.circle(screen, settings.green, (settings.target[0], settings.target[1]), 2)

        # Makes sure the simulation doesn't run faster than 60fps
        clock.tick(60)

        # Flip (render) display
        pygame.display.flip()

        # Handles input
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        sys.exit()

# __main__ loop
if __name__ == "__main__":
    main()

