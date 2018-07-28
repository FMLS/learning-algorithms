class Solution:
    def myAtoi(self, str_):
        """
        :type str: str
        :rtype: int
        """

        if not str_:
            return 0

        length = len(str_)
        sign = 1
        index = 0
        res = 0
        while index < length and str_[index] == ' ':
            index += 1

        if index < length:
            if str_[index] == '-':
                sign = -1
                index += 1
            elif str_[index] == '+':
                index += 1
            elif str_[index] < '0' or str_[index] > '9':
                return res
        
        while index < length:
            elem = str_[index]
            if elem >= '0' and elem <= '9':
                res = res * 10 + ord(elem) - ord('0')
            elif elem == ' ':
                pass
            else:
                break
            
            index += 1
        
        res *= sign
        if res > 2 ** 31 - 1:
            return 2 ** 31 -1
        elif res < -2 ** 31:
            return -(2 ** 31)
            
        
        return res

if __name__ == '__main__':

    res = Solution().myAtoi("   + 0 123")
    print(res)
