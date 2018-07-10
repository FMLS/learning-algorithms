class minPQ:
    def __init__(self, maxN):
        self.data = [None for i in range(maxN + 1)]
        self.N = 0
        self.maxN = maxN
    
    def swim(self, k):
        while k > 1 and self.data[k] < self.data[k // 2]:
            self.data[k], self.data[k // 2] = self.data[k // 2], self.data[k]
            k = k // 2
    
    def sink(self, k):
        while k * 2 <= self.N:
            j = k * 2
            if j < self.N and self.data[j] > self.data[j + 1]:
                j += 1
            if not self.data[k] > self.data[j]:
                break
            self.data[k], self.data[j] = self.data[j], self.data[k]
            #k *= 2
            k = j

    def heapInsert(self, value):
        if self.N < self.maxN:
            self.N += 1
        self.data[self.N] = value
        self.swim(self.N)
    
    def delMin(self):
        min_ = self.data[1]
        self.data[1], self.data[self.N] = self.data[self.N], self.data[1]
        self.N -= 1
        self.data[self.N + 1] = None
        self.sink(1)
        return min_
    
    def topK(self, data):
        for i, item in enumerate(data):
            count = i + 1
            if count <= self.maxN:
                self.heapInsert(item)
            elif item > self.data[1]:
                self.data[1] = item
                self.sink(1)

if __name__ == '__main__':
    minPQ_ = minPQ(10)
    minPQ_.topK([i for i in range(100)])
    print(minPQ_.data)
