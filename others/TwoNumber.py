# 给定一个整形递增数组arr = [1, 3, 5, 9, 10, 16], 从中找到两个数的和是给定值

def getNumbers(arr, target):
    if not arr:
        return -1, -1
    left = 0
    right = len(arr) - 1

    while left < right:
        sum_ = arr[left] + arr[right]
        if sum_ == target:
            return left, right
        if sum_ < target:
            left += 1
        if sum_ > target:
            right -= 1
    return -1, -1

if __name__ == '__main__':
    arr = [1, 3, 5, 9, 16]
    print(getNumbers(arr, 25))
