class Solution:
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        if not word:
            return False

        self.rows = len(board)
        self.cols = len(board[0])
        self.board = board
        self.word = word

        for row in range(self.rows):
            for col in range(self.cols):
                if self.dfs(row, col, 0):
                    return True
        
        return False

        
    def dfs(self, row, col, pos):
        if self.board[row][col] == self.word[pos]:
            if pos == len(self.word) - 1:
                return True
            else:
                #做标记
                temp = self.board[row][col]
                self.board[row][col] = None

                if row + 1 < self.rows and self.dfs(row + 1, col, pos + 1):
                    return True
                if col + 1 < self.cols and self.dfs(row, col + 1, pos + 1):
                    return True
                if row - 1 >= 0 and self.dfs(row - 1, col, pos + 1):
                    return True
                if col - 1 >= 0 and self.dfs(row, col - 1, pos + 1):
                    return True
                
                #回溯还原
                self.board[row][col] = temp 
                return False
        else:
            return False

board = [
    ['A','B','C','E'],
    ['S','F','C','S'],
    ['A','D','E','E']
]

word = 'ABFCSE'

res = Solution().exist(board, word)
print(res)
