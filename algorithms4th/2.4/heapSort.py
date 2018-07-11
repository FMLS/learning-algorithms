import math

class heapSort:
    def __init__(self):
        pass

    # 注意 python3中 负数的// 等价于 math.floor, 所以要用math.ceil达到负数的地板除效果
    def heapInsert(self, arr, index):
        while arr[index] > arr[math.ceil((index - 1) / 2)]:
            arr[index], arr[math.ceil((index - 1)/2)] = arr[math.ceil((index - 1)/2)], arr[index]
            index = math.ceil((index - 1) / 2)
        

    def sink(self, arr, k, heapSize):
        while k * 2 + 1 < heapSize:
            j = k * 2 + 1
            # 注意这里的越界判断, j < heapSize可能不报错但逻辑错误, 
            # 因为调整过程中heapSize下标后边有值, 数组不越界
            if j + 1 < heapSize and arr[j] < arr[j + 1]:
                j += 1
            if not arr[k] < arr[j]:
                break
            arr[k], arr[j] = arr[j], arr[k]
            k = j

    def Sort(self, arr):
        if not arr or len(arr) < 2:
            return
        for i in range(0, len(arr)):
            self.heapInsert(arr, i)
        print(arr)
        heapSize = len(arr)
        heapSize -= 1
        arr[0], arr[heapSize] = arr[heapSize], arr[0]
        while heapSize > 0:
            self.sink(arr, 0, heapSize)
            heapSize -= 1
            arr[0], arr[heapSize] = arr[heapSize], arr[0]
            
if __name__ == '__main__':
    data = [i for i in range(10, 0, -1)]
    data = [i for i in range(0, 10, 1)]
    hpSort = heapSort()
    hpSort.Sort(data)
    print(data)


