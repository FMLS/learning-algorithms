class Search:
    def __init__(self, graph, s, alg):
        """

        :param graph:
        :param int s: 起点
        """
        self.graph = graph
        self.s = s
        self.alg = alg(self.graph, s)

    def marked(self, v):
        """

        :param int v: 目标顶点
        :return:
        :rtype: bool
        """
        return self.alg.marked(v)

    def count(self):
        """
        与目标顶点连通的顶点总数
        :rtype: int
        :return:
        """
        return self.alg.count
