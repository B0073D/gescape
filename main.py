__author__ = 'Tim Suess'
# This is a genetic algorithm and Dijkstra test.

import pygame
import settings
import sys
import path
import random
import hex
import math

#pygame init things
pygame.init()
screen = pygame.display.set_mode(settings.size)
myfont = pygame.font.SysFont("monospace", 15)
label = myfont.render(str(0), 1, (255, 255, 0))
clock = pygame.time.Clock()

# Init hex coord translator
diplomat = hex.Translator(settings.hex_pixels_to_units, settings.hex_starting_offset)
origin_translated = diplomat.individual(settings.origin)
target_translated = diplomat.individual(settings.target)


def main():  # Main loop
    navmap = []
    tmp_map = []

    # Generates input map
    for i in xrange(settings.map_width):
        tmp_row = []
        for ii in xrange(settings.map_height):
            tmp_row.append(0)
        tmp_map.append(tmp_row)
    navmap.append(tmp_map)

    # Generates obstacle map
    tmp_map = []
    for i in xrange(settings.map_width):
        tmp_row = []
        for ii in xrange(settings.map_height):
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
        print 'navmap:'
        print navmap.map

    # Generate path
    pathnodes = navmap.get_path()

    hex_navmap = diplomat.map(navmap.map[0])
    if settings.debug > 0:
        print 'hex_navmap:'
        print hex_navmap


    units = []
    while 1:

        if units == []:
            while len(units) < 10:
                if settings.debug > 0:
                    print 'Units'
                    print units
                unit_location = [random.randint(0, settings.map_width - 1), random.randint(0, settings.map_height - 1)]
                if settings.debug > 0:
                    print 'Unit Location:'
                    print unit_location
                if navmap.map[1][unit_location[1]][unit_location[0]] != 1:
                    units.append(unit_location)

        tmp_units = []
        for unit in units:
            nexthop = navmap.get_next_hop(unit)
            if nexthop:
                tmp_units.append(nexthop)

        units = tmp_units[:]

        # Black screen fill
        screen.fill(settings.black)

        # Draw navigation map
        for node in hex_navmap:
            node_weight = node[2]
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
            # print node
            hex_lines = []
            for point in range(0, 6):
                angle = 2 * math.pi / 6 * (point + 0.5)
                x_point = node[0] + math.sqrt((settings.hex_pixels_to_units / 2) ** 2 + (diplomat.height_with_ratio / 3) ** 2) * math.cos(angle)
                y_point = node[1] + math.sqrt((settings.hex_pixels_to_units / 2) ** 2 + (diplomat.height_with_ratio / 3) ** 2) * math.sin(angle)
                hex_lines.append([int(x_point), int(y_point)])

            if settings.debug > 0:
                print hex_lines

            # pygame.draw.circle(screen, colour, (node[0], node[1]), 6)
            pygame.draw.polygon(screen, colour, hex_lines)

        # Draw path
        for node in pathnodes:
            node_translated = diplomat.individual(node)
            pygame.draw.circle(screen, settings.green, (node_translated[0], node_translated[1]), 3)

        # Draw units
        for unit in units:
            unit_translated = diplomat.individual(unit)
            pygame.draw.circle(screen, settings.booted, (unit_translated[0], unit_translated[1]), 3)
        # Draw start and end of path
        pygame.draw.circle(screen, settings.green, (origin_translated[0], origin_translated[1]), 7)
        pygame.draw.circle(screen, settings.green, (target_translated[0], target_translated[1]), 7)

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
