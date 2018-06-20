import sys

class graph(object):
    
    def __init__(self):
        first_line = sys.stdin.readline()
        self._v_num = int(first_line)
        #邻接表实现
        self._adj = [[] for i in range(self._v_num)]
        self._e_num = 0
        while True:
            v, w = map(int, ((sys.stdin.readline()).strip('\n')).split())
            if v < 0 or w < 0:
                break
            
            self.addEdge(v, w)

    @property
    def V(self):
        return self._v_num

    @property
    def E(self):
        return self._e_num

    def addEdge(self, v, w):
        self._adj[v].append(w)
        self._adj[w].append(v)
        self._e_num += 1

    def adj(self, v):
        return self._adj[v]

class search(object):
    def __init__(self, G, s):
        pass
    
    def marked(self, v):
        pass
    
    def count(self):
        pass

class DepthFirstSearch(object):

    def __init__(self, G, s):
        self.count = 0
        self.marked = [False for i in range(G.V)]
        self.edgeTo = [-1 for i in range(G.V)]
        self.s = s
        self.dfs(G, s)
    
    def dfs(self, G, v):
        self.marked[v] = True
        self.count += 1
        print(v)
        for w in G.adj(v):
            if (not self.marked[w]):
                self.edgeTo[w] = v
                self.dfs(G, w)
    
    def hasPathTo(self, v):
        print(self.marked)
        return self.marked[v]
    
    def pathTo(self, v):
        if not self.hasPathTo(v):
            return None
        
        res = []
        x = v
        while True:
            if x == self.s:
                res.append(x)
                break 
            res.append(x)
            x = self.edgeTo[x]
        res.reverse()


class BreadthFirstSearch(object):

    def __init__(self, G, s):
        self.count = 0
        self.marked = [False for i in range(G.V)]
        self.edgeTo = [-1 for i in range(G.V)]
        self.s = s
        self.bfs(G, s)
    
    def bfs(self, G, v):
        fifo = []
        self.marked[v] = True
        fifo.append(v)
        while len(fifo) > 0:
            current = fifo.pop()
            print(current)
            for i in G.adj(current):
                if not self.marked[i]:
                    self.marked[i] = True
                    fifo.append(i)
    

class Paths(object):

    def __init__(self, G, s):
        pass

    def hasPathTo(self, v):
        pass
    
    def pathTo(self, v):
        pass

if '__main__' == __name__:
    gra = graph()
    print(gra.V)
    print(gra.E)
    print(gra._adj)
    dfs = DepthFirstSearch(gra, 0)
    print('path to 6', dfs.pathTo(6))

    bfs = BreadthFirstSearch(gra, 0)
