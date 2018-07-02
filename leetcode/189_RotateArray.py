class Solution:

# time: O(n^2) 超时
#    def rotate(self, nums, k):
#        """
#        :type nums: List[int]
#        :type k: int
#        :rtype: void Do not return anything, modify nums in-place instead.
#        """
#        length = len(nums)
#        if k > length:
#            k = k % length
#
#        n = 0
#        while k > 0:
#            i = length - k - 1
#            target = nums[i + 1]
#            while i >= n:
#                nums[i + 1] = nums[i]
#                i -= 1
#            nums[n] = target
#            k -= 1
#            n += 1

# time: O(n) space:O(1)
    def rotate(self, nums, k):
        if not nums:
            return nums
        length = len(nums)
        k %= length

        self.reverse(nums, 0, length - 1)
        self.reverse(nums, 0, k - 1)
        self.reverse(nums, k, length - 1)
    
    def reverse(self, nums, start, end):
        while start < end:
            nums[start], nums[end] = nums[end], nums[start]
            start += 1
            end -= 1


if __name__ == '__main__':
    nums = [1, 2, 3, 4, 5, 6, 6]
    #nums = [1, 2]
    nums = []
    print(nums)
    so = Solution()
    so.rotate(nums, 3)
    print(nums)
