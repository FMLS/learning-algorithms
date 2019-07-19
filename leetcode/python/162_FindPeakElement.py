class Solution:
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        lo = 0
        hi = len(nums) - 1

        # 循环边界判断有问题
        # while lo < hi:

        # 正确的做法
        while lo < hi - 1:
            mid = (lo + hi) // 2
            if nums[mid] > nums[mid - 1] and nums[mid] > nums[mid + 1]:
                return mid

            # 这一段的判断思路错误
            # leftDis = mid - lo
            # leftMinus = nums[mid] - nums[lo]
            # if leftMinus < leftDis:
            #     hi = mid - 1
            # else:
            #     lo = mid + 1

            # 正确的做法

            if nums[mid] < nums[mid + 1]:
                lo = mid + 1
            else:
                hi = mid - 1
        
        return lo if nums[lo] > nums[hi] else hi 

if __name__ == '__main__':
    nums = [1,2,1,3,5,6,4]
    nums = [1,2,3,1]

    nums = [1] #except 0
    nums = [1, 2, 3, 4] #except 4
    nums = [6, 5, 4, 3]
    res = Solution().findPeakElement(nums)
    print(res)

