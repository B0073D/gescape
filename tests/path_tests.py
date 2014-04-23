__author__ = 'Tim Suess'

from nose.tools import *
import path

# Map layout
test_map_small = [[[-1, -1, -1, -1],
                   [-1, -1, -1, -1],
                   [-1, -1, -1, -1],
                   [-1, -1, -1, -1]],
                  [[0, 0, 0, 0],
                   [1, 1, 0, 0],
                   [0, 0, 0, 1],
                   [0, 0, 0, 0]]]

# Expected result map
result_map_small = [[[6, 5, 4, 4],
                     [-1, -1, 3, 4],
                     [4, 3, 2, -1],
                     [3, 2, 1, 0]],
                    [[0, 0, 0, 0],
                     [1, 1, 0, 0],
                     [0, 0, 0, 1],
                     [0, 0, 0, 0]]]


# Tests generate_map()
def test_generate_map():
    navigator = path.Dijkstra(test_map_small, [0, 0], [3, 3])
    navigator.generate_map()

    assert_equal(result_map_small, navigator.map)


# Tests get_path()
def test_get_path():
    navigator = path.Dijkstra(test_map_small, [0, 0], [3, 3])
    navigator.generate_map()
    returned_path = navigator.get_path()
    compare_path = [[0, 0], [1, 0], [2, 0], [2, 1], [2, 2], [2, 3]]
    assert_equal(returned_path, compare_path)



