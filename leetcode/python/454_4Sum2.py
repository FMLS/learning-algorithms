# 本题第一眼上去直觉就是四层循环, 但这样时间复杂度直接是O(n^4), 但显然不是我们想要的.
# 思路就是充分利用sum为0, a, b, c, d四个数字任意两个的sum和另外两个数的sum肯定互为相反数,
# 需要注意的是, A[a] + B[b] + C[c] + D[d] = 0等价于 A[a] + B[b] = -C[c] - D[d] 等形式
# 所以最终不会漏算, 随意组合两组数, 都可得到正确的结果
# 利用哈希表的性质, 将时间复杂度最终降到O(n^2)

class Solution:
    def fourSumCount(self, A, B, C, D):
        """
        :type A: List[int]
        :type B: List[int]
        :type C: List[int]
        :type D: List[int]
        :rtype: int
        """
        hashMap = {}        
        for a in A:
            for b in B:
                if a + b not in hashMap:
                    hashMap[a + b] = 1
                else:
                    hashMap[a + b] += 1
        
        sum_ = 0
        for c in C:
            for d in D:
                if -c - d in hashMap:
                    sum_ += hashMap[-c - d]

        return sum_

if __name__ == '__main__':
    A = [1, 2]
    B = [-2, -1]
    C = [-1, 2]
    D = [0, 2]

    ans = Solution().fourSumCount(A, B, C, D)
    print(ans)
