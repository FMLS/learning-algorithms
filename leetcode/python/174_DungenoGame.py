class Solution:
    def calculateMinimumHP(self, dungeon):
        """
        :type dungeon: List[List[int]]
        :rtype: int
        """

        self.dungeon = dungeon
        return self.doCalculate(2, 2)

    def doCalculate(self, a, b):
        if a == 0 and b == 0:
            return self.dungeon[0][0]

        if a == 0:
            return self.doCalculate(0, b - 1) + self.dungeon[0][b]
        if b == 0:
            return self.doCalculate(a - 1, 0) + self.dungeon[a][0]

        return min(self.doCalculate(a - 1, b), self.doCalculate(a, b - 1)) - self.dungeon[a][b]

so = Solution()
dungeon = [
    [-2, -3, 3],
    [-5, -10, 1],
    [10, 30, -5],
]

print(so.calculateMinimumHP(dungeon))
