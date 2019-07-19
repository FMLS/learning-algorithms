class Solution:
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        p1 = 0
        p2 = p1 + 1
        length = len(nums)

        while p2 < length and p1 < length:
            while p1 < length and nums[p1] != 0:
                p1 += 1
            p2 = p1
            while p2 < length and nums[p2] == 0:
                p2 += 1
            if p1 < length and p2 < length and nums[p1] == 0 and nums[p2] != 0:
                nums[p1], nums[p2] = nums[p2], nums[p1]
                p1 += 1
                p2 += 1

if __name__ == '__main__':
    nums = [0, 1, 0, 3, 12]
    nums = [0, 0, 0]
    nums = [1, 1, 1]
    nums = [4,2,4,0,0,3,0,5,1,0]
    Solution().moveZeroes(nums)
    print(nums)

