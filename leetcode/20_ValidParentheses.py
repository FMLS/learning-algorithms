class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if len(s) % 2 != 0:
            return False
        
        map = {
            '(': ')',
            '[': ']',
            '{': '}'
        }
        
        stack = []
        for char in s:
            #map.get replace map[..] because ')' not in map but
            #may be place at stack[-1]
            if len(stack) > 0 and map.get(stack[-1]) == char:
                stack.pop()
            else:
                stack.append(char)
        
        if len(stack) > 0:
            return False
        else:
            return True

so = Solution()
print(so.isValid('([)]'))
        

