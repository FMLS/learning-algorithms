class Solution:
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """

        cur = len(digits) - 1
        carry = 1
        while cur >= 0:
            tmp = digits[cur] + carry
            if tmp < 10:
                digits[cur] = tmp
                carry = 0
            else:
                digits[cur] = tmp - 10
                carry = 1
            cur -= 1

        if cur < 0 and carry == 1:
            digits.insert(0, carry)
        
        return digits

if __name__ == '__main__':
    digits = [9, 9, 9]
    print(Solution().plusOne(digits))
