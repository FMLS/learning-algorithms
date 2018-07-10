class maxPQ(object):

    def __init__(self, maxN):
        self.data = [None for i in range(0, maxN + 1)]
        self.N = 0
        self.maxN = maxN

    def insert(self, key):
        if self.N < self.maxN:
            self.N += 1
        self.data[self.N] = key
        self.swim(self.N)
    
    def max(self):
        return self.data[1]

    def delMax(self):
        dmax = self.data[1]
        self.data[1], self.data[self.N] = self.data[self.N], self.data[1]
        self.N -= 1
        self.data[self.N + 1] = None
        self.sink(1)
        
        return dmax


    def isEmpty(self):
        pass

    @property
    def size(self):
        return self.N
    
    def swim(self, k):
        # k > 1 必须放前边利用短路原理, self.data[0] = None 无法与int比较
        while(k > 1 and self.data[k] > self.data[k // 2]):
            self.data[k // 2], self.data[k] = self.data[k], self.data[k // 2]
            k = k // 2
    
    def sink(self, k):
        while(2 * k <= self.N):
            j = k * 2
            if (j < self.N and self.data[j] < self.data[j + 1]):
                j += 1
            
            if not self.data[j] > self.data[k]:
                break
            self.data[j], self.data[k] = self.data[k], self.data[j]
            
            k = j
    
if '__main__' == __name__:
    pq = maxPQ(10)
    for i in range(100, 0, -1):
        pq.insert(i)
    for i in range(10):
        print(pq.delMax())
