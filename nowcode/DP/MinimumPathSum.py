class MinimumPathSum:
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        return MinimumPathSum._getMinPathSum(grid, 0, 0)
    
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

if __name__ == '__main__':
    grid = [
        [1,3,1],
        [1,5,1],
        [4,2,1],
    ]

    res = MinimumPathSum().minPathSum(grid)
    print(res)
