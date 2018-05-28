def shellSort(data):
    N = len(data)
    h = 1
    while h < N // 3:
        #这里的+1是个小细节
        h = h * 3 + 1
    
    while h >= 1:
        for i in range(h, N):
            j = i
            while j >= h and data[j] < data[j - h]:
                data[j], data[j - h] = data[j - h], data[j]
                j -= h
        h = h // 3

data = [1, 8, 9, 2, 3, 0, 5, 4, 7, 6]
shellSort(data)
print(data)
