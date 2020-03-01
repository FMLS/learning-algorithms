class Graph(object):
    def __init__(self, v):
        self.vertex_count = v
        self.edge_count = 0
        self.adj = [[] for i in range(v)]

    def add_edge(self, v, w):
        # self.adj[v].append(w)
        # self.adj[w].append(v)

        # 邻接表内元素的顺序会直接影响dfs的路径, 为了和书本上用例输出保持一致, 这里使用头插法
        self.adj[v].insert(0, w)
        self.adj[w].insert(0, v)
        self.edge_count += 1

    def adj_vertex(self, vertex):
        """
        返回和vertex相邻的所有顶点
        :param vertex:
        :return:
        """
        return self.adj[vertex]

    # 顶点度数
    @staticmethod
    def degree(graph, v):
        degree = 0
        for w in graph.adj_vertex(v):
            degree += 1
        return degree

    @staticmethod
    def max_degree(graph):
        """
        所有顶点最大度数

        :param graph:
        :return:
        """
        max_degree = 0
        for v in range(graph.vertex_count):
            if Graph.degree(graph, v) > max_degree:
                max_degree = Graph.degree(graph, v)
        return max_degree

    @staticmethod
    def avg_degree(graph):
        return 2 * graph.edge_count / graph.vertex_count

    @staticmethod
    def number_of_self_loops(graph):
        count = 0
        for v in graph.vertex_count:
            for w in graph.adj_vertex(v):
                if v == w:
                    count += 1
        return count
