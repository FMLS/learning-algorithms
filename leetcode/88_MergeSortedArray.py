class Solution:
    # 反向神操作, 换个思维方式效率大幅提高

    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        
        cur = m + n - 1
        m -= 1
        n -= 1
        while m >= 0 and n >= 0:
            if nums1[m] > nums2[n]:
                nums1[cur] = nums1[m]
                m -= 1
            else:
                nums1[cur] = nums2[n]
                n -= 1
            cur -= 1
        if m < 0:
            # 注意这个n + 1的边界, 切片操作右侧开区间
            nums1[:n + 1] = nums2[:n + 1]


    # 第一次的思路
    #def merge(self, nums1, m, nums2, n):
    #    """
    #    :type nums1: List[int]
    #    :type m: int
    #    :type nums2: List[int]
    #    :type n: int
    #    :rtype: void Do not return anything, modify nums1 in-place instead.
    #    """
    #    n1 = n2 = 0 
    #    while n1 < m and n2 < n:
    #        if nums2[n2] < nums1[n1]:
    #            j = m
    #            while j > n1:
    #                nums1[j] = nums1[j - 1]
    #                j -= 1
    #            nums1[n1] = nums2[n2]
    #            n2 += 1
    #            m += 1
    #        else:
    #            n1 += 1
    #        
    #    while n2 != n:
    #        nums1[n1] = nums2[n2]
    #        n1 += 1
    #        n2 += 1

if __name__ == '__main__':
    nums1 = [5, 6, 7,0,0,0]
    m = 3
    nums2 = [1, 2, 3]
    n = 3
    Solution().merge(nums1, m, nums2, n)
    print(nums1)
