class Solution:
    def removeDuplicates(self, nums):
        if len(nums) == 0:
            return 0
        p = 0
        for i in nums:
            if i != nums[p]:
                p += 1
                nums[p] = i
        p += 1
        return p

    #def removeDuplicates(self, nums):
    #    p = 0 
    #    n = p
    #    olength = len(nums)

    #    if olength == 0:
    #        return 0

    #    nlength = 1
    #    while n < olength - 1:
    #        if nums[n] != nums[n + 1]:
    #            p += 1
    #            nums[p] = nums[n + 1]
    #            nlength += 1
    #        n += 1

    #    return nlength




#    def removeDuplicates(self, nums):
#        """
#        :type nums: List[int]
#        :rtype: int
#        """
#        p = 0
#        length = len(nums)
#        while p < length:
#            distance = 0
#            n = p + 1
#            while n < length and nums[p] == nums[n]:
#                n += 1
#                distance += 1
#
#            while n < length:
#                nums[n - distance] = nums[n] 
#                n += 1
#            
#            p += 1
#            length -= distance
#        return length 

if __name__ == '__main__':
    nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
    #nums = [0, 0, 8, 9, 12, 13, 13]
    #nums = [1, 1, 2]
    so = Solution()
    print(so.removeDuplicates(nums))
    print(nums)
