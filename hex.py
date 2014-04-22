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
    def map(self, inputmap):
        __even = 1
        outputmap = []
        __rowcount = 0

        for row in inputmap:
            __nodecount = 0
            if __even == 1:
                for node in row:
                    outputmap.append([int(__nodecount * self.pixels_to_units + self.offset[0]),
                                      int(__rowcount * self.height_with_ratio + self.offset[1]),
                                      node])
                    __nodecount += 1
                    __even = 0
            elif __even == 0:
                for node in row:
                    outputmap.append([int(__nodecount * self.pixels_to_units + self.offset[0] + self.pixels_to_units / 2),
                                      int(__rowcount * self.height_with_ratio + self.offset[1]),
                                      node])
                    __nodecount += 1
                    __even = 1
            __rowcount += 1

        return outputmap

    # Returns a translated individual set of coordinates
    def individual(self, input_coords):
        # Translates coordinates depending on if odd or even row
        if input_coords[1] % 2 == 0:
            output_coords = [int(input_coords[0] * self.pixels_to_units + self.offset[0]),
                             int(input_coords[1] * self.height_with_ratio + self.offset[1])]
        else:
            output_coords = [int(input_coords[0] * self.pixels_to_units + self.offset[0] + self.pixels_to_units / 2),
                             int(input_coords[1] * self.height_with_ratio + self.offset[1])]
        return output_coords