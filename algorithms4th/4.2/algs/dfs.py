from algs.graph import Graph


class DepthFirstSearch:
    def __init__(self, graph, start):
        """

        :param Graph graph:
        :param start:
        """
        self._marked = [False for i in range(graph.vertex_count)]
        self.count = 0
        self._dfs(graph, start)

    def _dfs(self, graph, vertex):
        self._marked[vertex] = True
        self.count += 1
        for v in graph.adj_vertex(vertex):
            if not self._marked[v]:
                self._dfs(graph, v)

    def marked(self, w):
        """

        :rtype: bool
        :param int w:
        :return:
        """
        return self._marked[w]


