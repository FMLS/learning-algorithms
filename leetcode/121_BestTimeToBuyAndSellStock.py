class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """

        if not prices:
            return 0

        imin = prices[0]
        maxr = 0

        for index, cur in enumerate(prices[0:]):
            if cur < imin:
                imin = cur

            if cur > imin:
                tmp = cur - imin
                maxr = tmp if tmp > maxr else maxr


        return maxr

if __name__ == '__main__':
    prices = [7,1,5,3,6,4]
    prices = [7,6,4,3,1]
    prices = [-1]
    r = Solution().maxProfit(prices)
    print(r)
