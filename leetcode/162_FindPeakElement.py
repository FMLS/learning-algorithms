class Solution:
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        lo = 0
        hi = len(nums) - 1

        while lo < hi:
            mid = (lo + hi) // 2
            if nums[mid] > nums[mid - 1] and nums[mid] > nums[mid + 1]:
                return mid

            leftDis = mid - lo
            leftMinus = nums[mid] - nums[lo]
            if leftMinus < leftDis:
                hi = mid - 1
            else:
                lo = mid + 1
        return 0

if __name__ == '__main__':
    nums = [1,2,1,3,5,6,4]
    nums = [1,2,3,1]

    nuns = [1] #except 0
    nums = [1, 2, 3, 4] #except 4
    res = Solution().findPeakElement(nums)
    print(res)

