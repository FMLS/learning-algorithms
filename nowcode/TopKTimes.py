# 给定string 类型的数组strArr, 再给定整数k, 请严格按照排名顺序打印出现次数前K名的字符串

import math

class Node:
    def __init__(self, s, t):
        self.str = s
        self.times = t
    
    def __gt__(self, other):
        return self.times > other.times
    
    def __ge__(self, other):
        return self.times >= other.times
    
    def __lt__(self, other):
        return self.times < other.times
    
    def __le__(self, other):
        return self.times >= other.times

class MinHeap:
    def __init__(self, maxN):
        self.maxN = maxN
        self.size = 0
        self.data = [None for i in range(0, maxN + 1)]

    def heapInsert(self, elem):
        if self.size < self.maxN:
            self.size += 1
            self.data[self.size] = elem
            self.swim(self.size)
        else:
            if elem > self.data[1]:
                self.data[1] = elem
                self.sink(1)
    
    def delMax(self):
        max_ = None
        if self.size > 0:
            max_ = self.data[1]
            self.data[1] = self.data[self.size]
            self.data[self.size] = None
            self.size -= 1
            self.sink(1)
        return max_

    
    def swim(self, k):
        parent = k // 2
        while k > 1 and self.data[k] < self.data[parent]:
            self.data[k], self.data[parent] = self.data[parent], self.data[k]
            k = parent
            parent = parent // 2
    
    def sink(self, k):
        while k * 2 <= self.size:
            j = k * 2
            if j < self.size and self.data[j] > self.data[j + 1]:
                j += 1
            if not (self.data[k] > self.data[j]):
                break
            self.data[k], self.data[j] = self.data[j], self.data[k]
            k = j

class TopKTimes:
    def __init__(self, arr, k):
        self.arr = arr
        self.k = k
    
    def getStrTimesTable(self):
        tab = {}
        for elem in self.arr:
            if elem not in tab:
                tab[elem] = 0
            else:
                tab[elem] += 1
        
        nodes = []
        for key, val in tab.items():
            nodes.append(
                Node(key, val)
            )

        minHeap = MinHeap(self.k)
        for elem in nodes:
            minHeap.heapInsert(elem)
        
        topK = []
        for i in range(0, minHeap.size):
            topK.append(minHeap.delMax().str)
        topK.reverse()
        
        return topK

if __name__ == '__main__':
    data = [1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3, 3]
    data = ['a', 'a', 'b', 'b', 'b', 'c']
    topKtimes = TopKTimes(data, 1)
    res = topKtimes.getStrTimesTable()
    print(res)
