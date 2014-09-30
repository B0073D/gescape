__author__ = 'Tim Suess'

from nose.tools import *
import hex

test_map_small = [[[-1, -1, -1, -1],
                   [-1, -1, -1, -1],
                   [-1, -1, -1, -1],
                   [-1, -1, -1, -1]],
                  [[0, 0, 0, 0],
                   [1, 1, 0, 0],
                   [0, 0, 0, 1],
                   [0, 0, 0, 0]]]

result_map_small = [[10, 10, [-1, -1, -1, -1]],
                    [25, 10, [-1, -1, -1, -1]],
                    [40, 10, [-1, -1, -1, -1]],
                    [55, 10, [-1, -1, -1, -1]],
                    [17, 26, [0, 0, 0, 0]],
                    [32, 26, [1, 1, 0, 0]],
                    [47, 26, [0, 0, 0, 1]],
                    [62, 26, [0, 0, 0, 0]]]


def test_individual():
    diplomat = hex.Translator(15, [10, 10])

    assert_equal(diplomat.individual([14, 14]), [220, 234])


def test_map():
    diplomat = hex.Translator(15, [10, 10])

    assert_equal(diplomat.map(test_map_small), result_map_small)