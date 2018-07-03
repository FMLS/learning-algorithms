class MinimumPathSum:
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        return MinimumPathSum._getMinPathSum(grid, 0, 0)
    # 暴力递归解法 - 试法 
    @staticmethod
    def _getMinPathSum(grid, i, j):
        #reach the last grid
        if i == len(grid) - 1 and j == len(grid[0]) - 1:
            return grid[i][j]
        #only right
        if i == len(grid) - 1 and j < len(grid[0]):
            return grid[i][j] + MinimumPathSum._getMinPathSum(grid, i, j + 1)
        #only down 
        if j == len(grid[0]) - 1 and i < len(grid):
            return grid[i][j] + MinimumPathSum._getMinPathSum(grid, i + 1, j)
        #two condition, choice minimum one
        if i < len(grid) and j < len(grid[0]):
            return grid[i][j] + min(
                MinimumPathSum._getMinPathSum(grid, i + 1, j), 
                MinimumPathSum._getMinPathSum(grid, i, j + 1)
            )

    #动态规划 - 算法 
    @staticmethod
    def dpGetminPathSum(grid):
        dp = [[None for i in range(len(grid[0]))] for i in range(len(grid))]
        dp[-1][-1] = grid[-1][-1]
        for j in range(len(grid[0]) - 2, -1, -1):
            dp[-1][j] = grid[-1][j] + dp[-1][j + 1]
        for i in range(len(grid) - 2, -1, -1):
            dp[i][-1] = grid[i][-1] + dp[i + 1][-1]
        
        for i in range(len(grid) - 2, -1, -1):
            for j in range(len(grid[0]) -2, -1, -1):
                dp[i][j] = grid[i][j] + min(dp[i + 1][j], dp[i][j + 1])
        
        return dp[0][0]

if __name__ == '__main__':
    grid = [
        [1,3,1],
        [1,5,1],
        [4,2,1],
    ]

    #res = MinimumPathSum().minPathSum(grid)
    #print(res)
    res = MinimumPathSum().dpGetminPathSum(grid)
    print(res)
