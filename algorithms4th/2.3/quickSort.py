def partition(data, lo, hi):
    v = data[lo]
    i = lo
    j = hi + 1

    while i < j:
        while True:
            i += 1
            if data[i] > v or i >= hi:
                break
        while True:
            j -= 1
            if data[j] < v or j <= lo:
                break
        if i >= j:
            break

        data[i], data[j] = data[j], data[i]

    data[j], data[lo] = data[lo], data[j]
    return j

def quickSort(data, lo, hi):
    if lo >= hi:
        return
    mid = partition(data, lo, hi)
    quickSort(data, lo, mid - 1)
    quickSort(data, mid + 1, hi)

data = [0, 0, 0, 9, 9, 9, 8, 4, 1, 3, 5, 2, 6, 7]
#data = [1, 1, 1, 1]

quickSort(data, 0, len(data) - 1)
print(data)
