class Solution:
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n < 1:
            return 0

        record = [1, 2]
        for i in range(2, n):
            record.append(record[i - 1] + record[i - 2])
        
        return record[n - 1]


so = Solution().climbStairs(2)
print(so)
