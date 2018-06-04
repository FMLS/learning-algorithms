
def merge(data, lo, mid, high):
    i = lo
    j = mid + 1
    aux = []

    for elem in data:
        aux.append(elem)
    
    k = lo
    try:
        while k <= high:
            if i > mid:
                data[k] = aux[j]
                j += 1
            elif j > high:
                data[k] = aux[i]
                i += 1
            elif aux[i] < aux[j]:
                data[k] = aux[i]
                i += 1
            else:
                data[k] = aux[j]
                j += 1
            k += 1
    except Exception as e:
        print(e, i, j)

def mergeSort(data, lo, hi):
    if lo >= hi:
        return
    mid = lo + (hi - lo) // 2
    mergeSort(data, lo, mid)
    mergeSort(data, mid + 1, hi)
    merge(data, lo, mid, hi)
    
data = [9, 8, 5, 1, 6, 3, 2, 7, 4, 0]
mergeSort(data, 0, len(data) - 1)
print(data)
