import math
#最普通的二分查找
def binSearch(key, data):
    length = len(data)
    low = 0
    high = length - 1
    # 为什么是 <= 而不是 <  ?
    # 因为low与high重叠时, mid = low = high 可能查找成功, 也可能失败, 但必须判定,
    # 不然就少了一次判断
    while low <= high:
        mid = low + (high - low) // 2
        if data[mid] == key:
            return mid
        elif data[mid] > key:
            #high = mid ok?
            #no, 导致左侧查找失败时(low = 0, high = 0, mid = 0, data[mid] > key, 
            # 但high = mid, mid = (0 + 0)//2  == 0 死循环
            high = mid - 1
        elif data[mid] < key:
            # low = mid ok?
            # no, 会导致中间或右侧查找不到时死循环
            low = mid + 1
    return None

#带重复元素的data中, 返回结果中最小的index
def binSearchFirst(key, data):
    length = len(data)
    low = 0
    high = length - 1

    #这里必须是 < 
    # <= 会导致low=high时进入死循环
    while low < high:
        mid = low + (high - low) // 2 # 从左侧开始找, // 等价于math.floor

        if key > data[mid]:
            low = mid + 1
        else:
            high = mid

    return low if data[low] == key else None

#带重复元素的data中, 返回结果中最大的index
def binSearchLast(key, data):
    length = len(data)
    low = 0
    high = length - 1
    while low < high:
        mid = math.ceil((low + high) / 2) # 从右侧开始找, 所以要用math.ceil把运算坐标像右靠
        if key < data[mid]:
            high = mid - 1
        else:
            low = mid
    return low if data[low] == key else None


data = [0, 0, 0, 0, 1, 1, 1, 2, 3, 4, 6,  7,  8,  9]
data = [0, 1, 1, 1, 2, 3, 4, 6, 7, 8, 9]
index= [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

print(binSearchFirst(1, data))
print(binSearchLast(1, data))
