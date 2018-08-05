class Solution:
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        sumIndex = 0
        sumValue = 0
        i = 0
        length = len(nums)
        while i < length:
            sumIndex += i
            sumValue += nums[i]
            i += 1
        sumIndex += i


        return sumIndex - sumValue

if __name__ == '__main__':
    nums = [9,6,4,2,3,5,7,0,1]
    nums = [3, 0, 1]
    ans = Solution().missingNumber(nums)
    print(ans)
