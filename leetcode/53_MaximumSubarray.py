class Solution:
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        sumNum = 0
        maxNum = float('-inf')
        for num in nums:
            sumNum += num
            if sumNum < 0:
                sumNum = 0
                continue
            if sumNum > maxNum:
                maxNum = sumNum
    
        return maxNum

    #暴力搜索 timeout
    #def maxSubArray(self, nums):
    #    """
    #    :type nums: List[int]
    #    :rtype: int
    #    """
    #    maxSum = float('-inf')
    #    for i in range(len(nums)):
    #        sumNum = 0
    #        for j in range(i, len(nums)):
    #            sumNum += nums[j]
    #            if sumNum > maxSum:
    #                maxSum = sumNum
    #    
    #    return maxSum


print(Solution().maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))
