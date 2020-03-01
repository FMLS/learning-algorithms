import unittest

from algs.graph import Graph
from algs.search import Search
from algs.dfs import DepthFirstSearch

edges = [
    (0, 5),
    (4, 3),
    (0, 1),
    (9, 12),
    (6, 4),
    (5, 4),
    (0, 2),
    (11, 12),
    (9, 10),
    (0, 6),
    (7, 8),
    (9, 11),
    (5, 3),
]


class SearchTestCase(unittest.TestCase):

    def test_search(self):
        graph = Graph(13)
        for edge in edges:
            graph.add_edge(*edge)

        search = Search(graph, 9, DepthFirstSearch)
        for i in range(graph.vertex_count):
            if search.marked(i):
                print('{} '.format(i), )
        print()

        if search.count() != graph.vertex_count:
            print('NOT')
        print("connected")
