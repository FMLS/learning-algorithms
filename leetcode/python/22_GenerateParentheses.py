# 有更好的思路
class Solution:
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        # total operation count
        n *= 2
        self.res = []
        self.doGen(n, 0, '')
        return self.res
    
    def doGen(self, n, sum_, str_):
        # wrong answer; end
        if sum_ < 0:
            return
        # total operation done
        if n == 0:
            if sum_ == 0:
                self.res.append(str_)
            return
        
        self.doGen(n - 1, sum_ + 1, str_ + '(')
        self.doGen(n - 1, sum_ - 1, str_ + ')')
        
if __name__ == '__main__':
    res = Solution().generateParenthesis(3)
    print(res)
