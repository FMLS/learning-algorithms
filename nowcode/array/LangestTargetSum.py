# 给定一个数组arr，该数组无序，但每个值均为正数，再给定一个正数k。求arr的所有子数组中所有元素相加和为k的最长子数组长度
# 例如，arr=[1，2，1，1，1]，k=3。累加和为3的最长子数组为[1，1，1]，所以结果返回3

class Solution():
    def longestTargetSum(self, arr, target):
        if not arr:
            return None

        length = len(arr)
        p = q = 0
        sum_ = 0
        maxSum = 0
        sumLen = 0
        while q < length:
            if sum_ < target:
                sum_ += arr[q]
                sumLen += 1
                q += 1
            elif sum_ > target:
                sum_ -= arr[p]
                p += 1
                sumLen -= 1

            if sum_ == target:
                maxSum = sumLen if sumLen > maxSum else maxSum
                sum_ -= arr[p]
                p += 1
                sumLen -= 1
        return maxSum

if __name__ == '__main__':
    arr = [5, 2, 2, 1, 1, 3, 1, 1, 1, 1]
    ans = Solution().longestTargetSum(arr, 4)
    print(ans)
