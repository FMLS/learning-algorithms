class Solution:
    def getSum(self, a, b):
        """
        :type a: int
        :type b: int
        :rtype: int
        """
        if b == 0:
            return a
        sum_ = a ^ b
        carry = (a & b) << 1
        return self.getSum(sum_, carry)

if __name__ == '__main__':
    print(Solution().getSum(-1, 1))
