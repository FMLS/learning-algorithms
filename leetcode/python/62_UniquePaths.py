class Solution:
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        self.total = 0
        self.m = m - 1
        self.n = n - 1
        #self.helper(m - 1, n - 1)
        #return self.helper2(0, 0)
        #return self.total
        return self.dp(0, 0)

    # 第一种递归写法
    def helper(self, m, n):
        if m == 0 and n == 0:
            self.total += 1
            return

        if m - 1 >= 0:
            self.helper(m - 1, n)
        if n - 1 >= 0:
            self.helper(m, n - 1)

    # 第二种递归写法, 此种写法可以优化为动态规划写法
    def helper2(self, i, j):
        if i == self.m and j == self.n:
            return 1
        if i == self.m:
            return self.helper2(self.m, j + 1)
        if j == self.n:
            return self.helper2(i + 1, self.n)

        return self.helper2(i + 1, j) + self.helper2(i, j + 1)

    # 动态规划的实现方法
    def dp(self, x, y):
        dp = [[None for i in range(0, self.m + 1)] for i in range(0, self.n + 1)]
        dp[self.n][self.m] = 1
        for i in range(0, self.m):
            dp[self.n][i] = 1
        for i in range(0, self.n):
            dp[i][self.m] = 1
        for j in range(self.m - 1, -1, -1):
            for i in range(self.n - 1, -1, -1):
                dp[i][j] = dp[i + 1][j] + dp[i][j + 1]
        return dp[x][y]

if __name__ == '__main__':
    ans = Solution().uniquePaths(7, 3)
    print(ans)

