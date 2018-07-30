# 本题的思路在于充分利用矩阵数字的规律, 选取矩阵右上角为起点, 根据当前值和目标值比较可以决定向下
# 或向左走, 一步步逼出目标数字或者越界为止 
# 同理可以选取左下角为起点, 但不能选取左上角和右下角, 因为这样两个方向上数字变化的规律相同
class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """

        rows = len(matrix)
        if not rows:
            return False

        cur_row = 0
        cols = len(matrix[cur_row])
        if not cols:
            return False
        cur_col = cols - 1

        while cur_row < rows and cur_col > -1:
            cur_value = matrix[cur_row][cur_col]
            if cur_value > target:
                cur_col -= 1
            elif cur_value < target:
                cur_row += 1
            else:
                return True
        return False

if __name__ == '__main__':
    matrix = [
        [1,   4,  7, 11, 15],
        [2,   5,  8, 12, 19],
        [3,   6,  9, 16, 22],
        [10, 13, 14, 17, 24],
        [18, 21, 23, 26, 30],
    ]

    #matrix = [[], [1]]
    matrix = [[]]

    ans = Solution().searchMatrix(matrix, 1)
    print(ans)
