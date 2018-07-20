class Solution:
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        self.totalAns = []
        self.helper(nums, [])
        return self.totalAns
        
    def helper(self, arr, ans):
        if not arr:
            self.totalAns.append(ans)
            return
        self.helper(arr[1:], ans[:])
        ans.append(arr[0])
        self.helper(arr[1:], ans[:])

# 这个解法很牛逼
# class Solution(object):
#     def subsets(self, nums):
#         nums.sort()
#         result = [[]]
#         for num in nums:
#             result += [i + [num] for i in result]
#         return result

# DP解法待看, 看后在这里补充


if __name__ == '__main__':
    nums = [1, 2, 3]
    nums = [1]
    ans = Solution().subsets(nums)
    print(ans)

