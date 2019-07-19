class Solution:
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return sorted(nums)[len(nums) // 2]

if __name__ == '__main__':
    nums = [1, 3, 3]
    ans = Solution().majorityElement(nums)
    print(ans)
