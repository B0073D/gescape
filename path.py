__author__ = 'Tim Suess'


from operator import itemgetter


class Dijkstra:
    map = []  # Navigation map
    map_bounds = []  # Boundary of map
    origin = []  # Starting point
    target = []  # End point
    best_path = []  # Best path based on calculated navigation map

    def __init__(self, input_map, origin, target):
        self.map = input_map
        self.map_bounds = [len(input_map[0][0]), len(input_map[0])]
        self.origin = origin
        self.target = target
        self.best_path = []

    @staticmethod
    def is_even(integer):
        if integer % 2 == 0:
            return True
        else:
            return False

    # Generates navigation map
    def generate_map(self):
        # Creates initial navigation map of 'infinite' values
        map_raw = []
        for i in xrange(self.map_bounds[0]):
            tmp_row = []
            for ii in xrange(self.map_bounds[1]):
                tmp_row.append(-1)
            map_raw.append(tmp_row)

        # Creates list of unvisited nodes
        nodes_unvisited = []
        for i in xrange(self.map_bounds[0]):
            for ii in xrange(self.map_bounds[1]):
                nodes_unvisited.append([i, ii])

        # Set target node to 0 weight
        map_raw[self.target[1]][self.target[0]] = 0

        # Sets initial nodes up for navigation
        current_node = self.target[:]
        initial_nodes = self.get_unvisited_neighbours(current_node, nodes_unvisited, self.map_bounds)
        for i in initial_nodes:
            map_raw[i[1]][i[0]] = 1
        nodes_unvisited.remove(current_node)

        # Generates navigation map
        running_loop = 1
        while running_loop == 1:
            # Creates set of nodes to pick from
            picker_set = []
            for i in nodes_unvisited:
                if map_raw[i[1]][i[0]] > 0:
                    picker_set.append([i[0], i[1], map_raw[i[1]][i[0]]])

            # Marks neighbouring valid nodes with smallest value
            if picker_set:
                picker_set.sort(key=itemgetter(2))
                current_node = picker_set[0]
                node_neighbours = self.get_unvisited_neighbours(current_node, nodes_unvisited, self.map_bounds)
                for node in node_neighbours:  # Checks neighbouring nodes and overwrites them if smaller or unwritten
                    if map_raw[node[1]][node[0]] < 0:
                        map_raw[node[1]][node[0]] = map_raw[current_node[1]][current_node[0]] + 1
                        if self.map[1][node[1]][node[0]] == 1:
                            map_raw[current_node[1]][current_node[0]] += 100
                    elif map_raw[node[1]][node[0]] > map_raw[current_node[1]][current_node[0]] + 1:
                        map_raw[node[1]][node[0]] = map_raw[current_node[1]][current_node[0]] + 1
                        if self.map[1][node[1]][node[0]] == 1:
                            map_raw[current_node[1]][current_node[0]] += 100
                nodes_unvisited.remove([current_node[0], current_node[1]])
            else:
                # Stops loop if there are no more valid nodes
                running_loop = 0
        self.map[0] = map_raw

    # Gets the best path based on navigation map generated by generate_map
    def get_path(self):
        current_node = self.origin
        self.best_path = []
        self.best_path.append(current_node)
        running = 1
        while running == 1:
            neighbours = []
            neighbours_tmp = self.get_neighbours(current_node, self.map_bounds)
            for i in neighbours_tmp:
                neighbours.append([i[0], i[1], self.map[0][i[1]][i[0]]])
            neighbours.sort(key=itemgetter(2))
            if neighbours[0][2] > self.map[0][current_node[1]][current_node[0]]:
                running = 0
            elif [neighbours[0][0], neighbours[0][1]] == self.target:
                running = 0
            else:
                current_node = [neighbours[0][0], neighbours[0][1]]
                self.best_path.append(current_node)
        return self.best_path

    # Gets valid node neighbours from set of unvisited nodes
    def get_unvisited_neighbours(self, current, unvisited, map_bounds):
        final_set = []
        for i in self.get_neighbours(current, map_bounds):
            if i in unvisited:
                final_set.append(i)
        return final_set

    def get_neighbours(self, current, map_bounds):
        tmp_set = []
        # Create first raw set to check
        if self.is_even(current[1]):  # Provides raw neighbours depending on row in hex tile set
            tmp_set.append([current[0], current[1]-1])
            tmp_set.append([current[0], current[1]+1])
            tmp_set.append([current[0]+1, current[1]])
            tmp_set.append([current[0]-1, current[1]])
            tmp_set.append([current[0]-1, current[1]-1])
            tmp_set.append([current[0]-1, current[1]+1])
        else:
            tmp_set.append([current[0], current[1]-1])
            tmp_set.append([current[0], current[1]+1])
            tmp_set.append([current[0]-1, current[1]])
            tmp_set.append([current[0]+1, current[1]])
            tmp_set.append([current[0]+1, current[1]-1])
            tmp_set.append([current[0]+1, current[1]+1])

        # Checks validity of raw set
        final_set = []
        for i in tmp_set:
            if i[0] >= 0 and i[1] >= 0 and i[0] < map_bounds[0] and i[1] < map_bounds[1]:
                if self.map[1][i[1]][i[0]] == 0:
                    final_set.append(i)
        return final_set

    # Returns the next hop for a node based on the navigation map
    def get_next_hop(self, current_node):
        neighbours = []
        neighbours_tmp = self.get_neighbours(current_node, self.map_bounds)
        for i in neighbours_tmp:
            neighbours.append([i[0], i[1], self.map[0][i[1]][i[0]]])
        neighbours.sort(key=itemgetter(2))
        if neighbours[0][2] > self.map[0][current_node[1]][current_node[0]]:
            return []
        elif [neighbours[0][0], neighbours[0][1]] == self.target:
            return []
        else:
            return [neighbours[0][0], neighbours[0][1]]
