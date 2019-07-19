class Solution:
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        # 总体思路是res[i]的值是它左边所有元素的值和右边所有元素值的乘积

        left = 1
        res = [1]
        length = len(nums)

        # 把res[i]左边左右元素的乘积保存到res[i]中, res[i] = res[0]到res[i - 1]累乘
        for i in range(1, length):
            res.append(res[i - 1] * nums[i - 1])

        # res[i]乘以它右边所有元素的乘积所得结果就是res[i]位置的数
        right = 1
        for i in range(length - 1, -1, -1):
            res[i] *= right
            right *= nums[i]

        return res


if __name__ == '__main__':
    nums = [1 ,2 ,3 ,4]
    res = Solution().productExceptSelf(nums)
    print(res)
