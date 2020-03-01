from algs.graph import Graph


class Paths:
    def __init__(self, graph, start_vertex):
        """
        在graph 中找出所有起点为s的路径
        :param Graph graph:
        :param start_vertex:
        """
        self.start = start_vertex
        self.graph = graph
        self.marked = [False for i in range(graph.vertex_count)]
        self.edge_to = [None for i in range(graph.vertex_count)]
        self._dfs(start_vertex)

    def _dfs(self, v):
        self.marked[v] = True
        for w in self.graph.adj_vertex(v):
            if not self.marked[w]:
                self.edge_to[w] = v
                self._dfs(w)

    def has_path_to(self, v):
        """
        是否存在从s到v的路径
        :rtype: bool
        :param int v:
        :return:
        """

        return self.marked[v]

    def path_to(self, v):
        """
        s->v 路径, 不存在返回None
        :rtype: list|None
        :param v:
        :return:
        """
        path = []
        x = v
        while x != self.start:
            path.append(x)
            x = self.edge_to[x]
        path.append(self.start)
        return path[::-1]
