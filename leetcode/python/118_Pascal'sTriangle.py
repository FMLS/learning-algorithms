class Solution:
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """

        result = [[] for i in range(numRows)]
        for i in range(0, numRows):
            for j in range(0, i + 1):
                if j == 0 or j == i:
                    result[i].append(1)
                else:
                    result[i].append(result[i - 1][j - 1] + result[i - 1][j])

        return result




if __name__ == '__main__':
    print(Solution().generate(10))

