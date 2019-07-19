class Solution:
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        slow = nums[0]
        fast = nums[nums[0]]

        while fast != slow:
            slow = nums[slow]
            fast = nums[nums[fast]]
        
        slow = nums[slow]
        fast = nums[0]
        while fast != slow:
            fast = nums[fast]
            slow = nums[slow]
        
        return slow
    
if __name__ == '__main__':

    nums = [1, 3, 4, 2, 2]
    nums = [3, 1, 3, 4, 2]
    ans = Solution().findDuplicate(nums)
    print(ans)
