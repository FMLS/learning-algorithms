class Solution:
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        lenHaystack = len(haystack)
        lenNeedle = len(needle)

        if needle == '':
            return 0

        i = 0
        while i < lenHaystack - lenNeedle + 1:
            j = 0
            if haystack[i] == needle[j]:
                while j < lenNeedle and haystack[i + j] == needle[j]:
                    j += 1
                if j == lenNeedle:
                    return i
            i += 1
        return -1

if __name__ == '__main__':
    #haystack = 'mississippi'
    #needle = 'issip'

    #haystack = 'hello'
    #needle = 'bb'
    haystack = 'aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa' * 1000 + 'b'
    needle = 'a' * 100 + 'b'

    res = Solution().strStr(haystack, needle)
    print(res)
