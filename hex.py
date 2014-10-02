__author__ = 'Tim Suess'
# Grid to Hex translator

import math


class Translator:
    pixels_to_units = 0  # Ratio of pixels to units, units being the distance between tile centers
    offset = [0, 0]  # Starting offset
    height_with_ratio = 0  # distance on the y axis between two rows

    def __init__(self, ratio, offset):
        self.pixels_to_units = ratio
        self.offset = offset
        self.height_with_ratio = int(math.sqrt(self.pixels_to_units ** 2 + (self.pixels_to_units / 2) ** 2))

    # Return translated map
    def map(self, input_map):
        __even = 1
        output_map = []
        __rowcount = 0

        for row in input_map:
            __node_count = 0
            if __even == 1:
                for node in row:
                    output_map.append([int(__node_count * self.pixels_to_units + self.offset[0]),
                                      int(__rowcount * self.height_with_ratio + self.offset[1]),
                                      node])
                    __node_count += 1
                    __even = 0
            elif __even == 0:
                for node in row:
                    output_map.append([int(__node_count * self.pixels_to_units + self.offset[0] + self.pixels_to_units / 2),
                                      int(__rowcount * self.height_with_ratio + self.offset[1]),
                                      node])
                    __node_count += 1
                    __even = 1
            __rowcount += 1

        return output_map

    # Returns a translated individual set of coordinates
    def individual(self, input_coordinates):
        # Translates coordinates depending on if odd or even row
        if input_coordinates[1] % 2 == 0:
            output_coordinates = [int(input_coordinates[0] * self.pixels_to_units + self.offset[0]),
                                  int(input_coordinates[1] * self.height_with_ratio + self.offset[1])]
        else:
            output_coordinates = [int(input_coordinates[0] * self.pixels_to_units + self.offset[0] + self.pixels_to_units / 2),
                                  int(input_coordinates[1] * self.height_with_ratio + self.offset[1])]
        return output_coordinates
