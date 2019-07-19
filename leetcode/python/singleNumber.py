def singleNumber(numlist):
    result = 0
    for item in numlist:
        result ^= item 
    return result

numlist = [1, 0, 1]

print singleNumber(numlist)