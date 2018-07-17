class Solution:
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        self.answer = []
        self.helper(nums, [])
        return self.answer
        
    def helper(self, nums, res):
        if not nums:
            self.answer.append(res)
            return

        for elem in nums:
            cpy = nums[:]
            cpy.remove(elem)
            self.helper(cpy, res[:] + [elem])

if __name__ == '__main__':
    res = Solution().permute([1, 2, 3])
    print(res)


