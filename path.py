__author__ = 'Tim Suess'

# Map layout
example_map = [[[-1, -1, -1, -1],
[-1, -1, -1, -1],
[-1, -1, -1, -1],
[-1, -1, -1, -1]],
[[1, 0, 1, 0],
[0, 1, 0, 0],
[0, 0, 0, 0],
[0, 0, 0, 0]]]

from operator import itemgetter


class Dijkstra:
    map = []
    map_bounds = []
    origin = []
    target = []

    def __init__(self, map, origin, target):
        self.map = map
        self.map_bounds = [len(map[0]), len(map[0][0])]
        self.origin = origin
        self.target = target

    def generate_map(self):
        map_raw = []
        for i in xrange(self.map_bounds[0]):
            tmp_row = []
            for ii in xrange(self.map_bounds[1]):
                tmp_row.append(-1)
            map_raw.append(tmp_row)

        map_obstacles = self.map[1]

        nodes_unvisited = []
        for i in xrange(self.map_bounds[0]):
            for ii in xrange(self.map_bounds[1]):
                nodes_unvisited.append([i, ii])

        # Set target node to 0 weight
        map_raw[self.target[0]][self.target[1]] = 0

        running_loop = 1
        current_node = self.target[:]
        initial_nodes = self.get_unvisited_neighbours(current_node, nodes_unvisited, self.map_bounds)
        for i in initial_nodes:
            map_raw[i[0]][i[1]] = 1
        nodes_unvisited.remove(current_node)

        running_loop = 1
        while running_loop == 1:
            picker_set = []
            for i in nodes_unvisited:
                if map_raw[i[0]][i[1]] > 0:
                    picker_set.append([i[0], i[1], map_raw[i[0]][i[1]]])
            if picker_set != []:
                picker_set.sort(key=itemgetter(2))
                current_node = picker_set[0]
                print current_node
                node_neighbours = self.get_unvisited_neighbours(current_node, nodes_unvisited, self.map_bounds)
                for node in node_neighbours:
                    if map_raw[node[0]][node[1]] < 0:
                        map_raw[node[0]][node[1]] = map_raw[current_node[0]][current_node[1]] + 1
                        if self.map[1][node[0]][node[1]] == 1:
                            map_raw[current_node[0]][current_node[1]] += 100
                    elif map_raw[node[0]][node[1]] > map_raw[current_node[0]][current_node[1]] + 1:
                        map_raw[node[0]][node[1]] = map_raw[current_node[0]][current_node[1]] + 1
                        if self.map[1][node[0]][node[1]] == 1:
                            map_raw[current_node[0]][current_node[1]] += 100
                nodes_unvisited.remove([current_node[0], current_node[1]])
            else:
                running_loop = 0
        print map_raw
        self.map[0] = map_raw

    def get_unvisited_neighbours(self, current, unvisited, map_bounds):
        tmp_set = []
        # Create first raw set to check
        tmp_set.append([current[0], current[1]-1])
        tmp_set.append([current[0], current[1]+1])
        tmp_set.append([current[0]-1, current[1]])
        tmp_set.append([current[0]+1, current[1]])

        final_set = []
        for i in tmp_set:
            if i in unvisited:
                if i[0] >= 0 and i[1] >= 0 and i[0] < map_bounds[0] and i[1] < map_bounds[1]:
                    final_set.append(i)
        print "Final set:"
        print final_set
        return final_set

def test():
    test_map = Dijkstra(example_map, [3, 3], [0, 0])
    test_map.generate_map()
    print test_map.map