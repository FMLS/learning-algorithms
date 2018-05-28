#API 定义
class UF(object):
    def __init__(self, N):
        self.N = N
        self.id = [ i for i in range(N)]
        self._count = N

    def UF(self, N):
        pass

    def union(self, p, q):
        pID = self.find(p)
        qID = self.find(q)

        if pID == qID:
            return

        for i in range(self.N):
            if self.id[i] == pID:
                self.id[i] = qID

        self._count -= 1

    def find(self, p):
        return self.id[p]
    
    def quickFind(self, p):
        while self.id[p] != p:
            p = self.id[p]
        return p
    
    def quickUnion(self, p, q):
        pRoot = self.quickFind(p)
        qRoot = self.quickFind(q)
        if self.id[pRoot] == self.id[qRoot]:
            return
        
        self.id[pRoot] = qRoot
        self._count -= 1
    
    def quickConnected(self, p, q):
        return self.quickFind(p) == self.quickFind(q)

    def connected(self, p, q):
        return self.find(p) == self.find(q)

    @property
    def count(self):
        return self._count

if '__main__' == __name__:
    uf = UF(10)
    r = True
    while r:
        r = input()
        p, q = r.split(' ')
        p = int(p)
        q = int(q)
        if uf.quickConnected(p, q):
            continue
        #uf.union(p, q)
        uf.quickUnion(p, q)
        print('union {} <-> {}'.format(p, q))
        print('connected union count: {}'.format(uf.count))
