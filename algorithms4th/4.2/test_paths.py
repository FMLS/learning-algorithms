from unittest import TestCase

from algs.graph import Graph
from algs.paths import Paths

edges = [
    (0, 5),
    (2, 4),
    (2, 3),
    (1, 2),
    (0, 1),
    (3, 4),
    (3, 5),
    (0, 2),
]


class TestPaths(TestCase):

    def test_path(self):
        graph = Graph(6)
        for edge in edges:
            graph.add_edge(*edge)

        search = Paths(graph, 0)
        for v in range(graph.vertex_count):
            if search.has_path_to(v):
                print(search.path_to(v))

