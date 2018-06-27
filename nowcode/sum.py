import random

class Sum(object):
    
    def __init__(self, array):
        self.data = array
    
    def _doSum(self, l, r):
        if l == r:
            return self.data[l]

        mid = l + (r - l) // 2
        return self._doSum(l, mid) + self._doSum(mid + 1, r)
        
    def sumRecursion(self):
        return self._doSum(0, len(self.data) - 1)

if __name__ == '__main__':
    data = random.sample(range(100), 10)
    assert sum(data) == Sum(data).sumRecursion() 
