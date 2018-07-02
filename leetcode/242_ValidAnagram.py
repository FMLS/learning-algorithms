class Solution:
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        
        if len(s) != len(t):
            return False
        
        counter = []
        for i in range(26):
            counter.append(0)

        for i in range(len(s)):
            counter[ord(s[i]) - ord('a')] += 1
            counter[ord(t[i]) - ord('a')] -= 1
        
        for i in counter:
            if i != 0:
                return False

        return True

so = Solution()
print(so.isAnagram("anagram", "nagaram"))
