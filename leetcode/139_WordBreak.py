class Solution:
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        return self.doBreak(s, wordDict)
        
    def doBreak(self, s, wordDict):
        if s == '':
            return False

        s_len = len(s)
        results = []
        for word in wordDict:
            i = 0
            word_len = len(word)
            while (i < word_len and i < s_len and s[i] == word[i]):
                i += 1
            #这个单词匹配失败
            if i < word_len:
                continue
            #匹配成功
            elif i == word_len:
                results.append(
                    True if i == s_len else self.doBreak(s[word_len:], wordDict)
                )
        
        return any(results)


if '__main__' == __name__:
    #s = 'catapplea'
    #wordDict = ['cat', 'apple', 'app', 'lea']

    #s = 'applecatapple'
    #wordDict = ['apple', 'cat']

    #s = "catsandog"
    #wordDict = ["cats","dog","sand","and","cat"]

    s = 'aabbccddeaf'
    wordDict = ['a', 'b', 'c', 'd', 'eaf']

    so = Solution()
    print(so.wordBreak(s, wordDict))


