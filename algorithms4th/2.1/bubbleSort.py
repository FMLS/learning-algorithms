def bubbleSort(data):
    len_ = len(data)
    for i in range(0, len_):
        for j in range(0, len_ - 1 - i):
            if data[j] > data[j + 1]:
                data[j], data[j + 1] = data[j + 1], data[j]

if __name__ == '__main__':
    data = [i for i in range(9, -1, -1)]
    bubbleSort(data)
    print(data)
