#求数组小和
#思路是利用归并排序的merge过程批量算取每部分小和
class SmallSum(object):
    
    def __init__(self, array):
        self.data = array
        self.helper = [None for i in range(len(array))]

    def merge(self, lo, mid, high):
        i = lo
        j = mid + 1
        h = lo
        res = 0

        while i <= mid and j <= high:
            if self.data[i] <= self.data[j]:
                self.helper[h] = self.data[i]
                res += self.data[i] * (high - j + 1)
                i += 1
            else:
                self.helper[h] = self.data[j]
                j += 1
            h += 1
        
        while i <= mid:
            self.helper[h] = self.data[i]
            i += 1
            h += 1
        while j <= high:
            self.helper[h] = self.data[j]
            j += 1
            h += 1
        #拷贝回去 
        for i in self.helper[lo:high + 1]:
            self.data[lo] = i
            lo += 1
        return res
    
    def doSmallSum(self, lo, hi):
        if lo >= hi:
            #return self.data[lo]
            return 0
        
        mid = lo + (hi - lo) // 2
        return self.doSmallSum(lo, mid) + self.doSmallSum(mid + 1, hi) + self.merge(lo, mid, hi)

    def smallSum(self):
        return self.doSmallSum(0, len(self.data) - 1)

if __name__ == '__main__':
    sS = SmallSum([5, 8, 2, 3, 0, 1, 9, -1])
    sS = SmallSum([1, 3, 4, 2, 5])
    print(sS.smallSum())
    

